import pandas as pd
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from FondosApp.models import BudgetItemExpenses

class Command(BaseCommand):
    help = 'Importación de rubros presupuestales de gastos desde archivo CSV local'  
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='data/budget_item_expenses_data.csv',
            help='Ruta del archivo CSV relativa al proyecto'
        )

    def handle(self, *args, **options):
        file_path = os.path.join(settings.BASE_DIR, options['file'])
        
        self.stdout.write(f"Leyendo archivo: {file_path}")
        
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"Archivo no encontrado: {file_path}"))
            return
        
        try:
            df = pd.read_csv(file_path, encoding='utf-8', delimiter=';')
            self.stdout.write(f"Filas encontradas: {len(df)}")
            
            created_count = 0
            existing_count = 0
            error_count = 0
            
            for index, row in df.iterrows():
                try:
                    # Campos obligatorios - siempre deben tener valor
                    code = str(row['code']).strip()
                    level = str(row['level']).strip()
                    type_val = str(row['type']).strip()
                    account_name = str(row['account_name']).strip()
                    
                    # Campo OPCIONAL: father (único que puede ser nulo)
                    father_val = None
                    if pd.notna(row.get('father')) and str(row['father']).strip() != '':
                        father_val = str(row['father']).strip()
                    
                    defaults = {
                        'code': code,
                        'level': level,
                        'type': type_val,
                        'account_name': account_name,
                        'father': father_val  # Único que puede ser None
                    }
                    
                    # Crear registro
                    obj, created = BudgetItemExpenses.objects.get_or_create(
                        code=code,
                        defaults=defaults
                    )
                    
                    if created:
                        created_count += 1
                        father_info = f" (Padre: {father_val})" if father_val else " (Sin padre)"
                        self.stdout.write(f"Creado: {obj.code} - {obj.account_name}{father_info}")
                    else:
                        existing_count += 1
                        self.stdout.write(f"Ya existía: {obj.code}")
                        
                except Exception as e:
                    error_count += 1
                    self.stdout.write(self.style.ERROR(
                        f"Error en fila {index + 2}: {str(e)}"
                    ))
                    continue
            
            # Resumen final
            self.stdout.write(self.style.SUCCESS(
                f"\nIMPORTACIÓN COMPLETADA:\n"
                f"• Nuevos registros: {created_count}\n"
                f"• Registros existentes: {existing_count}\n"
                f"• Errores: {error_count}\n"
                f"• Total procesado: {len(df)}"
            ))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {str(e)}"))