import os, django, csv, sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
django.setup()

from product.models import (
    Menu,
    MainCategory,
    SubCategory,
    Product,
    Image,
    Description,
    Component,
    ProductFlag
)

CSV_PATH = './product.csv'

with open (CSV_PATH, encoding='UTF-8') as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    def product_csv_reader():
        for row in data_reader:
            Product.object.create(
                category_id =1,
                product_line = row[0],
                name = row[1],
                sale_price = row[3],
                price = row[4],
                hash_tag = row[5],
            )
    def product_flag_csv_reader():
        i = 1
        for row in data_reader:
            ProductFlag.object.create(
                product_id = i,
                new = row[11]
                best = row[10]
                gift = row[6]
                sale = row[7]
            )
            i += 1


