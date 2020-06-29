# Generated by Django 2.2.7 on 2020-06-26 18:00

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
            name='RegularUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb', models.URLField()),
                ('phone', models.CharField(default=0, max_length=11)),
                ('city', models.CharField(max_length=20)),
                ('about_you', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='regular_user/')),
                ('user_r', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_name', models.CharField(blank=True, max_length=30)),
                ('purpose', models.TextField()),
                ('web', models.URLField()),
                ('phone', models.CharField(default=0, max_length=11)),
                ('city', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=30)),
                ('photo', models.ImageField(default='default.jpg', upload_to='organization_user/')),
                ('user_o', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
