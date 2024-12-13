from random import choices

from django.db import models

class CallBack(models.Model):
    class Question(models.IntegerChoices):
        POVERKA_SCHETCHIKOV_VODY = 1, 'Поверке счетчиков воды'
        ZAMENA_SCHETCHIKOV_VODY = 2, 'Замене счетчиков воды'
        USTANOVKA_SCHETCHIKOV_VODY = 3, 'Установке счетчиков воды'
        OTHER_QUESTION = 4, 'Другой вопрос'

    creation_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Дата создания',
                                         )
    question = models.IntegerField(choices=Question.choices,
                                                       default=Question.POVERKA_SCHETCHIKOV_VODY,
                                                       verbose_name="Вопрос по",
                                                       )
    phone_number = models.CharField(max_length=20,
                                    verbose_name="Номер телефона",
                                    )
    client_name = models.CharField(max_length=100,
                                   verbose_name='Ваше имя',
                                   )

    def get_question_display(self):
        return self.Question(self.question).label

    class Meta:
        verbose_name = "Заявка на обратный звонок"
        verbose_name_plural = "Заявки на обратный звонок"
        ordering = ['-creation_date']


class ServicePrice(models.Model):
    name_service = models.CharField(max_length=120, verbose_name='Услуга')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    slug = models.CharField(max_length=120, db_index=True, verbose_name='URL-название')

    def __str__(self):
        return f"{self.name_service}"

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class TimeSlot(models.Model):
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")

    def __str__(self):
        return f"{self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')}"

    class Meta:
        verbose_name = "Интервал времени"
        verbose_name_plural = "Интервалы времени"


class OrderService(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True,
                                         verbose_name='Дата создания',
                                         )
    name_service = models.ForeignKey(ServicePrice,
                                     on_delete=models.SET_NULL,
                                     verbose_name='Услуга',
                                     related_name='order_service',
                                     null=True,
                                     )
    number_counters = models.IntegerField(verbose_name='Количество счетчиков', null=True, blank=True)
    service_date = models.DateField(verbose_name='Дата выполнения услуги', null=True, blank=True)
    time_slot = models.ForeignKey(TimeSlot,
                                  on_delete=models.SET_NULL,
                                  verbose_name="Время выполнения услуги",
                                  null=True,
                                  blank=True,
                                  )
    address = models.CharField(max_length=100,
                               verbose_name='Введите адрес',
                               blank=True,
                               null=True
                               )
    phone_number = models.CharField(max_length=20,
                                    verbose_name="Номер телефона",
                                    )
    client_name = models.CharField(max_length=100,
                                   verbose_name='Ваше имя',
                                   )

    class Meta:
        verbose_name = "Заявка на услугу"
        verbose_name_plural = "Заявки на услугу"
        ordering = ['-creation_date']


class County(models.Model):
    name_county = models.CharField(verbose_name='Округ', max_length=50)
    full_name_county = models.CharField(verbose_name='Полное название округа', max_length=50, blank=True)
    slug = models.CharField(max_length=50, db_index=True, verbose_name='URL-название')

    def __str__(self):
        return f'{self.name_county}'

    class Meta:
        verbose_name = "Округ"
        verbose_name_plural = "Округа"
        ordering = ['-name_county']


class WaterMeter(models.Model):
    name_meter = models.CharField(verbose_name='Название счетчика', max_length=50, null=True, blank=True)
    name_model = models.CharField(verbose_name='Модель счетчика', max_length=50, null=True, blank=True)
    country_origin = models.CharField(verbose_name='Страна производства', max_length=50, null=True, blank=True)
    factory_manufacturer = models.CharField(verbose_name='Завод производитель', max_length=100, null=True, blank=True)
    length_installation = models.DecimalField(verbose_name='Установочная длина', max_digits=5, decimal_places=2, null=True, blank=True)
    nominal_diameter = models.DecimalField(verbose_name='Условный диаметр', max_digits=5, decimal_places=2, null=True, blank=True)
    pulse_output = models.IntegerField(verbose_name='Импульсный выход', choices=[(0, 'Нет'), (1, 'Да')], default=0, null=True, blank=True)
    fittings_included = models.IntegerField(verbose_name='Сгоны в комплекте', choices=[(0, 'Нет'), (1, 'Да')], default=0, null=True, blank=True)
    service_life = models.IntegerField(verbose_name='Срок службы', null=True, blank=True)
    guarantee = models.IntegerField(verbose_name='Гарантия от завода', null=True, blank=True)
    verification_method = models.CharField(verbose_name='Методика поверки', max_length=30, null=True, blank=True)
    cold_verification_interval = models.IntegerField(verbose_name='Поверочный интервал ХВС', null=True, blank=True)
    hot_verification_interval = models.IntegerField(verbose_name='Поверочный интервал ГВС', null=True, blank=True)
    register_number = models.CharField(verbose_name='Номер в реестре', max_length=10, null=True, blank=True)
    price_meter = models.DecimalField(verbose_name='Цена счетчика', max_digits=10, decimal_places=2, null=True, blank=True)
    price_meter_replacement = models.DecimalField(verbose_name='Цена счетчика с заменой', max_digits=10, decimal_places=2, null=True, blank=True)
    price_meter_installation = models.DecimalField(verbose_name='Цена счетчика с установкой', max_digits=10, decimal_places=2, null=True, blank=True)
    images_meter = models.ImageField(verbose_name='Изображение счетчика', upload_to="images_meters", default=None, null=True, blank=True)

    def __str__(self):
        return f'{self.name_meter}'

    class Meta:
        verbose_name = "Счетчик воды"
        verbose_name_plural = "Счетчики воды"