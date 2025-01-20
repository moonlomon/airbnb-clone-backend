from django.db import models


class CommonModel(models.Model):
    """Common Model definition"""

    create_at = models.DateTimeField(
        auto_now_add=True,
    )
    update_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True
