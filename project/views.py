# Create your views here.
from django.views.generic import ListView
from project.models import Project
from django.contrib.auth.models import User


class ProjectView(ListView):
    model = Project
    template_name = "index.html"
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)
        context['users'] = User.objects.filter(userprofile__isnull=False)
        return context