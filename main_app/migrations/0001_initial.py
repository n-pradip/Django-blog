# Generated by Django 4.0.1 on 2022-01-21 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('cat_slug', models.SlugField()),
                ('image', models.ImageField(upload_to='category_img/')),
            ],
        ),
        migrations.CreateModel(
            name='Blogposts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('blogpost_slug', models.SlugField()),
                ('date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='blogposts_img/')),
                ('author', models.CharField(max_length=100)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.category')),
            ],
        ),
    ]
