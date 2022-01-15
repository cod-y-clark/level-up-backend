# Generated by Django 4.0 on 2022-01-04 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_gametype_rename_gamer_event_creator_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='game_name',
        ),
        migrations.RemoveField(
            model_name='game',
            name='gametype',
        ),
        migrations.AddField(
            model_name='game',
            name='game_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='levelupapi.gametype'),
        ),
        migrations.AddField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='levelupapi.gamer'),
        ),
        migrations.AddField(
            model_name='game',
            name='maker',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='number_of_players',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='skill_level',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
