from django.db.models import F
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.db import models
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone

from .models import Note, User, NoteForm
# from .forms import Note_form


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

    def post(self, request, *args, **kwargs):
        admin_user = User.objects.get(username="admin")
        note = Note.objects.create_note("", "", admin_user)
        note.save()
        new_id = note.id
        # context = {"title": "", "content": "", "user": admin_user,
        #            "note_id": new_id}

        return HttpResponseRedirect(f"/noteit/notes/{new_id}")
        # return render(request, f"noteit/{new_id}/detail.html", context)


class NewNoteView(generic.CreateView):
    admin_user = User.objects.get(username="admin")
    note = Note.objects.create_note("", "", admin_user)
    note.save()
    note_id = note.id
    model = Note
    fields = ['title', 'content']
    template_name = "noteit/new_note.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('noteit:note_detail',
                            kwargs={'pk': self.object.pk})


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

# <a href="{% url 'noteit:new_note' %}" style="text-decoration: none;">new note</a>