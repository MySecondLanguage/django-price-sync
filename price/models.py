from django.db import models

class Product(models.Model):
    url = models.URLField(
        null=True,
        blank=True,
        unique=True
    )
    title = models.CharField(
        null=True,
        blank=True,
        max_length=200
    )
    sku = models.CharField(
        null=True,
        blank=True,
        max_length=100
    )
    price= models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    extracted_price= models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    sync_success = models.BooleanField(
        default=False
    )
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(
        null=True,
        blank=True
    )
    

    class Meta:
        unique_together = ('url', 'sku',)

    def __str__(self):
        return self.sku


