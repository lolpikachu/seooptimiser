from django import forms

class LinksForm(forms.Form):
    link = forms.CharField(label='Вставьте ссылку', max_length=100)
    keyword = forms.CharField(label='Вставьте ключевое слово', max_length=100)

# class KeywordForm(forms.Form):
#     keyword = forms.CharField(label='Add the keywords separated by the comma', max_length=150)