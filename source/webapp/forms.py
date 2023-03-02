from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'type')
        labels = {
            'title': 'Заголовок задачи',
            'description': 'Описание задачи',
            'status': 'Статус',
            'type': 'Тип'
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длинее 2-ух символов')
        return title
