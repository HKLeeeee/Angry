from django.forms import ModelForm
from commu.models import Board
from django import forms


class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['b_title', 'b_content']

        labels = {
            'b_title': '글 제목',
            'b_content': '글 내용'
        }
        widgets = {
            'b_title': forms.TextInput(
                attrs={
                    'class': 'form-control w-50',
                    'placeholder': '제목을 써주세요'
                }
            ),
            'b_content': forms.Textarea(
                attrs={
                    'class': 'form-control w-75',
                    'placeholder': '내용을 써주세요'
                }
            )
        }


class BoardDetailForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = "__all__"
        labels={
            'b_title': '글 제목',
            'b_author': '글 작성자',
            'b_content': '글 내용',
            'b_like': '좋아요',
            'b_date': '게시 날짜'
        }
