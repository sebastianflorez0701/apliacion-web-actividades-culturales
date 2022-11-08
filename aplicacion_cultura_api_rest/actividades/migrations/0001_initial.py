# Generated by Django 4.1.3 on 2022-11-07 22:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenido', models.TextField()),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('login', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Valoraciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valoracion', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('id_actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.actividades')),
            ],
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(blank=True, null=True)),
                ('id_actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.actividades')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='ActividadesUsuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.actividades')),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.usuarios')),
            ],
        ),
        migrations.AddField(
            model_name='actividades',
            name='id_categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actividades.categorias'),
        ),
    ]
