from django.db import models


class MagicSet(models.Model):
    TYPES_OF_SETS = [
        ('BOO', 'Booster Box'),
        ('PLD', 'Planeswalker Deck'),
        ('PRM', 'Promotional (Judge/FNM/WPN)'),
        ('DD', 'Duel Deck'),
        ('EDH', 'Commander Preconstructed Deck'),
        ('MST', 'Masterpiece Series')
    ]

    name = models.CharField(max_length=64, unique=True)
    set_code = models.CharField(max_length=5)
    type = models.CharField(max_length=3, choices=TYPES_OF_SETS)
    card_count = models.PositiveSmallIntegerField()
    mtgo_only = models.BooleanField(default=False)
    block = models.CharField(max_length=64, blank=True)
    scryfall_id = models.CharField(max_length=40)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} [{self.set_code}]'


class MagicCard(models.Model):
    name = models.CharField(max_length=64)
    set = models.ForeignKey(MagicSet, on_delete=models.CASCADE)
    gatherer_id = models.CharField(max_length=32, blank=True)
    oracle_id = models.CharField(max_length=32)
    cmc = models.DecimalField(max_digits=5, decimal_places=2)
    mana_cost = models.CharField(max_length=32, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    power = models.CharField(max_length=16, blank=True)
    toughness = models.CharField(max_length=16, blank=True)
    loyalty = models.CharField(max_length=16, blank=True)
    type_line = models.CharField(max_length=64)
    oracle_text = models.CharField(max_length=1024, blank=True)
    rarity = models.CharField(max_length=10, blank=True)
    collector_number = models.CharField(max_length=10)
    frame_type = models.CharField(max_length=20)

    reserved_list = models.BooleanField(default=False, blank=True)
    oversized = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return f'{self.name} [{self.set.set_code}]'


class Store(models.Model):
    TYPES_OF_STORES = [
        ('SCG', 'Sun Country Games')
    ]
    name = models.CharField(max_length=64)
    store_type = models.CharField(max_length=3, choices=TYPES_OF_STORES)
    url = models.CharField(max_length=64)

    def __str__(self):
        return self.name
