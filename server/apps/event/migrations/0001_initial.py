# Generated by Django 5.0.3 on 2024-03-05 21:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField()),
                ('location', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('id_created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='User_event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'unique_together': {('id_user', 'id_event')},
            },
        ),
    ]
