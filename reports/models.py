from django.db import models


class UserReport(models.Model):
    """A text report filed by a user."""

    timestamp = models.DateTimeField(auto_now=True,
                                     help_text="Timestamp of this snapshot")

    text = models.TextField(null=False,
                            help_text="User-provided description")

    user_email = models.TextField(null=True,
                                  help_text="Optional e-mail address of the user for responding")

    is_resolved = models.BooleanField(null=False, default=False,
                                      help_text="Whether this report has been resolved")
