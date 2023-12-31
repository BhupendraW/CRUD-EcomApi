# Generated by Django 4.1.7 on 2023-10-26 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ECommerce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.CharField(max_length=50)),
                ('item_name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiApp.category')),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ApiApp.company')),
            ],
        ),
    ]
