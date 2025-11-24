from django import forms


class ContactForm(forms.Form):
    sender = forms.EmailField(label="Sender Email", max_length=254)
    subject = forms.CharField(max_length=255)
    message = forms.CharField(widget=forms.Textarea)
