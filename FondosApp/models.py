import uuid
from django.db import models

# Create your models here.

# Microservicio Institusiones
class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Nombre", help_text="Nombre de la institucion") 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")
    
    def __str__(self):
        return f'{self.name}'
    
# Periodo de reporte de información presupuestal
class BudgetReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    period_type = models.CharField(max_length=20,  choices=(('Semestral', 'Semestral'), ('Trimestral', 'Trimestral'), ('Mensual', 'Mensual')), verbose_name="Tipo de periodo", help_text="Tipo de periodo")
    period_number = models.IntegerField(verbose_name="Número de periodo", help_text="Número de periodo")
    year = models.IntegerField(verbose_name="Año", help_text="Año")
    start_date = models.DateField(blank=True, null=True, verbose_name="Fecha de inicio", help_text="Fecha de inicio")
    end_date = models.DateField(blank=True, null=True, verbose_name="Fecha de fin", help_text="Fecha de fin")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")
    
    def __str__(self):
        return f'{self.period_type} - {self.period_number} - {self.year}'

# Modelo de rubros presupuestales de ingresos
class BudgetItemRevenue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100, verbose_name="Código", help_text="Código del rubro presupuestal de ingresos")
    level = models.CharField(max_length=100, verbose_name="Nivel", help_text="Nivel del rubro presupuestal de ingresos")
    type = models.CharField(max_length=100, verbose_name="Tipo", help_text="Tipo del rubro presupuestal de ingresos") # A o C
    account_name = models.CharField(max_length=100, verbose_name="Nombre Contable", help_text="Nombre contable del rubro presupuestal de ingresos")
    father = models.CharField(max_length=100, null=True, blank=True, verbose_name="Padre", help_text="Padre del rubro presupuestal de ingresos")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")
    
    def __str__(self):
        return f'{self.code} - {self.account_name}'

# Modelo de rubros presupuestales de gastos
class BudgetItemExpenses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100, verbose_name="Código", help_text="Código del rubro presupuestal de gastos")
    level = models.CharField(max_length=100, verbose_name="Nivel", help_text="Nivel del rubro presupuestal de gastos")
    type = models.CharField(max_length=100, choices=(('A', 'A'), ('C', 'C')), verbose_name="Tipo", help_text="Tipo del rubro presupuestal de gastos") # A o C
    account_name = models.CharField(max_length=100, verbose_name="Nombre Contable", help_text="Nombre contable del rubro presupuestal de gastos")
    father = models.CharField(max_length=100, null=True, blank=True, verbose_name="Padre", help_text="Padre del rubro presupuestal de gastos")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")    
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")

    def __str__(self):
        return f'{self.code} - {self.account_name}'
    
# Modelo de Plan contable
class AccountantPuc(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100, verbose_name="Código", help_text="Código del plan contable")
    name = models.CharField(max_length=100, verbose_name="Nombre", help_text="Nombre del plan contable")
    nature = models.CharField(max_length=100, verbose_name="Naturaleza", help_text="Naturaleza del plan contable") # Debito o Credito
    father = models.CharField(max_length=100, blank=True, null=True, verbose_name="Padre", help_text="Padre del plan contable")
    type = models.CharField(max_length=100, verbose_name="Tipo", help_text="Tipo del plan contable") # General o Detalle
    level = models.IntegerField(blank=True, null=True, verbose_name="Nivel", help_text="Nivel del plan contable")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")
    
    def __str__(self):
        return f'{self.code} - {self.name} - {self.father} - {self.type} - {self.level}'
    
# Modelo de cuentas de gastos
class ExpenseAccounts(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    budget_code_expenses = models.CharField(max_length=100, verbose_name="Código de Cuenta", help_text="Código para Presupuesto de Gastos")
    accountant_name = models.CharField(max_length=100, verbose_name="Nombre Contable", help_text="Nombre contable")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")
    
    def __str__(self):
        return f'{self.budget_code_expenses} - {self.accountant_name}'

# Modelo de fuente de recursos
class SourceResources(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source_name = models.CharField(max_length=100, verbose_name="Fuente nombre", help_text="Nombre de la fuente de recursos")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")
    
    def __str__(self):
        return f'{self.source_name}'

# Modelo de bancos
class Bank(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bank_name = models.CharField(max_length=100, verbose_name="Nombre Banco", help_text="Nombre del banco")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")
    
    def __str__(self):
        return f'{self.bank_name}'

# Modelo de ejecución presupuestal de gastos e ingresos F7
class F7BudgetExecutionExpenses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_budget_item_expenses = models.ForeignKey(BudgetItemExpenses, on_delete=models.PROTECT, verbose_name="Detalle presupuestal de gastos", help_text="Detalle presupuestal de gastos asociado")
    id_institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name="Institucion", help_text="Institucion asociada")
    id_budget_report = models.ForeignKey(BudgetReport, on_delete=models.PROTECT, verbose_name="Perido de reporte presupuestal", help_text="Perido de reporte presupuestal asociado")    
    program_code = models.ForeignKey(ExpenseAccounts, on_delete=models.PROTECT, verbose_name="Programa", help_text="Programa asociado")
    
    initial_appropriation = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Apropiación Inicial", help_text="Apropiación inicial")
    credit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Crédito", help_text="Crédito")
    countercredit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Crédito Contrario", help_text="Crédito contrario")
    postponement = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Aplazamiento", help_text="Aplazamiento")
    displacement = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Desplazamiento", help_text="Desplazamiento")
    reductions = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Reducciones", help_text="Reducciones")
    additions = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Adiciones", help_text="Adiciones")
    commitment_budget_registration = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Compromisos Registro Presupuestal", help_text="Compromisos de registro presupuestal")
    obligations = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Obligaciones", help_text="Obligaciones")
    payments = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Pagos", help_text="Pagos")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")   
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")
    
    def __str__(self):
        return f'{self.id_budget_item_expenses} - {self.id_institution} - {self.program_code}'

# Modelo de cuentas por pagar F11
class F11AccountsPayable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_budget_item_expenses = models.ForeignKey(BudgetItemExpenses, on_delete=models.PROTECT, verbose_name="Rubro Presupuestal de Gastos", help_text="Rubro presupuestal de gastos asociado")
    id_institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name="Institucion", help_text="Institucion asociada")
    id_budget_report = models.ForeignKey(BudgetReport, on_delete=models.PROTECT, verbose_name="Perido de reporte presupuestal", help_text="Perido de reporte presupuestal asociado")
    
    description = models.CharField(max_length=100, verbose_name="Descripción", help_text="Descripción")
    account_payable = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cuenta por Pagar", help_text="Cuenta por pagar")
    cancelation_certificate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Acta de Cancelación", help_text="Acta de cancelación")
    payment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Pago", help_text="Pago")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")
    
    def __str__(self):
        return f'{self.id_budget_item_expenses} - {self.id_institution} - {self.description}'

# Modelo de formato de contratación F13
class F13Hiring(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_budget_item_expenses = models.ForeignKey(BudgetItemExpenses, on_delete=models.PROTECT, verbose_name="Rubro Presupuestal de Gastos", help_text="Rubro presupuestal de gastos asociado")
    id_institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name="Institucion", help_text="Institucion asociada")
    id_budget_report = models.ForeignKey(BudgetReport, on_delete=models.PROTECT, verbose_name="Perido de reporte presupuestal", help_text="Perido de reporte presupuestal asociado")    
    source_resources = models.ForeignKey(SourceResources, on_delete=models.PROTECT, verbose_name="Fuente de Recursos", help_text="Fuente de recursos")
    class_h = models.ForeignKey(ExpenseAccounts, on_delete=models.PROTECT, verbose_name="Cuenta gastos", help_text="Cuenta de gastos")
    
    contract_number = models.CharField(max_length=100, verbose_name="Número de Contrato", help_text="Número de contrato")
    object = models.CharField(max_length=100, verbose_name="Objeto", help_text="Objeto")
    contract_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor del Contrato", help_text="Valor del contrato")
    contractor_name = models.CharField(max_length=100, verbose_name="Nombre del Contratista", help_text="Nombre del contratista")
    nit_cc_contractor = models.CharField(max_length=100, verbose_name="NIT/CC del Contratista", help_text="NIT/CC del contratista")
    budget_unavailability = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Disponibilidad Presupuestal", help_text="Disponibilidad presupuestal")
    value_availability = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Disponibilidad Valor", help_text="Disponibilidad valor")
    signature_date = models.DateField(verbose_name="Fecha de Firma", help_text="Fecha de firma")
    contract_form = models.CharField(max_length=100, verbose_name="Formulario de Contrato", help_text="Formulario de contrato")
    budget_registration_date = models.DateField(verbose_name="Fecha de Registro Presupuestal", help_text="Fecha de registro presupuestal")
    budget_registration_number = models.CharField(max_length=100, verbose_name="Número de Registro Presupuestal", help_text="Número de registro presupuestal")
    budget_record_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor de Registro Presupuestal", help_text="Valor de registro presupuestal")
    date_approval_single_guarantee = models.DateField(blank=True, null=True, verbose_name="Fecha de Aprobación Guarantee", help_text="Fecha de aprobación guarantee")
    start_date = models.DateField(verbose_name="Fecha de Inicio", help_text="Fecha de inicio")
    contract_term = models.CharField(max_length=100, verbose_name="Periodo de Contrato", help_text="Periodo de contrato")
    addition_date = models.DateField(blank=True, null=True, verbose_name="Fecha de Adición", help_text="Fecha de adición")
    addtion_term = models.CharField(max_length=100, blank=True, null=True, verbose_name="Periodo de Adición", help_text="Periodo de adición")
    addition_value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Valor de Adición", help_text="Valor de adición")
    value_payments_made = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor de Pagos Realizados", help_text="Valor de pagos realizados")
    completion_date = models.DateField(verbose_name="Fecha de Terminación", help_text="Fecha de terminación")
    sattlement_date = models.DateField(verbose_name="Fecha de Liquidación", help_text="Fecha de liquidación")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")
    
    def __str__(self):
        return f'{self.contract_number} - {self.contractor_name} - {self.id_institution}'
    
# Modelo de informes y anexos generales F31
"""class F31GeneralAnnexes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name="Institucion", help_text="Institucion asociada")
    id_budget_report = models.ForeignKey(BudgetReport, on_delete=models.PROTECT, verbose_name="Perido de reporte presupuestal", help_text="Perido de reporte presupuestal asociado")
    
    report_title = models.CharField(max_length=100, verbose_name="Título del Informe", help_text="Título del informe")
    responsible = models.CharField(max_length=100, verbose_name="Responsable", help_text="Responsable")
    number_pages = models.IntegerField(verbose_name="Número de Fólios", help_text="Número de Fólios")
    comments = models.TextField(blank=True, null=True, verbose_name="Observaciones", help_text="Observaciones")
    
    def __str__(self):
        return f'{self.id_institution} - {self.report_title}'
"""

# Modelo de relación de ingresos IEF02
class Ief02RevenueStatement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_budget_item_revenue = models.ForeignKey(BudgetItemRevenue, on_delete=models.PROTECT, verbose_name="Rubro Presupuestal de Ingresos", help_text="Rubro presupuestal de ingresos asociado")
    id_institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name="Institucion", help_text="Institucion asociada")
    id_budget_report = models.ForeignKey(BudgetReport, on_delete=models.PROTECT, verbose_name="Perido de reporte presupuestal", help_text="Perido de reporte presupuestal asociado")
    
    collection_date = models.DateField(verbose_name="Fecha de Recaudo", help_text="Fecha de recaudo")
    detail= models.CharField(max_length=100, verbose_name="Detalle", help_text="Detalle")
    receipt_bank = models.ForeignKey(Bank, on_delete=models.PROTECT, verbose_name="Recibo de", help_text="Recibo de")
    value= models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor", help_text="Valor")
    bank_account_number = models.CharField(max_length=100, verbose_name="Número de Cuenta Bancaria", help_text="Número de cuenta bancaria")
    bank= models.CharField(max_length=100, verbose_name="Banco", help_text="Banco") # Revisar problema de bancos
    revenue_resources = models.ForeignKey(SourceResources, on_delete=models.PROTECT, verbose_name="Fuente de Ingresos", help_text="Fuente de ingresos")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")
    
    def __str__(self):
        return f'{self.id_budget_item_revenue} - {self.id_institution} - {self.collection_date}'

# Modelo de relación de pagos IEF04
class Ief04PaymentsRelationship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_budget_item_expenses = models.ForeignKey(BudgetItemExpenses, on_delete=models.PROTECT, verbose_name="Rubro Presupuestal de Gastos", help_text="Rubro presupuestal de gastos asociado")
    id_institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name="Institucion", help_text="Institucion asociada")
    id_budget_report = models.ForeignKey(BudgetReport, on_delete=models.PROTECT, verbose_name="Perido de reporte presupuestal", help_text="Perido de reporte presupuestal asociado")
    
    collection_date = models.DateField(verbose_name="Fecha de Pago", help_text="Fecha de pago")
    receipt_number = models.CharField(max_length=100, verbose_name="Comprobante N°", help_text="Número de recibo")
    detail = models.CharField(max_length=100, verbose_name="Detalle", help_text="Detalle")
    beneficiary = models.CharField(max_length=100, verbose_name="Beneficiario", help_text="Beneficiario")
    cc_nit = models.CharField(max_length=100, verbose_name="Cédula o NIT", help_text="Cédula o NIT")
    total_value_receipt = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Total Comprobante", help_text="Valor total del comprobante")
    withholdings = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Descuentos", help_text="Descuentos")
    discounts = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Descuentos", help_text="Descuentos")
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT, verbose_name="Banco", help_text="Banco")
    account_number = models.CharField(max_length=100, verbose_name="Número de Cuenta", help_text="Número de cuenta")
    check_number = models.CharField(max_length=100, verbose_name="Cheque Número", help_text="Cheque número")
    funding_source = models.ForeignKey(SourceResources, on_delete=models.PROTECT, verbose_name="Fuente de Financiación", help_text="Fuente de financiación")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")
    
    def __str__(self):
        return f'{self.id_budget_item_expenses} - {self.id_institution} - {self.collection_date}'

#! Modelos para el cirre presupuestal de ingreos

# Modelo de presupuesto de ingresos
class RevenueBudget(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name="Institución", help_text="Institución asociada") 
    id_budget_item_revenue = models.ForeignKey(BudgetItemRevenue, on_delete=models.PROTECT, verbose_name="Rubro presupuestal de ingresos", help_text="Rubro presupuestal de ingresos asociado")
    period = models.CharField(max_length=100, verbose_name="Periodo", help_text="Periodo")
    initial_appropriation = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Apropiación Inicial", help_text="Apropiación inicial")
    final_appropriation = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Apropiación Final", help_text="Apropiación final")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")
    
    def __str__(self):
        return f'{self.id_institution} - {self.period}'

    # class Meta:
    #     db_table = 'revenue_budget'

# Modelo de modificaciones del perido - ingresos
class ChangesRevenuePeriod(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_revenue_budget = models.ForeignKey(
        RevenueBudget, on_delete=models.PROTECT, db_column='id_revenue_budget'
    ) 
    addition = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Adiciones', help_text='Adiciones')
    reduction = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Reducciones', help_text='Reducciones')
    credit_transfer = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Transferencias de Crédito', help_text='Transferencias de Crédito')
    countercredit_transfer = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Transferencias de Contracrédito', help_text='Transferencias de Contracrédito')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")

    def __str__(self):
        return f'{self.id_revenue_budget} - {self.addition} - {self.reduction} - {self.credit_transfer} - {self.countercredit_transfer}'

# Modelo de modificaciones acumuladas - ingresos
class CumulativeChangesRevenue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_revenue_budget = models.ForeignKey(
        RevenueBudget, on_delete=models.PROTECT, verbose_name='Presupuesto de Ingresos', help_text='Presupuesto de Ingresos asociado'
    ) 
    accumulated_additions = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Adiciones Acumuladas', help_text='Adiciones Acumuladas')
    accumulated_reductions = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Reducciones Acumuladas', help_text='Reducciones Acumuladas')
    transfer_accumulated_credits = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Traslado de creditos acumulados', help_text='Traslado de creditos acumulados')
    transfer_accumulated_countercredits = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Traslado de contracréditos acumulados', help_text='Traslado de contracréditos acumulados')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")

    def __str__(self):
        return f'{self.id_revenue_budget} - {self.accumulated_additions} - {self.accumulated_reductions} - {self.transfer_accumulated_credits} - {self.transfer_accumulated_counterdebits}'

# Modelo de ejecución de ingresos
class RevenueExecution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_revenue_budget = models.ForeignKey(
        RevenueBudget, on_delete=models.PROTECT, verbose_name='Presupuesto de Ingresos', help_text='Presupuesto de Ingresos asociado'
    )
    monthly_revenue_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor de Ingresos Mensual", help_text="Valor mensual de ingresos")
    accumulated_revenue = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ingresos acumulados", help_text="Ingresos acumulados")
    income_receivable = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Ingresos por recibir", help_text="Ingresos por recibir")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")

    def __str__(self):
        return f'{self.id_revenue_budget} - {self.monthly_revenue_value} - {self.accumulated_revenue} - {self.income_receivable}'
    
#! Modelos para el cierre presupuestal de gastos

# Modelo de presupuesto de gastos
class ExpensesBudget(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name="Institución", help_text="Institución asociada")
    id_budget_item_expenses = models.ForeignKey(BudgetItemExpenses, on_delete=models.PROTECT, verbose_name="Rubro presupuestal de gastos", help_text="Rubro presupuestal de gastos asociado")
    period = models.CharField(max_length=100, verbose_name="Periodo", help_text="Periodo")
    initial_appropriation = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Apropiación Inicial", help_text="Apropiación inicial")
    final_appropriation = models.DecimalField(max_digits=10, null=True, blank=True, decimal_places=2, verbose_name="Apropiación Final", help_text="Apropiación final")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")

    def __str__(self):
        return f"{self.period} - {self.id_budget_item_expenses}"

# Modelo de modificaciones del periodo - gastos
class ChangesExpensesPeriod(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_expenses_budget = models.ForeignKey(ExpensesBudget, on_delete=models.PROTECT, verbose_name="Presupuesto de Gastos", help_text="Presupuesto de Gastos asociado")
    addition = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Adiciones", help_text="Adiciones")
    reduction = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Reducciones", help_text="Reducciones")
    credits = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Créditos", help_text="Créditos")
    countercredits = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Contracréditos", help_text="Contracréditos")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")

    def __str__(self):
        return f"Changes for {self.id_expenses_budget.period}"

# Modelo de modificaciones acumuladas - gastos
class CumulativeChangesExpenses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_expenses_budget = models.ForeignKey(ExpensesBudget, on_delete=models.PROTECT, verbose_name="Presupuesto de Gastos", help_text="Presupuesto de Gastos asociado")
    accumulated_additions = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Adiciones Acumuladas", help_text="Adiciones acumuladas")
    accumulated_reductions = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Reducciones Acumuladas", help_text="Reducciones acumuladas")
    accumulated_credits = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Creditos Acumulados", help_text="Creditos acumulados")
    accumulated_countercredits = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Contracreditos Acumulados", help_text="Contracreditos acumulados")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")

    def __str__(self):
        return f"Cumulative changes for {self.id_revenue_budget.period}"

# Modelo de ejecución de gastos
class ExpensesExecution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_revenue_budget = models.ForeignKey(ExpensesBudget, on_delete=models.PROTECT, verbose_name="Presupuesto de Gastos", help_text="Presupuesto de Gastos asociado")
    certificates_period = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Certificados del Periodo", help_text="Certificados del periodo")
    accumulated_certificates = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Certificados Acumulados", help_text="Certificados acumulados")
    available_balance = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Balance Disponible", help_text="Balance disponible")
    period_commitments = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Compromisos del Periodo", help_text="Compromisos del periodo")
    accumulated_commitments = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Compromisos Acumulados", help_text="Compromisos acumulados")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")

    def __str__(self):
        return f"Execution for {self.id_revenue_budget.period}"

# Modelo de obligaciones de pago
class PaymentObligations(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_revenue_budget = models.ForeignKey(ExpensesBudget, on_delete=models.PROTECT, verbose_name="Presupuesto de Gastos", help_text="Presupuesto de Gastos asociado")
    open_positions = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Disponibilidades de Pago Abiertas", help_text="Disponibilidades abiertas")
    obligations_period = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Obligaciones del Periodo", help_text="Obligaciones del periodo")
    accumulated_obligations = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Obligaciones Acumuladas", help_text="Obligaciones acumuladas")
    period_payments = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Pagos del Periodo", help_text="Pagos del periodo")
    accumulated_payments = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Pagos Acumulados", help_text="Pagos acumulados")
    balance_payable = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Saldo por pagar", help_text="Saldo por pagar")
    reservations = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Reservas", help_text="Reservas")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")

    def __str__(self):
        return f"Payments for {self.id_revenue_budget.period}"

# Modelo de relaciones de pagos
class PaymentRelationship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name="Institución", help_text="Institución asociada")
    date = models.DateField(verbose_name="Fecha", help_text="Fecha")
    no_exit_receipt = models.CharField(max_length=100, verbose_name="No. Comprobante de Egreso", help_text="Número de comprobante de egreso")
    accounting_account = models.CharField(max_length=100, verbose_name="Cuenta Contable", help_text="Cuenta contable")
    id_budget_item_expenses = models.ForeignKey(BudgetItemExpenses, on_delete=models.PROTECT, verbose_name="Rubro Presupuestal de Gastos", help_text="Rubro presupuestal de gastos asociado")
    contract_number = models.CharField(max_length=10, verbose_name="Número de Contrato", help_text="Número de contrato")
    invoice_number = models.CharField(max_length=10, verbose_name="Número de Factura", help_text="Número de factura")
    invoice_date = models.DateField(verbose_name="Fecha de Factura", help_text="Fecha de factura")
    beneficiary_payment = models.CharField(max_length=20, verbose_name="Beneficiario del Pago", help_text="Beneficiario del pago")
    cc_nit = models.CharField(max_length=20, verbose_name="Cédula o NIT", help_text="Cédula o NIT")
    detail = models.TextField(verbose_name="Detalle", help_text="Detalle")
    invoice_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor de la Factura", help_text="Valor de la factura")
    rte_fte = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="RTE. FTE", help_text="RTE. FTE")
    reteiva = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="RETE IVA", help_text="RETE IVA")
    other_discounts = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Otros Descuentos", help_text="Otros descuentos")
    net_value = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor Neto", help_text="Valor neto")  
    bank = models.ForeignKey(Bank, on_delete=models.PROTECT, verbose_name="Banco", help_text="Banco")
    check_number = models.CharField(max_length=100, verbose_name="Número de Cheque", help_text="Número de cheque")
    source_fundig = models.CharField(max_length=100, verbose_name="Fuente de Financiación", help_text="Fuente de financiación")
    benefited = models.CharField(max_length=100, verbose_name="Beneficiado", help_text="Beneficiado")    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")

    def __str__(self):
        return str(self.id)

# Catalogo de cuentas
class AccountCatalog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100, verbose_name="Código", help_text="Código de la cuenta")
    name = models.CharField(max_length=100, verbose_name="Nombre", help_text="Nombre de la cuenta")
    nature = models.CharField(max_length=100, verbose_name="Naturaleza", help_text="Naturaleza de la cuenta")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación", help_text="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización", help_text="Fecha de actualización")

    def __str__(self):
        return f'{self.code} - {self.name} - {self.nature}'
        