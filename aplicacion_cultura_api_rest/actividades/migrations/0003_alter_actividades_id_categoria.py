# Generated by Django 4.1.3 on 2022-11-20 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0002_actividades_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividades',
            name='id_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.categorias', to_field='nombre'),
        ),
    ]
