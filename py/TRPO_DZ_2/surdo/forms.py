from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)


class TaskAddForm(forms.Form):
    author_id = forms.IntegerField(label='ID автора')
    title = forms.CharField(max_length=100, label='Название задания')
    text = forms.CharField(widget=forms.Textarea, label='Текст задания')
