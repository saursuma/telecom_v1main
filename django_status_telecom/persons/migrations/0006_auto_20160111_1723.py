# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0005_auto_20160110_1921'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.CharField(max_length=254, null=True)),
                ('CreatedOn', models.CharField(max_length=254, null=True)),
                ('CreatedBy', models.CharField(max_length=254, null=True)),
                ('TaskType', models.CharField(max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaskStatus', models.CharField(max_length=254, null=True)),
                ('TaskPriority', models.CharField(max_length=254, null=True)),
                ('CreatedOn', models.CharField(max_length=254, null=True)),
                ('CreatedBy', models.CharField(max_length=254, null=True)),
                ('CompletedOn', models.CharField(max_length=254, null=True)),
                ('CompletedBy', models.CharField(max_length=254, null=True)),
                ('TaskType', models.CharField(max_length=254, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='comments',
            name='article',
        ),
        migrations.RemoveField(
            model_name='persons',
            name='body',
        ),
        migrations.RemoveField(
            model_name='persons',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='persons',
            name='title',
        ),
        migrations.AddField(
            model_name='persons',
            name='address',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='persons',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='persons',
            name='city',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='persons',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='persons',
            name='email',
            field=models.CharField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='persons',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='persons',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='persons',
            name='state_province',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='persons',
            name='website',
            field=models.URLField(null=True),
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
        migrations.AddField(
            model_name='task',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Persons'),
        ),
        migrations.AddField(
            model_name='comment',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.Task'),
        ),
    ]
