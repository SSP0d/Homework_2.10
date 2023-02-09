from django.db.models import ForeignKey, CharField, TextField, CASCADE, ManyToManyField


class Author(models.Model):
    fullname = CharField(max_length=50, unique=True)
    born_date = CharField(max_length=10, null=False)
    born_location = CharField(max_length=100, null=False)
    bio = TextField(null=False)

class Quote(models.Model):
    author = ForeignKey(Author, on_delete=CASCADE)
    text = TextField(unique=True, null=False)
    tags = ManyToManyField(Tag)


class Tag(models.Model):
    name = CharField(max_length=50, null=False, unique=True)
