from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from django import forms

from .models import Comment, Post


class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'username')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class PostForm(forms.ModelForm):
    pub_date = forms.DateTimeField(
        label='Дата и время публикации',
        input_formats=['%d.%m.%Y'],
        widget=forms.DateTimeInput(
            format='%d.%m.%Y %H:%M:%S',
            attrs={
                'placeholder': 'ДД.ММ.ГГГГ ЧЧ:ММ:СС',
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = Post
        fields = ['title', 'text', 'pub_date', 'category', 'location', 'image']
