# Generated by Django 4.2.2 on 2023-06-15 18:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("products", "0005_alter_saleitem_options_sell"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={},
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="quantity",
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name="sell",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.RemoveField(
            model_name="userprofile",
            name="products",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="products",
            field=models.ManyToManyField(to="products.product"),
        ),
    ]
