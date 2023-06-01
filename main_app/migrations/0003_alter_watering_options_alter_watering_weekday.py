# Generated by Django 4.2.1 on 2023-06-01 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_watering'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watering',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='watering',
            name='weekday',
            field=models.CharField(choices=[('Sun', 'Sunday'), ('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday')], default='Sun', max_length=3),
        ),
    ]