# Generated by Django 5.0.6 on 2025-04-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0017_rename_listing_bid_item_alter_auctionlisting_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlisting',
            name='is_active',
        ),
        migrations.AddField(
            model_name='auctionlisting',
            name='start_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
