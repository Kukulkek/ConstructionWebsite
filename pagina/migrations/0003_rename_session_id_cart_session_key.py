# Generated by Django 4.2.6 on 2023-11-06 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagina', '0002_cart_cartmaterial_cart_materials'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='session_id',
            new_name='session_key',
        ),
    ]
