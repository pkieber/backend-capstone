# Generated by Django 4.2.10 on 2024-02-29 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0002_rename_menu_menuitem"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]