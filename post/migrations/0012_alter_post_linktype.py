# Generated by Django 3.2.9 on 2021-12-19 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_alter_post_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='linktype',
            field=models.CharField(blank=True, choices=[('Whatsapp', 'Whatsapp'), ('Telegram', 'Telegram'), ('Facebook', 'Facebook'), ('Youtube', 'Youtube'), ('TikTok', 'TikTok'), ('Instagram', 'Instagram')], max_length=100, null=True, verbose_name='Platforma'),
        ),
    ]
