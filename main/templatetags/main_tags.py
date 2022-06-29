from django import template

from main.models import Comment

register = template.Library()


@register.simple_tag
def get_comments(qs=5):
    return Comment.objects.all()