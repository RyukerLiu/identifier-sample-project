# Generated by Django 2.2.6 on 2021-03-19 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filed_x', models.CharField(max_length=128, null=True)),
                ('filed_y', models.CharField(max_length=128, null=True)),
                ('filed_z', models.CharField(max_length=128, null=True)),
                ('filed_other', models.CharField(max_length=128, null=True)),
            ],
            options={
                'unique_together': {('filed_x', 'filed_y')},
            },
        ),
    ]
