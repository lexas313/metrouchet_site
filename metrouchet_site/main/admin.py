from django.contrib import admin

from main.models import CallBack, ServicePrice, TimeSlot, OrderService, County, WaterMeter


@admin.register(CallBack)
class CallBackAdmin(admin.ModelAdmin):
    fields = ('creation_date', 'question', 'phone_number', 'client_name')
    readonly_fields = ('creation_date', )
    list_display = ('question', 'phone_number', 'client_name', 'creation_date')
    list_display_links = ('question', 'phone_number', 'client_name', 'creation_date')
    search_fields = ('id', 'question', 'phone_number', 'client_name', 'creation_date')
    list_filter = ('question', )
    list_per_page = 20


@admin.register(ServicePrice)
class ServicePriceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_service',)}
    list_display = ('name_service', 'price')
    list_display_links = ('name_service', 'price')
    list_per_page = 20


@admin.register(TimeSlot)
class TimeSlotPriceAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'end_time')
    list_display_links = ('start_time', 'end_time')


@admin.register(OrderService)
class OrderServicePriceAdmin(admin.ModelAdmin):
    fields = ('creation_date', 'name_service', 'number_counters', 'service_date', 'time_slot', 'address', 'phone_number', 'client_name')
    readonly_fields = ('creation_date',)
    list_display = ('name_service', 'service_date', 'time_slot', 'address', 'phone_number', 'client_name', 'creation_date')
    list_display_links = ('name_service', 'service_date', 'time_slot', 'address', 'phone_number', 'client_name', 'creation_date')
    search_fields = ('id', 'name_service__name_service', 'service_date', 'address', 'phone_number', 'client_name')
    list_filter = ('name_service', 'service_date')
    list_per_page = 20


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name_county',)}
    list_display = ('name_county', 'full_name_county')
    list_display_links = ('name_county', 'full_name_county')
    list_per_page = 20


@admin.register(WaterMeter)
class WaterMeterAdmin(admin.ModelAdmin):
    list_display = ('name_meter', 'name_model', 'length_installation', 'nominal_diameter', 'pulse_output')
    list_display_links = ('name_meter', 'name_model', 'length_installation', 'nominal_diameter', 'pulse_output')
    list_per_page = 20