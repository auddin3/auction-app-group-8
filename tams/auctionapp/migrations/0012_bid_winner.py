# Generated by Django 4.1.3 on 2022-12-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionapp', '0011_rename_winner_bid_bidder_alter_faq_answer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='winner',
            field=models.BooleanField(default=False),
        ),
    ]
