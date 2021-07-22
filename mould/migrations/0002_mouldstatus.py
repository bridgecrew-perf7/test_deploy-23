# Generated by Django 3.1.5 on 2021-07-21 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mould', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MouldStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_update', models.DateTimeField(auto_now_add=True)),
                ('count_increment', models.IntegerField()),
                ('mould_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mould_status', to='mould.mould')),
            ],
        ),
    ]
