from django import template
from django.contrib.auth.models import User
from apps.tenda import auth_groups

register = template.Library()


@register.inclusion_tag('tags/login_form_fields.html')
def login_form_field(field, hide_label=False):
    field.field.widget.attrs.update({"data-test-field": field.label})
    field.field.widget.attrs.update({'class': 'form-control'})
    return {
        'field': field,
        'hide_label': hide_label
    }


@register.inclusion_tag('tags/non_field_errors.html')
def non_field_errors(form):
    return {'form': form}


# Auth Membership Check
def _is_member(user, group_name):
    """
    Returns True if the given User object is a member of a group with the given name.
    Please choose the names from the reobst.settings.auth_groups constants.
    :type group_name: basestring
    :type user: django.contrib.auth.User
    """
    if isinstance(user, User):
        return user.groups.filter(name=group_name).exists()

    return False


@register.filter(name='is_super_admin')
def is_super_admin(u):
    return _is_member(u, auth_groups.SUPER_ADMIN)


@register.filter(name='is_ecoxarxa_admin')
def is_ecoxarxa_admin(u):
    return _is_member(u, auth_groups.XARXA_ADMIN)


@register.filter(name='is_rebost_admin')
def is_rebost_admin(u):
    return _is_member(u, auth_groups.REBOST_ADMIN)
