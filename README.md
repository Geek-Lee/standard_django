# standard_django
Django从无到有

普通评论
从实例化article中查找comment（对外叫under_comments）
{% for comment in article.under_comments.all %}

优秀评论
从实例化comment中筛选best_comment
{% if best_comment %}