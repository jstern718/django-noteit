from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db import models
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone

from .models import Note, User
from .forms import Note_form


def MessageView(x):
    return HttpResponse("Hello World!")


class IndexView(generic.ListView):
    print("index")
    template_name = "noteit/index.html"
    context_object_name = "latest_note_list"

    def get_queryset(self):
        print("objects", Note.objects.all())
        """Return the last five published questions."""

        return Note.objects.filter(updated_at__lte=timezone.now()).order_by(
            "-updated_at")[
            :5
        ]

    def format_date(old_date):
        return old_date.strftime("%H:%M:%S")


class NewNoteView(generic.CreateView):
    model = Note
    form_class = Note_form
    initial = {'title': '', 'content': ''}
    template_name = "noteit/new_note.html"

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {"form": form})

    # def post(self, request):
    #     form = self.form_class(request.POST)
    #     return render(request, self.template_name, {"form": form})

    # def form_valid(self, form):
    #     u = User.objects.get(username='admin')
    #     form.instance.user = u
    #     return super().form_valid(form)

    # new = Note(user=u)
    # new.save()
    # new_id = new.id
    # print("new_id", new_id)
    # print("new title", new.title)
    # content = models.TextField()
    # template_name = "noteit/detail.html"
    # note_instance = get_object_or_404(Note, pk=new_id)
    # content = models.TextField()
    # def get_queryset(self, nid=new_id):
    #     return Note.objects.filter(pk=nid)


class DetailView(generic.DetailView):
    print("detail")
    model = Note
    content = models.TextField()
    template_name = "noteit/detail.html"


class ResultsView(generic.DetailView):
    print("results")
    model = Note
    content = Note.content
    template_name = "noteit/results.html"


def submit(request, pk):
    print("submit")

    note_instance = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form_data = request.POST
        # print("form_data", form_data)
        # print("form_data.content", form_data['content'])
        # print("note_instance.title", note_instance.title)
        # print("note_instance.content", note_instance.content)
        note_instance.title = form_data['title']
        note_instance.content = form_data['content']
        note_instance.updated_at = timezone.localtime()
        note_instance.save()
        # note_instance.save()
        return HttpResponseRedirect(reverse(
            'noteit:index', args=()))

    # else:
    #     form = Note_form(instance=note_instance)

    # context = {
    #     'form': form,
    #     'note_instance': note_instance,
    # }

    # return render(request, "noteit/index.html", context)
