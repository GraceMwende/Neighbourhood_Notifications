# Generated by Django 4.0.3 on 2022-03-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alerts', '0004_remove_post_comments_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighbourhood',
            name='health',
            field=models.CharField(default='health@gmail.com', max_length=100),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='police',
            field=models.CharField(default='police@gmail.com', max_length=100),
        ),
    ]
