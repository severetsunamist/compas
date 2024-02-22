from django.db import models
from datetime import date

# DROPDOWNS Всплывающие списки
class DropDown:
    property_types = (
        ('Дом', 'Дом'),
        ('1+1', '1+1'),
        ('2+1', '2+1'),
        ('3+1', '3+1'),
        ('4+1', '4+1'),
        ('5+1', '5+1'),
        ('6+1+','6+1+')
    )
    heating_types = (
        ('Нет', 'Нет'),
        ('Кондиционером', 'Кондиционером'),
        ('Комби (Газ)', 'Комби (Газ)'),
        ('Центральное', 'Центральное'),
    )
    project_status = (
        ('Готов', 'Готов'),
        ('Идёт стройка','Идёт стройка'),
        ('Котлован', 'Котлован'),
        ('Проект', 'Проект'),

    # )
    # country = (
    #     ('0', 'Россия'),
    #     ('1', 'Турция'),
    #     # ('3', 'Сербия'),
    #     # ('4', 'Аргентина'),
    #     # ('5', 'Бали'),
    #     # ('6', 'Финляндия'),
    # )
    # location = (
    #
    #     ('0', 'Стамбул'),
    #     ('1', 'Измир'),
    #     ('2', 'Анкара'),
    #     ('3', 'Мерсин'),
    #     ('4', 'Анталия'),
    #     ('5', 'Бодрум'),
    #     ('6', 'Москва'),
    #     ('7', 'Питер'),
    #     ('8', 'Минск'),
    #     ('9', 'Киев'),

    )
    # ad_giver = (
    #     ('Собственник','Собственник'),
    #     ('Риэлтор','Риэлтор'),
    #     ('Агентство','Агентство'),
    #     ('Управляющая компания','Управляющая компания'),
    # )

dropdowns = DropDown()
# ===============================================

# Create your models here.
class Flat(models.Model):
    publication_date = models.DateField(auto_now_add=True)
    property_type = models.CharField("Планировка", choices=dropdowns.property_types, max_length=4, default="2+1")
    name = models.CharField("Заголовок", max_length=30, null=True, blank=True)
    # location
    lat = models.CharField("Широта", max_length=12, default="36.7727692")
    lng = models.CharField("Долгота", max_length=12, default="34.5670689")
    address = models.CharField("Адрес", max_length=64, null=True, blank=True)
    # contact credentials
    contact_name = models.CharField('Имя', max_length=25)
    contact_phone = models.CharField('Телефон', max_length=15)
    contact_tg = models.CharField('Telegram', max_length=64, null=True)
    # legal
    tapu = models.BooleanField('Тапу', default=True)
    iskan = models.BooleanField('Искан', default=True)
    project_status = models.CharField("Стадия проекта", choices=dropdowns.project_status, default="Дом построен", max_length=20)
    comment = models.CharField("Комментарий", max_length=96, null=True, blank=True)
    # sale
    sale_offered = models.BooleanField(default=True)
    sale_price = models.PositiveIntegerField("Цена продажи", null=True, blank=True)
    # rent
    rent_offered = models.BooleanField(default=False)
    rental_price = models.PositiveIntegerField("Цена аренды", null=True, blank=True)
    deposit = models.PositiveIntegerField("Депозит", null=True, blank=True)
    condo_fee = models.PositiveSmallIntegerField("Айдат", null=True, blank=True)

    # area and room clarification

    gross_area = models.PositiveIntegerField("Общая площадь", null=False, blank=False)
    net_area = models.PositiveIntegerField("Жилая площадь", null=True, blank=True)
    floor = models.PositiveSmallIntegerField("Этаж", null=True, blank=True)
    total_floors = models.PositiveSmallIntegerField("Всего этажей", null=False, default=12)
    # property equipped with
    bedrooms = models.PositiveSmallIntegerField("Кол-во спален", null=True, blank=True)
    bathrooms = models.PositiveSmallIntegerField("Кол-во ванных комнат", null=True, blank=True)
    wc = models.PositiveSmallIntegerField("Кол-во сан.узлов", null=True, blank=True)
    balcony = models.PositiveSmallIntegerField("Кол-во балконов", null=True, blank=True)
    heating = models.CharField("Отопление", choices=dropdowns.heating_types, max_length=20, default="Комби (Газ)")

    furnitured = models.BooleanField("Мебель", default=False)
    internet = models.BooleanField("Интернет", default=True)
    conditioner = models.BooleanField("Кондиционер", default=False)
    fridge = models.BooleanField("Холодильник", default=False)
    cooker = models.BooleanField("Плита", default=False)
    washer = models.BooleanField("Стиральная машниа", default=False)
    dish_washer = models.BooleanField("Посудомоечная машина", default=False)
    sea_view = models.BooleanField("Вид на море")
    # additional infrastructure
    private_territory = models.BooleanField("Закрытая территория", default=False)
    security = models.BooleanField("Охрана", default=False)
    parking = models.BooleanField("Парковка", default=True)
    pool = models.BooleanField("Бассейн", default=True)
    playground = models.BooleanField("Детская площадка", default=True)
    reserve_generator = models.BooleanField("Генератор", default=True)
    gym = models.BooleanField("Спортзал", default=False)
    spa = models.BooleanField("Сауна/СПА", default=False)


    class Meta:
        verbose_name = 'Жильё'
        verbose_name_plural = 'Жильё'
    def __str__(self):
        return self.name

class Photo(models.Model):
    flat_id = models.ForeignKey(Flat, on_delete=models.CASCADE, related_name='photos')
    img = models.ImageField('', blank=True, null=True)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'

