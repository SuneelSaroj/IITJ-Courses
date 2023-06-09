# Generated by Django 4.2 on 2023-04-23 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("firstyear", "0011_secondsemestercourse_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="secondsemestercourse",
            name="activities4",
            field=models.CharField(blank=True, default="", max_length=1000),
        ),
        migrations.AddField(
            model_name="secondsemestercourse",
            name="learning_outcome4",
            field=models.CharField(blank=True, default="", max_length=500),
        ),
        migrations.AddField(
            model_name="secondsemestercourse",
            name="learning_outcome5",
            field=models.CharField(blank=True, default="", max_length=500),
        ),
        migrations.AddField(
            model_name="secondsemestercourse",
            name="objective4",
            field=models.CharField(blank=True, default="", max_length=500),
        ),
        migrations.AddField(
            model_name="secondsemestercourse",
            name="objective5",
            field=models.CharField(blank=True, default="", max_length=500),
        ),
        migrations.AddField(
            model_name="secondsemestercourse",
            name="self_mearning_material4",
            field=models.CharField(blank=True, default="", max_length=500),
        ),
        migrations.AddField(
            model_name="secondsemestercourse",
            name="self_mearning_material5",
            field=models.CharField(blank=True, default="", max_length=500),
        ),
    ]
