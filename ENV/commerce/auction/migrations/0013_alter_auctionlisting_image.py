# Generated by Django 5.0.6 on 2025-03-19 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0012_auctionlisting_end_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlisting',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='auction_images/'),
        ),
    ]
