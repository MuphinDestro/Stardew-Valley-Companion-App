from django.db import models

# Create your models here.


class Item(models.Model):
    # TODO: move this into it's own
    """ an item... duh """
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Villager(models.Model):
    """ A citizen of Stardew Valley """
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    datable = models.BooleanField()
    birth_day = models.CharField(max_length=10)  # e.g. fall 8, summer 28
    address = models.CharField(max_length=20)
    portrait = models.CharField(max_length=200)
    # item preferences
    items_hated = models.ManyToManyField(
        Item, related_name='hate', blank=True, null=True)
    items_disliked = models.ManyToManyField(
        Item, related_name='disliked', blank=True, null=True)
    items_neutral = models.ManyToManyField(
        Item, related_name='neutral', blank=True, null=True)
    items_liked = models.ManyToManyField(
        Item, related_name='liked', blank=True, null=True)
    items_loved = models.ManyToManyField(
        Item, related_name='loved', blank=True, null=True)

    def __str__(self):
        return self.name


class HeartEvent(models.Model):
    """
    A thing that happens when your relationship reaches 
    a certain amount with a person 
    """
    villager = models.ForeignKey(Villager, on_delete=models.CASCADE)
    heart_threshold = models.IntegerField(default=0)
    event_text = models.TextField()
