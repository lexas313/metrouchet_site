from django import forms
from django.core.exceptions import ValidationError

from main.models import CallBack, OrderService, TimeSlot
from re import match

def validate_russian_characters(value):
    if not match(r'^[А-Яа-яЁё\s]+$', value):
        raise ValidationError('Только символы кириллицы.')


class CallBackForm(forms.ModelForm):
    privacy_policy = forms.BooleanField(label='Я согласен с политикой конфиденциальности', initial=True, required=True)
    phone_number = forms.CharField(label='Номер телефона',
                                   max_length=18,
                                   min_length=18,
                                   widget=forms.TextInput(attrs={'placeholder': '+7 ('}),
                                   error_messages={'max_length': 'Проверьте номер телефона.',
                                                   'min_length': 'Проверьте номер телефона.'
                                                   }
                                   )
    client_name = forms.CharField(label='Ваше имя',
                                  max_length=100,
                                  validators=[validate_russian_characters]
                                  )

    class Meta:
        model = CallBack
        fields = ('question', 'phone_number', 'client_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name not in ['privacy_policy']:
                field.widget.attrs['class'] = 'form-input'


class OrderServiceForm(forms.ModelForm):
    privacy_policy = forms.BooleanField(label='Я согласен с политикой конфиденциальности', initial=True, required=True)
    service_date = forms.DateField(label='Выберите дату', required=False,
                                   widget=forms.DateInput())
    time_slot = forms.ModelChoiceField(queryset=TimeSlot.objects.all(), label='Выберите время', required=False,
                                       widget=forms.RadioSelect(attrs={'class': 'radio-button'}))
    phone_number = forms.CharField(label='Номер телефона',
                                   max_length=18,
                                   min_length=18,
                                   widget=forms.TextInput(attrs={'placeholder': '+7 ('}),
                                   error_messages={'max_length': 'Проверьте номер телефона.',
                                                   'min_length': 'Проверьте номер телефона.'
                                                   }
                                   )
    client_name = forms.CharField(label='Ваше имя',
                                  max_length=100,
                                  validators=[validate_russian_characters]
                                  )

    class Meta:
        model = OrderService
        fields = (
        'name_service', 'number_counters', 'service_date', 'time_slot', 'address', 'phone_number', 'client_name')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Применяем классы к полям формы, кроме `privacy_policy` и `time_slot`
        for name, field in self.fields.items():
            if name not in ['privacy_policy', 'time_slot', 'service_date']:
                field.widget.attrs['class'] = 'form-input'