from django.db import models

class Menu(models.Model):
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'menus'

    def __str__(self):
        return self.name

class MainCategory(models.Model):
    menu = models.ForeignKey(Menu, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'main_categories'

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)

    class Meta:
        db_table = 'sub_categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    product_line = models.CharField(max_length = 50)
    name = models.CharField(max_length = 200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    hash_tag = models.CharField(max_length= 500)

    class Meta:
        db_table = 'products'

    def __str__(self):
        return self.name

class ProductFlag(models.Model):
    sale_flag = models.BooleanField(default=False)
    gift_flag = models.BooleanField(default=False)
    best_flag = models.BooleanField(default=False)
    new_flag = models.BooleanField(default=False)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)


    class Meta:
        db_table = 'product_flags'


class Description(models.Model):
    description = models.CharField(max_length=1000)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'descriptions'

    def __str__(self):
        return self.description

class Image(models.Model):
    image_url = models.URLField(max_length=2000)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

    def __str__(self):
        return self.image_url

class Component(models.Model):
    component = models.CharField(max_length=400)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'components'

    def __str__(self):
        return self.components




