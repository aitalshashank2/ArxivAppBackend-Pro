from django.db import models


class DownloadLocation(models.Model):
    """
    This model is the link between a downloaded paper and a user
    used to store the location of storage on the frontend user's
    device
    """

    user = models.ForeignKey(
        'ArxivApp.User',
        related_name='download_locations',
        on_delete=models.CASCADE,
    )

    paper = models.ForeignKey(
        'ArxivApp.Paper',
        related_name='download_locations',
        on_delete=models.CASCADE,
    )

    html_url = models.TextField(
        null=False,
        blank=False,
        default='/',
    )

    def __str__(self):

        return self.html_url
