from django.db import models


class Lesson(models.Model):
    """Describes the fields and attributes of the Lesson model in the database."""

    name = models.CharField(max_length=250)
    product = models.ForeignKey(
        to="product",
        on_delete=models.CASCADE,
        related_name="lessons"
    )
    video_link = models.URLField()

    class Meta:
        """Describes class metadata."""

        db_table = "lessons"
