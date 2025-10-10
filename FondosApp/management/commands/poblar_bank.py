from django.core.management.base import BaseCommand
from FondosApp.models import Bank

class Command(BaseCommand):
    help = 'Importación de datos de la tabla Bank'   

    def handle(self, *args, **kwargs):
        # Lista de datos acrear
        datos = [
            {'bank_name': 'Banco Agrario'},
            {'bank_name': 'Banco de Bogotá'},
            {'bank_name': 'BANCOLOMBIA'},
            {'bank_name': 'Banco Davivienda'},
            {'bank_name': 'Banco de Occidente'},
            {'bank_name': 'Banco Popular'},
            {'bank_name': 'Banco AV Villas'},
        ]
            
        for item in datos:  
            # Se usan get_or_create para no duplicar registros si ejecuta varias veces
                obj, created = Bank.objects.get_or_create(
                    bank_name=item["bank_name"]
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Creado: {obj}'))
                else:
                    self.stdout.write(f'Ya existe!: {obj}')  
        
        # Resumen final
        self.stdout.write(self.style.SUCCESS(
            f"\nIMPORTACIÓN COMPLETADA:\n"
            f"• Nuevos registros: {len(datos)}\n"
            f"• Registros existentes: {len(datos)}\n"
            f"• Total procesado: {len(datos)}"
        ))
                    