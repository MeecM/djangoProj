from django.shortcuts import render
from django.views.generic import TemplateView  # new added


def home_page_view(request):
    context = {
        "inventory_list": ["Wiget 1", "Widget 2", "Widget 3"],
        "greeting": "THank you FOR VisitING",
    }
    return render(request, "home.html", context)


class AboutPageView(TemplateView):  # new
    template_name = "about.html"

    def get_context_data(self, **kwags):
        context = super().get_context_data(**kwags)
        context["contact_address"] = "123 main"
        context["phone_number"] = "555-555-5555"
        return context
