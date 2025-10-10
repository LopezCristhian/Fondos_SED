from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from django.views.generic import TemplateView

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

from .serializers import (
    InstitutionSerializer, 
    BudgetReportSerializer, 
    BudgetItemRevenueSerializer,
    BudgetItemExpensesSerializer,
    AccountantPucSerializer,
    ExpenseAccountsSerializer,
    SourceResourcesSerializer,
    BankSerializer,
    F7BudgetExecutionExpensesSerializer,
    F11AccountsPayableSerializer,
    F13HiringSerializer,
    Ief02RevenueStatementSerializer,
    Ief04PaymentsRelationshipSerializer,
    RevenueBudgetSerializer,
    ChangesRevenuePeriodSerializer,
    CumulativeChangesRevenueSerializer,
    RevenueExecutionSerializer,
    ExpensesBudgetSerializer,
    ChangesExpensesPeriodSerializer,
    CumulativeChangesExpensesSerializer,
    ExpensesExecutionSerializer,
    PaymentObligationsSerializer,
    PaymentRelationshipSerializer
    
)

# ViewSet para gestionar las instituciones
@extend_schema_view(
    list=extend_schema(
        summary="Listar todas las instituciones", 
        description="Obtiene una lista de todas las instituciones registradas en el sistema", 
        tags=['Instituciones']),
    
    retrieve=extend_schema(
        summary="Obtener una institución específica",
        description="Obtiene los detalles de una institución por su ID", 
        tags=['Instituciones']),
    
    create=extend_schema(
        summary="Crear una nueva institución", 
        description="Crea una nueva institución en el sistema", 
        tags=['Instituciones'], 
        examples=[OpenApiExample('Ejemplo de creación', value={'name': 'Nuestra señora de las nieves'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar una institución",
        description="Actualiza completamente una institución existente",
        tags=['Instituciones']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una institución",
        description="Actualiza uno o más campos de una institución existente",
        tags=['Instituciones']
    ),
    destroy=extend_schema(
        summary="Eliminar una institución",
        description="Elimina una institución del sistema",
        tags=['Instituciones']
    )
)
class InstitutionViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar las instituciones.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todas las instituciones
    - retrieve: Obtener una institución específica
    - create: Crear una nueva institución
    - update: Actualizar una institución completa
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar una institución
    """
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    
    @extend_schema(
        summary="Buscar instituciones por nombre",
        description="Busca instituciones que contengan el nombre especificado",
        parameters=[
            OpenApiParameter(
                name='name',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Nombre de la institución a buscar',
                required=True
            )
        ],
        tags=['Instituciones']
    )
    @action(detail=False, methods=['get'])
    def search_by_name(self, request):
        """Busca instituciones por nombre"""
        name = request.query_params.get('name', '')
        institutions = self.queryset.filter(name__icontains=name)
        serializer = self.get_serializer(institutions, many=True)        
        return Response(serializer.data)

# # ViewSet para modelo el perido de reporte de información presupuestal
@extend_schema_view(
    list=extend_schema(
        summary="Listar todos los reportes de presupuesto",
        description="Obtiene una lista de todos los reportes de presupuesto registrados en el sistema",
        tags=['Reporte de Presupuesto']),
    
    retrieve=extend_schema(
        summary="Obtener un reporte de presupuesto específico",
        description="Obtiene los detalles de un reporte de presupuesto por su ID",
        tags=['Reporte de Presupuesto']),
    
    create=extend_schema(
        summary="Crear un nuevo reporte de presupuesto",
        description="Crea un nuevo reporte de presupuesto en el sistema",
        tags=['Reporte de Presupuesto'],
        examples=[OpenApiExample('Ejemplo de creación', value={'period_type': 'Trimestral', 'period_number': 1, 'year': 2024}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar un reporte de presupuesto",
        description="Actualiza completamente un reporte de presupuesto existente",
        tags=['Reporte de Presupuesto']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente un reporte de presupuesto",
        description="Actualiza uno o más campos de un reporte de presupuesto existente",
        tags=['Reporte de Presupuesto']
    ),
    destroy=extend_schema(
        summary="Eliminar un reporte de presupuesto",
        description="Elimina un reporte de presupuesto del sistema",
        tags=['Reporte de Presupuesto']
    )
)
class BudgetReportViewSet(viewsets.ModelViewSet):
    """
    ViewSet para el reporte de presupuesto.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todos los reportes de presupuesto
    - retrieve: Obtener un reporte de presupuesto específico
    - create: Crear un nuevo reporte de presupuesto
    - update: Actualizar un reporte de presupuesto completo
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar un reporte de presupuesto
    """
    queryset = BudgetReport.objects.all()
    serializer_class = BudgetReportSerializer
    
    @extend_schema(
        summary="Buscar reportes de presupuesto por periodo",
        description="Busca reportes de presupuesto que contengan el periodo especificado",
        parameters=[
            OpenApiParameter(
                name='period',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Periodo del reporte a buscar',
                required=True
            )
        ],
        tags=['Reporte de Presupuesto']
    )
    @action(detail=False, methods=['get'])
    def search_by_period(self, request):
        """Busca reportes de presupuesto por periodo"""
        period = request.query_params.get('period', '')
        reports = self.queryset.filter(period_type__icontains=period)
        serializer = self.get_serializer(reports, many=True)        
        return Response(serializer.data)    

# ViewSet para gestionar los rubros presupuestales de ingresos
@extend_schema_view(
    list=extend_schema(
        summary="Listar todos los rubros presupuestales de ingresos",
        description="Obtiene una lista de todos los rubros presupuestales de ingresos registrados en el sistema",
        tags=['Rubros Presupuestales de Ingresos']),
    
    retrieve=extend_schema(
        summary="Obtener un rubro presupuestal de ingresos específico",
        description="Obtiene los detalles de un rubro presupuestal de ingresos por su ID",
        tags=['Rubros Presupuestales de Ingresos']),
    
    create=extend_schema(
        summary="Crear un nuevo rubro presupuestal de ingresos",
        description="Crea un nuevo rubro presupuestal de ingresos en el sistema",
        tags=['Rubros Presupuestales de Ingresos'],
        examples=[OpenApiExample('Ejemplo de creación', value={'code': '001-2024-ADM', 'level': '1', 'type': 'A', 'account_name': 'Gastos Administrativos', 'father': '001-2024-ADM'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar un rubro presupuestal de ingresos",
        description="Actualiza completamente un rubro presupuestal de ingresos existente",
        tags=['Rubros Presupuestales de Ingresos']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente un rubro presupuestal de ingresos",
        description="Actualiza uno o más campos de un rubro presupuestal de ingresos existente",
        tags=['Rubros Presupuestales de Ingresos']
    ),
    destroy=extend_schema(
        summary="Eliminar un rubro presupuestal de ingresos",
        description="Elimina un rubro presupuestal de ingresos del sistema",
        tags=['Rubros Presupuestales de Ingresos']
    )
)
class BudgetItemRevenueViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar los rubros presupuestales de ingresos.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todos los rubros presupuestales de ingresos
    - retrieve: Obtener un rubro presupuestal de ingresos específico
    - create: Crear un nuevo rubro presupuestal de ingresos
    - update: Actualizar un rubro presupuestal de ingresos completo
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar un rubro presupuestal de ingresos
    """
    queryset = BudgetItemRevenue.objects.all()
    serializer_class = BudgetItemRevenueSerializer
    
    @extend_schema(
        summary="Buscar rubros presupuestales de ingresos por código",
        description="Busca rubros presupuestales de ingresos que contengan el código especificado",
        parameters=[
            OpenApiParameter(
                name='code',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Código de presupuesto a buscar',
                required=True
            )
        ],
        tags=['Rubros Presupuestales de Ingresos']
    )
    @action(detail=False, methods=['get'])
    def search_by_code(self, request):
        """Busca rubros presupuestales de ingresos por código"""
        code = request.query_params.get('code', '')
        rubros = self.queryset.filter(code__icontains=code)
        serializer = self.get_serializer(rubros, many=True)
        return Response(serializer.data)    

# ViewSet para gestionar los rubros presupuestales de gastos
@extend_schema_view(
    list=extend_schema(
        summary="Listar todos los rubros presupuestales de gastos",
        description="Obtiene una lista de todos los rubros presupuestales de gastos registrados en el sistema",
        tags=['Rubros Presupuestales de Gastos']),
    
    retrieve=extend_schema(
        summary="Obtener un rubro presupuestal de gastos específico",
        description="Obtiene los detalles de un rubro presupuestal de gastos por su ID",
        tags=['Rubros Presupuestales de Gastos']),
    
    create=extend_schema(
        summary="Crear un nuevo rubro presupuestal de gastos",
        description="Crea un nuevo rubro presupuestal de gastos en el sistema",
        tags=['Rubros Presupuestales de Gastos'],
        examples=[OpenApiExample('Ejemplo de creación', value={'code': '001-2024-ADM', 'level': '1', 'type': 'A', 'account_name': 'Gastos Administrativos', 'father': '001-2024-ADM'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar un rubro presupuestal de gastos",
        description="Actualiza completamente un rubro presupuestal de gastos existente",
        tags=['Rubros Presupuestales de Gastos']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente un rubro presupuestal de gastos",
        description="Actualiza uno o más campos de un rubro presupuestal de gastos existente",
        tags=['Rubros Presupuestales de Gastos']
    ),
    destroy=extend_schema(
        summary="Eliminar un rubro presupuestal de gastos",
        description="Elimina un rubro presupuestal de gastos del sistema",
        tags=['Rubros Presupuestales de Gastos']
    )
)
class BudgetItemExpensesViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar los rubros presupuestales de gastos.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todos los rubros presupuestales de gastos
    - retrieve: Obtener un rubro presupuestal de gastos específico
    - create: Crear un nuevo rubro presupuestal de gastos
    - update: Actualizar un rubro presupuestal de gastos completo
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar un rubro presupuestal de gastos
    """
    queryset = BudgetItemExpenses.objects.all()
    serializer_class = BudgetItemExpensesSerializer
    
    @extend_schema(
        summary="Buscar rubros presupuestales de gastos por código",
        description="Busca rubros presupuestales de gastos que contengan el código especificado",
        parameters=[
            OpenApiParameter(
                name='code',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Código de presupuesto a buscar',
                required=True
            )
        ],
        tags=['Rubros Presupuestales de Gastos']
    )
    @action(detail=False, methods=['get'])
    def search_by_code(self, request):
        """Busca rubros presupuestales de gastos por código"""
        code = request.query_params.get('code', '')
        rubros = self.queryset.filter(code__icontains=code)
        serializer = self.get_serializer(rubros, many=True)
        return Response(serializer.data)

# ViewSet para gestionar los plan contables
@extend_schema_view(
    list=extend_schema(
        summary="Listar todos los plan contables",
        description="Obtiene una lista de todos los plan contables registrados en el sistema",
        tags=['Plan Contable']),
    
    retrieve=extend_schema(
        summary="Obtener un plan contable específico",
        description="Obtiene los detalles de un plan contable por su ID",
        tags=['Plan Contable']),
    
    create=extend_schema(
        summary="Crear un nuevo plan contable",
        description="Crea un nuevo plan contable en el sistema",
        tags=['Plan Contable'],
        examples=[OpenApiExample('Ejemplo de creación', value={'code': '001-2024-ADM', 'name': 'Plan Contable Administrativo', 'nature': 'General', 'father': '001-2024-ADM', 'type': 'General'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar un plan contable",
        description="Actualiza completamente un plan contable existente",
        tags=['Plan Contable']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente un plan contable",
        description="Actualiza uno o más campos de un plan contable existente",
        tags=['Plan Contable']
    ),
    destroy=extend_schema(
        summary="Eliminar un plan contable",
        description="Elimina un plan contable del sistema",
        tags=['Plan Contable']
    )
)
class AccountantPucViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar los plan contables.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todos los plan contables
    - retrieve: Obtener un plan contable específico
    - create: Crear un nuevo plan contable
    - update: Actualizar un plan contable completo
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar un plan contable
    """
    queryset = AccountantPuc.objects.all()
    serializer_class = AccountantPucSerializer
    
    @extend_schema(
        summary="Buscar plan contables por código",
        description="Busca plan contables que contengan el código especificado",
        parameters=[
            OpenApiParameter(
                name='code',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Código de presupuesto a buscar',
                required=True
            )
        ],
        tags=['Plan Contable']
    )
    @action(detail=False, methods=['get'])
    def search_by_code(self, request):
        """Busca plan contables por código"""
        code = request.query_params.get('code', '')
        plan_contables = self.queryset.filter(code__icontains=code)
        serializer = self.get_serializer(plan_contables, many=True)
        return Response(serializer.data)    

# ViewSet para gestionar las cuentas de gastos
@extend_schema_view(
    list=extend_schema(
        summary="Listar todas las cuentas de gastos",
        description="Obtiene una lista de todas las cuentas de gastos registradas en el sistema",
        tags=['Cuentas de Gastos']
    ),
    retrieve=extend_schema(
        summary="Obtener una cuenta de gasto específica",
        description="Obtiene los detalles de una cuenta de gasto por su ID",
        tags=['Cuentas de Gastos']
    ),
    create=extend_schema(
        summary="Crear una nueva cuenta de gasto",
        description="Crea una nueva cuenta de gasto en el sistema",
        tags=['Cuentas de Gastos'],
        examples=[
            OpenApiExample(
                'Ejemplo de creación',
                value={
                    'budget_code_expenses': '001-2024-ADM',
                    'accountant_name': 'Gastos Administrativos'
                },
                request_only=True
            )
        ]
    ),
    update=extend_schema(
        summary="Actualizar una cuenta de gasto",
        description="Actualiza completamente una cuenta de gasto existente",
        tags=['Cuentas de Gastos']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una cuenta de gasto",
        description="Actualiza uno o más campos de una cuenta de gasto existente",
        tags=['Cuentas de Gastos']
    ),
    destroy=extend_schema(
        summary="Eliminar una cuenta de gasto",
        description="Elimina una cuenta de gasto del sistema",
        tags=['Cuentas de Gastos']
    )
)
class ExpenseAccountsViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar las cuentas de gastos.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todas las cuentas
    - retrieve: Obtener una cuenta específica
    - create: Crear una nueva cuenta
    - update: Actualizar una cuenta completa
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar una cuenta
    """
    queryset = ExpenseAccounts.objects.all()
    serializer_class = ExpenseAccountsSerializer
    
    @extend_schema(
        summary="Buscar cuentas por código",
        description="Busca cuentas de gasto que contengan el código especificado",
        parameters=[
            OpenApiParameter(
                name='code',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Código de presupuesto a buscar',
                required=True
            )
        ],
        tags=['Cuentas de Gastos']
    )
    @action(detail=False, methods=['get'])
    def search_by_code(self, request):
        """Busca cuentas por código de presupuesto"""
        code = request.query_params.get('code', '')
        accounts = self.queryset.filter(budget_code_expenses__icontains=code)
        serializer = self.get_serializer(accounts, many=True)
        return Response(serializer.data)

# ViewSet para gestionar las fuentes de recursos
@extend_schema_view(    
    list=extend_schema(
        summary="Listar todas las fuentes de recursos",
        description="Obtiene una lista de todas las fuentes de recursos registradas en el sistema",
        tags=['Fuentes de Recursos']),
    
    retrieve=extend_schema(
        summary="Obtener una fuente de recursos específico",
        description="Obtiene los detalles de una fuente de recursos por su ID",
        tags=['Fuentes de Recursos']),
    
    create=extend_schema(
        summary="Crear una nueva fuente de recursos",
        description="Crea una nueva fuente de recursos en el sistema",
        tags=['Fuentes de Recursos'],
        examples=[OpenApiExample('Ejemplo de creación', value={'source_name': 'Fuente de Recursos Administrativa'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar una fuente de recursos",
        description="Actualiza completamente una fuente de recursos existente",
        tags=['Fuentes de Recursos']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una fuente de recursos",
        description="Actualiza uno o más campos de una fuente de recursos existente",
        tags=['Fuentes de Recursos']
    ),
    destroy=extend_schema(
        summary="Eliminar una fuente de recursos",
        description="Elimina una fuente de recursos del sistema",
        tags=['Fuentes de Recursos']
    )
)
class SourceResourcesViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar las fuentes de recursos.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todas las fuentes de recursos
    - retrieve: Obtener una fuente de recursos específica
    - create: Crear una nueva fuente de recursos
    - update: Actualizar una fuente de recursos completa
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar una fuente de recursos
    """
    queryset = SourceResources.objects.all()
    serializer_class = SourceResourcesSerializer
    
    @extend_schema(
        summary="Buscar fuentes de recursos por nombre",
        description="Busca fuentes de recursos que contengan el nombre especificado",
        parameters=[
            OpenApiParameter(
                name='name',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Nombre de la fuente de recursos a buscar',
                required=True
            )
        ],
        tags=['Fuentes de Recursos']
    )
    @action(detail=False, methods=['get'])
    def search_by_name(self, request):
        """Busca fuentes de recursos por nombre"""
        name = request.query_params.get('name', '')
        fuentes = self.queryset.filter(source_name__icontains=name)
        serializer = self.get_serializer(fuentes, many=True)        
        return Response(serializer.data)

# ViewSet para gestionar los bancos
@extend_schema_view(    
    list=extend_schema(
        summary="Listar todos los bancos",
        description="Obtiene una lista de todos los bancos registrados en el sistema",
        tags=['Bancos']),
    
    retrieve=extend_schema(
        summary="Obtener un banco específico",
        description="Obtiene los detalles de un banco por su ID",
        tags=['Bancos']),
    
    create=extend_schema(
        summary="Crear un nuevo banco",
        description="Crea un nuevo banco en el sistema",
        tags=['Bancos'],
        examples=[OpenApiExample('Ejemplo de creación', value={'bank_name': 'Banco de Prueba'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar un banco",
        description="Actualiza completamente un banco existente",
        tags=['Bancos']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente un banco",
        description="Actualiza uno o más campos de un banco existente",
        tags=['Bancos']
    ),
    destroy=extend_schema(
        summary="Eliminar un banco",
        description="Elimina un banco del sistema",
        tags=['Bancos']
    )
)
class BankViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar los bancos.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todos los bancos
    - retrieve: Obtener un banco específico
    - create: Crear un nuevo banco
    - update: Actualizar un banco completo
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar un banco
    """
    queryset = Bank.objects.all()
    serializer_class = BankSerializer
    
    @extend_schema(
        summary="Buscar bancos por nombre",
        description="Busca bancos que contengan el nombre especificado",
        parameters=[
            OpenApiParameter(
                name='name',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Nombre del banco a buscar',
                required=True
            )
        ],
        tags=['Bancos']
    )
    @action(detail=False, methods=['get'])
    def search_by_name(self, request):
        """Busca bancos por nombre"""
        name = request.query_params.get('name', '')
        bancos = self.queryset.filter(bank_name__icontains=name)
        serializer = self.get_serializer(bancos, many=True)        
        return Response(serializer.data)

# ViewSet para gestionar la ejecución presupuestal de gastos F7
@extend_schema_view(    
    list=extend_schema(
        summary="Listar todas las ejecuciones presupuestal de gastos F7",
        description="Obtiene una lista de todas las ejecuciones presupuestal de gastos F7 registradas en el sistema",
        tags=['Ejecución Presupuestal de Gastos F7']),
    
    retrieve=extend_schema(
        summary="Obtener una ejecución presupuestal de gastos F7 específica",
        description="Obtiene los detalles de una ejecución presupuestal de gastos F7 por su ID",
        tags=['Ejecución Presupuestal de Gastos F7']),
    
    create=extend_schema(
        summary="Crear una nueva ejecución presupuestal de gastos F7",
        description="Crea una nueva ejecución presupuestal de gastos F7 en el sistema",
        tags=['Ejecución Presupuestal de Gastos F7'],
        examples=[OpenApiExample('Ejemplo de creación', value={'id_budget_item_expenses': '001-2024-ADM', 'id_institution': '001-2024-ADM', 'id_budget_report': '001-2024-ADM', 'program_code': '001-2024-ADM'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar una ejecución presupuestal de gastos F7",
        description="Actualiza completamente una ejecución presupuestal de gastos F7 existente",
        tags=['Ejecución Presupuestal de Gastos F7']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una ejecución presupuestal de gastos F7",
        description="Actualiza uno o más campos de una ejecución presupuestal de gastos F7 existente",
        tags=['Ejecución Presupuestal de Gastos F7']
    ),
    destroy=extend_schema(
        summary="Eliminar una ejecución presupuestal de gastos F7",
        description="Elimina una ejecución presupuestal de gastos F7 del sistema",
        tags=['Ejecución Presupuestal de Gastos F7']
    )
)
class F7BudgetExecutionExpensesViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar la ejecución presupuestal de gastos F7.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todas las ejecuciones presupuestal de gastos F7
    - retrieve: Obtener una ejecución presupuestal de gastos F7 específica
    - create: Crear una nueva ejecución presupuestal de gastos F7
    - update: Actualizar una ejecución presupuestal de gastos F7 completa
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar una ejecución presupuestal de gastos F7
    """
    queryset = F7BudgetExecutionExpenses.objects.all()
    serializer_class = F7BudgetExecutionExpensesSerializer
    
    @extend_schema(
        summary="Buscar ejecuciones presupuestal de gastos F7 por código",
        description="Busca ejecuciones presupuestal de gastos F7 que contengan el código especificado",
        parameters=[
            OpenApiParameter(
                name='code',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Código de presupuesto a buscar',
                required=True
            )
        ],
        tags=['Ejecución Presupuestal de Gastos F7']
    )
    @action(detail=False, methods=['get'])
    def search_by_code(self, request):
        """Busca ejecuciones presupuestal de gastos F7 por código"""
        code = request.query_params.get('code', '')
        ejecuciones = self.queryset.filter(id_budget_item_expenses__icontains=code)
        serializer = self.get_serializer(ejecuciones, many=True)        
        return Response(serializer.data)    

# ViewSet para gestionar las cuentas por pagar F11
@extend_schema_view(    
    list=extend_schema(
        summary="Listar todas las cuentas por pagar F11",
        description="Obtiene una lista de todas las cuentas por pagar F11 registradas en el sistema",
        tags=['Cuentas por Pagar F11']),
    
    retrieve=extend_schema(
        summary="Obtener una cuenta por pagar F11 específica",
        description="Obtiene los detalles de una cuenta por pagar F11 por su ID",
        tags=['Cuentas por Pagar F11']),
    
    create=extend_schema(
        summary="Crear una nueva cuenta por pagar F11",
        description="Crea una nueva cuenta por pagar F11 en el sistema",
        tags=['Cuentas por Pagar F11'],
        examples=[OpenApiExample('Ejemplo de creación', value={'id_budget_item_expenses': '001-2024-ADM', 'id_institution': '001-2024-ADM', 'id_budget_report': '001-2024-ADM', 'description': 'Descripción de la cuenta'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar una cuenta por pagar F11",
        description="Actualiza completamente una cuenta por pagar F11 existente",
        tags=['Cuentas por Pagar F11']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una cuenta por pagar F11",
        description="Actualiza uno o más campos de una cuenta por pagar F11 existente",
        tags=['Cuentas por Pagar F11']
    ),
    destroy=extend_schema(
        summary="Eliminar una cuenta por pagar F11",
        description="Elimina una cuenta por pagar F11 del sistema",
        tags=['Cuentas por Pagar F11']
    )
)
class F11AccountsPayableViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar las cuentas por pagar F11.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todas las cuentas por pagar F11
    - retrieve: Obtener una cuenta por pagar F11 específica
    - create: Crear una nueva cuenta por pagar F11
    - update: Actualizar una cuenta por pagar F11 completa
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar una cuenta por pagar F11
    """
    queryset = F11AccountsPayable.objects.all()
    serializer_class = F11AccountsPayableSerializer
    
    @extend_schema(
        summary="Buscar cuentas por pagar F11 por código",
        description="Busca cuentas por pagar F11 que contengan el código especificado",
        parameters=[
            OpenApiParameter(
                name='code',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Código de presupuesto a buscar',
                required=True
            )
        ],
        tags=['Cuentas por Pagar F11']
    )
    @action(detail=False, methods=['get'])
    def search_by_code(self, request):
        """Busca cuentas por pagar F11 por código"""
        code = request.query_params.get('code', '')
        cuentas = self.queryset.filter(id_budget_item_expenses__icontains=code)
        serializer = self.get_serializer(cuentas, many=True)        
        return Response(serializer.data)            

# ViewSet para gestionar las contrataciones F13
@extend_schema_view(    
    list=extend_schema(
        summary="Listar todas las contrataciones",
        description="Obtiene una lista de todas las contrataciones registradas en el sistema",
        tags=['Contrataciones F13']),
    
    retrieve=extend_schema(
        summary="Obtener una contratación específica",
        description="Obtiene los detalles de una contratación por su ID",
        tags=['Contrataciones F13']),
    
    create=extend_schema(
        summary="Crear una nueva contratación",
        description="Crea una nueva contratación en el sistema",
        tags=['Contrataciones F13'],
        examples=[OpenApiExample('Ejemplo de creación', value={'contract_number': '001-2024-ADM', 'contractor_name': 'Contratista', 'nit_cc_contractor': '1234567890', 'budget_unavailability': '100', 'value_availability': '100', 'signature_date': '2024-01-01', 'contract_form': 'Formulario 1', 'budget_registration_date': '2024-01-01', 'budget_registration_number': '001-2024-ADM', 'budget_record_value': '100', 'date_approval_single_guarantee': '2024-01-01', 'start_date': '2024-01-01', 'contract_term': '1', 'addition_date': '2024-01-01', 'addtion_term': '1', 'addition_value': '100', 'value_payments_made': '100', 'completion_date': '2024-01-01', 'sattlement_date': '2024-01-01'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar una contratación",
        description="Actualiza completamente una contratación existente",
        tags=['Contrataciones F13']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una contratación",
        description="Actualiza uno o más campos de una contratación existente",
        tags=['Contrataciones F13']
    ),
    destroy=extend_schema(
        summary="Eliminar una contratación",
        description="Elimina una contratación del sistema",
        tags=['Contrataciones F13']
    )
)
class F13HiringViewSet(viewsets.ModelViewSet):    
    """
    ViewSet para gestionar las contrataciones F13.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todas las contrataciones
    - retrieve: Obtener una contratación específica
    - create: Crear una nueva contratación
    - update: Actualizar una contratación completa
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar una contratación
    """
    queryset = F13Hiring.objects.all()
    serializer_class = F13HiringSerializer
    
    @extend_schema(
        summary="Buscar contrataciones por código",
        description="Busca contrataciones que contengan el código especificado",
        parameters=[
            OpenApiParameter(
                name='code',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Código de presupuesto a buscar',
                required=True
            )
        ],
        tags=['Contrataciones F13']
    )
    @action(detail=False, methods=['get'])
    def search_by_code(self, request):
        """Busca contrataciones por código"""
        code = request.query_params.get('code', '')
        contrataciones = self.queryset.filter(contract_number__icontains=code)
        serializer = self.get_serializer(contrataciones, many=True)        
        return Response(serializer.data)        

# ViewSet para gestionar la relación de ingresos IEF02
@extend_schema_view(    
    list=extend_schema(
        summary="Listar todas las relaciones de ingresos IEF02",
        description="Obtiene una lista de todas las relaciones de ingresos IEF02 registradas en el sistema",
        tags=['Relaciones de Ingresos IEF02']),
    
    retrieve=extend_schema(
        summary="Obtener una relación de ingresos IEF02 específica",
        description="Obtiene los detalles de una relación de ingresos IEF02 por su ID",
        tags=['Relaciones de Ingresos IEF02']),
    
    create=extend_schema(
        summary="Crear una nueva relación de ingresos IEF02",
        description="Crea una nueva relación de ingresos IEF02 en el sistema",
        tags=['Relaciones de Ingresos IEF02'],
        examples=[OpenApiExample('Ejemplo de creación', value={'id_budget_item_revenue': '001-2024-ADM', 'id_institution': '001-2024-ADM', 'id_budget_report': '001-2024-ADM', 'collection_date': '2024-01-01', 'detail': 'Detalle', 'receipt_bank': 'Banco', 'value': '100', 'bank_account_number': '1234567890', 'bank': 'Banco', 'revenue_resources': 'Fuente de Ingresos', 'created_at': '2024-01-01', 'updated_at': '2024-01-01'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar una relación de ingresos IEF02",
        description="Actualiza completamente una relación de ingresos IEF02 existente",
        tags=['Relaciones de Ingresos IEF02']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una relación de ingresos IEF02",        
        description="Actualiza uno o más campos de una relación de ingresos IEF02 existente",
        tags=['Relaciones de Ingresos IEF02']
    ),
    destroy=extend_schema(
        summary="Eliminar una relación de ingresos IEF02",
        description="Elimina una relación de ingresos IEF02 del sistema",
        tags=['Relaciones de Ingresos IEF02']
    )
)
class Ief02RevenueStatementViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar la relación de ingresos IEF02.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todas las relaciones de ingresos IEF02
    - retrieve: Obtener una relación de ingresos IEF02 específica
    - create: Crear una nueva relación de ingresos IEF02
    - update: Actualizar una relación de ingresos IEF02 completa
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar una relación de ingresos IEF02
    """
    queryset = Ief02RevenueStatement.objects.all()
    serializer_class = Ief02RevenueStatementSerializer
    
    @extend_schema(
        summary="Buscar relaciones de ingresos IEF02 por código",
        description="Busca relaciones de ingresos IEF02 que contengan el código especificado",
        parameters=[
            OpenApiParameter(
                name='code',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Código de presupuesto a buscar',
                required=True
            )
        ],
        tags=['Relaciones de Ingresos IEF02']
    )
    @action(detail=False, methods=['get'])
    def search_by_code(self, request):
        """Busca relaciones de ingresos IEF02 por código"""
        code = request.query_params.get('code', '')
        relaciones = self.queryset.filter(id_budget_item_revenue__icontains=code)
        serializer = self.get_serializer(relaciones, many=True)        
        return Response(serializer.data)

# ViewSet para gestionar la relación de pagos IEF04
@extend_schema_view(    
    list=extend_schema(
        summary="Listar todas las relaciones de pagos IEF04",
        description="Obtiene una lista de todas las relaciones de pagos IEF04 registradas en el sistema",
        tags=['Relaciones de Pagos IEF04']),
    
    retrieve=extend_schema(
        summary="Obtener una relación de pagos IEF04 específica",
        description="Obtiene los detalles de una relación de pagos IEF04 por su ID",
        tags=['Relaciones de Pagos IEF04']),
    
    create=extend_schema(
        summary="Crear una nueva relación de pagos IEF04",
        description="Crea una nueva relación de pagos IEF04 en el sistema",
        tags=['Relaciones de Pagos IEF04'],
        examples=[OpenApiExample('Ejemplo de creación', value={'id_budget_item_expenses': '001-2024-ADM', 'id_institution': '001-2024-ADM', 'id_budget_report': '001-2024-ADM', 'collection_date': '2024-01-01', 'receipt_number': '1234567890', 'detail': 'Detalle', 'beneficiary': 'Beneficiario', 'cc_nit': '1234567890', 'total_value_receipt': '100', 'withholdings': '100', 'discounts': '100', 'bank': 'Banco', 'account_number': '1234567890', 'check_number': '1234567890', 'funding_source': 'Fuente de Financiación', 'beneficiary': 'Beneficiario', 'created_at': '2024-01-01', 'updated_at': '2024-01-01'}, request_only=True)]),
    
    update=extend_schema(        
        summary="Actualizar una relación de pagos IEF04",
        description="Actualiza completamente una relación de pagos IEF04 existente",
        tags=['Relaciones de Pagos IEF04']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una relación de pagos IEF04",        
        description="Actualiza uno o más campos de una relación de pagos IEF04 existente",
        tags=['Relaciones de Pagos IEF04']
    ),
    destroy=extend_schema(
        summary="Eliminar una relación de pagos IEF04",
        description="Elimina una relación de pagos IEF04 del sistema",
        tags=['Relaciones de Pagos IEF04']
    )
)
class Ief04PaymentsRelationshipViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar la relación de pagos IEF04.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todas las relaciones de pagos IEF04
    - retrieve: Obtener una relación de pagos IEF04 específica
    - create: Crear una nueva relación de pagos IEF04
    - update: Actualizar una relación de pagos IEF04 completa
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar una relación de pagos IEF04
    """
    queryset = Ief04PaymentsRelationship.objects.all()
    serializer_class = Ief04PaymentsRelationshipSerializer
    
    @extend_schema(
        summary="Buscar relaciones de pagos IEF04 por código",
        description="Busca relaciones de pagos IEF04 que contengan el código especificado",
        parameters=[
            OpenApiParameter(
                name='code',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Código de presupuesto a buscar',
                required=True
            )
        ],
        tags=['Relaciones de Pagos IEF04']
    )
    @action(detail=False, methods=['get'])
    def search_by_code(self, request):
        """Busca relaciones de pagos IEF04 por código"""
        code = request.query_params.get('code', '')
        relaciones = self.queryset.filter(id_budget_item_expenses__icontains=code)
        serializer = self.get_serializer(relaciones, many=True)        
        return Response(serializer.data)    

#! ViewSet para gestionar cierre presupuestal de ingresos

#* ViewSet para gestionar presupuesto de ingresos
@extend_schema_view(
    list=extend_schema(
        summary="Listar todos los presupuestos de ingresos",
        description="Obtiene una lista de todos los presupuestos de ingresos registrados en el sistema",
        tags=['Presupuesto de Ingresos']),
    
    retrieve=extend_schema(
        summary="Obtener un presupuesto de ingresos específico",
        description="Obtiene los detalles de un presupuesto de ingresos por su ID",
        tags=['Presupuesto de Ingresos']),
    
    create=extend_schema(
        summary="Crear un nuevo presupuesto de ingresos",
        description="Crea un nuevo presupuesto de ingresos en el sistema",
        tags=['Presupuesto de Ingresos'],
        examples=[OpenApiExample('Ejemplo de creación', value={'id_institution': '001-2024-ADM', 'id_budget_item_revenue': '001-2024-ADM', 'period': 'Trimestral', 'initial_appropriation': '100', 'final_appropriation': '100', 'created_at': '2024-01-01', 'updated_at': '2024-01-01'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar un presupuesto de ingresos",
        description="Actualiza completamente un presupuesto de ingresos existente",
        tags=['Presupuesto de Ingresos']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente un presupuesto de ingresos",
        description="Actualiza uno o más campos de un presupuesto de ingresos existente",
        tags=['Presupuesto de Ingresos']
    ),
    destroy=extend_schema(
        summary="Eliminar un presupuesto de ingresos",
        description="Elimina un presupuesto de ingresos del sistema",
        tags=['Presupuesto de Ingresos']
    )
)
class RevenueBudgetViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar presupuesto de ingresos.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todos los presupuestos de ingresos
    - retrieve: Obtener un presupuesto de ingresos específico
    - create: Crear un nuevo presupuesto de ingresos
    - update: Actualizar un presupuesto de ingresos completo
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar un presupuesto de ingresos
    """
    queryset = RevenueBudget.objects.all()
    serializer_class = RevenueBudgetSerializer
    
    @extend_schema(
        summary="Buscar presupuestos de ingresos por código",
        description="Busca presupuestos de ingresos que contengan el código especificado",
        parameters=[
            OpenApiParameter(
                name='code',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Código de presupuesto a buscar',
                required=True
            )
        ],
        tags=['Presupuesto de Ingresos']
    )
    @action(detail=False, methods=['get'])
    def search_by_code(self, request):
        """Busca presupuestos de ingresos por código"""
        code = request.query_params.get('code', '')
        presupuestos = self.queryset.filter(id_budget_item_revenue__icontains=code)
        serializer = self.get_serializer(presupuestos, many=True)        
        return Response(serializer.data)

#* ViewSet para gestionar modificaciones del periodo - ingresos
@extend_schema_view(
    list=extend_schema(
        summary="Listar todas las modificaciones del periodo - ingresos",
        description="Obtiene una lista de todas las modificaciones del periodo - ingresos registradas en el sistema",
        tags=['Modificaciones del Periodo - Ingresos']),
    
    retrieve=extend_schema(
        summary="Obtener una modificación del periodo - ingresos específica",
        description="Obtiene los detalles de una modificación del periodo - ingresos por su ID",
        tags=['Modificaciones del Periodo - Ingresos']),
    
    create=extend_schema(
        summary="Crear una nueva modificación del periodo - ingresos",
        description="Crea una nueva modificación del periodo - ingresos en el sistema",
        tags=['Modificaciones del Periodo - Ingresos'],
        examples=[OpenApiExample('Ejemplo de creación', value={'id_revenue_budget': '001-2024-ADM', 'addition': '100', 'reduction': '100', 'credit_transfer': '100', 'countercredit_transfer': '100', 'created_at': '2024-01-01', 'updated_at': '2024-01-01'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar una modificación del periodo - ingresos",
        description="Actualiza completamente una modificación del periodo - ingresos existente",
        tags=['Modificaciones del Periodo - Ingresos']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una modificación del periodo - ingresos",
        description="Actualiza uno o más campos de una modificación del periodo - ingresos existente",
        tags=['Modificaciones del Periodo - Ingresos']
    ),
    destroy=extend_schema(
        summary="Eliminar una modificación del periodo - ingresos",
        description="Elimina una modificación del periodo - ingresos del sistema",
        tags=['Modificaciones del Periodo - Ingresos']
    )
)
class ChangesRevenuePeriodViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar modificaciones del periodo - ingresos.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todas las modificaciones del periodo - ingresos
    - retrieve: Obtener una modificación del periodo - ingresos específica
    - create: Crear una nueva modificación del periodo - ingresos
    - update: Actualizar una modificación del periodo - ingresos completa
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar una modificación del periodo - ingresos
    """
    queryset = ChangesRevenuePeriod.objects.all()
    serializer_class = ChangesRevenuePeriodSerializer
    
    @extend_schema(
        summary="Buscar modificaciones del periodo - ingresos por código",
        description="Busca modificaciones del periodo - ingresos que contengan el código especificado",
        parameters=[
            OpenApiParameter(
                name='code',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Código de presupuesto a buscar',
                required=True
            )
        ],
        tags=['Modificaciones del Periodo - Ingresos']
    )
    @action(detail=False, methods=['get'])
    def search_by_code(self, request):
        """Busca modificaciones del periodo - ingresos por código"""
        code = request.query_params.get('code', '')
        modificaciones = self.queryset.filter(id_revenue_budget__icontains=code)
        serializer = self.get_serializer(modificaciones, many=True)        
        return Response(serializer.data)
    
#* ViewSet para gestionar modificaciones acumuladas - ingresos
@extend_schema_view(
    list=extend_schema(
        summary="Listar todas las modificaciones acumuladas - ingresos",
        description="Obtiene una lista de todas las modificaciones acumuladas - ingresos registradas en el sistema",
        tags=['Modificaciones Acumuladas - Ingresos']), 
    retrieve=extend_schema(
        summary="Obtener una modificación acumulada - ingresos específica", 
        description="Obtiene los detalles de una modificación acumulada - ingresos por su ID", 
        tags=['Modificaciones Acumuladas - Ingresos']),
    
    create=extend_schema(
        summary="Crear una nueva modificación acumulada - ingresos", 
        description="Crea una nueva modificación acumulada - ingresos en el sistema", 
        tags=['Modificaciones Acumuladas - Ingresos'],
        examples=[OpenApiExample('Ejemplo de creación', value={'id_revenue_budget': '001-2024-ADM', 'accumulated_additions': '100', 'accumulated_reductions': '100', 'transfer_accumulated_credits': '100', 'transfer_accumulated_countercredits': '100', 'created_at': '2024-01-01', 'updated_at': '2024-01-01'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar una modificación acumulada - ingresos", 
        description="Actualiza completamente una modificación acumulada - ingresos existente", 
        tags=['Modificaciones Acumuladas - Ingresos']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una modificación acumulada - ingresos", 
        description="Actualiza uno o más campos de una modificación acumulada - ingresos existente", 
        tags=['Modificaciones Acumuladas - Ingresos']
    ),
    destroy=extend_schema(
        summary="Eliminar una modificación acumulada - ingresos", 
        description="Elimina una modificación acumulada - ingresos del sistema",         
        tags=['Modificaciones Acumuladas - Ingresos']
    )
)
class CumulativeChangesRevenueViewSet(viewsets.ModelViewSet):
    """            
    ViewSet para gestionar modificaciones acumuladas - ingresos.            
            
    Proporciona operaciones CRUD completas:            
    - list: Listar todas las modificaciones acumuladas - ingresos            
    - retrieve: Obtener una modificación acumulada - ingresos específica            
    - create: Crear una nueva modificación acumulada - ingresos            
    - update: Actualizar una modificación acumulada - ingresos completa            
    - partial_update: Actualizar campos específicos            
    - destroy: Eliminar una modificación acumulada - ingresos            
    """
    queryset = CumulativeChangesRevenue.objects.all()            
    serializer_class = CumulativeChangesRevenueSerializer                      
    
    @extend_schema(            
        summary="Buscar modificaciones acumuladas - ingresos por código",   
        description="Busca modificaciones acumuladas - ingresos que contengan el código especificado",            
        parameters=[            
            OpenApiParameter(                
                name='code',                
                type=OpenApiTypes.STR,                
                location=OpenApiParameter.QUERY,                
                description='Código de presupuesto a buscar',                
                required=True                
            )            
        ],            
        tags=['Modificaciones Acumuladas - Ingresos']            
    )            
    @action(detail=False, methods=['get'])            
    def search_by_code(self, request):                
        """Busca modificaciones acumuladas - ingresos por código"""                
        code = request.query_params.get('code', '')                
        modificaciones = self.queryset.filter(id_revenue_budget__icontains=code)                
        serializer = self.get_serializer(modificaciones, many=True)        
        return Response(serializer.data)    
    
#* ViewSet para gestionar la ejecución de ingresos
@extend_schema_view(
    list=extend_schema(
        summary="Listar todas las ejecuciones de ingresos",
        description="Obtiene una lista de todas las ejecuciones de ingresos registradas en el sistema",
        tags=['Ejecución de Ingresos']),
    
    retrieve=extend_schema(
        summary="Obtener una ejecución de ingresos específica",
        description="Obtiene los detalles de una ejecución de ingresos por su ID",
        tags=['Ejecución de Ingresos']),
    
    create=extend_schema(
        summary="Crear una nueva ejecución de ingresos",
        description="Crea una nueva ejecución de ingresos en el sistema",
        tags=['Ejecución de Ingresos'],        
        examples=[OpenApiExample('Ejemplo de creación', value={'id_revenue_budget': '001-2024-ADM', 'monthly_revenue_value': '100', 'accumulated_revenue': '100', 'income_receivable': '100', 'created_at': '2024-01-01', 'updated_at': '2024-01-01'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar una ejecución de ingresos",
        description="Actualiza completamente una ejecución de ingresos existente",
        tags=['Ejecución de Ingresos']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una ejecución de ingresos",
        description="Actualiza uno o más campos de una ejecución de ingresos existente",
        tags=['Ejecución de Ingresos']
    ),
    destroy=extend_schema(
        summary="Eliminar una ejecución de ingresos",
        description="Elimina una ejecución de ingresos del sistema",
        tags=['Ejecución de Ingresos']
    )
)
class RevenueExecutionViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar ejecución de ingresos.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todas las ejecuciones de ingresos
    - retrieve: Obtener una ejecución de ingresos específica
    - create: Crear una nueva ejecución de ingresos
    - update: Actualizar una ejecución de ingresos completa
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar una ejecución de ingresos
    """
    queryset = RevenueExecution.objects.all()
    serializer_class = RevenueExecutionSerializer
    
    @extend_schema(
        summary="Buscar ejecuciones de ingresos por código",
        description="Busca ejecuciones de ingresos que contengan el código especificado",
        parameters=[
            OpenApiParameter(
                name='code',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Código de presupuesto a buscar',
                required=True
            )
        ],
        tags=['Ejecución de Ingresos']
    )
    @action(detail=False, methods=['get'])
    def search_by_code(self, request):
        """Busca ejecuciones de ingresos por código"""
        code = request.query_params.get('code', '')
        ejecuciones = self.queryset.filter(id_revenue_budget__icontains=code)
        serializer = self.get_serializer(ejecuciones, many=True)        
        return Response(serializer.data)    

#! ViewSet para gestionar presupuesto de gastos

#* ViewSet para gestionar presupuesto de gastos
@extend_schema_view(
    list=extend_schema(
        summary="Listar todos los presupuestos de gastos",
        description="Obtiene una lista de todos los presupuestos de gastos registrados en el sistema",
        tags=['Presupuesto de Gastos']),    
    retrieve=extend_schema(
        summary="Obtener un presupuesto de gastos específico",
        description="Obtiene los detalles de un presupuesto de gastos por su ID",
        tags=['Presupuesto de Gastos']),
    create=extend_schema(
        summary="Crear un nuevo presupuesto de gastos",
        description="Crea un nuevo presupuesto de gastos en el sistema",
        tags=['Presupuesto de Gastos'],
        examples=[OpenApiExample('Ejemplo de creación', value={'id_institution': '001-2024-ADM', 'id_budget_item_expenses': '001-2024-ADM', 'period': 'Trimestral', 'initial_appropriation': '100', 'final_appropriation': '100', 'created_at': '2024-01-01', 'updated_at': '2024-01-01'}, request_only=True)]),
    update=extend_schema(
        summary="Actualizar un presupuesto de gastos",
        description="Actualiza completamente un presupuesto de gastos existente",
        tags=['Presupuesto de Gastos']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente un presupuesto de gastos",
        description="Actualiza uno o más campos de un presupuesto de gastos existente",
        tags=['Presupuesto de Gastos']
    ),
    destroy=extend_schema(
        summary="Eliminar un presupuesto de gastos",
        description="Elimina un presupuesto de gastos del sistema",
        tags=['Presupuesto de Gastos']
    )
)
class ExpensesBudgetViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar presupuesto de gastos.    
    
    Proporciona operaciones CRUD completas:
    - list: Listar todos los presupuestos de gastos
    - retrieve: Obtener un presupuesto de gastos específico
    - create: Crear un nuevo presupuesto de gastos
    - update: Actualizar un presupuesto de gastos completo
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar un presupuesto de gastos
    """
    queryset = ExpensesBudget.objects.all()
    serializer_class = ExpensesBudgetSerializer
    
    @extend_schema(
        summary="Buscar presupuestos de gastos por código",
        description="Busca presupuestos de gastos que contengan el código especificado",
        parameters=[
            OpenApiParameter(
                name='code',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Código de presupuesto a buscar',
                required=True
            )
        ],
        tags=['Presupuesto de Gastos']
    )
    @action(detail=False, methods=['get'])
    def search_by_code(self, request):
        """Busca presupuestos de gastos por código"""
        code = request.query_params.get('code', '')
        presupuestos = self.queryset.filter(id_budget_item_expenses__icontains=code)
        serializer = self.get_serializer(presupuestos, many=True)        
        return Response(serializer.data)

#* ViewSet para gestionar modificaciones del periodo - gastos
@extend_schema_view(
    list=extend_schema(
        summary="Listar todas las modificaciones del periodo - gastos",
        description="Obtiene una lista de todas las modificaciones del periodo - gastos registradas en el sistema",
        tags=['Modificaciones del Periodo - Gastos']),
    
    retrieve=extend_schema(
        summary="Obtener una modificación del periodo - gastos específica",
        description="Obtiene los detalles de una modificación del periodo - gastos por su ID",
        tags=['Modificaciones del Periodo - Gastos']),
    
    create=extend_schema(
        summary="Crear una nueva modificación del periodo - gastos",
        description="Crea una nueva modificación del periodo - gastos en el sistema",
        tags=['Modificaciones del Periodo - Gastos'],
        examples=[OpenApiExample('Ejemplo de creación', value={'id_budget_item_expenses': '001-2024-ADM', 'addition': '100', 'reduction': '100', 'credits': '100', 'countercredits': '100', 'created_at': '2024-01-01', 'updated_at': '2024-01-01'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar una modificación del periodo - gastos",
        description="Actualiza completamente una modificación del periodo - gastos existente",
        tags=['Modificaciones del Periodo - Gastos']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una modificación del periodo - gastos",
        description="Actualiza uno o más campos de una modificación del periodo - gastos existente",
        tags=['Modificaciones del Periodo - Gastos']
    ),
    destroy=extend_schema(
        summary="Eliminar una modificación del periodo - gastos",
        description="Elimina una modificación del periodo - gastos del sistema",
        tags=['Modificaciones del Periodo - Gastos']
    )
)
class ChangesExpensesPeriodViewSet(viewsets.ModelViewSet):
    """
    ViewSet para gestionar modificaciones del periodo - gastos.
    
    Proporciona operaciones CRUD completas:
    - list: Listar todas las modificaciones del periodo - gastos
    - retrieve: Obtener una modificación del periodo - gastos específica
    - create: Crear una nueva modificación del periodo - gastos
    - update: Actualizar una modificación del periodo - gastos completa
    - partial_update: Actualizar campos específicos
    - destroy: Eliminar una modificación del periodo - gastos
    """
    queryset = ChangesExpensesPeriod.objects.all()
    serializer_class = ChangesExpensesPeriodSerializer
    
    @extend_schema(
        summary="Buscar modificaciones del periodo - gastos por código",
        description="Busca modificaciones del periodo - gastos que contengan el código especificado",
        parameters=[
            OpenApiParameter(
                name='code',
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description='Código de presupuesto a buscar',
                required=True
            )
        ],
        tags=['Modificaciones del Periodo - Gastos']
    )
    @action(detail=False, methods=['get'])
    def search_by_code(self, request):
        """Busca modificaciones del periodo - gastos por código"""
        code = request.query_params.get('code', '')
        modificaciones = self.queryset.filter(id_budget_item_expenses__icontains=code)
        serializer = self.get_serializer(modificaciones, many=True)        
        return Response(serializer.data)
    
#* ViewSet para gestionar modificaciones acumuladas - gastos
@extend_schema_view(
    list=extend_schema(
        summary="Listar todas las modificaciones acumuladas - gastos",
        description="Obtiene una lista de todas las modificaciones acumuladas - gastos registradas en el sistema",
        tags=['Modificaciones Acumuladas - Gastos']), 
    retrieve=extend_schema(
        summary="Obtener una modificación acumulada - gastos específica", 
        description="Obtiene los detalles de una modificación acumulada - gastos por su ID", 
        tags=['Modificaciones Acumuladas - Gastos']),
    
    create=extend_schema(
        summary="Crear una nueva modificación acumulada - gastos", 
        description="Crea una nueva modificación acumulada - gastos en el sistema", 
        tags=['Modificaciones Acumuladas - Gastos'],
        examples=[OpenApiExample('Ejemplo de creación', value={'id_budget_item_expenses': '001-2024-ADM', 'accumulated_additions': '100', 'accumulated_reductions': '100', 'accumulated_credits': '100', 'accumulated_custordis': '100', 'created_at': '2024-01-01', 'updated_at': '2024-01-01'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar una modificación acumulada - gastos", 
        description="Actualiza completamente una modificación acumulada - gastos existente", 
        tags=['Modificaciones Acumuladas - Gastos']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una modificación acumulada - gastos", 
        description="Actualiza uno o más campos de una modificación acumulada - gastos existente", 
        tags=['Modificaciones Acumuladas - Gastos']
    ),
    destroy=extend_schema(
        summary="Eliminar una modificación acumulada - gastos", 
        description="Elimina una modificación acumulada - gastos del sistema",         
        tags=['Modificaciones Acumuladas - Gastos']
    )
)
class CumulativeChangesExpensesViewSet(viewsets.ModelViewSet):
    """            
    ViewSet para gestionar modificaciones acumuladas - gastos.            
            
    Proporciona operaciones CRUD completas:            
    - list: Listar todas las modificaciones acumuladas - gastos            
    - retrieve: Obtener una modificación acumulada - gastos específica            
    - create: Crear una nueva modificación acumulada - gastos            
    - update: Actualizar una modificación acumulada - gastos completa            
    - partial_update: Actualizar campos específicos            
    - destroy: Eliminar una modificación acumulada - gastos            
    """
    queryset = CumulativeChangesExpenses.objects.all()            
    serializer_class = CumulativeChangesExpensesSerializer                      
    
    @extend_schema(            
        summary="Buscar modificaciones acumuladas - gastos por código",   
        description="Busca modificaciones acumuladas - gastos que contengan el código especificado",            
        parameters=[            
            OpenApiParameter(                
                name='code',                
                type=OpenApiTypes.STR,                
                location=OpenApiParameter.QUERY,                
                description='Código de presupuesto a buscar',                
                required=True                
            )            
        ],            
        tags=['Modificaciones Acumuladas - Gastos']            
    )            
    @action(detail=False, methods=['get'])            
    def search_by_code(self, request):                
        """Busca modificaciones acumuladas - gastos por código"""                
        code = request.query_params.get('code', '')                
        modificaciones = self.queryset.filter(id_budget_item_expenses__icontains=code)                
        serializer = self.get_serializer(modificaciones, many=True)        
        return Response(serializer.data)    
    
#* ViewSet para gestionar la ejecución de gastos
@extend_schema_view(
    list=extend_schema(
        summary="Listar todas las ejecuciones de gastos",
        description="Obtiene una lista de todas las ejecuciones de gastos registradas en el sistema",
        tags=['Ejecución de Gastos']),
    
    retrieve=extend_schema(
        summary="Obtener una ejecución de gastos específica",
        description="Obtiene los detalles de una ejecución de gastos por su ID",
        tags=['Ejecución de Gastos']),
    
    create=extend_schema(
        summary="Crear una nueva ejecución de gastos",
        description="Crea una nueva ejecución de gastos en el sistema",
        tags=['Ejecución de Gastos'],
        examples=[OpenApiExample('Ejemplo de creación', value={'id_budget_item_expenses': '001-2024-ADM', 'id_institution': '001-2024-ADM', 'id_budget_report': '001-2024-ADM', 'program_code': '001-2024-ADM', 'created_at': '2024-01-01', 'updated_at': '2024-01-01'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar una ejecución de gastos",
        description="Actualiza completamente una ejecución de gastos existente",
        tags=['Ejecución de Gastos']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una ejecución de gastos",
        description="Actualiza uno o más campos de una ejecución de gastos existente",
        tags=['Ejecución de Gastos']
    ),
    destroy=extend_schema(
        summary="Eliminar una ejecución de gastos",
        description="Elimina una ejecución de gastos del sistema",
        tags=['Ejecución de Gastos']
    )
)
class ExpensesExecutionViewSet(viewsets.ModelViewSet):
    """            
    ViewSet para gestionar la ejecución de gastos.            
            
    Proporciona operaciones CRUD completas:            
    - list: Listar todas las ejecuciones de gastos            
    - retrieve: Obtener una ejecución de gastos específica            
    - create: Crear una nueva ejecución de gastos            
    - update: Actualizar una ejecución de gastos completa            
    - partial_update: Actualizar campos específicos            
    - destroy: Eliminar una ejecución de gastos            
    """
    queryset = ExpensesExecution.objects.all()            
    serializer_class = ExpensesExecutionSerializer                      
    
    @extend_schema(            
        summary="Buscar ejecuciones de gastos por código",   
        description="Busca ejecuciones de gastos que contengan el código especificado",            
        parameters=[            
            OpenApiParameter(                
                name='code',                
                type=OpenApiTypes.STR,                
                location=OpenApiParameter.QUERY,                
                description='Código de presupuesto a buscar',                
                required=True                
            )            
        ],            
        tags=['Ejecución de Gastos']            
    )            
    @action(detail=False, methods=['get'])            
    def search_by_code(self, request):                
        """Busca ejecuciones de gastos por código"""                
        code = request.query_params.get('code', '')                
        ejecuciones = self.queryset.filter(id_budget_item_expenses__icontains=code)                
        serializer = self.get_serializer(ejecuciones, many=True)        
        return Response(serializer.data)    

#* ViewSet para gestionar la obligación de pagoes
@extend_schema_view(    
    list=extend_schema(
        summary="Listar todas las obligaciones de pago",
        description="Obtiene una lista de todas las obligaciones de pago registradas en el sistema",
        tags=['Obligaciones de Pago']),
    
    retrieve=extend_schema(
        summary="Obtener una obligación de pago específica",
        description="Obtiene los detalles de una obligación de pago por su ID",
        tags=['Obligaciones de Pago']),
    
    create=extend_schema(
        summary="Crear una nueva obligación de pago",
        description="Crea una nueva obligación de pago en el sistema",
        tags=['Obligaciones de Pago'],
        examples=[OpenApiExample('Ejemplo de creación', value={'id_budget_item_expenses': '001-2024-ADM', 'id_institution': '001-2024-ADM', 'id_budget_report': '001-2024-ADM', 'open_positions': '100', 'obligations_period': '100', 'accumulated_obligations': '100', 'period_payments': '100', 'accumulated_payments': '100', 'balance_payable': '100', 'reservations': '100', 'created_at': '2024-01-01', 'updated_at': '2024-01-01'}, request_only=True)]),
    
    update=extend_schema(
        summary="Actualizar una obligación de pago",
        description="Actualiza completamente una obligación de pago existente",
        tags=['Obligaciones de Pago']
    ),
    partial_update=extend_schema(
        summary="Actualizar parcialmente una obligación de pago",
        description="Actualiza uno o más campos de una obligación de pago existente",
        tags=['Obligaciones de Pago']
    ),
    destroy=extend_schema(
        summary="Eliminar una obligación de pago",
        description="Elimina una obligación de pago del sistema",
        tags=['Obligaciones de Pago']
    )
)
class PaymentObligationsViewSet(viewsets.ModelViewSet):
    """            
    ViewSet para gestionar la obligación de pago.            
            
    Proporciona operaciones CRUD completas:            
    - list: Listar todas las obligaciones de pago            
    - retrieve: Obtener una obligación de pago específica            
    - create: Crear una nueva obligación de pago            
    - update: Actualizar una obligación de pago completa            
    - partial_update: Actualizar campos específicos            
    - destroy: Eliminar una obligación de pago            
    """
    queryset = PaymentObligations.objects.all()            
    serializer_class = PaymentObligationsSerializer                      
    
    @extend_schema(            
        summary="Buscar obligaciones de pago por código",   
        description="Busca obligaciones de pago que contengan el código especificado",            
        parameters=[            
            OpenApiParameter(                
                name='code',                
                type=OpenApiTypes.STR,                
                location=OpenApiParameter.QUERY,                
                description='Código de presupuesto a buscar',                
                required=True                
            )            
        ],            
        tags=['Obligaciones de Pago']            
    )            
    @action(detail=False, methods=['get'])            
    def search_by_code(self, request):                
        """Busca obligaciones de pago por código"""                
        code = request.query_params.get('code', '')                
        obligaciones = self.queryset.filter(id_budget_item_expenses__icontains=code)                
        serializer = self.get_serializer(obligaciones, many=True)        
        return Response(serializer.data)    

#* ViewSet para gestionar la relación de pago
@extend_schema_view(    
    list=extend_schema(        
        summary="Listar todas las relaciones de pago",
        description="Obtiene una lista de todas las relaciones de pago registradas en el sistema",
        tags=['Relaciones de Pago']),    
    
    retrieve=extend_schema(
        summary="Obtener una relación de pago específica",
        description="Obtiene los detalles de una relación de pago por su ID",
        tags=['Relaciones de Pago']),    
    
    create=extend_schema(
        summary="Crear una nueva relación de pago",
        description="Crea una nueva relación de pago en el sistema",
        tags=['Relaciones de Pago'],        
        examples=[OpenApiExample('Ejemplo de creación', value={'id_payment_obligation': '001-2024-ADM', 'id_institution': '001-2024-ADM', 'id_budget_report': '001-2024-ADM', 'program_code': '001-2024-ADM', 'created_at': '2024-01-01', 'updated_at': '2024-01-01'}, request_only=True)]),  
      
    update=extend_schema(   
        summary="Actualizar una relación de pago",
        description="Actualiza completamente una relación de pago existente",
        tags=['Relaciones de Pago']),
        
    partial_update=extend_schema(
        summary="Actualizar parcialmente una relación de pago",
        description="Actualiza uno o más campos de una relación de pago existente",
        tags=['Relaciones de Pago']
    ),    
    destroy=extend_schema(
        summary="Eliminar una relación de pago",
        description="Elimina una relación de pago del sistema",
        tags=['Relaciones de Pago']
    )
)
class PaymentRelationshipViewSet(viewsets.ModelViewSet):
    """            
    ViewSet para gestionar la relación de pago.            
            
    Proporciona operaciones CRUD completas:            
    - list: Listar todas las relaciones de pago            
    - retrieve: Obtener una relación de pago específica            
    - create: Crear una nueva relación de pago            
    - update: Actualizar una relación de pago completa            
    - partial_update: Actualizar campos específicos            
    - destroy: Eliminar una relación de pago            
    """
    queryset = PaymentRelationship.objects.all()            
    serializer_class = PaymentRelationshipSerializer    
    
    @extend_schema(            
        summary="Buscar relaciones de pago por código",   
        description="Busca relaciones de pago que contengan el código especificado",            
        parameters=[            
            OpenApiParameter(                
                name='code',                
                type=OpenApiTypes.STR,                
                location=OpenApiParameter.QUERY,                
                description='Código de presupuesto a buscar',                
                required=True                
            )            
        ],            
        tags=['Relaciones de Pago']            
    )            
    @action(detail=False, methods=['get'])            
    def search_by_code(self, request):                
        """Busca relaciones de pago por código"""                
        code = request.query_params.get('code', '')                
        relaciones = self.queryset.filter(id_budget_item_expenses__icontains=code)                
        serializer = self.get_serializer(relaciones, many=True)        
        return Response(serializer.data)    
    
class ScalarDocsView(TemplateView):
    template_name = 'scalar_docs.html'    

    