import pandas as pd
import os
import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from FondosApp.models import ExpenseAccounts

class Command(BaseCommand):
    help = 'Pobla la tabla ExpenseAccounts desde archivo CSV'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='data/expense_accounts_data.csv',  # Ruta
            help='Ruta del archivo CSV relativa al proyecto'
        )

    def handle(self, *args, **options):
        # Construir ruta absoluta
        file_path = os.path.join(settings.BASE_DIR, options['file'])
        
        self.stdout.write(f"Leyendo archivo: {file_path}")
        
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"Archivo no encontrado: {file_path}"))
            return
        
        try:
            # OPCIÓN 1: Con pandas (similar a Excel)
            df = pd.read_csv(file_path, encoding='utf-8', delimiter=';')
            
            # OPCIÓN 2: Con csv nativo (más eficiente)
            # with open(file_path, 'r', encoding='utf-8', delimiter=';') as file:
            #     reader = csv.DictReader(file)
            #     df = list(reader)
            
            self.stdout.write(f"Filas encontradas: {len(df)}")
            
            created_count = 0
            existing_count = 0
            
            for index, row in df.iterrows():  # Para pandas
            # for row in df:  # Para csv.DictReader
                
                # Crear registro - solo los 2 campos obligatorios
                obj, created = ExpenseAccounts.objects.get_or_create(
                    budget_code_expenses=row['budget_code_expenses'],
                    defaults={
                        'accountant_name': row['accountant_name']
                    }
                )
                
                if created:
                    created_count += 1
                    self.stdout.write(f"Creado: {obj.budget_code_expenses} - {obj.accountant_name}")
                else:
                    existing_count += 1
                    self.stdout.write(f"Ya existe: {obj.budget_code_expenses}")
            
            # Resumen final
            self.stdout.write(self.style.SUCCESS(
                f"\nIMPORTACIÓN COMPLETADA:\n"
                f"• Nuevos registros: {created_count}\n"
                f"• Registros existentes: {existing_count}\n"
                f"• Total procesado: {len(df)}"
            ))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {str(e)}"))