# Generated by Django 5.0.3 on 2024-03-28 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=20)),
                ('student_name', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
                ('marks', models.IntegerField(max_length=20)),
            ],
        ),
    ]