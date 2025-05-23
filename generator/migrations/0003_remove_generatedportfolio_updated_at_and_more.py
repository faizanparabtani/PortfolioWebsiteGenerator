# Generated by Django 5.2 on 2025-04-20 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_portfoliotemplate_generatedportfolio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generatedportfolio',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='generatedportfolio',
            name='netlify_deploy_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='generatedportfolio',
            name='netlify_site_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='generatedportfolio',
            name='netlify_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='generatedportfolio',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='generatedportfolio',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
