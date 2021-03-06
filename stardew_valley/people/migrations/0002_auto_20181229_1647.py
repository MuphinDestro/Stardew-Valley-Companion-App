# Generated by Django 2.1.4 on 2018-12-29 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='villager',
            name='items_disliked',
            field=models.ManyToManyField(blank=True, null=True, related_name='disliked', to='people.Item'),
        ),
        migrations.AlterField(
            model_name='villager',
            name='items_hated',
            field=models.ManyToManyField(blank=True, null=True, related_name='hate', to='people.Item'),
        ),
        migrations.AlterField(
            model_name='villager',
            name='items_liked',
            field=models.ManyToManyField(blank=True, null=True, related_name='liked', to='people.Item'),
        ),
        migrations.AlterField(
            model_name='villager',
            name='items_loved',
            field=models.ManyToManyField(blank=True, null=True, related_name='loved', to='people.Item'),
        ),
        migrations.AlterField(
            model_name='villager',
            name='items_neutral',
            field=models.ManyToManyField(blank=True, null=True, related_name='neutral', to='people.Item'),
        ),
    ]
