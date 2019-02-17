# Generated by Django 2.1.7 on 2019-02-17 09:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('corpus_url', models.URLField(validators=[django.core.validators.URLValidator])),
                ('corpus_title', models.TextField()),
                ('corpus_text', models.TextField(blank=True, null=True)),
                ('model_status', models.CharField(choices=[('FAKE', 'Fake'), ('REAL', 'Real'), ('NA', 'Not sure')], max_length=10)),
                ('time', models.TimeField(auto_now=True)),
            ],
        ),
    ]
