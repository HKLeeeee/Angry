# Generated by Django 3.2.5 on 2022-02-23 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_title', models.CharField(max_length=50)),
                ('b_content', models.CharField(max_length=200)),
                ('b_like', models.IntegerField(default=0)),
                ('b_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_content', models.CharField(max_length=50)),
                ('c_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
