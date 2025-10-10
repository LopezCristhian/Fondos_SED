from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    InstitutionViewSet,
    BudgetReportViewSet,
    BudgetItemRevenueViewSet,
    BudgetItemExpensesViewSet,
    AccountantPucViewSet,
    ExpenseAccountsViewSet,
    SourceResourcesViewSet,
    BankViewSet,
    F7BudgetExecutionExpensesViewSet,
    F11AccountsPayableViewSet,
    F13HiringViewSet,
    Ief02RevenueStatementViewSet,
    Ief04PaymentsRelationshipViewSet,
    RevenueBudgetViewSet,
    ChangesRevenuePeriodViewSet,
    CumulativeChangesRevenueViewSet,
    RevenueExecutionViewSet,
    ExpensesBudgetViewSet,
    ChangesExpensesPeriodViewSet,
    CumulativeChangesExpensesViewSet,
    ExpensesExecutionViewSet,
    PaymentObligationsViewSet,
    PaymentRelationshipViewSet
    
)

router = DefaultRouter()
router.register(r'institutions', InstitutionViewSet, basename='institutions')
router.register(r'budget_report', BudgetReportViewSet, basename='budget_report')
router.register(r'budget_item_revenue', BudgetItemRevenueViewSet, basename='budget_item_revenue')
router.register(r'budget_item_expenses', BudgetItemExpensesViewSet, basename='budget_item_expenses')
router.register(r'accountant_puc', AccountantPucViewSet, basename='accountant_puc')
router.register(r'expense_accounts', ExpenseAccountsViewSet, basename='expense_accounts')
router.register(r'source_resources', SourceResourcesViewSet, basename='source_resources')
router.register(r'bank', BankViewSet, basename='bank')
router.register(r'f7_budget_execution_expenses', F7BudgetExecutionExpensesViewSet, basename='f7_budget_execution_expenses')
router.register(r'f11_accounts_payable', F11AccountsPayableViewSet, basename='f11_accounts_payable')
router.register(r'f13_hiring', F13HiringViewSet, basename='f13_hiring')
router.register(r'ief02_revenue_statement', Ief02RevenueStatementViewSet, basename='ief02_revenue_statement')
router.register(r'ief04_payments_relationship', Ief04PaymentsRelationshipViewSet, basename='ief04_payments_relationship')
router.register(r'revenue_budget', RevenueBudgetViewSet, basename='revenue_budget')
router.register(r'changes_revenue_period', ChangesRevenuePeriodViewSet, basename='changes_revenue_period')
router.register(r'cumulative_changes_revenue', CumulativeChangesRevenueViewSet, basename='cumulative_changes_revenue')
router.register(r'revenue_execution', RevenueExecutionViewSet, basename='revenue_execution')
router.register(r'expenses_budget', ExpensesBudgetViewSet, basename='expenses_budget')
router.register(r'changes_expenses_period', ChangesExpensesPeriodViewSet, basename='changes_expenses_period')
router.register(r'cumulative_changes_expenses', CumulativeChangesExpensesViewSet, basename='cumulative_changes_expenses')
router.register(r'expenses_execution', ExpensesExecutionViewSet, basename='expenses_execution')
router.register(r'payment_obligations', PaymentObligationsViewSet, basename='payment_obligations')
router.register(r'payment_relationship', PaymentRelationshipViewSet, basename='payment_relationship')

urlpatterns = [
    # API routes
    path('', include(router.urls)),
        
]