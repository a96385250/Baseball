# Generated by Django 3.0 on 2020-02-24 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('teamID', models.IntegerField(max_length=3, primary_key=True, serialize=False)),
                ('teamName', models.CharField(max_length=10)),
                ('teamEng', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'teams',
            },
        ),
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('account', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.team')),
            ],
            options={
                'db_table': 'member',
            },
        ),
    ]
