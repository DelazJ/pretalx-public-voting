# Generated by Django 3.2.10 on 2022-01-11 15:28

from django.db import migrations, models
import django.db.models.deletion
import i18nfield.fields
import pretalx_public_voting.models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0029_event_domain"),
        ("pretalx_public_voting", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PublicVotingSettings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("start", models.DateTimeField(blank=True, null=True)),
                ("end", models.DateTimeField(blank=True, null=True)),
                ("text", i18nfield.fields.I18nTextField(null=True)),
                ("anonymize_speakers", models.BooleanField(default=False)),
                ("show_session_image", models.BooleanField(default=True)),
                ("min_score", models.IntegerField(default=1)),
                ("max_score", models.IntegerField(default=3)),
                (
                    "score_names",
                    models.JSONField(default=pretalx_public_voting.models.get_dict),
                ),
                (
                    "event",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="public_vote_settings",
                        to="event.event",
                    ),
                ),
            ],
        ),
    ]
