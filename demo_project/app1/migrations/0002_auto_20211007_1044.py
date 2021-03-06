# Generated by Django 3.2.8 on 2021-10-07 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics/')),
                ('disc', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='people',
            name='img',
            field=models.ImageField(upload_to='pics/'),
        ),
    ]
