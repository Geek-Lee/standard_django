from django.shortcuts import render, HttpResponse, redirect
from firstapp.models import Article, Comment
from django.template import Context, Template
from firstapp.form import CommentForm

# Create your views here.
def index(request):
    queryset = request.GET.get('tag')
    if queryset:
        article_list = Article.objects.filter(tag=queryset)
    else:
        article_list = Article.objects.all()
    context = {}
    context['article_list'] = article_list
    index_page = render(request, 'first_web_2.html', context)
    return index_page

def detail(request, page_num):#新增page_num参数
    if request.method == "GET":
        form = CommentForm
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            a = Article.objects.get(id=page_num)
            # 实例化id=page_num的文章
            c = Comment(name=name, comment=comment, belong_to=a)
            # 实例化评论（归属于文章a）
            c.save()
            return redirect(to='detail', page_num=page_num)
            # 重定向到page_num页的文章
    context = {}
    article = Article.objects.get(id=page_num)#从数据库中找到id=page_num的文章
    best_comment = Comment.objects.filter(best_comment=True, belong_to=article)
    # 在评论中筛选评论属性best_comment为True，从属于article的的评论
    # best_comment=models.BooleanField(default=True)【勾选为best_comment的评论】<=============等价于============>best_comment=True
    context['article'] = article#装入context上下文中
    context['form'] = form
    if best_comment:
        context['best_comment'] = best_comment[0]
    #如果有best_comment，则挑选第一个best_comment
    #print(context)#{'article': <Article: A Rose For Marly>, 'form': <class 'firstapp.form.CommentForm'>}
    #print(type(context))#<class 'dict'>
    return render(request, 'article_detail.html', context)