# Generated by Django 3.0.8 on 2020-07-29 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_component'),
        ('user', '0005_auto_20200729_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'cartproducts',
            },
        ),
    ]
