# Generated by Django 4.0.4 on 2022-06-27 22:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import filebrowser.fields
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id_instrument', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LieuObservation',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id_lieu_observation', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('IAU_code', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TypeObservation',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id_type_observation', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('lg_onde', models.FloatField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id_observation', models.AutoField(primary_key=True, serialize=False)),
                ('nom_obj', models.TextField(default='Undefined')),
                ('temps_exp', models.IntegerField(default=0)),
                ('nb_exp', models.IntegerField(default=1)),
                ('date', models.DateField(blank=True, null=True)),
                ('remarques', models.TextField(blank=True, null=True)),
                ('typeobservation', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='website.typeobservation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImageObservation',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('image', filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Image')),
                ('description', models.TextField(blank=True, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('observation', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='img_o', to='website.observation')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id_collection', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('observations', models.ManyToManyField(related_name='collections', to='website.observation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
