# Generated by Django 3.0.5 on 2020-04-28 20:42

from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_answer_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='info',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='about',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('phone', models.CharField(max_length=30)),
                ('website', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=400)),
                ('description', django_summernote.fields.SummernoteTextField()),
                ('active', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='partners', to='blog.Image')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
