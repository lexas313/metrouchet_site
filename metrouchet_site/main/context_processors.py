from .forms import CallBackForm, OrderServiceForm

def form_context(request):
    return {
        'call_back_form': CallBackForm(),
        'order_service_form': OrderServiceForm(),
    }