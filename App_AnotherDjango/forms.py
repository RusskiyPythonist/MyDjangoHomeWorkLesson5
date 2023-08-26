from django import forms
from .models import Advertisement
from django.core.exceptions import ValidationError

# class AdvForm(forms.Form):
#     title = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': 'form-control-lg'}))
#     text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
#     price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
#     auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
#     image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))

class AdvForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 1 дз
        # print(self.fields)
        self.fields['title'].widget.attrs['class'] = "form-control-lg"
        self.fields['text'].widget.attrs['class'] = "form-control-lg"
        self.fields['price'].widget.attrs['class'] = "form-control-lg"
        self.fields['auction'].widget.attrs['class'] = "form-check-input"
        self.fields['image'].widget.attrs['class'] = "form-control-lg"

    class Meta:
        model = Advertisement
        fields = ['title', 'text', 'price', 'auction', 'image']

    # 2дз
    def clean_title(self):
        title = self.cleaned_data['title']  # извлек название из данных пользователя
        if title.startswith('?'):  # проверяю что начинеается с ?
            raise ValidationError("Название не может начинаться с ?")
        return title  # если не ? то возвращаю title обратно
