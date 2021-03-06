# Generated by Django 4.0 on 2021-12-15 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gametype', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='event',
            old_name='gamer',
            new_name='creator',
        ),
        migrations.RemoveField(
            model_name='game',
            name='game_type',
        ),
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(related_name='MyEvents', to='levelupapi.Gamer'),
        ),
        migrations.AddField(
            model_name='game',
            name='gametype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='levelupapi.gametype'),
        ),
    ]
