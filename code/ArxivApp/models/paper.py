from ArxivApp.models.base import Model
from django.db import models

class Paper(Model):
    """
    This model is used to create objects of research paper
    for users to bookmark. An instance is deleted if it hsa zero
    references
    """

    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )

    authors = models.CharField(
        max_length=1023,
        null=False,
        blank=False,
    )

    summary = models.TextField(
        null=True,
        blank=True,
    )

    comment = models.TextField(
        null=True,
        blank=True,
    )

    subject_classification = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )

    arxiv_id = models.CharField(
        max_length=63,
        null=False,
        blank=False,
        unique=True,
    )

    html_url = models.TextField(
        null=True,
        blank=True,
    )

    pdf_url = models.TextField(
        null=True,
        blank=True,
    )

    datetime_paper_published = models.DateTimeField(
        null=False,
        blank=False,
    )

    datetime_paper_updated = models.DateTimeField(
        null=False,
        blank=False,
    )

    def __str__(self):

        return f'{self.title} - by - {self.authors}'
