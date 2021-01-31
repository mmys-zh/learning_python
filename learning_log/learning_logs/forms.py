from django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    """用于添加新主题"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text':''}

# 最简单的ModelForm版本只包含一个内嵌的Meta类，它告诉django根据那个模型创建表单，以及在表单中包含哪些字段

class EntryForm(forms.ModelForm):
    """用于添加新条目"""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        widgets = {'text':forms.Textarea(attrs={'cols':80})}
        # 通过设置属性widgets，可覆盖django选择的默认小部件