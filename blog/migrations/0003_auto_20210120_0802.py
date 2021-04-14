# Generated by Django 3.1.1 on 2021-01-20 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210120_0428'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_blog',
            name='image',
        ),
        migrations.RemoveField(
            model_name='project_blog',
            name='url',
        ),
        migrations.AddField(
            model_name='project_blog',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project_blog',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='project_blog',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]