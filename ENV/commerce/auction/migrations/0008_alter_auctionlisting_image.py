# Generated by Django 5.0.6 on 2025-03-11 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0007_alter_auctionlisting_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='auction_images'),
        ),
    ]
