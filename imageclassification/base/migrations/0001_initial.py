# Generated by Django 4.0.3 on 2022-03-03 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageClassification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageLink', models.CharField(max_length=200)),
                ('result', models.CharField(max_length=50)),
            ],
        ),
    ]