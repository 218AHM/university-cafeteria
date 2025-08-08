from django import forms
from cafeteria.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name']
        widgets = {
            'customer_name': forms.TextInput(attrs={
                'placeholder': 'Your Name',
                'class': 'input-name'
            }),
        }
        
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request", None)
        super().__init__(*args, **kwargs)
        if self.request and self.request.user.is_authenticated:
            for f in ["customer_name", "customer_id"]:
                self.fields.pop(f, None)


class QuantityForm(forms.Form):
    def __init__(self, *args, food_items=None, **kwargs):
        super().__init__(*args, **kwargs)
        if food_items:
            for item in food_items:
                self.fields[f'qty_{item.food_item_id}'] = forms.IntegerField(
                    min_value=0,
                    required=False,
                    initial=0,
                    widget=forms.NumberInput(attrs={
                        'class': 'qty-input',
                        'min': '0',
                        'step': '1'
                    })
                )