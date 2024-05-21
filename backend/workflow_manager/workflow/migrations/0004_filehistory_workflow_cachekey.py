# Generated by Django 4.2.1 on 2024-05-14 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("workflow", "0003_workflowexecution_execution_log_id_and_more"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="filehistory",
            constraint=models.UniqueConstraint(
                fields=("workflow", "cache_key"), name="workflow_cacheKey"
            ),
        ),
    ]