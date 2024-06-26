# Generated by Django 3.1.4 on 2024-06-10 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FinanceTerms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('downpayment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_date', models.DateField()),
                ('amount_financed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='InsurancePolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('premium', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_fee', models.DecimalField(decimal_places=2, max_digits=10)),
                ('agreed', models.BooleanField(default=False)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.customer')),
            ],
        ),
        migrations.CreateModel(
            name='FinanceTermsInsurancePolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finance_terms_aggregate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.financeterms')),
                ('insurance_policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.insurancepolicy')),
            ],
            options={
                'unique_together': {('finance_terms_aggregate', 'insurance_policy')},
            },
        ),
    ]
