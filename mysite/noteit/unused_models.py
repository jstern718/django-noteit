# edit_date = models.DateTimeField("date edited")
    # note_title = models.CharField(max_length=50)
    # folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    # tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


# class Chirp(models.Model):
#     chirp_text = models.CharField(max_length=400)
#     pub_date = models.DateTimeField("date published")
#     edit_date = models.DateTimeField("date edited")
#     folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


# class Short(models.Model):
#     short_text = models.CharField(max_length=2000)
#     pub_date = models.DateTimeField("date published")
#     short_title = models.CharField(max_length=50)
#     edit_date = models.DateTimeField("date edited")
#     folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


# class Long(models.Model):
#     long_text = models.CharField(max_length=200000)
#     pub_date = models.DateTimeField("date published")
#     edit_date = models.DateTimeField("date edited")
#     long_title = models.CharField(max_length=50)
#     folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)



# class Folder(models.Model):
#     folder_title = models.CharField(max_length=30)


# class Tag(models.Model):
#     folder_title = models.CharField(max_length=20)



# <!-- {% extends 'noteit/base.html' %} -->

# <!-- {% block content %} -->

# <!-- {% endblock %} -->