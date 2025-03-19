from django import forms


PRODUCT_CHOICES = [(i, str(i)) for i in range(1, 11)]


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.HiddenInput())
