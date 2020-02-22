# Generated by Django 3.0.3 on 2020-02-22 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MagicSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('set_code', models.CharField(max_length=5)),
                ('type', models.CharField(choices=[('BOO', 'Booster Box'), ('PLD', 'Planeswalker Deck'), ('PRM', 'Promotional (Judge/FNM/WPN)'), ('DD', 'Duel Deck'), ('EDH', 'Commander Preconstructed Deck'), ('MST', 'Masterpiece Series')], max_length=3)),
                ('card_count', models.PositiveSmallIntegerField()),
                ('mtgo_only', models.BooleanField(default=False)),
                ('block', models.CharField(blank=True, max_length=64)),
                ('scryfall_id', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('store_type', models.CharField(choices=[('SCG', 'Sun Country Games')], max_length=3)),
                ('url', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='MagicCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('gatherer_id', models.CharField(blank=True, max_length=32)),
                ('oracle_id', models.CharField(max_length=32)),
                ('cmc', models.DecimalField(decimal_places=2, max_digits=5)),
                ('mana_cost', models.CharField(blank=True, max_length=32)),
                ('power', models.CharField(blank=True, max_length=16)),
                ('toughness', models.CharField(blank=True, max_length=16)),
                ('loyalty', models.CharField(blank=True, max_length=16)),
                ('type_line', models.CharField(max_length=64)),
                ('oracle_text', models.CharField(blank=True, max_length=1024)),
                ('rarity', models.CharField(blank=True, max_length=10)),
                ('collector_number', models.CharField(max_length=10)),
                ('frame_type', models.CharField(max_length=20)),
                ('reserved_list', models.BooleanField(blank=True, default=False)),
                ('oversized', models.BooleanField(blank=True, default=False)),
                ('set', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.MagicSet')),
            ],
        ),
    ]
