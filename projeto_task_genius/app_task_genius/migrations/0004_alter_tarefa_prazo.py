# Generated by Django 5.0.2 on 2024-04-26 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_task_genius', '0003_alter_tarefa_prazo_alter_tarefa_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='prazo',
            field=models.DateField(max_length=100),
        ),
    ]
