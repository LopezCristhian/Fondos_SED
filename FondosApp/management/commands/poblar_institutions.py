# Poblar la tabla SourceResources con Command 

from django.core.management.base import BaseCommand
from FondosApp.models import Institution

class Command(BaseCommand):
    help = 'Importación de datos de la tabla SourceResources'   

    def handle(self, *args, **kwargs):
            # Lista de datos acrear
            datos = [
                {'name': 'Nuestra señora de las nieves'},
                {'name': 'Nuestra señora del pilar'},
                {'name': 'Maria auxiliadora'},
                {'name': 'Nuestra señora de la asunción'},
                {'name': 'Nuestra señora del carmen'},
                {'name': 'Nuestra señora de la merced'},

            ]

            # Se crean los registros
            for item in datos:
                # Se usa get_or_create para no duplicar registros si ejecuta varias veces
                obj, created = Institution.objects.get_or_create(
                    name=item["name"]
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