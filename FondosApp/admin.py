

from django.contrib import admin

from FondosApp.models import Institution, BudgetReport, BudgetItemRevenue, BudgetItemExpenses, AccountantPuc, ExpenseAccounts, SourceResources, Bank, F7BudgetExecutionExpenses, F11AccountsPayable, F13Hiring, Ief02RevenueStatement, Ief04PaymentsRelationship, RevenueBudget, ChangesRevenuePeriod, CumulativeChangesRevenue, RevenueExecution, ExpensesBudget, ChangesExpensesPeriod, CumulativeChangesExpenses, ExpensesExecution, PaymentObligations, PaymentRelationship

# Register your models here.

# Microservicio Institusiones
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name', ) 
    list_filter = ('name', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10

# Modelo de periodo de reporte presupuestal
class BudgetReportAdmin(admin.ModelAdmin):
    list_display = ('period_type', 'period_number', 'year', 'created_at', 'updated_at')
    search_fields = ('period_type', 'period_number', 'year')
    list_filter = ('period_type', 'period_number', 'year', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10

# Modelo de rubros presupuestales de ingresos
class BudgetItemRevenueAdmin(admin.ModelAdmin):
    list_display = ('code', 'level', 'type', 'account_name', 'father', 'created_at', 'updated_at')
    search_fields = ('code', 'level', 'type', 'account_name', 'father')
    list_filter = ('type', 'level', 'father', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10

# Modelo de rubros presupuestales de gastos
class BudgetItemExpensesAdmin(admin.ModelAdmin):
    list_display = ('code', 'level', 'type', 'account_name', 'father', 'created_at', 'updated_at')
    search_fields = ('code', 'level', 'type', 'account_name', 'father')
    list_filter = ('type', 'level', 'father', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10

# Modelo de Plan contable
class AccountantPucAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'nature', 'father', 'type', 'level', 'created_at', 'updated_at')
    search_fields = ('code', 'name', 'nature', 'father', 'type', 'level')
    list_filter = ('nature', 'father', 'type', 'level', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 25

# Modelo de cuentas de gastos
class ExpenseAccountsAdmin(admin.ModelAdmin):
    list_display = ('budget_code_expenses', 'accountant_name', 'created_at', 'updated_at')
    search_fields = ('budget_code_expenses', 'accountant_name')
    list_filter = ('budget_code_expenses', 'accountant_name', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 25

# Modelo de fuente de recursos
class SourceResourcesAdmin(admin.ModelAdmin):
    list_display = ('source_name', 'created_at', 'updated_at')
    search_fields = ('source_name', )
    list_filter = ('source_name', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10
    
# Modelo de bancos
class BankAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'created_at', 'updated_at')
    search_fields = ('bank_name', )
    list_filter = ('bank_name', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10

# Modelo de ejecución presupuestal de gastos y ingresos F7
class F7BudgetExecutionExpensesAdmin(admin.ModelAdmin):
    list_display = ('id_institution', 'id_budget_item_expenses', 'id_budget_report', 'program_code', 'credit', 'countercredit', 'postponement', 'displacement', 'reductions', 'additions', 'commitment_budget_registration', 'obligations', 'payments', 'created_at', 'updated_at')
    search_fields = ('id_budget_item_expenses', 'id_institution', 'id_budget_report', 'program_code', 'credit', 'countercredit', 'postponement', 'displacement', 'reductions', 'additions', 'credit', 'countercredit', 'postponement', 'displacement', 'reductions', 'additions', 'commitment_budget_registration', 'obligations', 'payments',)
    list_filter = ('id_institution',  'id_budget_item_expenses','id_budget_report', 'program_code', 'credit', 'countercredit', 'postponement', 'displacement', 'reductions', 'additions', 'credit', 'countercredit', 'postponement', 'displacement', 'reductions', 'additions', 'commitment_budget_registration', 'obligations', 'payments', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10
     
# Modelo de cuentas por pagar F11
class F11AccountsPayableAdmin(admin.ModelAdmin):
    list_display = ('id_budget_item_expenses', 'id_institution', 'id_budget_report', 'description', 'account_payable', 'cancelation_certificate', 'payment', 'created_at', 'updated_at')
    search_fields = ('id_budget_item_expenses', 'id_institution', 'id_budget_report', 'description', 'account_payable', 'cancelation_certificate', 'payment', 'created_at', 'updated_at')
    list_filter = ('id_budget_item_expenses', 'id_institution', 'id_budget_report', 'description', 'account_payable', 'cancelation_certificate', 'payment', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10

# Modelo de forrmato de contratación F13
class F13HiringAdmin(admin.ModelAdmin):
    list_display = ('id_institution', 'id_budget_item_expenses', 'id_budget_report', 'source_resources', 'class_h', 'contract_number', 'object', 'contract_value', 'contractor_name', 'nit_cc_contractor', 'budget_unavailability', 'value_availability', 'signature_date', 'contract_form', 'budget_registration_date', 'budget_registration_number', 'budget_record_value', 'date_approval_single_guarantee', 'start_date', 'contract_term', 'addition_date', 'addtion_term', 'addition_value', 'value_payments_made', 'completion_date', 'sattlement_date', 'created_at', 'updated_at')
    search_fields = ('id_institution', 'id_budget_item_expenses', 'id_budget_report', 'source_resources', 'class_h', 'contract_number', 'object', 'contract_value', 'contractor_name', 'nit_cc_contractor', 'budget_unavailability', 'value_availability', 'signature_date', 'contract_form', 'budget_registration_date', 'budget_registration_number', 'budget_record_value', 'date_approval_single_guarantee', 'start_date', 'contract_term', 'addition_date', 'addtion_term', 'addition_value', 'value_payments_made', 'completion_date', 'sattlement_date', 'created_at', 'updated_at')
    list_filter = ('id_institution', 'id_budget_item_expenses', 'id_budget_report', 'source_resources', 'class_h', 'contract_number', 'object', 'contract_value', 'contractor_name', 'nit_cc_contractor', 'budget_unavailability', 'value_availability', 'signature_date', 'contract_form', 'budget_registration_date', 'budget_registration_number', 'budget_record_value', 'date_approval_single_guarantee', 'start_date', 'contract_term', 'addition_date', 'addtion_term', 'addition_value', 'value_payments_made', 'completion_date', 'sattlement_date', 'created_at', 'updated_at')   
    date_hierarchy = 'created_at'
    list_per_page = 10

# Modelo de informe y anexos generales F31
"""class F31GeneralAnnexesAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_institution', 'id_budget_report')
    search_fields = ('id', 'id_institution', 'id_budget_report')
    list_filter = ('id_institution', 'id_budget_report')
"""

# Modelo de relación de ingresos IEF02
class Ief02RevenueStatementAdmin(admin.ModelAdmin):
    list_display = ('id_institution', 'id_budget_item_revenue', 'id_budget_report', 'collection_date', 'detail', 'receipt_bank', 'value', 'bank_account_number', 'bank', 'revenue_resources', 'created_at', 'updated_at')
    search_fields = ('id_institution','id_budget_item_revenue', 'id_budget_report', 'collection_date', 'detail', 'receipt_bank', 'value', 'bank_account_number', 'bank', 'revenue_resources', 'created_at', 'updated_at')
    list_filter = ('id_institution', 'id_budget_item_revenue', 'id_budget_report', 'collection_date', 'detail', 'receipt_bank', 'value', 'bank_account_number', 'bank', 'revenue_resources', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10

# Modelo de relación de pagos IEF04
class Ief04PaymentsRelationshipAdmin(admin.ModelAdmin):
    list_display = ('id_institution', 'id_budget_item_expenses', 'id_budget_report', 'collection_date', 'receipt_number', 'detail', 'beneficiary', 'cc_nit', 'total_value_receipt', 'withholdings', 'discounts', 'bank', 'account_number', 'check_number', 'funding_source', 'created_at', 'updated_at')
    search_fields = ('id_institution', 'id_budget_item_expenses', 'id_budget_report', 'collection_date', 'receipt_number', 'detail', 'beneficiary', 'cc_nit', 'total_value_receipt', 'withholdings', 'discounts', 'bank', 'account_number', 'check_number', 'funding_source', 'created_at', 'updated_at')
    list_filter = ('id_institution', 'id_budget_item_expenses', 'id_budget_report', 'collection_date', 'receipt_number', 'detail', 'beneficiary', 'cc_nit', 'total_value_receipt', 'withholdings', 'discounts', 'bank', 'account_number', 'check_number', 'funding_source', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10
    
#! Modelos para el cierre presupuestal de ingresos

# Modelo de presupuesto de ingresos
class RevenueBudgetAdmin(admin.ModelAdmin):
    list_display = ('id_institution', 'id_budget_item_revenue', 'period', 'initial_appropriation', 'final_appropriation', 'created_at', 'updated_at')
    search_fields = ('id_institution', 'id_budget_item_revenue', 'period', 'initial_appropriation', 'final_appropriation', 'created_at', 'updated_at')
    list_filter = ('id_institution', 'id_budget_item_revenue', 'period', 'initial_appropriation', 'final_appropriation', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'   
    list_per_page = 10

# Modelo de modificaciones del periodo - ingresos
class ChangesRevenuePeriodAdmin(admin.ModelAdmin):
    list_display = ('id_revenue_budget', 'addition', 'reduction', 'credit_transfer',    'countercredit_transfer', 'created_at', 'updated_at')
    search_fields = ('id_revenue_budget', 'addition', 'reduction', 'credit_transfer',    'countercredit_transfer', 'created_at', 'updated_at')
    list_filter = ('id_revenue_budget', 'addition', 'reduction', 'credit_transfer',    'countercredit_transfer', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10

# Modelo de modificaciones acumuladas - ingresos
class CumulativeChangesRevenueAdmin(admin.ModelAdmin):
    list_display = ('id_revenue_budget', 'accumulated_additions', 'accumulated_reductions', 'transfer_accumulated_credits', 'transfer_accumulated_countercredits', 'created_at', 'updated_at')
    search_fields = ('id_revenue_budget', 'accumulated_additions', 'accumulated_reductions', 'transfer_accumulated_credits', 'transfer_accumulated_countercredits', 'created_at', 'updated_at')
    list_filter = ('id_revenue_budget', 'accumulated_additions', 'accumulated_reductions', 'transfer_accumulated_credits', 'transfer_accumulated_countercredits', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10

# Modelo de ejecución de ingresos
class RevenueExecutionAdmin(admin.ModelAdmin):
    list_display = ('id_revenue_budget', 'monthly_revenue_value', 'accumulated_revenue', 'income_receivable', 'created_at', 'updated_at')
    search_fields = ('id_revenue_budget', 'monthly_revenue_value', 'accumulated_revenue', 'income_receivable')
    list_filter = ('id_revenue_budget', 'monthly_revenue_value', 'accumulated_revenue', 'income_receivable', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10
    
#! Modelos para el cierre presupuestal de gastos

# Modelo de presupuesto de gastos
class ExpensesBudgetAdmin(admin.ModelAdmin):
    list_display = ('id_institution', 'id_budget_item_expenses', 'period', 'initial_appropriation', 'final_appropriation', 'created_at', 'updated_at')
    search_fields = ('id_institution', 'id_budget_item_expenses', 'period')
    list_filter = ('id_institution', 'id_budget_item_expenses', 'period', 'initial_appropriation', 'final_appropriation', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10

# Modelo de modificaciones del periodo - gastos
class ChangesExpensesPeriodAdmin(admin.ModelAdmin):
    list_display = ('id_expenses_budget', 'addition', 'reduction', 'credits', 'countercredits', 'created_at', 'updated_at')
    search_fields = ('id_expenses_budget', )    
    list_filter = ('id_expenses_budget', 'addition', 'reduction', 'credits', 'countercredits', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10  

# Modelo de modificaciones acumuladas - gastos
class CumulativeChangesExpensesAdmin(admin.ModelAdmin):
    list_display = ('id_expenses_budget', 'accumulated_additions', 'accumulated_reductions', 'accumulated_credits', 'accumulated_countercredits', 'created_at', 'updated_at')
    search_fields = ('id_expenses_budget', )        
    list_filter = ('id_expenses_budget', 'accumulated_additions', 'accumulated_reductions', 'accumulated_credits', 'accumulated_countercredits', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10  

# Modelo de ejecución de gastos
class ExpensesExecutionAdmin(admin.ModelAdmin):
    list_display = ('id_revenue_budget', 'certificates_period', 'accumulated_certificates', 'available_balance', 'period_commitments', 'accumulated_commitments', 'created_at', 'updated_at')
    search_fields = ('id_revenue_budget', 'certificate_period', 'accumulated_certificates', 'available_balance', 'period_commitments', 'accumulated_commitments')
    list_filter = ('id_revenue_budget', 'certificates_period', 'accumulated_certificates', 'available_balance', 'period_commitments', 'accumulated_commitments', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10

# Modelo de obligaciones de pago
class PaymentObligationsAdmin(admin.ModelAdmin):
    list_display = ('id_revenue_budget', 'open_positions', 'obligations_period', 'accumulated_obligations', 'period_payments', 'accumulated_payments', 'balance_payable', 'reservations', 'created_at', 'updated_at')
    search_fields = ('id_revenue_budget', 'open_positions', 'obligations_period', 'accumulated_obligations', 'period_payments', 'accumulated_payments', 'balance_payable', 'reservations', 'created_at', 'updated_at')
    list_filter = ('id_revenue_budget', 'open_positions', 'obligations_period', 'accumulated_obligations', 'period_payments', 'accumulated_payments', 'balance_payable', 'reservations', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10  

# Modelo de relación de pagos
class PaymentRelationshipAdmin(admin.ModelAdmin):
    list_display = ('id_institution', 'date', 'no_exit_receipt', 'accounting_account', 'id_budget_item_expenses', 'contract_number', 'invoice_number', 'invoice_date', 'beneficiary_payment', 'cc_nit', 'detail', 'invoice_value', 'rte_fte', 'reteiva', 'other_discounts', 'net_value', 'bank', 'check_number', 'source_fundig', 'benefited', 'created_at', 'updated_at')
    search_fields = ('id_institution', 'date', 'no_exit_receipt', 'accounting_account', 'id_budget_item_expenses', 'contract_number', 'invoice_number', 'invoice_date', 'beneficiary_payment', 'cc_nit', 'detail', 'invoice_value', 'rte_fte', 'reteiva', 'other_discounts', 'net_value', 'bank', 'check_number', 'source_fundig', 'benefited', 'created_at', 'updated_at')
    list_filter = ( 'id_institution', 'date', 'no_exit_receipt', 'accounting_account', 'id_budget_item_expenses', 'contract_number', 'invoice_number', 'invoice_date', 'beneficiary_payment', 'cc_nit', 'detail', 'invoice_value', 'rte_fte', 'reteiva', 'other_discounts', 'net_value', 'bank', 'check_number', 'source_fundig', 'benefited', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    list_per_page = 10

# Registro de los modelos en el admin de Django

admin.site.register(Institution, InstitutionAdmin)
admin.site.register(BudgetReport, BudgetReportAdmin)
admin.site.register(BudgetItemRevenue, BudgetItemRevenueAdmin)
admin.site.register(BudgetItemExpenses, BudgetItemExpensesAdmin)
admin.site.register(AccountantPuc, AccountantPucAdmin)
admin.site.register(ExpenseAccounts, ExpenseAccountsAdmin)
admin.site.register(SourceResources, SourceResourcesAdmin)
admin.site.register(Bank, BankAdmin)
admin.site.register(F7BudgetExecutionExpenses, F7BudgetExecutionExpensesAdmin)
admin.site.register(F11AccountsPayable, F11AccountsPayableAdmin)
admin.site.register(F13Hiring, F13HiringAdmin)
# admin.site.register(F31GeneralAnnexes, F31GeneralAnnexesAdmin)
admin.site.register(Ief02RevenueStatement, Ief02RevenueStatementAdmin)
admin.site.register(Ief04PaymentsRelationship, Ief04PaymentsRelationshipAdmin)
admin.site.register(RevenueBudget, RevenueBudgetAdmin)
admin.site.register(ChangesRevenuePeriod, ChangesRevenuePeriodAdmin)
admin.site.register(CumulativeChangesRevenue, CumulativeChangesRevenueAdmin)
admin.site.register(RevenueExecution, RevenueExecutionAdmin)
admin.site.register(ExpensesBudget, ExpensesBudgetAdmin)
admin.site.register(ChangesExpensesPeriod, ChangesExpensesPeriodAdmin)
admin.site.register(CumulativeChangesExpenses, CumulativeChangesExpensesAdmin)
admin.site.register(ExpensesExecution, ExpensesExecutionAdmin)
admin.site.register(PaymentObligations, PaymentObligationsAdmin)
admin.site.register(PaymentRelationship, PaymentRelationshipAdmin)
