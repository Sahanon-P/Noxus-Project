# Generated by Django 3.1.2 on 2020-11-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noxusProject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='summonnerspell',
            name='img',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='ImageSummonnerSpell',
        ),
    ]