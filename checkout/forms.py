from django import forms
from django.core.validators import RegexValidator
from .models import Order


class OrderForm(forms.ModelForm):
    phone_number = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message=(
                    "Phone number must be in the format: '+999999999'. "
                    "Must be between 10-15 digits."
                )
            ),
        ],
        required=False
    )

    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number:
            # Remove any non-digit characters
            phone_number = ''.join(filter(str.isdigit, phone_number))
            # Ensure the phone number has at least 10 digits
            if len(phone_number) < 10:
                raise forms.ValidationError(
                    "Phone number must be between 10 and 15 digits.")
        return phone_number
