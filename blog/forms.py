from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from .models_posts import PostComment
from .models_questions import Question, QuestionComment

class PostCommentForm(forms.ModelForm):
	class Meta:
		model = PostComment
		fields = ('name', 'email', 'body')

		widgets = {
			'body': SummernoteWidget()
		}

class QuestionCommentForm(forms.ModelForm):
	class Meta:
		model = QuestionComment
		fields = ('name', 'email', 'body')

		widgets = {
			'body': SummernoteWidget()
		}

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('name', 'email', 'category', 'content')

		widgets = {
			'content': SummernoteWidget()
		}