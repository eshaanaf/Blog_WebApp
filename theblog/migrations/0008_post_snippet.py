# Generated by Django 3.2.3 on 2021-06-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0007_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click the title to read the post!', max_length=255),
        ),
    ]
