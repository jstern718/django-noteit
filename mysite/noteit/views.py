from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.db import models
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
# from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note, User, Folder, Tag
# from .forms import LoginForm
# from django.middleware.csrf import CsrfViewMiddleware


def MessageView(x):
    return HttpResponse("Hello World!")


class IndexView(LoginRequiredMixin, generic.ListView):
    print("index runs")
    login_url = "/accounts/login/"
    # redirect_field_name = "redirect_to"

    template_name = "noteit/index.html"
    context_object_name = "latest_note_list"

    def get_queryset(self):
        print("index-get_queryset runs")
        """Return notes that user owns."""
        # username = get_username(request)
        # return Note.objects.filter(Note.user == username)
        return Note.objects.filter(user=self.request.user).order_by(
            "-updated_at")[
            :50
        ]

    def get_context_data(self, **kwargs):
        print("index-get_context runs")
        context = super().get_context_data(**kwargs)
        context['folders'] = Folder.objects.filter(user=self.request.user)
        return context

    def format_date(old_date):
        return old_date.strftime("%H:%M:%S")

    def post(self, request, *args, **kwargs):
        print("index-post runs")
        username = self.request.user
        text = request.POST.get('new-text')
        # User.objects.get(username="admin")
        note = Note.objects.create_note(title=text, content=text, user=username)
        note.save()
        new_id = note.id
        # context = {"title": "", "content": "", "user": admin_user,
        #            "note_id": new_id}

        return HttpResponseRedirect(f"/noteit/notes/{new_id}")
        # return render(request, f"noteit/{new_id}/detail.html", context)


class FolderIndexView(LoginRequiredMixin, generic.ListView):
    print("folder_index")
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"
    template_name = "noteit/folder_index.html"
    context_object_name = "folder_note_list"
    model = Note

    def get_queryset(self):
        folder_name = self.kwargs.get('folder')
        folder = get_object_or_404(Folder, name=folder_name)
        return Note.objects.filter(user=self.request.user).filter(
            folder=folder)


class TagIndexView(LoginRequiredMixin, generic.ListView):
    print("tag_index")
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"
    template_name = "noteit/tag_index.html"
    context_object_name = "tag_note_list"
    model = Note

    def get_queryset(self):
        tag_name = self.kwargs.get('tag')
        tag = get_object_or_404(Tag, name=tag_name)
        return Note.objects.filter(user=self.request.user).filter(
            tag=tag)


class DetailView(LoginRequiredMixin, generic.DetailView):
    print("detail")
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"

    model = Note
    content = models.TextField()
    template_name = "noteit/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Access Note object
        note = self.object
        # Access and manipulate updated_at attribute
        updated_at = note.updated_at
        updated_at_str = updated_at.strftime("%m.%d.%y_%H:%M")
        created_at = note.created_at
        created_at_str = created_at.strftime("%m.%d.%y_%H:%M")
        if note.tags.exists():
            tags = " | ".join(tag.name for tag in note.tags.all())
        else:
            tags = "None"
        # Pass manipulated value to context
        context['updated_at'] = updated_at_str
        context['created_at'] = created_at_str
        context['tags'] = tags
        return context


class ResultsView(LoginRequiredMixin, generic.DetailView):
    print("results")
    login_url = "/accounts/login/"
    redirect_field_name = "redirect_to"

    model = Note
    content = Note.content
    template_name = "noteit/results.html"


# class LoginView(generic.FormView):
#     print("loginView runs")
#     next = "noteit/notes/"
#     # model = User
#     form_class = LoginForm

#     def form_valid(self, form):
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(self.request, user)
#             return redirect('/noteit/notes/')
#         else:
#             form.add_error(None, 'Invalid username or password.')
#         return super().form_valid(form)


def submit(LoginRequiredMixin, request, pk):
    print("submit")

    note_instance = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form_data = request.POST
        note_instance.title = form_data['title']
        note_instance.content = form_data['content']
        note_instance.updated_at = timezone.localtime()
        note_instance.save()
        return HttpResponseRedirect(reverse(
            'noteit:index', args=()))


def get_username(request):
    current_user = request.user
    if current_user.is_authenticated:
        username = current_user.username
    else:
        username = None
    return username


# class NewNoteView(generic.CreateView):
#     print("new note view runs")
#     admin_user = User.objects.get(username="admin")
#     note = Note.objects.create_note("", "", admin_user)
#     note.save()
#     note_id = note.id
#     model = Note
#     fields = ['title', 'content']
#     template_name = "noteit/new_note.html"

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

#     def get_success_url(self):
#         return reverse_lazy('noteit:note_detail',
#                             kwargs={'pk': self.object.pk})



        # return Note.objects.filter(updated_at__lte=timezone.now()).order_by(
        #     "-updated_at")[
        #     :50
        # ]