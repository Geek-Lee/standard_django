# standard_django
Django从无到有

普通评论
从实例化article中查找comment（对外叫under_comments）
{% for comment in article.under_comments.all %}

优秀评论
从实例化comment中筛选best_comment
{% if best_comment %}

提交评论的form验证视图和整个页面的视图分离
各分配一个url
form验证视图的url：url(r'^detail/(?P<page_num>\d+)/comment$', detail_comment, name="comment")
整个页面的视图的url：url(r'^detail/(?P<page_num>\d+)$', detail_comment, name="comment")