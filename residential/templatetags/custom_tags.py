from django import template

register = template.Library()
@register.simple_tag
def get_photo_for_flat(images, flat_id):
    filtered_images = images.filter(flat_id=flat_id)
    if filtered_images.exists():
        return filtered_images[0].img.url
    else:
        return None
