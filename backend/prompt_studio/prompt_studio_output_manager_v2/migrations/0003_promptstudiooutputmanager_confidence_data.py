# Generated by Django 4.2.1 on 2025-03-07 07:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "prompt_studio_output_manager_v2",
            "0002_promptstudiooutputmanager_highlight_data",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="promptstudiooutputmanager",
            name="confidence_data",
            field=models.JSONField(
                blank=True, db_comment="Field to store confidence data", null=True
            ),
        ),
    ]
