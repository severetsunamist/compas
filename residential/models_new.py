from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date

class DropDown:
    res_types = (
        ('0', 'Квартира'),
        ('1', 'Дом'),
        ('2', 'Таунхаус'),
        ('3', 'Вилла'),
    )
    estate_types = (
        ('0', 'Жилая'),
        ('1', 'Торговая'),
        ('2', 'Офисы'),
        ('3', 'Складская'),
        ('4', 'Земля'),
    )

    planning = (
        ('1', '1+1'),
        ('2', '2+1'),
        ('3', '3+1'),
        ('4', '4+1'),
        ('5', '5+1'),
        ('6', '6+1+')
    )
    heating_types = (
        ('0', 'Нет'),
        ('1', 'Кондиционером'),
        ('2', 'Комби (Газ)'),
        ('3', 'Центральное'),
    )
    project_status = (
        ('1', 'Готов'),
        ('2', 'Проект'),
        ('3', 'Котлован'),
        ('4', 'Идёт стройка'),
        ('5', 'Финал строительства'),
    )

    # landlord = (
    #     ('Собственник','Собственник'),
    #     ('Риэлтор','Риэлтор'),
    #     ('Агентство','Агентство'),
    #     ('Управляющая компания','Управляющая компания'),
    # )

dropdowns = DropDown()


class Contact(AbstractUser):
    pass


class Estate(models.Model):
    type = models.CharField("Тип", choices=dropdowns.estate_types, max_length=4, default="Жилая")
    total_area = models.PositiveIntegerField("Общая площадь", null=False, blank=False)
    # location
    lat = models.CharField("Широта", max_length=12, null=False, blank=False)
    lng = models.CharField("Долгота", max_length=12, null=False, blank=False)
    address = models.CharField("Адрес", max_length=128, null=True, blank=True)
    # meta data
    publication_date = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(Contact, on_delete=models.CASCADE)


class Residential(Estate):
    net_area = models.PositiveIntegerField("Жилая площадь", null=True, blank=True)
    floor = models.PositiveSmallIntegerField("Этаж", null=True, blank=True)
    total_floors = models.PositiveSmallIntegerField("Всего этажей", null=True, blank=True)
    # rooms
    bedrooms = models.PositiveSmallIntegerField("Кол-во спален", null=True, blank=True)
    bathrooms = models.PositiveSmallIntegerField("Кол-во ванных комнат", null=True, blank=True)
    wc = models.PositiveSmallIntegerField("Кол-во сан.узлов", null=True, blank=True)
    balcony = models.PositiveSmallIntegerField("Кол-во балконов", null=True, blank=True)
    heating = models.CharField("Отопление", choices=dropdowns.heating_types, max_length=20, default="Комби (Газ)")
    # vital infrastructure
    furnitured = models.BooleanField("Мебель", default=False)
    internet = models.BooleanField("Интернет", default=True)
    conditioner = models.BooleanField("Кондиционер", default=False)
    fridge = models.BooleanField("Холодильник", default=False)
    cooker = models.BooleanField("Плита", default=False)
    washer = models.BooleanField("Стиральная машниа", default=False)
    dish_washer = models.BooleanField("Посудомоечная машина", default=False)
    sea_view = models.BooleanField("Вид на море", default=False)
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


class Offer(models.Model):
    # status
    active = models.BooleanField(default=True)
    comment = models.CharField('Комментарий', max_length=140)
    # sale
    sale_offered = models.BooleanField(default=True)
    sale_price = models.PositiveIntegerField("Цена продажи", null=True, blank=True)
    # rent
    rent_offered = models.BooleanField(default=False)
    rental_price = models.PositiveIntegerField("Цена аренды", null=True, blank=True)
    deposit = models.PositiveIntegerField("Депозит", null=True, blank=True)
    #
    condo_fee = models.PositiveSmallIntegerField("Айдат", null=True, blank=True)

    project_status = models.CharField("Стадия проекта", choices=dropdowns.project_status, default="Готов",
                                      max_length=20)
    tapu = models.BooleanField('Тапу', default=True)
    iskan = models.BooleanField('Искан', default=True)
    estate = models.ForeignKey(Estate, on_delete=models.CASCADE, related_name='estate')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='contact')


    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'



class Photo(models.Model):
    flat_id = models.ForeignKey(Estate, on_delete=models.CASCADE, related_name='photos')
    img = models.ImageField('', blank=True, null=True)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


