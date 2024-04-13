from django import forms
from .models import Notes


class NewNoteForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'content']
        labels = {
            'title': 'Заголовок',  # Изменяем отображаемое имя поля title на "Заголовок"
            'content': 'Содержание'
        }