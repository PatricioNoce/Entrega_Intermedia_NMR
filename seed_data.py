from ejemplo.models import Familiar

Familiar(nombre="Patricio", direccion="Manola Castre 1473", numero_pasaporte=33444888).save()
Familiar(nombre="Cintia", direccion="Manola Castre 1473", numero_pasaporte=30500228).save()
Familiar(nombre="Gonzalo", direccion="Dardo Roche 3480", numero_pasaporte=345345).save()
Familiar(nombre="Esteban", direccion="Dardo Roche 3480", numero_pasaporte=567567).save()
Familiar(nombre="Rosalia", direccion="Calle Falsa 123", numero_pasaporte=5987400).save()

print("Se cargo con éxito los usuarios de pruebas")