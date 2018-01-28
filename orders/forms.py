from django import forms
from django.contrib.auth import get_user_model
from .models import UserAddress
User = get_user_model()

class GuestCheckoutForm(forms.Form):
	email = forms.EmailField()
	email2 = forms.EmailField(label='Verify Email')

	def clean_email2(self):
		email = self.cleaned_data.get("email")
		email2 = self.cleaned_data.get("email2")

		if email == email2:
			if User.objects.filter(email=email).count() != 0:
				raise forms.ValidationError("This User already exists. Please login instead.")
			return email2
		else:
			raise forms.ValidationError("Please confirm emails are the same")
# DATA should contain these keys
#     amount           : amount of order
#     currency         : currency of order
#     receipt          : receipt id of order
#     payment_capture  : 1 if capture should be done automatically or else 0
#     notes(optional)  : optional notes for order
# class PaymentForm(forms.Form):
# 	amount = forms.DecimalField(decimal_places=2)



class AddressForm(forms.Form):
    billing_address = forms.ModelChoiceField(queryset=UserAddress.objects.filter(type="billing"),empty_label=None,widget=forms.RadioSelect)
    shipping_address = forms.ModelChoiceField(queryset=UserAddress.objects.filter(type="shipping"),empty_label=None,widget=forms.RadioSelect)

class UserAddressForm(forms.Form):
	class Meta:
		model = UserAddress
		fields = [
			'street',
			'state',
			'zipcode',
			'type'
		]
