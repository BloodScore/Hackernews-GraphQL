# Generated by Django 3.2.5 on 2021-07-16 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_vote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votess', to='links.link'),
        ),
    ]
