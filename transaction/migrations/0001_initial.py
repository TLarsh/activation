# Generated by Django 4.1.3 on 2023-08-02 12:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('account_number', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
    ]
