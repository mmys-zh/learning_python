from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 模型告诉Django如何处理应用程序中存储的数据
# 在代码层面，模型就是一个类

#
#定义模型Topic
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200) #由字符或文本组成的数据
    data_added = models.DateTimeField(auto_now_add=True) #记录日期和时间的数据
    owner = models.ForeignKey(User,on_delete=models.CASCADE,null=True) #使模型建立到与模型User的外键关系,可以设置为空

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
        #__str__()来显示模型的简单表示，【python2.7使用__unicode__()方法】
    
#
#定义模型Entry
class Entry(models.Model):
    """学到的有关某个主题的具体知识"""
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)  #外键
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta存储用于管理模型的额外信息"""
        verbose_name_plural = 'entries'
    
    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50]+"..."
    # P384