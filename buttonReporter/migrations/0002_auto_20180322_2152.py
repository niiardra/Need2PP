# Generated by Django 2.0.3 on 2018-03-23 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buttonReporter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='floor',
            name='availableWashrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='floor',
            name='totalWashrooms',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='floor',
            name='floorNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='washroom',
            name='availableStalls',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='washroom',
            name='gender',
            field=models.CharField(default='f', max_length=1),
        ),
        migrations.AlterField(
            model_name='washroom',
            name='totalStalls',
            field=models.IntegerField(default=0),
        ),
    ]
