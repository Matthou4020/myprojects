# Generated by Django 5.0.3 on 2024-03-25 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_bid_comment_delete_bids_delete_comments_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionlisting',
            old_name='owner',
            new_name='user',
        ),
    ]
