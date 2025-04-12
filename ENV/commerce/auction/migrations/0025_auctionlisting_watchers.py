# Generated by Django 5.0.7 on 2025-04-12 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0024_auctionlisting_sold_to'),
        ('user', '0003_alter_profile_email_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='watchers',
            field=models.ManyToManyField(blank=True, related_name='watchlist', to='user.profile'),
        ),
    ]
