from django import template


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
