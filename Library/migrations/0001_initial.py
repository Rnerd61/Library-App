# Generated by Django 4.2.5 on 2023-09-06 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('createdAt', models.DateTimeField(auto_created=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('published', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'BookModel',
            },
        ),
    ]