# Generated by Django 5.1.6 on 2025-02-09 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('Admin_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Admin_name', models.CharField(max_length=50, unique=True)),
                ('Admin_password', models.CharField(max_length=60)),
            ],
            options={
                'db_table': 'admin_table',
            },
        ),
        migrations.CreateModel(
            name='Elec_Name',
            fields=[
                ('Election_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Election_Name', models.CharField(max_length=80, unique=True)),
                ('Election_Year', models.IntegerField(unique=True)),
            ],
            options={
                'db_table': 'Election_Name',
            },
        ),
        migrations.CreateModel(
            name='Elec_Results',
            fields=[
                ('Vote_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Political_Party', models.CharField(max_length=80, null=True)),
                ('First_Vote', models.IntegerField(null=True)),
                ('Second_Vote', models.IntegerField(null=True)),
                ('Third_Vote', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'election_results',
            },
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('Party_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Party_Name', models.CharField(max_length=80, unique=True)),
                ('Party_Logo', models.ImageField(upload_to='media')),
                ('Party_Color', models.CharField(max_length=7)),
            ],
            options={
                'db_table': 'political_party',
            },
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('NIC_Number', models.BigIntegerField(primary_key=True, serialize=False)),
                ('First_Name', models.CharField(max_length=20)),
                ('Last_Name', models.CharField(max_length=20)),
                ('Middle_Name', models.CharField(max_length=20)),
                ('Phone_Number', models.IntegerField(unique=True)),
                ('Address', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=150, unique=True)),
                ('User_Name', models.CharField(max_length=20, unique=True)),
                ('Password', models.CharField(max_length=16, unique=True)),
                ('OTP_Count', models.IntegerField(default=3)),
            ],
            options={
                'db_table': 'details_of_voters',
            },
        ),
    ]
