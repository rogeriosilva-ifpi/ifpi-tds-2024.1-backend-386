# Generated by Django 5.0.2 on 2024-02-28 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('futebol', '0004_clube_modalidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogador',
            name='foto',
            field=models.ImageField(null=True, upload_to='jogadores'),
        ),
    ]
