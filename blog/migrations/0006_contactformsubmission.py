# Generated by Django 3.2.9 on 2021-12-03 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_body_comment_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('reason', models.CharField(choices=[('a', 'a'), ('b', 'b')], default='a', max_length=100)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
