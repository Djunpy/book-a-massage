# Generated by Django 4.0.5 on 2022-07-02 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_comment_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='the_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='the_date',
            field=models.DateField(),
        ),
    ]
