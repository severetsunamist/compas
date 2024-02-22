# Generated by Django 4.1.7 on 2023-08-17 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Заголовок объявления')),
                ('publication_date', models.DateField(auto_now_add=True)),
                ('commerce_valid', models.DateField(auto_now_add=True)),
                ('sale_offered', models.BooleanField(default=True)),
                ('rent_offered', models.BooleanField(default=False)),
                ('sale_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена продажи')),
                ('rental_price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Цена аренды')),
                ('deposit', models.PositiveIntegerField(blank=True, null=True, verbose_name='Депозит')),
                ('condo_fee', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Айдат')),
                ('property_type', models.CharField(choices=[('1+1', '1+1'), ('2+1', '2+1'), ('3+1', '3+1'), ('4+1', '4+1'), ('5+1', '5+1'), ('6+1+', '6+1+')], default='2+1', max_length=4, verbose_name='Планировка')),
                ('gross_area', models.PositiveIntegerField(verbose_name='Общая площадь')),
                ('net_area', models.PositiveIntegerField(blank=True, null=True, verbose_name='Жилая площадь')),
                ('floor', models.PositiveSmallIntegerField(default=1, verbose_name='Этаж')),
                ('total_floors', models.PositiveSmallIntegerField(default=5, verbose_name='Всего этажей')),
                ('bedrooms', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Кол-во спален')),
                ('bathrooms', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Кол-во ванных комнат')),
                ('wc', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Кол-во сан.узлов')),
                ('balcony', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Кол-во балконов')),
                ('heating', models.CharField(choices=[('Нет', 'Нет'), ('Кондиционером', 'Кондиционером'), ('Комби (Газ)', 'Комби (Газ)'), ('Центральное', 'Центральное')], default='Комби (Газ)', max_length=20, verbose_name='Отопление')),
                ('furnitured', models.BooleanField(default=False, verbose_name='Мебель')),
                ('internet', models.BooleanField(default=True, verbose_name='Интернет')),
                ('conditioner', models.BooleanField(default=False, verbose_name='Кондиционер')),
                ('fridge', models.BooleanField(default=False, verbose_name='Холодильник')),
                ('cooker', models.BooleanField(default=False, verbose_name='Плита')),
                ('washer', models.BooleanField(default=False, verbose_name='Стиральная машниа')),
                ('dish_washer', models.BooleanField(default=False, verbose_name='Посудомоечная машина')),
                ('sea_view', models.BooleanField(verbose_name='Вид на море')),
                ('private_territory', models.BooleanField(default=False, verbose_name='Закрытая территория')),
                ('security', models.BooleanField(default=False, verbose_name='Охрана')),
                ('parking', models.BooleanField(default=True, verbose_name='Парковка')),
                ('pool', models.BooleanField(default=True, verbose_name='Бассейн')),
                ('playground', models.BooleanField(default=True, verbose_name='Детская площадка')),
                ('reserve_generator', models.BooleanField(default=True, verbose_name='Генератор')),
                ('gym', models.BooleanField(default=False, verbose_name='Спортзал')),
                ('spa', models.BooleanField(default=False, verbose_name='Сауна/СПА')),
                ('ll', models.CharField(blank=True, max_length=24, null=True, verbose_name='ШиротаXДолгота')),
                ('address', models.CharField(blank=True, max_length=64, null=True, verbose_name='Адрес')),
                ('tapu', models.BooleanField(default=True, verbose_name='Тапу')),
                ('iskan', models.BooleanField(default=True, verbose_name='Искан')),
                ('project_status', models.CharField(choices=[('Готов', 'Готов'), ('Проект', 'Проект'), ('Котлован', 'Котлован'), ('Идёт стройка', 'Идёт стройка'), ('Финал строительства', 'Финал строительства')], default='Дом построен', max_length=20, verbose_name='Стадия проекта')),
                ('comment', models.CharField(blank=True, max_length=96, null=True, verbose_name='Комментарий')),
                ('ad_giver_name', models.CharField(max_length=25, verbose_name='Имя')),
                ('ad_giver_phone', models.CharField(max_length=15, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Квартира',
                'verbose_name_plural': 'Квартиры',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='')),
                ('flat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='residential.flat')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
            },
        ),
    ]