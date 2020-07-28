import os, django, csv, sys, time

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
"""
Menu.objects.create(name='HOT 아이템')
Menu.objects.create(name='스킨케어')
Menu.objects.create(name='바디케어')
Menu.objects.create(name='UV 케어')
Menu.objects.create(name='맘/베이비')
Menu.objects.create(name='리얼리뷰')

time.sleep(2)
MainCategory.objects.create(name='피부고민별', menu_id=2)
MainCategory.objects.create(name='제품라인별', menu_id=2)
MainCategory.objects.create(name='사용단계별', menu_id=2)
time.sleep(2)

SubCategory.objects.create(name='전체', main_category_id=1)
SubCategory.objects.create(name='민감성 피부', main_category_id=1)
SubCategory.objects.create(name='지성/트러블 피부', main_category_id=1)
SubCategory.objects.create(name='손상 피부', main_category_id=1)
SubCategory.objects.create(name='건조한 피부', main_category_id=1)
SubCategory.objects.create(name='UV 차단', main_category_id=1)
SubCategory.objects.create(name='톤업/메이크업', main_category_id=1)
SubCategory.objects.create(name='탄력', main_category_id=1)
SubCategory.objects.create(name='주름', main_category_id=1)
SubCategory.objects.create(name='브라이트닝', main_category_id=1)
"""


CSV_PATH = './product.csv'
def product_csv_reader():
    with open (CSV_PATH, encoding='UTF-8') as in_file:
        data_reader =csv.reader(in_file)
        next(data_reader, None)
        for row in data_reader:
            product_line = row[0]
            name = row[1]
            if not row[3]:
                sale_price = row[4]
            else:
                sale_price = row[3]
            price = row[4]
            hash_tag = row[5]
            Product.objects.create(category_id=1, product_line = product_line, name = name, sale_price = sale_price, price = price, hash_tag = hash_tag)

def product_flag_csv_reader():
    with open (CSV_PATH, encoding='UTF-8') as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        i = 1
        for row in data_reader:
            pid = i
            try:
                best = row[10]
            except:
                best =False
            try:
                new = row[11]
            except:
                new = False

            if not row[6]:
                gift =False
            else:
                gift = row[6]

            if not row[7]:
                sale =False
            else:
                sale = row[7]
            i += 1
            print(pid, i)
            ProductFlag.objects.create(product =Product.objects.get(id=pid), best_flag = best, gift_flag = gift, new_flag = new, sale_flag = sale)

def description_csv_reader():
    with open (CSV_PATH, encoding='UTF-8') as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        i = 1
        for row in data_reader:
            product_id = i
            description = row[2]
            i += 1
            Description.objects.create(product_id = product_id,description = description)

def image_csv_reader():
    with open (CSV_PATH, encoding='UTF-8') as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        i = 1
        for row in data_reader:
            product_id = i
            image_url = row[9].split("뿌")
            i += 1
            Image.objects.create(product_id = product_id, image_url = image_url)

def component_csv_reader():
    with open (CSV_PATH, encoding='UTF-8') as in_file:
        data_reader = csv.reader(in_file)
        next(data_reader, None)
        i = 1
        for row in data_reader:
            component = row[8]
            product_id = i
            i += 1
            Component.objects.create(product_id = product_id, component = component)

#product_csv_reader()
#product_flag_csv_reader()
#description_csv_reader()
#image_csv_reader()
#component_csv_reader()
# 업로딩시 주의!!!
#돌릴때 오류 걸리면 하나씩 해야함, time.sleep 조금 더 길게 해도 ok
#함수는 하나씩 업로딩 해야함





