# Generated by Django 4.0.4 on 2022-06-22 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shInvSol', '0009_alter_evenement_observation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='observation',
            name='support',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='observations', to='shInvSol.support'),
        ),
    ]
