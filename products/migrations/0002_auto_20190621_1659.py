# Generated by Django 2.2.2 on 2019-06-21 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['nutrition_grade'], 'verbose_name_plural': 'products'},
        ),
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='products',
            field=models.ManyToManyField(related_name='categories', to='products.Product'),
        ),
    ]