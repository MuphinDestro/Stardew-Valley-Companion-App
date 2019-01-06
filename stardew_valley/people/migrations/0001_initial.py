# Generated by Django 2.1.4 on 2018-12-29 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeartEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_threshold', models.IntegerField(default=0)),
                ('event_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Villager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=10)),
                ('datable', models.BooleanField()),
                ('birth_day', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=20)),
                ('portrait', models.CharField(max_length=200)),
                ('items_disliked', models.ManyToManyField(related_name='disliked', to='people.Item')),
                ('items_hated', models.ManyToManyField(related_name='hate', to='people.Item')),
                ('items_liked', models.ManyToManyField(related_name='liked', to='people.Item')),
                ('items_loved', models.ManyToManyField(related_name='loved', to='people.Item')),
                ('items_neutral', models.ManyToManyField(related_name='neutral', to='people.Item')),
            ],
        ),
        migrations.AddField(
            model_name='heartevent',
            name='villager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='people.Villager'),
        ),
    ]