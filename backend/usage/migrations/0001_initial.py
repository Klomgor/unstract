# Generated by Django 4.2.1 on 2024-04-22 12:55

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Usage",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("workflow_id", models.CharField(max_length=255)),
                ("execution_id", models.CharField(max_length=255)),
                ("adapter_instance_id", models.CharField(max_length=255)),
                ("run_id", models.CharField(max_length=255)),
                ("usage_type", models.CharField(max_length=255)),
                ("model_name", models.CharField(max_length=255)),
                ("embedding_tokens", models.IntegerField()),
                ("prompt_tokens", models.IntegerField()),
                ("completion_tokens", models.IntegerField()),
                ("total_tokens", models.IntegerField()),
            ],
            options={
                "db_table": "token_usage",
            },
        ),
    ]