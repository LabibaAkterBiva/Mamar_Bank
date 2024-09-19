# Generated by Django 5.0.7 on 2024-09-19 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0003_alter_transaction_transaction_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(2, 'Withdrawal'), (1, 'Deposit'), (5, 'Money Transfer'), (3, 'Loan'), (4, 'Loan Paid')], null=True),
        ),
    ]
