# Generated by Django 5.2 on 2025-04-18 11:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="due_date",
            field=models.DateField(db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.IntegerField(
                choices=[(1, "High"), (2, "Medium"), (3, "Low")], db_index=True
            ),
        ),
    ]
