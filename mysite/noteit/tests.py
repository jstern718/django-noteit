import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Note


class NoteModelTests(TestCase):
    def test_was_edited_recently_false(self):
        """
        edited_recently() returns False for notes whose updated_at
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_note = Note(updated_at=time)
        print("time", time, "updated_at", Note.updated_at)
        self.assertIs(old_note.was_published_recently(), False)

    def test_was_edited_recently_true(self):
        """
        was_published_recently() returns True for notes whose updated_at
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59,
                                                   seconds=59)
        recent_note = Note(updated_at=time)
        self.assertIs(recent_note.was_published_recently(), True)


def create_note(content, days):
    """
    Create a note with the given `content` and updated the
    given number of `days` offset to now (negative for notes published
    in the past).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Note.objects.create(content=content, updated_at=time)


class NoteIndexViewTests(TestCase):
    def test_no_notes(self):
        """
        If no notes exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("noteit:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No notes are available.")
        self.assertQuerySetEqual(response.context["latest_notes_list"], [])

    def test_past_notes(self):
        """
        Notes with a updated_at date in the past are displayed on the
        index page.
        """
        note = create_note(content="Past note.", days=-30)
        response = self.client.get(reverse("noteit:index"))
        self.assertQuerySetEqual(
            response.context["latest_notes_list"],
            [note],
        )


    def test_two_past_notes(self):
        """
        The notes index page may display multiple notes.
        """
        note1 = create_note(content="Past note 1.", days=-30)
        note2 = create_note(content="Past note 2.", days=-5)
        response = self.client.get(reverse("noteit:index"))
        self.assertQuerySetEqual(
            response.context["latest_note_list"],
            [note2, note1],
        )


class noteDetailViewTests(TestCase):
    def test_past_note(self):
        """
        The detail view of a note with a updated_at in the past
        displays the note's text.
        """
        past_note = create_note(content="Past note.", days=-5)
        url = reverse("noteit:detail", args=(past_note.id,))
        response = self.client.get(url)
        self.assertContains(response, past_note.content)