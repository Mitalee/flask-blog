from datetime import datetime

from flask import url_for

from blog import db


class Comment(db.EmbeddedDocument):
    author = db.StringField(verbose_name='Name', max_length=255, required=True)
    content = db.StringField(verbose_name='Comment', required=True)
    created_at = db.DateTimeField(default=datetime.now, required=True)


class Post(db.Document):
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))
    content = db.StringField(required=True)
    created_at = db.DateTimeField(default=datetime.now, required=True)
    slug = db.StringField(max_length=255, required=True)
    title = db.StringField(max_length=255, required=True)

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }
