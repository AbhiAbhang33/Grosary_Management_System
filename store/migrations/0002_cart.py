# Generated by Django 5.0.6 on 2024-06-03 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('products', models.ManyToManyField(to='store.product')),
            ],
        ),
    ]
