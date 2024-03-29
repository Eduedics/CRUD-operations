# Generated by Django 4.1.3 on 2024-02-07 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Description', models.TimeField()),
                ('Status', models.BooleanField(choices=[('PENDING', 'pending'), ('COMPLETE', 'complete'), ('CANCELED', 'canceled')], default='PENDING', max_length=10)),
                ('Created_at', models.DateTimeField(auto_now_add=True)),
                ('Updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
