"""定义learning_logs的URL模式"""

# 导入url函数，使用它来将URL映射到视图
from django.conf.urls import url

# 导入模块views,句点让python从当前的urls.py模块所在的文件夹中导入视图
from . import views

urlpatterns = [
    #主页
    url(r'^$',views.index,name='index'),
    #显示所有的主题
    url(r'^topics/$',views.topics,name='topics'),
    #显示特定主题的详情页面
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    #添加主题页面
    url(r'^new_topic/$',views.new_topic,name='new_topic'),
    # 添加条目页面
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    # 编辑条目页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name='edit_entry')
]
# 实际的url模式是一个对函数url()的调用，这个函数接收三个实参
    # -一个正则表达式  定义了django可查找的模式
    # -指定了要调用的视图函数
    # -指定这个URL模式的别名，能在代码的其他地方引用它