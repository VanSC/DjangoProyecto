# Generated by Django 4.2.2 on 2023-06-28 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreusuario', models.CharField(max_length=40)),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=40)),
                ('contraseña', models.CharField(max_length=12)),
            ],
        ),
    ]
