# Generated by Django 4.0.6 on 2022-07-21 04:48

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
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=55)),
                ('email', models.CharField(max_length=50)),
                ('jins', models.CharField(choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')], max_length=30)),
                ('shahar', models.CharField(max_length=120)),
                ('mamlakat', models.CharField(max_length=75)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
