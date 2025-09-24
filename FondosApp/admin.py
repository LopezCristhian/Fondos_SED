from django.contrib import admin

from FondosApp.models import Institution, BudgetReport, BudgetItemRevenue, BudgetItemExpenses, AccountantPuc, F7BudgetExecutionExpenses, F11AccountsPayable, F13Hiring, F31GeneralAnnexes, Ief02RevenueStatement, Ief04PaymentsRelationship

# Register your models here.

# Microservicio Institusiones
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('name')

# Modelo de periodo de reporte presupuestal
class BudgetReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'period_type', 'period_number', 'year')
    search_fields = ('id', 'period_type', 'period_number', 'year')
    list_filter = ('period_type', 'period_number', 'year')

# Modelo de rubros presupuestales de ingresos
class BudgetItemRevenueAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'level', 'type', 'accountant_name', 'father')
    search_fields = ('id', 'code', 'level', 'type', 'accountant_name', 'father')
    list_filter = ('type', 'level', 'father')

# Modelo de rubros presupuestales de gastos
class BudgetItemExpensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'level', 'type', 'accountant_name', 'father')
    search_fields = ('id', 'code', 'level', 'type', 'accountant_name', 'father')
    list_filter = ('type', 'level', 'father')

# Modelo de Plan contable
class AccountantPucAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'nature', 'father', 'type', 'level')
    search_fields = ('id', 'code', 'name', 'nature', 'father', 'type', 'level')
    list_filter = ('nature', 'father', 'type', 'level')
    
# Modelo de ejecución presupuestal de gastos y ingresos F7
class F7BudgetExecutionExpensesAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_budget_item_expenses', 'id_institution', 'id_budget_report')
    search_fields = ('id', 'id_budget_item_expenses', 'id_institution', 'id_budget_report')
    list_filter = ('id_budget_item_expenses', 'id_institution', 'id_budget_report')

# Modelo de cuentas por pagar F11
class F11AccountsPayableAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_budget_item_expenses', 'id_institution', 'id_budget_report')
    search_fields = ('id', 'id_budget_item_expenses', 'id_institution', 'id_budget_report')
    list_filter = ('id_budget_item_expenses', 'id_institution', 'id_budget_report')

# Modelo de forrmato de contratación F13
class F13HiringAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_budget_item_expenses', 'id_institution', 'id_budget_report')
    search_fields = ('id', 'id_budget_item_expenses', 'id_institution', 'id_budget_report')
    list_filter = ('id_budget_item_expenses', 'id_institution', 'id_budget_report')

# Modelo de informe y anexos generales F31
class F31GeneralAnnexesAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_institution', 'id_budget_report')
    search_fields = ('id', 'id_institution', 'id_budget_report')
    list_filter = ('id_institution', 'id_budget_report')

# Modelo de relación de ingresos IEF02
class Ief02RevenueStatementAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_budget_item_revenue', 'id_institution', 'id_budget_report')
    search_fields = ('id', 'id_budget_item_revenue', 'id_institution', 'id_budget_report')
    list_filter = ('id_budget_item_revenue', 'id_institution', 'id_budget_report')

# Modelo de relación de pagos IEF04
class Ief04PaymentsRelationshipAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_budget_item_expenses', 'id_institution', 'id_budget_report')
    search_fields = ('id', 'id_budget_item_expenses', 'id_institution', 'id_budget_report')
    list_filter = ('id_budget_item_expenses', 'id_institution', 'id_budget_report')    
    
# Registro de los modelos en el admin de Django
admin.site.register(Institution, InstitutionAdmin)
admin.site.register(BudgetReport, BudgetReportAdmin)
admin.site.register(BudgetItemRevenue, BudgetItemRevenueAdmin)
admin.site.register(BudgetItemExpenses, BudgetItemExpensesAdmin)
admin.site.register(AccountantPuc, AccountantPucAdmin)
admin.site.register(F7BudgetExecutionExpenses, F7BudgetExecutionExpensesAdmin)
admin.site.register(F11AccountsPayable, F11AccountsPayableAdmin)
admin.site.register(F13Hiring, F13HiringAdmin)
admin.site.register(F31GeneralAnnexes, F31GeneralAnnexesAdmin)
admin.site.register(Ief02RevenueStatement, Ief02RevenueStatementAdmin)
admin.site.register(Ief04PaymentsRelationship, Ief04PaymentsRelationshipAdmin)
