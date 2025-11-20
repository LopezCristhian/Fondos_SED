from django.test import TestCase

# Create your tests here.

# Para ejecutar los tests, ejecutar el siguiente comando desde la carpeta del proyecto:
# python manage.py test

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from .models import (
    BudgetItemRevenue,
    BudgetItemExpenses,
    AccountantPuc,
    ExpenseAccounts,
    SourceResources,
    Bank,
    F7BudgetExecutionExpenses,
)

# Test para el modelo de rubros presupuestales de ingresos
class BudgetItemRevenueAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/budget_item_revenue/'  # ruta
        self.item = BudgetItemRevenue.objects.create(
            code='1',
            level='1',
            type='A',
            account_name='Ingresos',
            father=None
        )

    def test_listar_budget_items(self):
        """Debe listar los rubros presupuestales de ingresos"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Ingresos")

    def test_crear_budget_item(self):
        """Debe crear un nuevo rubro presupuestal de ingresos"""
        data = {
            "code": "1.1",
            "level": "2",
            "type": "A",
            "account_name": "Ingresos corrientes",
            "father": "1"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BudgetItemRevenue.objects.count(), 2)
        self.assertEqual(BudgetItemRevenue.objects.get(code="1.1").account_name, "Ingresos corrientes")

    def test_obtener_detalle_budget_item(self):
        """Debe obtener el detalle de un rubro presupuestal"""
        response = self.client.get(f"{self.url}{self.item.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["code"], "1")

    def test_actualizar_budget_item(self):
        """Debe actualizar un rubro presupuestal existente"""
        data = {
            "code": "1",
            "level": "1",
            "type": "A",
            "account_name": "Ingresos Actualizados",
            "father": None
        }
        response = self.client.put(f"{self.url}{self.item.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.account_name, "Ingresos Actualizados")

    def test_eliminar_budget_item(self):
        """Debe eliminar un rubro presupuestal"""
        response = self.client.delete(f"{self.url}{self.item.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BudgetItemRevenue.objects.count(), 0)

# Test para el modelo de rubros presupuestales de gastos
class BudgetItemExpensesAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/budget_item_expenses/'  # ruta
        self.item = BudgetItemExpenses.objects.create(
            code='2',
            level='1',
            type='A',
            account_name='Gastos',
            father=None
        )

    def test_listar_budget_items(self):
        """Debe listar los rubros presupuestales de gastos"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Gastos")

    def test_crear_budget_item(self):
        """Debe crear un nuevo rubro presupuestal de gastos"""
        data = {
            "code": "2.1",
            "level": "2",
            "type": "A",
            "account_name": "Funcionamiento",
            "father": "2"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BudgetItemExpenses.objects.count(), 2)
        self.assertEqual(BudgetItemExpenses.objects.get(code="2.1").account_name, "Funcionamiento")

    def test_obtener_detalle_budget_item(self):
        """Debe obtener el detalle de un rubro presupuestal"""
        response = self.client.get(f"{self.url}{self.item.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["code"], "2")

    def test_actualizar_budget_item(self):
        """Debe actualizar un rubro presupuestal existente"""
        data = {
            "code": "2",
            "level": "1",
            "type": "A",
            "account_name": "Gastos Actualizados",
            "father": None
        }
        response = self.client.put(f"{self.url}{self.item.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.item.refresh_from_db()
        self.assertEqual(self.item.account_name, "Gastos Actualizados")
        
    def test_eliminar_budget_item(self):
        """Debe eliminar un rubro presupuestal"""
        response = self.client.delete(f"{self.url}{self.item.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BudgetItemExpenses.objects.count(), 0)
        
# # Test para el modelo del Plan Único de Cuentas Contables
class AccountantPucAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/accountant_puc/'  # ruta
        self.account = AccountantPuc.objects.create(
            code='1',
            name='Activos',
            nature='Debito',
            father=None,
            type='General',
            level=1
        )     
        
    def test_listar_accounts(self):
        """Debe listar las cuentas del PUC"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Activos")     
        
    def test_crear_account(self):        
        """Debe crear una cuenta del PUC"""
        data = {
            "code": "11",
            "name": "Efectivo y equivalentes al efectivo",
            "nature": "Debito",
            "father": "1",
            "type": "General",
            "level": "2"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)         
        self.assertEqual(AccountantPuc.objects.count(), 2)
        self.assertEqual(AccountantPuc.objects.get(code="11").name, "Efectivo y equivalentes al efectivo")
        
    def test_obtener_detalle_account(self):
        """Debe obtener el detalle de una cuenta del PUC"""
        response = self.client.get(f"{self.url}{self.account.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)      
        self.assertEqual(response.data["code"], "1")
    
    def test_actualizar_account(self):
        """Debe actualizar una cuenta del PUC existente"""
        data = {
            "code": "1",
            "name": "Activos Actualizado",
            "nature": "Debito",
            "father": None,
            "type": "General",
            "level": 1
        }
        response = self.client.put(f"{self.url}{self.account.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.account.refresh_from_db()
        self.assertEqual(self.account.name, "Activos Actualizado")    
    
    def test_eliminar_account(self):
        """Debe eliminar una cuenta del PUC"""
        response = self.client.delete(f"{self.url}{self.account.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  
        self.assertEqual(AccountantPuc.objects.count(), 0)
   
# # Test para el modelo de cuentas de gastos
class ExpenseAccountsAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/expense_accounts/'  # ruta
        self.account = ExpenseAccounts.objects.create(
            budget_code_expenses='A',
            accountant_name='Gastos de funcionamiento'
        )        

    def test_listar_accounts(self):
        """Debe listar las cuentas de gastos"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Gastos de funcionamiento")

    def test_crear_account(self):
        """Debe crear una nueva cuenta de gasto"""
        data = {
            "budget_code_expenses": "A1",
            "accountant_name": "Gastos de personal",
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ExpenseAccounts.objects.count(), 2)
        self.assertEqual(ExpenseAccounts.objects.get(budget_code_expenses="A1").accountant_name, "Gastos de personal")

    def test_obtener_detalle_account(self):
        """Debe obtener el detalle de una cuenta de gasto"""
        response = self.client.get(f"{self.url}{self.account.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["budget_code_expenses"], "A")

    def test_actualizar_account(self):
        """Debe actualizar una cuenta de gasto existente"""
        data = {
            "budget_code_expenses": "A",
            "accountant_name": "Gastos de funcionamiento Actualizado",
        }
        response = self.client.put(f"{self.url}{self.account.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.account.refresh_from_db()
        self.assertEqual(self.account.accountant_name, "Gastos de funcionamiento Actualizado")

    def test_eliminar_account(self):
        """Debe eliminar una cuenta de gasto"""
        response = self.client.delete(f"{self.url}{self.account.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ExpenseAccounts.objects.count(), 0)
        
# Test para el modelo de fuentes de recursos
class SourceResourcesAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/source_resources/'  # ruta
        self.source = SourceResources.objects.create(
            source_name='SGP'
        )        

    def test_listar_sources(self):
        """Debe listar las fuentes de recursos"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "SGP")

    def test_crear_source(self):
        """Debe crear una nueva fuente de recurso"""
        data = {
            "source_name": "Recursos propios",
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(SourceResources.objects.count(), 2)
        self.assertEqual(SourceResources.objects.get(source_name="Recursos propios").source_name, "Recursos propios")

    def test_obtener_detalle_source(self):
        """Debe obtener el detalle de una fuente de recurso"""
        response = self.client.get(f"{self.url}{self.source.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["source_name"], "SGP")

    def test_actualizar_source(self):
        """Debe actualizar una fuente de recurso existente"""
        data = {
            "source_name": "SGP Actualizado",
        }

        response = self.client.put(f"{self.url}{self.source.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.source.refresh_from_db()
        self.assertEqual(self.source.source_name, "SGP Actualizado")

    def test_eliminar_source(self):
        """Debe eliminar una fuente de recurso"""
        response = self.client.delete(f"{self.url}{self.source.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(SourceResources.objects.count(), 0)
        
# Test para el modelo de bancos
class BankAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/bank/'  # ruta
        self.bank = Bank.objects.create(
            bank_name='Banco Agrario'
        )
    
    def test_listar_banks(self):
        """Debe listar los bancos"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Banco Agrario")
        
    def test_crear_bank(self):
        """Debe crear un nuevo banco"""
        data = {
            "bank_name": "Banco de Bogotá",
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Bank.objects.count(), 2)
        self.assertEqual(Bank.objects.get(bank_name="Banco de Bogotá").bank_name, "Banco de Bogotá")
        
    def test_obtener_detalle_bank(self):
        """Debe obtener el detalle de un banco"""
        response = self.client.get(f"{self.url}{self.bank.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["bank_name"], "Banco Agrario")
        
    def test_actualizar_bank(self):
        """Debe actualizar un banco existente"""
        data = {
            "bank_name": "Banco Agrario Actualizado",
        }
        response = self.client.put(f"{self.url}{self.bank.id}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.bank.refresh_from_db()
        self.assertEqual(self.bank.bank_name, "Banco Agrario Actualizado")
        
    def test_eliminar_bank(self):
        """Debe eliminar un banco"""
        response = self.client.delete(f"{self.url}{self.bank.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Bank.objects.count(), 0)      
        
# Test para el modelo de ejecución presupuestal de gastos e ingresos F7
class F7BudgetExecutionExpensesAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/api/f7_budget_execution_expenses/'  # ruta
        self.budget_execution = F7BudgetExecutionExpenses.objects.create(
            id_budget_item_expenses=1,
            id_institution=1,
            id_budget_report=1,
            program_code=ExpenseAccounts.objects.create(
                budget_code_expenses='A',
                accountant_name='Gastos de funcionamiento'
            ),
            initial_appropriation=1000,
            credit=1000,
            countercredit=0,
            postponement=0,
            displacement=0,
            reductions=0,
            additions=0,
            commitment_budget_registration=0,
            obligations=0,
            payments=0,
        )
    def test_listar_budget_executions(self):
        """Debe listar las ejecuciones presupuestales F7"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)