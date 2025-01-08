from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    RATING_CHOICES = [
        (i, str(i)) for i in range(1, 6)
    ]  # Choices for 1 to 5 stars

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        label='Rating',
        initial=5,
        required=True
    )

    class Meta:
        model = Review
        fields = ('rating', 'comment')
