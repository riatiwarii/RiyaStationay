# Generated by Django 4.2.3 on 2023-09-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_cartitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='product_name',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='price',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
    ]