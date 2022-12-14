# Generated by Django 4.1.1 on 2022-10-27 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0011_alter_game_publisher_alter_gamereview_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='publisher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='reviews.publisher'),
        ),
        migrations.AlterField(
            model_name='gamereview',
            name='rating',
            field=models.PositiveIntegerField(verbose_name='Rating'),
        ),
    ]
