from django.db import models

class ProductDetailTag(models.Model):
    banner        = models.TextField()
    productDetail = models.TextField()
    sec3          = models.TextField()
    sec5          = models.TextField()
    sec6          = models.TextField()
    purchaseView  = models.TextField()

    class Meta:
        db_table = "product_detail_tags"




