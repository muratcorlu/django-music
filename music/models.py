import os
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from utils import get_file_upload_path, get_cover_upload_path

import eyeD3

class Song(models.Model):
    file = models.FileField(_('File'), upload_to=get_file_upload_path)
    file_size = models.IntegerField(_('File size'),editable=False)
    duration = models.IntegerField(_('Song duration in seconds'),editable=False,default=0)

    title = models.CharField(_('Title'), max_length=100)
    artist = models.CharField(_('Artist'), max_length=100, blank=True)
    album = models.CharField(_('Album name'), max_length=100, blank=True)
    track_number = models.SmallIntegerField(_('Track number'), blank=True, null=True)
    track_total = models.SmallIntegerField(_('Total track count'), blank=True, null=True)
    genre = models.CharField(_('Genre'), max_length=50, blank=True)
    disc_number = models.SmallIntegerField(_('Disc number'), blank=True, null=True)
    disc_total = models.SmallIntegerField(_('Total disc count'), blank=True, null=True)
    year = models.CharField(_('Year'), max_length=4, blank=True)
    publisher = models.CharField(_('Publisher'), max_length=100, blank=True)
    cover_image = models.ImageField(_('Cover image'), upload_to=get_cover_upload_path, blank=True)

    play_count = models.IntegerField(_('Play count'), default=0)

    added_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.file_size = self.file.size

        super(Song, self).save(*args, **kwargs)

        file_path = os.path.join(settings.MEDIA_ROOT, self.file.name)

        if eyeD3.isMp3File(file_path):
            audioFile = eyeD3.Mp3AudioFile(file_path)
            self.duration = audioFile.getPlayTime()
            
            tag = audioFile.getTag()
            self.artist = tag.getArtist()
            self.album = tag.getAlbum()
            self.track_number = tag.getTrackNum()


        super(Song, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s" % self.title

class Lyric(models.Model):
    song = models.ForeignKey(Song)
    language = models.CharField(_('language'), max_length=5, choices=settings.LANGUAGES)
    content = models.TextField(_('Lyrics'))

    def __unicode__(self):
        return _("%s Lyrics") % self.song.title