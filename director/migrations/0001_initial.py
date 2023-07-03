# Generated by Django 4.2.1 on 2023-07-03 15:07

import director.models.user
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(blank=True, max_length=124, null=True)),
                ('last_name', models.CharField(blank=True, max_length=128, null=True)),
                ('phone', models.CharField(blank=True, max_length=131, null=True)),
                ('password', models.CharField(max_length=1029)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('join_date', models.DateField(auto_now_add=True)),
                ('type', models.SmallIntegerField(default=0)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', director.models.user.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='chetdan_buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shartnome_raqami', models.IntegerField()),
                ('davlat_nomi', models.CharField(max_length=128)),
                ('zavod_nomi', models.CharField(max_length=128)),
                ('date', models.DateField()),
                ('holati', models.CharField(choices=[('tuzildi', 'tuzildi'), ('yakunlandi', 'yakunlandi'), ('yolda', 'yolda'), ('qabul_qilindi', 'qabul_qilindi')], max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=50)),
                ('oxirgi_product', models.DateTimeField(auto_now=True)),
                ('xabar_berish', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Karzina_zakaz',
            fields=[
                ('karzina_name', models.CharField(max_length=128)),
                ('nomer_zakaza', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Magazin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magazin_nomi', models.CharField(max_length=128)),
                ('magazin_joylashuvi', models.CharField(max_length=128)),
                ('maxsulot_soni', models.IntegerField()),
                ('valyuta', models.CharField(choices=[('USD', 'USD'), ('YUAN', 'YUAN'), ('UZS', 'UZS')], max_length=128)),
                ('xodimlar_soni', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Magazin_zakaz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('size', models.CharField(max_length=128)),
                ('date', models.DateTimeField(auto_now=True)),
                ('color', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('nomer_zakaza', models.IntegerField()),
                ('jonatish_nomeri', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Maxsulot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxsulot_nomi', models.CharField(max_length=128)),
                ('razmer', models.CharField(max_length=128)),
                ('rangi', models.CharField(max_length=128)),
                ('joyi', models.CharField(max_length=128)),
                ('sotish_narxi', models.IntegerField(default=0)),
                ('sotish_narxi_type', models.CharField(max_length=10)),
                ('kirib_kelgan_narxi', models.IntegerField(default=0)),
                ('kirib_kelgan_narxi_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ombor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=128)),
                ('xodim_soni', models.IntegerField()),
                ('maxsulot', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=1024)),
                ('email', models.CharField(max_length=50)),
                ('is_conf', models.BooleanField(default=False)),
                ('is_expire', models.BooleanField(default=False)),
                ('tries', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Savdolar_royxati',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Shartnoma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_number', models.IntegerField(default=1)),
                ('product_date', models.DateField()),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='director.maxsulot')),
            ],
        ),
        migrations.CreateModel(
            name='Xodimlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xodim_ismi', models.CharField(max_length=128)),
                ('phone', models.CharField(max_length=50)),
                ('passport', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Shartnoma_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('total', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('contract_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='director.shartnoma')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='director.maxsulot')),
            ],
        ),
        migrations.CreateModel(
            name='savdo_oynasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxsulot_nomi', models.CharField(max_length=128)),
                ('maxsulot_rangi', models.CharField(max_length=128)),
                ('size', models.CharField(max_length=128)),
                ('soni', models.IntegerField(default=0)),
                ('sotish_narxi', models.CharField(max_length=50)),
                ('valyuta', models.CharField(choices=[('USD', 'USD'), ('YUAN', 'YUAN'), ('UZS', 'UZS')], max_length=128)),
                ('clent_bolsa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='director.client')),
            ],
        ),
        migrations.CreateModel(
            name='Magazin_buyurtma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zakaz_status', models.CharField(choices=[('Buyurtma qilindi', 'Buyurtma qilindi'), ("Yig'ilyapti", "Yig'ilyapti"), ("Yo'lda", "Yo'lda"), ('Keldi', 'Keldi')], max_length=128)),
                ('magazin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='director.magazin')),
                ('zakaz', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='director.magazin_zakaz')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('dis', models.BooleanField(default=False)),
                ('prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='director.maxsulot')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Korzina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narxi', models.BigIntegerField()),
                ('narxi_tupy', models.CharField(max_length=7)),
                ('nechtaligi', models.IntegerField(default=1)),
                ('status', models.BooleanField(default=True)),
                ('product', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='director.maxsulot')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]