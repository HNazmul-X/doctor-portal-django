# Generated by Django 3.2.8 on 2021-10-25 10:34

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('fullname', models.CharField(max_length=140, verbose_name='Full Name')),
                ('username', models.CharField(max_length=100, verbose_name='User Name')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='DoctorsModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=100)),
                ('specialize', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('mobile', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PateintFeestatus',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PateintModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=150)),
                ('symptoms', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=150)),
                ('mobile', models.CharField(max_length=20)),
                ('feeStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorPortal.pateintfeestatus')),
            ],
        ),
        migrations.CreateModel(
            name='AppointmentModel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject', models.CharField(max_length=100)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorPortal.doctorsmodel')),
                ('pateint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctorPortal.pateintmodel')),
            ],
        ),
    ]
