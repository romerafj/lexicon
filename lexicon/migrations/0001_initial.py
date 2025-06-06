# Generated by Django 5.2.1 on 2025-05-27 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccAuxCasus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caso', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Auxiliar de Caso',
                'verbose_name_plural': 'Auxiliares de Casos',
            },
        ),
        migrations.CreateModel(
            name='AccAuxGeneros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Auxiliar de Género',
                'verbose_name_plural': 'Auxiliares de Géneros',
            },
        ),
        migrations.CreateModel(
            name='AccAuxGradacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gradacion', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Auxiliar de Gradación',
                'verbose_name_plural': 'Auxiliares de Gradaciones',
            },
        ),
        migrations.CreateModel(
            name='AccAuxNum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Auxiliar de Número',
                'verbose_name_plural': 'Auxiliares de Números',
            },
        ),
        migrations.CreateModel(
            name='AccAuxPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('persona', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Auxiliar de Persona',
                'verbose_name_plural': 'Auxiliares de Personas',
            },
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=75)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
            },
        ),
        migrations.CreateModel(
            name='Bibliografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150)),
                ('colacion', models.TextField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Bibliografía',
                'verbose_name_plural': 'Bibliografías',
            },
        ),
        migrations.CreateModel(
            name='CamposSemanticos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo_semantico', models.CharField(max_length=75)),
            ],
            options={
                'verbose_name': 'Campo Semántico',
                'verbose_name_plural': 'Campos Semánticos',
            },
        ),
        migrations.CreateModel(
            name='Lema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lema', models.CharField(max_length=150)),
                ('observaciones', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Lema',
                'verbose_name_plural': 'Lemas',
            },
        ),
        migrations.CreateModel(
            name='SubtiposLemas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtipo_lema', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name': 'Subtipo de Lema',
                'verbose_name_plural': 'Subtipos de Lemas',
            },
        ),
        migrations.CreateModel(
            name='Textos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField()),
            ],
            options={
                'verbose_name': 'Texto',
                'verbose_name_plural': 'Textos',
            },
        ),
        migrations.CreateModel(
            name='TiposLemas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_lema', models.CharField(max_length=35)),
            ],
            options={
                'verbose_name': 'Tipo de Lema',
                'verbose_name_plural': 'Tipos de Lemas',
            },
        ),
        migrations.CreateModel(
            name='Forma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma', models.CharField(max_length=50)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('lema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lexicon.lema')),
            ],
            options={
                'verbose_name': 'Forma',
                'verbose_name_plural': 'Formas',
            },
        ),
        migrations.CreateModel(
            name='Significados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('significado', models.CharField(max_length=75)),
                ('campo_semantico', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lexicon.campossemanticos')),
            ],
            options={
                'verbose_name': 'Significado',
                'verbose_name_plural': 'Significados',
            },
        ),
        migrations.AddField(
            model_name='lema',
            name='subtipo_lema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lexicon.subtiposlemas'),
        ),
        migrations.AddField(
            model_name='subtiposlemas',
            name='tipo_lema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lexicon.tiposlemas'),
        ),
        migrations.CreateModel(
            name='BibliografiaAutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lexicon.autor')),
                ('bibliografia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lexicon.bibliografia')),
            ],
            options={
                'verbose_name': 'Autor de Bibliografía',
                'verbose_name_plural': 'Autores de Bibliografía',
                'unique_together': {('bibliografia', 'autor')},
            },
        ),
        migrations.CreateModel(
            name='LemasBibliografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.TextField(blank=True, null=True)),
                ('bibliografia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lexicon.bibliografia')),
                ('lema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lexicon.lema')),
            ],
            options={
                'verbose_name': 'Lema en Bibliografía',
                'verbose_name_plural': 'Lemas en Bibliografía',
                'unique_together': {('lema', 'bibliografia')},
            },
        ),
        migrations.CreateModel(
            name='TextoBibliografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posicion', models.TextField(blank=True, null=True)),
                ('bibliografia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lexicon.bibliografia')),
                ('texto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lexicon.textos')),
            ],
            options={
                'verbose_name': 'Texto en Bibliografía',
                'verbose_name_plural': 'Textos en Bibliografía',
                'unique_together': {('texto', 'bibliografia')},
            },
        ),
    ]
