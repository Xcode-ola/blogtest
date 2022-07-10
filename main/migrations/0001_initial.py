# Generated by Django 4.0.1 on 2022-07-10 00:24

import ckeditor.fields
import datetime
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
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('snippet', models.CharField(default='Click the link to read more', max_length=255)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('posted_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('comment', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.blog')),
            ],
        ),
    ]