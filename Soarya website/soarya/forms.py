from django import forms


class ContactForm(forms.Form):
    message = forms.CharField(max_length=1000)
    email = forms.EmailField(max_length = 254)
    name = forms.CharField(max_length=128,required=False)

class CommentForm(forms.Form):
    content = forms.CharField(max_length=2048)  # comment
    score = forms.IntegerField()
    difficulty = forms.IntegerField()