# Con ruta por defecto
# python manage.py poblar_AccountantPuc

# O especificando otro archivo
# python manage.py poblar_AccountantPuc --file="data/otro_archivo.csv"

import pandas as pd
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from FondosApp.models import AccountantPuc  

class Command(BaseCommand):
    help = 'Importación del PUC desde archivo CSV local'
    
    def add_arguments(self, parser):
        parser.add_argument(
            '--file',
            type=str,
            default='data/accountant_puc_data.csv',  # Ruta
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
            # Leer CSV en lugar de Excel
            df = pd.read_csv(file_path, encoding='utf-8', delimiter=';')
            self.stdout.write(f"Filas encontradas: {len(df)}")
            
            created_count = 0
            existing_count = 0
            
            for index, row in df.iterrows():
                # Convertir NaN a None para campos opcionales
                defaults = {
                    'code': str(row['code']),
                    'name': row['name'],
                    'nature': row['nature'],
                    'type': row.get('type')
                    
                }
                
                # Father opcional
                father_code = row.get('father')
                if pd.notna(father_code) and father_code != '':
                    try:
                        defaults['father'] = AccountantPuc.objects.get(code=str(father_code))
                    except AccountantPuc.DoesNotExist:
                        self.stdout.write(f"Padre no encontrado: {father_code}")
                
                # Level opcional
                level = row.get('level')
                if pd.notna(level):
                    defaults['level'] = int(level)
                
                # Crear registro
                obj, created = AccountantPuc.objects.get_or_create(
                    code=str(row['code']),
                    defaults=defaults
                )
                
                if created:
                    created_count += 1
                    self.stdout.write(f"Creado: {obj.code} - {obj.name}")
                else:
                    existing_count += 1
            
            # Resumen final
            self.stdout.write(self.style.SUCCESS(
                f"\nIMPORTACIÓN COMPLETADA:\n"
                f"• Nuevos registros: {created_count}\n"
                f"• Registros existentes: {existing_count}\n"
                f"• Total procesado: {len(df)}"
            ))
            
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {str(e)}"))