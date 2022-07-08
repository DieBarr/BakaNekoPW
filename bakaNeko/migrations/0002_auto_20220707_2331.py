# Generated by Django 3.2.13 on 2022-07-07 23:31

from django.db import migrations

def poblarRoles(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Rol = apps.get_model('bakaNeko', 'Rol')
    Rol.objects.get_or_create(nombreRol = "admin")
    Rol.objects.get_or_create(nombreRol = "usuario")

def poblarTipos(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Tipo = apps.get_model('bakaNeko', 'Tipo')
    Tipo.objects.get_or_create(nombreTipo = "Anime")
    Tipo.objects.get_or_create(nombreTipo = "Videojuegos")

def poblarEstados(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Estado = apps.get_model('bakaNeko', 'Estado')
    Estado.objects.get_or_create(nombre = "activo")
    Estado.objects.get_or_create(nombre = "inactivo")


class Migration(migrations.Migration):

    dependencies = [
        ('bakaNeko', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(poblarRoles),

        migrations.RunPython(poblarTipos),

        migrations.RunPython(poblarEstados),
    ]
