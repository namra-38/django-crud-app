# Generated by Django 3.1.4 on 2020-12-23 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employes', '0006_auto_20201223_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='employe_categories',
            field=models.CharField(blank=True, choices=[('Perminent', 'Perminent'), ('Contract Based', 'Contract Based'), ('Grass Sales', 'Grass Sales'), ('Weekly Based', 'Weekly Based')], max_length=14, null=True),
        ),
    ]
