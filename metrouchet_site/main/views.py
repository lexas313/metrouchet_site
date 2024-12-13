import asyncio
import telegram
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import View
from django.views.generic import CreateView, FormView
from main.forms import CallBackForm, OrderServiceForm
from main.models import CallBack, County, WaterMeter, ServicePrice
from django.conf import settings
from re import sub

# Телеграм бот
async def send_telegram_message(message):
    if settings.TELEGRAM_BOT_TOKEN and settings.TELEGRAM_CHAT_ID:
        bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)
        await bot.send_message(chat_id=settings.TELEGRAM_CHAT_ID, text=message)


class Index(View):
    def get(self, request, *args, **kwargs):
        county_list = County.objects.all().order_by('name_county')
        county = None
        slug = self.kwargs.get('slug')  # Получаем значение slug
        page_title = 'Поверка и обслуживание счетчиков воды в Москве'
        header_title = 'Поверка и обслуживание счетчиков воды в '
        service_prices = ServicePrice.objects.all()
        price = next((int(sp.price) for sp in service_prices if sp.slug == 'poverka-schetchikov-vody'), None)

        # Если нужно в форму установить услугу соответствующей страницы по умолчанию
        # service = ServicePrice.objects.filter(slug='poverka-schetchikov-vody').first()
        # if service:
        #     order_service_form = OrderServiceForm(initial={'name_service': service.id})
        #     call_back_form = CallBackForm(initial={'name_service': service.id})
        # else:
        #     order_service_form = OrderServiceForm()
        #     call_back_form = CallBackForm()


        if slug:  # Проверяем, был ли передан slug
            county = get_object_or_404(County, slug=slug)
            page_title = f'Поверка и обслуживание счетчиков воды в {county.name_county}'
            header_title = 'Поверка и обслуживание счетчиков воды в '

        context = {'county_list': county_list,
                   'county': county,
                   'page_title': page_title,
                   'header_title': header_title,
                   'price': price,
                   'price_2': f'Стоимость поверки от {price}р',
                   'service_prices': service_prices,
                   # 'order_service_form': order_service_form,
                   # 'call_back_form': call_back_form,
                   }

        return render(request, 'main/index.html', context)


class PoverkaVody(View):
    def get(self, request, *args, **kwargs):
        county_list = County.objects.all().order_by('name_county')
        county = None
        slug = self.kwargs.get('slug')  # Получаем значение slug
        header_title = 'Поверка счетчиков воды в '
        service_prices = ServicePrice.objects.all()
        price = next((int(sp.price) for sp in service_prices if sp.slug == 'poverka-schetchikov-vody'), None)
        page_title = f'Поверка счетчиков воды в Москве от {price}р'

        if slug:  # Проверяем, был ли передан slug
            county = get_object_or_404(County, slug=slug)
            page_title = f'Поверка счетчиков воды в {county.name_county} от {price}р'
            header_title = 'Поверка счетчиков воды в '

        context = {'county_list': county_list,
                   'county': county,
                   'page_title': page_title,
                   'header_title': header_title,
                   'price': price,
                   'price_2': f'Стоимость поверки от {price}р',
                   'service_prices': service_prices,
                   }
        return render(
            request,
            'main/poverka_schetchikov_vody.html',
            context
        )


class ZamenaVody(View):
    def get(self, request, *args, **kwargs):
        county_list = County.objects.all().order_by('name_county')
        county = None
        slug = self.kwargs.get('slug')  # Получаем значение slug
        header_title = 'Замена счетчиков воды в '
        water_meter = WaterMeter.objects.all()
        service_prices = ServicePrice.objects.all()
        price = next((int(sp.price) for sp in service_prices if sp.slug == 'zamena-schetchikov-vody'), None)
        page_title = f'Замена счетчиков воды в Москве от {price}р'

        if slug:  # Проверяем, был ли передан slug
            county = get_object_or_404(County, slug=slug)
            page_title = f'Замена счетчиков воды в {county.name_county} от {price}р'
            header_title = 'Замена счетчиков воды в '

        context = {'county_list': county_list,
                   'county': county,
                   'page_title': page_title,
                   'header_title': header_title,
                   'water_meter': water_meter,
                   'price': price,
                   'price_2': f'Стоимость замены от {price}р',
                   'service_prices': service_prices,
                   }
        return render(
            request,
            'main/zamena_schetchikov_vody.html',
            context
        )


class UstanovkaVody(View):
    def get(self, request, *args, **kwargs):
        county_list = County.objects.all().order_by('name_county')
        county = None
        slug = self.kwargs.get('slug')  # Получаем значение slug
        header_title = 'Установка счетчиков воды в '
        water_meter = WaterMeter.objects.all()
        service_prices = ServicePrice.objects.all()
        price = next((int(sp.price) for sp in service_prices if sp.slug == 'ustanovka-schetchikov-vody'), None)
        page_title = f'Установка счетчиков воды в Москве от {price}р'

        if slug:  # Проверяем, был ли передан slug
            county = get_object_or_404(County, slug=slug)
            page_title = f'Установка счетчиков воды в {county.name_county} от {price}р'
            header_title = 'Установка счетчиков воды в '

        context = {'county_list': county_list,
                   'county': county,
                   'page_title': page_title,
                   'header_title': header_title,
                   'water_meter': water_meter,
                   'price': price,
                   'price_2': f'Стоимость установки от {price}р',
                   'service_prices': service_prices,
                   }
        return render(
            request,
            'main/ustanovka_schetchikov_vody.html',
            context
        )


class OrderServiceFormView(View):
    def post(self, request, *args, **kwargs):
        form = OrderServiceForm(request.POST)
        if form.is_valid():
            order_service = form.save()

            # Отправить уведомление в Telegram

            # Если нужно отправлять дату и время сохранения формы
            # creation_date = timezone.localtime(order_service.creation_date)
            # creation_date_str = creation_date.strftime('%d.%m.%Y %H:%M:%S')
            name_service = order_service.name_service
            number_counters = order_service.number_counters
            service_date = order_service.service_date.strftime('%d.%m.%Y')
            time_slot = order_service.time_slot
            address = order_service.address
            phone_number = order_service.phone_number
            clean_phone_number = sub(r'[^+\d]', '', phone_number)
            client_name = order_service.client_name
            message = f'Заявка на услугу\n{name_service}\nКол-во сч. {number_counters}\nНа {service_date} {time_slot}\nАдрес: {address}\n{clean_phone_number} - {client_name}'
            asyncio.run(send_telegram_message(message))  # Вызываем асинхронную функцию внутри asyncio.run

            return JsonResponse({'success': True, 'message': 'Форма успешно отправлена'}, status=200)
        else:
            # Формируем ошибки по полям
            errors = {field: error.get_json_data(escape_html=True) for field, error in form.errors.items()}

            return JsonResponse({'success': False, 'errors': errors}, status=400)


class CallBackFormView(View):
    def post(self, request, *args, **kwargs):
        form = CallBackForm(request.POST)
        if form.is_valid():
            call_back = form.save()

            # Отправить уведомление в Telegram

            # Если нужно отправлять дату и время сохранения формы
            # creation_date = timezone.localtime(call_back.creation_date)
            # creation_date_str = creation_date.strftime('%d.%m.%Y %H:%M:%S')

            question_text = call_back.get_question_display()
            phone_number = call_back.phone_number
            clean_phone_number = sub(r'[^+\d]', '', phone_number)
            client_name = call_back.client_name
            message = f'Заявка на обратный звонок\nВопрос по: {question_text}\n{clean_phone_number} - {client_name}'
            asyncio.run(send_telegram_message(message))  # Вызываем асинхронную функцию внутри asyncio.run

            return JsonResponse({'success': True, 'message': 'Форма успешно отправлена'}, status=200)
        else:
            # Формируем ошибки по полям
            errors = {field: error.get_json_data(escape_html=True) for field, error in form.errors.items()}

            return JsonResponse({'success': False, 'errors': errors}, status=400)










# Для обработки форм не через Ajax
# class Index(View):
#     def get(self, request, *args, **kwargs):
#         return self.render_with_forms(
#             request,  # Передаем request в render_with_forms
#             call_back_form=CallBackForm(),
#             order_service_form=OrderServiceForm()
#         )
#
#     def post(self, request, *args, **kwargs):
#         if 'call_back_form_submit' in request.POST:
#             return self.handle_call_back_form(request)
#         elif 'order_service_form_submit' in request.POST:
#             return self.handle_order_service_form(request)
#         return self.get(request)
#
#     def handle_call_back_form(self, request):
#         form = CallBackForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Заявка успешно отправлена!')
#             return self.render_with_forms(request, call_back_form=None, scroll_to_form='callback-form-block-id')
#         else:
#             messages.error(request, 'Пожалуйста, исправьте ошибки в форме обратной связи.')
#             return self.render_with_forms(request, call_back_form=form, scroll_to_form='callback-form-block-id')
#
#     def handle_order_service_form(self, request):
#         form = OrderServiceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Другая форма успешно отправлена!')
#             return self.render_with_forms(request, order_service_form=None, scroll_to_form='another-form-block-id')
#         else:
#             messages.error(request, 'Пожалуйста, исправьте ошибки в другой форме.')
#             return self.render_with_forms(request, order_service_form=form, scroll_to_form='another-form-block-id')
#
#     def render_with_forms(self, request, call_back_form=None, order_service_form=None, scroll_to_form=None):
#         return render(request, 'main/index.html', {
#             'call_back_form': call_back_form or CallBackForm(),
#             'order_service_form': order_service_form or OrderServiceForm(),
#             'scroll_to_form': scroll_to_form  # Уникальный ID формы для прокрутки
#         })