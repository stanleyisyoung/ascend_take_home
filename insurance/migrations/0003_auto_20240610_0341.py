# Generated by Django 3.1.4 on 2024-06-10 03:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0002_auto_20240610_0241'),
    ]

    operations = [
        migrations.RenameField(
            model_name='financetermsinsurancepolicy',
            old_name='finance_terms_aggregate',
            new_name='finance_terms',
        ),
        migrations.AlterUniqueTogether(
            name='financetermsinsurancepolicy',
            unique_together={('finance_terms', 'insurance_policy')},
        ),
    ]
