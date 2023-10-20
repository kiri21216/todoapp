from .models import Task
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        self.fields['timeField'].initial = 0
        self.fields['minutes'].initial = 0

    model = Task
    title = forms.CharField(max_length=30, label='タイトル', error_messages={"required": "30文字以内に納めてください"})
    description = forms.CharField(max_length=100, label='内容', error_messages={"required": "100文字以内に納めてください"})
    completed = forms.BooleanField(required=False, label='完了')
    timeField = forms.IntegerField(initial=0, label='所要時間', help_text='時間')
    minutes = forms.IntegerField(initial=0, label='', help_text='分')

    class Meta:
        model = Task
        fields = ["title", "description", "timeField", "minutes"]

class UpForm(forms.ModelForm):

    model = Task
    title = forms.CharField(max_length=30, label='タイトル', error_messages={"required": "30文字以内に納めてください"})
    description = forms.CharField(max_length=100, label='内容', error_messages={"required": "100文字以内に納めてください"})
    completed = forms.BooleanField(required=False, label='完了')
    timeField = forms.IntegerField(initial=0, label='所要時間', help_text='時間')
    minutes = forms.IntegerField(initial=0, label='', help_text='分')

    class Meta:
        model = Task
        fields = ["title", "description", "timeField", "minutes", "completed"]
