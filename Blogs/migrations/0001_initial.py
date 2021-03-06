# Generated by Django 4.0.5 on 2022-06-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('blog_id', models.AutoField(primary_key=True, serialize=False)),
                ('blog_title', models.CharField(default='', max_length=50)),
                ('blog_img_caption', models.CharField(default='', max_length=50)),
                ('blog', models.CharField(max_length=30000000)),
                ('blog_image', models.ImageField(default='', upload_to='doge/blog_image')),
                ('blog_bg', models.ImageField(default='', upload_to='doge/blog_image')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=50)),
                ('desc_type', models.CharField(default='', max_length=25)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
