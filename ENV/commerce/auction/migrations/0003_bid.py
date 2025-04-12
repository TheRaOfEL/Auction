# Generated by Django 5.0.6 on 2025-03-10 19:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_remove_auctionlisting_current_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('auction_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.auctionlisting')),
            ],
        ),
    ]
