from rest_framework import serializers

from .models import (
    Institution, 
    BudgetReport, 
    BudgetItemRevenue,
    BudgetItemExpenses,
    AccountantPuc,
    ExpenseAccounts,
    SourceResources,
    Bank,
    F7BudgetExecutionExpenses,
    F11AccountsPayable,
    F13Hiring,
    Ief02RevenueStatement,
    Ief04PaymentsRelationship,
    RevenueBudget,
    ChangesRevenuePeriod,
    CumulativeChangesRevenue,
    RevenueExecution,
    ExpensesBudget,
    ChangesExpensesPeriod,
    CumulativeChangesExpenses,
    ExpensesExecution,
    PaymentObligations,
    PaymentRelationship,
    F1ChartOfAccounts,
    AccountPurpose,
    BankAccount,
    F3BankAccountReport,
    InsuranceCompany,
    F4InsurancePolicy,
    F5PropertyPlantEquipment,
    F5BPropertyInventory,
    F6RevenueExecution
)

# Serializer para modelo de instituciones
class InstitutionSerializer(serializers.ModelSerializer):
    """
    Serializer para las instituciones.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = Institution
        fields = '__all__'
        read_only_fields = ['id']

# Serializer para modelo el perido de reporte de información presupuestal
class BudgetReportSerializer(serializers.ModelSerializer):
    """
    Serializer para el reporte de presupuesto.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = BudgetReport
        fields = '__all__'
        read_only_fields = ['id']

# Serializer para modelo de rubros presupuestales de ingresos
class BudgetItemRevenueSerializer(serializers.ModelSerializer):
    """
    Serializer para el rubro presupuestal de ingresos.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = BudgetItemRevenue
        fields = '__all__'
        read_only_fields = ['id']   
        
        def validate_budget_code(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value

# Serializer para modelo de rubros presupuestales de gastos
class BudgetItemExpensesSerializer(serializers.ModelSerializer):
    """
    Serializer para el rubro presupuestal de gastos.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = BudgetItemExpenses
        fields = '__all__'
        read_only_fields = ['id']       
        
        def validate_budget_codemExpenses(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value

# Serializer para modelo de plan contable
class AccountantPucSerializer(serializers.ModelSerializer):
    """
    Serializer para el plan contable.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = AccountantPuc
        fields = '__all__'
        read_only_fields = ['id']       
        
        def validate_code(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value

# Serializer para modelo de cuentas de gastos
class ExpenseAccountsSerializer(serializers.ModelSerializer):
    """
    Serializer para las cuentas de gastos.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = ExpenseAccounts
        fields = '__all__'
        read_only_fields = ['id']
        
    def validate_budget_codesRevenue(self, value):
        """Valida que el código de presupuesto no esté vacío"""
        if not value.strip():
            raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
        return value

# Serializer para modelo de fuentes de recursos
class SourceResourcesSerializer(serializers.ModelSerializer):    
    """
    Serializer para las fuentes de recursos.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = SourceResources
        fields = '__all__'
        read_only_fields = ['id']   
        
        def validate_source_name(self, value):
            """Valida que el nombre de la fuente no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El nombre de la fuente no puede estar vacío")
            return value

# Serializer para modelo de bancos
class BankSerializer(serializers.ModelSerializer):    
    """
    Serializer para los bancos.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = Bank
        fields = '__all__'
        read_only_fields = ['id']   
        
        def validate_bank_name(self, value):
            """Valida que el nombre del banco no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El nombre del banco no puede estar vacío")
            return value

# Serializer para modelo de ejecución presupuestal de gastos (Formulario 7)
class F7BudgetExecutionExpensesSerializer(serializers.ModelSerializer):   
    """
    Serializer para la ejecución presupuestal de gastos (Formulario 7).
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = F7BudgetExecutionExpenses
        fields = '__all__'
        read_only_fields = ['id']   
        
        def validate_budget_codenExpenses(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value        

# Serializer para modelo de cuentas por pagar (Formulario 11)
class F11AccountsPayableSerializer(serializers.ModelSerializer):    
    """
    Serializer para las cuentas por pagar (Formulario 11).
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = F11AccountsPayable
        fields = '__all__'
        read_only_fields = ['id']   
        
        def validate_budget_codesRevenue(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value

# Serializer para modelo de contratación (Formulario 13)
class F13HiringSerializer(serializers.ModelSerializer):    
    """
    Serializer para la contratación.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = F13Hiring
        fields = '__all__'
        read_only_fields = ['id']       
        
        def validate_budget_codesRevenue(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value

# Serializer para modelo de relación de ingresos (Ief02)        
class Ief02RevenueStatementSerializer(serializers.ModelSerializer): 
    """
    Serializer para el estado de ingresos (Ief02).
    Maneja la conversión entre instancias del modelo y JSON.
    """

    class Meta:
        model = Ief02RevenueStatement
        fields = '__all__'
        read_only_fields = ['id']

        def validate_budget_code_revenue(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value

# Serializer para modelo de relación de pagos (Ief04)
class Ief04PaymentsRelationshipSerializer(serializers.ModelSerializer): 
    """
    Serializer para el estado de pagos (Ief04).
    Maneja la conversión entre instancias del modelo y JSON.
    """

    class Meta:
        model = Ief04PaymentsRelationship
        fields = '__all__'
        read_only_fields = ['id']

        def validate_budget_codesRevenue(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")            
            return value

#! Serializer para modelos de cierre presupuestal de ingresos

#* Serializer para modelo de presupuesto de ingresos
class RevenueBudgetSerializer(serializers.ModelSerializer):
    """
    Serializer para el presupuesto de ingresos.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = RevenueBudget
        fields = '__all__'
        read_only_fields = ['id']
        
        def validate_budget_code(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value

#* Serializer para modelo de modificaciones del periodo - ingresos      
class ChangesRevenuePeriodSerializer(serializers.ModelSerializer):
    """
    Serializer para modificaciones del periodo - ingresos.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = ChangesRevenuePeriod
        fields = '__all__'
        read_only_fields = ['id']
        
        def validate_budget_code(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value    

#* Serializer para modelo de modificaciones acumuladas - ingreos
class CumulativeChangesRevenueSerializer(serializers.ModelSerializer):
    """
    Serializer para modificaciones acumuladas - ingresos.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = CumulativeChangesRevenue
        fields = '__all__'
        read_only_fields = ['id']
        
        def validate_budget_code(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value    
        
#* Serializer para modelo de ejecución de ingresos        
class RevenueExecutionSerializer(serializers.ModelSerializer):
    """
    Serializer para la ejecución de ingresos.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = RevenueExecution
        fields = '__all__'
        read_only_fields = ['id']
        
        def validate_budget_code(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value

#! Serializers para el cierre presupuestal de gastos        

#* Serializer para modelo de presupuesto de gastos
class ExpensesBudgetSerializer(serializers.ModelSerializer):
    """
    Serializer para el presupuesto de gastos.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = ExpensesBudget
        fields = '__all__'
        read_only_fields = ['id']
        
        def validate_budget_codesRevenue(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value

#* Serializer para modelo de modificaciones del periodo - gastos
class ChangesExpensesPeriodSerializer(serializers.ModelSerializer):
    """
    Serializer para modificaciones del periodo - gastos.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = ChangesExpensesPeriod
        fields = '__all__'
        read_only_fields = ['id']
        
        def validate_budget_code(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value    

#* Serializer para modelo de modificaciones acumuladas - gastos
class CumulativeChangesExpensesSerializer(serializers.ModelSerializer):
    """
    Serializer para modificaciones acumuladas - gastos.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = CumulativeChangesExpenses
        fields = '__all__'
        read_only_fields = ['id']
        
        def validate_budget_code(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value    

#* Serializer para modelo de ejecución de gastos
class ExpensesExecutionSerializer(serializers.ModelSerializer):
    """
    Serializer para la ejecución de gastos.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = ExpensesExecution
        fields = '__all__'
        read_only_fields = ['id']
        
        def validate_budget_code(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value

#* Serializer para modelo de obligaciones de pago
class PaymentObligationsSerializer(serializers.ModelSerializer):
    """
    Serializer para la obligaciones de pago.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = PaymentObligations
        fields = '__all__'
        read_only_fields = ['id']
        
        def validate_budget_code(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value

#* Serializer para modelo de relación de pagos
class PaymentRelationshipSerializer(serializers.ModelSerializer):
    """
    Serializer para la relación de pagos.
    Maneja la conversión entre instancias del modelo y JSON.
    """
    
    class Meta:
        model = PaymentRelationship
        fields = '__all__'
        read_only_fields = ['id']
        
        def validate_budget_code(self, value):
            """Valida que el código de presupuesto no esté vacío"""
            if not value.strip():
                raise serializers.ValidationError("El código de presupuesto no puede estar vacío")
            return value

# Serializer para F1 - Catálogo de Cuentas
class F1ChartOfAccountsSerializer(serializers.ModelSerializer):
    """
    Serializer para el formato F1 - Catálogo de Cuentas.
    Incluye información relacionada de la cuenta PUC.
    """
    # Campos de solo lectura para mostrar información completa
    account_code = serializers.CharField(source='id_account.code', read_only=True)
    account_name = serializers.CharField(source='id_account.name', read_only=True)
    institution_name = serializers.CharField(source='id_institution.name', read_only=True)
    report_period = serializers.CharField(source='id_report.__str__', read_only=True)
    
    class Meta:
        model = F1ChartOfAccounts
        fields = '__all__'
        read_only_fields = ['id_detail_f1', 'created_at', 'updated_at']
    
    def validate(self, data):
        """Validación de integridad de saldos"""
        if 'debit' in data and 'credit' in data:
            if data['debit'] < 0:
                raise serializers.ValidationError("El débito no puede ser negativo")
            if data['credit'] < 0:
                raise serializers.ValidationError("El crédito no puede ser negativo")
        return data

# Serializer para propósito de cuenta bancaria
class AccountPurposeSerializer(serializers.ModelSerializer):
    """
    Serializer para el propósito o destinación de cuentas bancarias.
    """
    
    class Meta:
        model = AccountPurpose
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

# Serializer para cuentas bancarias
class BankAccountSerializer(serializers.ModelSerializer):
    """
    Serializer para cuentas bancarias.
    Incluye información relacionada del banco, PUC y propósito.
    """
    bank_name = serializers.CharField(source='bank.name', read_only=True)
    accounting_code_value = serializers.CharField(source='accounting_code.code', read_only=True)
    accounting_name = serializers.CharField(source='accounting_code.name', read_only=True)
    purpose_description = serializers.CharField(source='purpose.description', read_only=True)
    institution_name = serializers.CharField(source='id_institution.name', read_only=True)
    
    class Meta:
        model = BankAccount
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_account_number(self, value):
        """Valida que el número de cuenta no esté vacío"""
        if not value.strip():
            raise serializers.ValidationError("El número de cuenta no puede estar vacío")
        return value

# Serializer para F3 - Reporte de Cuentas Bancarias
class F3BankAccountReportSerializer(serializers.ModelSerializer):
    """
    Serializer para el formato F3 - Cuentas Bancarias.
    Incluye información completa de la cuenta bancaria.
    """
    # Información de la cuenta bancaria
    bank_name = serializers.CharField(source='bank_account.bank.name', read_only=True)
    account_number = serializers.CharField(source='bank_account.account_number', read_only=True)
    accounting_code = serializers.CharField(source='bank_account.accounting_code.code', read_only=True)
    purpose = serializers.CharField(source='bank_account.purpose.description', read_only=True)
    institution_name = serializers.CharField(source='bank_account.id_institution.name', read_only=True)
    report_period = serializers.CharField(source='id_report.__str__', read_only=True)
    
    class Meta:
        model = F3BankAccountReport
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate(self, data):
        """Validaciones de integridad"""
        if 'incomes' in data and data['incomes'] < 0:
            raise serializers.ValidationError("Los ingresos no pueden ser negativos")
        return data

# Serializer para entidades aseguradoras
class InsuranceCompanySerializer(serializers.ModelSerializer):
    """
    Serializer para entidades aseguradoras.
    """
    
    class Meta:
        model = InsuranceCompany
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

# Serializer para F4 - Pólizas de Aseguramiento
class F4InsurancePolicySerializer(serializers.ModelSerializer):
    """
    Serializer para el formato F4 - Pólizas de Aseguramiento.
    Incluye información de la aseguradora y validaciones de fechas.
    """
    insurance_company_name = serializers.CharField(source='insurance_company.name', read_only=True)
    institution_name = serializers.CharField(source='id_institution.name', read_only=True)
    report_period = serializers.CharField(source='id_report.__str__', read_only=True)
    department_display = serializers.CharField(source='get_department_display', read_only=True)
    
    class Meta:
        model = F4InsurancePolicy
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate(self, data):
        """Validaciones de integridad"""
        if 'initial_validity' in data and 'final_validity' in data:
            if data['initial_validity'] >= data['final_validity']:
                raise serializers.ValidationError(
                    "La fecha de vigencia inicial debe ser anterior a la final"
                )
        
        if 'insured_value' in data and data['insured_value'] <= 0:
            raise serializers.ValidationError("El valor asegurado debe ser mayor a cero")
        
        return data

# Serializer para F5 - Propiedad, Planta y Equipo (movimientos)
class F5PropertyPlantEquipmentSerializer(serializers.ModelSerializer):
    """
    Serializer para el formato F5 - Movimientos de Propiedad, Planta y Equipo.
    Incluye información de la cuenta contable.
    """
    accounting_code_value = serializers.CharField(source='accounting_code.code', read_only=True)
    accounting_name = serializers.CharField(source='accounting_code.name', read_only=True)
    institution_name = serializers.CharField(source='id_institution.name', read_only=True)
    report_period = serializers.CharField(source='id_report.__str__', read_only=True)
    concept_display = serializers.CharField(source='get_concept_display', read_only=True)
    
    class Meta:
        model = F5PropertyPlantEquipment
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate(self, data):
        """Validaciones de integridad"""
        if 'value' in data and data['value'] <= 0:
            raise serializers.ValidationError("El valor debe ser mayor a cero")
        return data

# Serializer para F5B - Inventario de Propiedad, Planta y Equipo
class F5BPropertyInventorySerializer(serializers.ModelSerializer):
    """
    Serializer para el formato F5B - Inventario de Propiedad, Planta y Equipo.
    Incluye campo calculado de saldo final.
    """
    accounting_code_value = serializers.CharField(source='accounting_code.code', read_only=True)
    accounting_name = serializers.CharField(source='accounting_code.name', read_only=True)
    institution_name = serializers.CharField(source='id_institution.name', read_only=True)
    report_period = serializers.CharField(source='id_report.__str__', read_only=True)
    final_balance = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    
    class Meta:
        model = F5BPropertyInventory
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate(self, data):
        """Validaciones de integridad"""
        if 'initial_balance' in data and data['initial_balance'] < 0:
            raise serializers.ValidationError("El saldo inicial no puede ser negativo")
        if 'entries' in data and data['entries'] < 0:
            raise serializers.ValidationError("Las entradas no pueden ser negativas")
        if 'exits' in data and data['exits'] < 0:
            raise serializers.ValidationError("Las salidas no pueden ser negativas")
        return data

# Serializer para F6 - Ejecución Presupuestal de Ingresos
class F6RevenueExecutionSerializer(serializers.ModelSerializer):
    """
    Serializer para el formato F6 - Ejecución Presupuestal de Ingresos.
    Incluye campos calculados de presupuesto final y porcentaje de ejecución.
    """
    budget_code = serializers.CharField(source='budget_item_revenue.code', read_only=True)
    budget_name = serializers.CharField(source='budget_item_revenue.account_name', read_only=True)
    institution_name = serializers.CharField(source='id_institution.name', read_only=True)
    report_period = serializers.CharField(source='id_report.__str__', read_only=True)
    final_budget = serializers.DecimalField(max_digits=15, decimal_places=2, read_only=True)
    execution_percentage = serializers.DecimalField(max_digits=5, decimal_places=2, read_only=True)
    
    class Meta:
        model = F6RevenueExecution
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate(self, data):
        """Validaciones de integridad"""
        if 'initial_budget' in data and data['initial_budget'] < 0:
            raise serializers.ValidationError("El presupuesto inicial no puede ser negativo")
        if 'additions' in data and data['additions'] < 0:
            raise serializers.ValidationError("Las adiciones no pueden ser negativas")
        if 'reductions' in data and data['reductions'] < 0:
            raise serializers.ValidationError("Las reducciones no pueden ser negativas")
        if 'collection' in data and data['collection'] < 0:
            raise serializers.ValidationError("El recaudo no puede ser negativo")
        return data