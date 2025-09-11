import uuid
from django.db import models

# Create your models here.

# Microservicio Institusiones
"""class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)"""

# Modelo de rubros presupuestales de ingresos
class BudgetItemRevenue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100) # verbose_name="Codigo", help_text="Codigo del rubro presupuestal"
    level = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    accountant_name = models.CharField(max_length=100)
    father = models.CharField(max_length=100)

# Modelo de rubros presupuestales de gastos
class BudgetItemExpenses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100)
    level = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    accountant_name = models.CharField(max_length=100)
    father = models.CharField(max_length=100)
    
# Modelo de Plan contable
class AccountantPuc(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    nature = models.CharField(max_length=100, choices=(('DEBITO', 'Debito'), ('CREDITO', 'Credito')))
    subaccount = models.CharField(max_length=100, blank=True, null=True)
    account = models.CharField(max_length=100, blank=True, null=True)
    group = models.CharField(max_length=100, blank=True, null=True)
    class_puc = models.CharField(max_length=100, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)