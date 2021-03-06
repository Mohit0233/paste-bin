# Generated by Django 4.0.3 on 2022-03-27 12:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paste_hash', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=50)),
                ('content_url', models.CharField(max_length=2048)),
                ('formatter', models.CharField(choices=[('TEXT', 'Text'), ('C', 'C'), ('C_PLUS_PLUS', 'C Plus Plus'), ('SQL', 'Sql')], max_length=50)),
                ('visibility', models.CharField(choices=[('PUBLIC', 'Public'), ('UNLISTED', 'Unlisted'), ('PRIVATE', 'Private')], default='PUBLIC', max_length=50)),
                ('expiration_date', models.DateTimeField()),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('password', models.CharField(max_length=10)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
