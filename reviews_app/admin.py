
from django.contrib import admin
from .models import *

admin.site.register(User)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    fields=("author", "rating", "text", "date_created", "published")
    readonly_fields=('published',)
    change_form_template = "change_form.html"

    def response_change(self, request, obj):
        opts = self.model._meta
        pk_value = obj._get_pk_val()
        preserved_filters = self.get_preserved_filters(request)

        if "_customaction" in request.POST:
            # handle the action on your obj
            redirect_url = reverse('admin:%s_%s_change' %(opts.app_label, opts.model_name), args=(pk_value,), current_app=self.admin_site.name)
            redirect_url = add_preserved_filters({'preserved_filters': preserved_filters, 'opts': opts}, redirect_url)
            return HttpResponseRedirect(redirect_url)
        else:
            return super(ReviewAdmin, self).response_change(request, obj)

