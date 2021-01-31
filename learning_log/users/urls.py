"""为users APP定义URL模式"""

from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    #登录页面
    # 这里的login是视图函数
    url(r'^login/$',LoginView,{'tempalte_name':'users/login.html'},name='login'),
    #注销按钮
    url(r'^logout/$',views.logout_view,name='logout'),
    #注册页面
    url(r'^register/$',views.register,name='register'),
]