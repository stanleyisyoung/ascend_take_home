# Generated by Django 3.1.4 on 2024-06-10 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insurance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancepolicy',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='insurance.customer'),
        ),
    ]