from django.core.validators import RegexValidator
from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    default_phone_number = forms.CharField(
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
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = (
                'border-black profile-form-input'
            )
            self.fields[field].label = False

    def clean_default_phone_number(self):
        phone_number = self.cleaned_data.get('default_phone_number')
        if phone_number:
            # Remove any non-digit characters
            phone_number = ''.join(filter(str.isdigit, phone_number))

            # Check if the phone number has a valid length
            if len(phone_number) < 10 or len(phone_number) > 15:
                raise forms.ValidationError(
                    "Phone number must be between 10 and 15 digits.")

        return phone_number
