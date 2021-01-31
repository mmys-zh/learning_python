from django.contrib import admin

# Register your models here.

# 导入要注册的模型topic
from learning_logs.models import Topic,Entry


# 在管理网站中注册模型
admin.site.register(Topic)
admin.site.register(Entry)