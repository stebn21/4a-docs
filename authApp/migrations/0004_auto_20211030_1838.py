# Generated by Django 3.2.7 on 2021-10-30 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0003_invoice_sale'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='idInvoice',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='idSale',
            new_name='id',
        ),
    ]
