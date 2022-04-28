from django import template

register = template.Library()


@register.filter
def display_rating(rating_count):
    html = ""
    count = 5-rating_count
    
    for i in range(rating_count):
        html += '<span class="fa fa-star active"></span>'
    for i in range(count):
        html += '<span class="fa fa-star"></span>'
        
    html += f'<span class="rounded bg-warning text-dark pl-1 pr-1">5/{rating_count}</span>'
    
    return html