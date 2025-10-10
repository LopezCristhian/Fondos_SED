from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Ejecuta todos los scripts de población'

    def handle(self, *args, **options):
        commands = [
            'poblar_bank',
            'poblar_institutions',
            'poblar_accountant_puc',
            'poblar_source_resources', 
            'poblar_expense_accounts',
            'poblar_budget_item_revenue',
            'poblar_budget_item_expenses'
        ]
        
        for command in commands:
            self.stdout.write(f'Ejecutando: {command}')
            try:
                call_command(command)
                self.stdout.write(
                    self.style.SUCCESS(f'{command} completado')
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'Error en {command}: {str(e)}')
                )
                