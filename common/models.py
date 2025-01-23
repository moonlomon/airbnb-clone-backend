from django.db import models


class CommonModel(models.Model):
    """Common Model definition"""

    create_at = models.DateTimeField(
        auto_now_add=True,
    )
    update_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:  # abstract : db에서 칼럼에 포함시키지 않게 하기, admin에도 안뜸뜸
        abstract = True
