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
    PaymentRelationship
    
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