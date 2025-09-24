import uuid
from django.db import models

# Create your models here.

# Microservicio Institusiones
class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, verbose_name="Nombre", help_text="Nombre de la institucion") 
    
    def __str__(self):
        return f'{self.name}'

# Perido de reporte de información presupuestal
class BudgetReport(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    period_type = models.CharField(max_length=20,  choices=(('Semestral', 'Semestral'), ('Trimestral', 'Trimestral'), ('Mensual', 'Mensual')), verbose_name="Tipo de periodo", help_text="Tipo de periodo")
    period_number = models.IntegerField(verbose_name="Número de periodo", help_text="Número de periodo")
    year = models.IntegerField(verbose_name="Año", help_text="Año")
    start_date = models.DateField(blank=True, null=True, verbose_name="Fecha de inicio", help_text="Fecha de inicio")
    end_date = models.DateField(blank=True, null=True, verbose_name="Fecha de fin", help_text="Fecha de fin")
    
    def __str__(self):
        return f'{self.period_type} - {self.period_number} - {self.year}'

# Modelo de rubros presupuestales de ingresos
class BudgetItemRevenue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100, verbose_name="Código", help_text="Código del rubro presupuestal de ingresos")
    level = models.CharField(max_length=100, verbose_name="Nivel", help_text="Nivel del rubro presupuestal de ingresos")
    type = models.CharField(max_length=100, verbose_name="Tipo", help_text="Tipo del rubro presupuestal de ingresos")
    accountant_name = models.CharField(max_length=100, verbose_name="Nombre Contable", help_text="Nombre contable del rubro presupuestal de ingresos")
    father = models.CharField(max_length=100, verbose_name="Padre", help_text="Padre del rubro presupuestal de ingresos")
    
    def __str__(self):
        return f'{self.code} - {self.accountant_name}'

# Modelo de rubros presupuestales de gastos
class BudgetItemExpenses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100, verbose_name="Código", help_text="Código del rubro presupuestal de gastos")
    level = models.CharField(max_length=100, verbose_name="Nivel", help_text="Nivel del rubro presupuestal de gastos")
    type = models.CharField(max_length=100, verbose_name="Tipo", help_text="Tipo del rubro presupuestal de gastos")
    accountant_name = models.CharField(max_length=100, verbose_name="Nombre Contable", help_text="Nombre contable del rubro presupuestal de gastos")
    father = models.CharField(max_length=100, verbose_name="Padre", help_text="Padre del rubro presupuestal de gastos")

    def __str__(self):
        return f'{self.code} - {self.accountant_name}'
    
# Modelo de Plan contable
class AccountantPuc(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=100, verbose_name="Código", help_text="Código del plan contable")
    name = models.CharField(max_length=100, verbose_name="Nombre", help_text="Nombre del plan contable")
    nature = models.CharField(max_length=100, choices=(('DEBITO', 'Debito'), ('CREDITO', 'Credito')), verbose_name="Naturaleza", help_text="Naturaleza del plan contable")
    father = models.CharField(max_length=100, blank=True, null=True, verbose_name="Padre", help_text="Padre del plan contable")
    type = models.CharField(max_length=100, choices=(('GASTO', 'Gasto'), ('DETALLE', 'Detalle')), blank=True, null=True, verbose_name="Tipo", help_text="Tipo del plan contable")
    level = models.IntegerField(blank=True, null=True, verbose_name="Nivel", help_text="Nivel del plan contable")
    
    def __str__(self):
        return f'{self.code} - {self.name} - {self.father} - {self.type}'
    
# Modelo de ejecución presupuestal de gastos e ingresos F7
class F7BudgetExecutionExpenses(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_budget_item_expenses = models.ManyToManyField(BudgetItemExpenses, on_delete=models.PROTECT, verbose_name="Rubro Presupuestal de Gastos", help_text="Rubro presupuestal de gastos asociado")
    id_institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name="Institucion", help_text="Institucion asociada")
    id_budget_report = models.ForeignKey(BudgetReport, on_delete=models.PROTECT, verbose_name="Perido de reporte presupuestal", help_text="Perido de reporte presupuestal asociado")
    
    program_code = models.CharField(max_length=100, verbose_name="Código del Programa", help_text="Código del programa")
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
    
    
    def __str__(self):
        return f'{self.id_budget_item_expenses} - {self.id_institution} - {self.program_code}'

# Modelo de cuentas por pagar F11
class F11AccountsPayable(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_budget_item_expenses = models.ManyToManyField(BudgetItemExpenses, on_delete=models.PROTECT, verbose_name="Rubro Presupuestal de Gastos", help_text="Rubro presupuestal de gastos asociado")
    id_institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name="Institucion", help_text="Institucion asociada")
    id_budget_report = models.ForeignKey(BudgetReport, on_delete=models.PROTECT, verbose_name="Perido de reporte presupuestal", help_text="Perido de reporte presupuestal asociado")
    
    description = models.CharField(max_length=100, verbose_name="Descripción", help_text="Descripción")
    account_payable = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Cuenta por Pagar", help_text="Cuenta por pagar")
    cancelation_certificate = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Acta de Cancelación", help_text="Acta de cancelación")
    payment = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Pago", help_text="Pago")
    
    def __str__(self):
        return f'{self.id_budget_item_expenses} - {self.id_institution} - {self.description}'

# Modelo de formato de contratación F13
class F13Hiring(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_budget_item_expenses = models.ManyToManyField(BudgetItemExpenses, on_delete=models.PROTECT, verbose_name="Rubro Presupuestal de Gastos", help_text="Rubro presupuestal de gastos asociado")
    id_institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name="Institucion", help_text="Institucion asociada")
    id_budget_report = models.ForeignKey(BudgetReport, on_delete=models.PROTECT, verbose_name="Perido de reporte presupuestal", help_text="Perido de reporte presupuestal asociado")
    
    contract_number = models.CharField(max_length=100, verbose_name="Número de Contrato", help_text="Número de contrato")
    source_resources = models.CharField(max_length=100, verbose_name="Fuente de Recursos", help_text="Fuente de recursos")
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
    
    def __str__(self):
        return f'{self.contract_number} - {self.contractor_name} - {self.id_institution}'
    
# Modelo de informes y anexos generales F31
class F31GeneralAnnexes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name="Institucion", help_text="Institucion asociada")
    id_budget_report = models.ForeignKey(BudgetReport, on_delete=models.PROTECT, verbose_name="Perido de reporte presupuestal", help_text="Perido de reporte presupuestal asociado")
    
    report_title = models.CharField(max_length=100, verbose_name="Título del Informe", help_text="Título del informe")
    responsible = models.CharField(max_length=100, verbose_name="Responsable", help_text="Responsable")
    number_pages = models.IntegerField(verbose_name="Número de Fólios", help_text="Número de Fólios")
    comments = models.TextField(blank=True, null=True, verbose_name="Observaciones", help_text="Observaciones")
    
    def __str__(self):
        return f'{self.id_institution} - {self.report_title}'

# Modelo de relación de ingresos IEF02
class Ief02RevenueStatement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_budget_item_revenue = models.ManyToManyField(BudgetItemRevenue, on_delete=models.PROTECT, verbose_name="Rubro Presupuestal de Ingresos", help_text="Rubro presupuestal de ingresos asociado")
    id_institution = models.ForeignKey(Institution, on_delete=models.PROTECT, verbose_name="Institucion", help_text="Institucion asociada")
    id_budget_report = models.ForeignKey(BudgetReport, on_delete=models.PROTECT, verbose_name="Perido de reporte presupuestal", help_text="Perido de reporte presupuestal asociado")
    
    collection_date = models.DateField(verbose_name="Fecha de Recaudo", help_text="Fecha de recaudo")
    detail= models.CharField(max_length=100, verbose_name="Detalle", help_text="Detalle")
    receipt = models.CharField(max_length=100, verbose_name="Recibo de", help_text="Recibo de")
    value= models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor", help_text="Valor")
    bank_account_number = models.CharField(max_length=100, verbose_name="Número de Cuenta Bancaria", help_text="Número de cuenta bancaria")
    bank= models.CharField(max_length=100, verbose_name="Banco", help_text="Banco")
    revenue_resources = models.CharField(max_length=100, verbose_name="Fuente de Ingresos", help_text="Fuente de ingresos")
    
    def __str__(self):
        return f'{self.id_budget_item_revenue} - {self.id_institution} - {self.collection_date}'

# Modelo de relación de pagos IEF04
class Ief04PaymentsRelationship(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_budget_item_expenses = models.ManyToManyField(BudgetItemExpenses, on_delete=models.PROTECT, verbose_name="Rubro Presupuestal de Gastos", help_text="Rubro presupuestal de gastos asociado")
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
    bank = models.CharField(max_length=100, verbose_name="Banco", help_text="Banco")
    account_number = models.CharField(max_length=100, verbose_name="Número de Cuenta", help_text="Número de cuenta")
    check_number = models.CharField(max_length=100, verbose_name="Cheque Número", help_text="Cheque número")
    funding_source = models.CharField(max_length=100, verbose_name="Fuente de Financiación", help_text="Fuente de financiación")
    
    def __str__(self):
        return f'{self.id_budget_item_expenses} - {self.id_institution} - {self.collection_date}'

    