# Generated by Django 4.0.4 on 2022-06-02 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shInvSol", "0004_alter_support_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="collection",
            name="observations",
            field=models.ManyToManyField(
                related_name="collections",
                through="shInvSol.CollectionObservation",
                to="shInvSol.observation",
            ),
        ),
        migrations.AddField(
            model_name="collectionobservation",
            name="observation",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="shInvSol.observation",
            ),
        ),
        migrations.AlterField(
            model_name="collectionobservation",
            name="collection",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="shInvSol.collection",
            ),
        ),
        migrations.AlterField(
            model_name="observation",
            name="collectionobservation",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="+",
                to="shInvSol.collectionobservation",
            ),
        ),
    ]
