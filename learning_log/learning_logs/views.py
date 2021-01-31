#render()函数根据视图提供的数据渲染响应
from django.shortcuts import render
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse

# 导入与所需数据相关联的模型
from .models import Topic,Entry
from .forms import TopicForm,EntryForm

# 导入装饰器
from django.contrib.auth.decorators import login_required

# Create your views here.
# 主页
def index(request):
    """学习笔记的主页"""
    return render(request,'learning_logs/index.html')

#限制对topics页面的访问
@login_required()
# 所有主题页
def topics(request):
    """显示所有主题页"""
    # topics = Topic.objects.order_by('date_added') #查询数据库操作
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # 从数据仓库中只获取owner属性为当前用户名的Topics对象
    context = {'topics':topics} #发送给模板的上下文
    return render(request,'learning_logs/topics.html',context)

#限制对topic页面的访问
@login_required()
# 特定主题页
def topic(request,topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id) #查询数据库操作

    # 确认请求的主题属于当前用户
    # if topic.owner != request.user:
    #     raise Http404
    check_topic_owner(topic,request)

    entries = topic.entry_set.order_by('-data_added')
    context = {'topic':topic,'entries':entries} #发送给模板的上下文
    return render(request,'learning_logs/topic.html',context)

#限制对主题页面的访问
@login_required()
# 添加主题页
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
# from .forms import TopicForm
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user #将新主题关联到当前用户
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
            
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)

#限制对添加新条目页面的访问
@login_required()
#添加新条目
def new_entry(request,topic_id):
    """在特定作主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    
    check_topic_owner(topic,request)

    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            # 传递实参commit=False，让django创建一个新的条目对象，并将其存储到new_entry中，但不将其保存到数据库中
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic_id]))
            
    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

#限制对编辑新条目页面的访问
@login_required()
#编辑条目
def edit_entry(request,entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    # 保护页面不被输入URL直接访问
    # if topic.owner != request.user:
    #     raise Http404
    check_topic_owner(topic,request)

    if request.method != 'POST':
        # 初始请求，使用当前条目填充菜单
        form = EntryForm(instance=entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
            
    context = {'entry':entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)


# 函数
def check_topic_owner(t,req):
    """验证用户信息"""
    if t.owner != req.user:
        raise Http404