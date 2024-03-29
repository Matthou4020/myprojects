# Generated by Django 5.0.3 on 2024-03-26 12:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_remove_auctionlisting_onwatchlist_watchlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlisting',
            name='won',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='AuctionWinner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winners', to='auctions.auctionlisting')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winners', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
