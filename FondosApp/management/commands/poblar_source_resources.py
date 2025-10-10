# Poblar la tabla Institutions con Command 

from django.core.management.base import BaseCommand
from FondosApp.models import SourceResources

class Command(BaseCommand):
    help = 'Importación de datos de la tabla SourceResources'   

    def handle(self, *args, **kwargs):
            # Lista de datos acrear
            datos = [
                {'source_name': 'SGP'},
                {'source_name': 'Recursos Propios'},
                {'source_name': 'Transferencias departamentales'},
                {'source_name': 'Otros'},

            ]

            # Se crean los registros
            for item in datos:
                # Se usa get_or_create para no duplicar registros si ejecuta varias veces
                obj, created = SourceResources.objects.get_or_create(
                    source_name=item["source_name"]
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