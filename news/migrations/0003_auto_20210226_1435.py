# Generated by Django 3.1.6 on 2021-02-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210226_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactenty',
            name='message',
            field=models.TextField(blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactenty',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]
