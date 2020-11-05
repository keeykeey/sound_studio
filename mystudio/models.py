from django.db import models
from django.conf import settings
from audiofield.fields import AudioField
import os.path
from pydub import AudioSegment
from pydub.playback import play
import numpy as np

# Create your models here.
class PostedSong(models.Model):
    id = models.AutoField(primary_key=True)
    #username = models.CharField(max_length=50)
    song_title = models.CharField(max_length=50)
    artist_name = models.CharField(max_length=50)
    genre = models.CharField(max_length = 25)
    tag = models.CharField(max_length=50)
    audio_file = models.FileField(default='', upload_to='')
#    sound = AudioSegment.from_file(audio_file,format="mp3")
#    ndarray = np.array(sound.get_array_of_samples())

    def __str__(self):
        return self.song_title

#    def audio_to_mp3(self):
#        sound = AudioSegment.from_file(audio_file, format="mp3")
#        return sound

#    def audio_to_ndarray(self):
#        sound = AudioSevment.from_file(audio_file,format="mp3")
#        ndarray = np.array(sound.get_array_of_samples())
#        return ndarray

#    audio_file = AudioField(upload_to='media',blank=True,
#        ext_whitelist=(".mp3",".wav",".ogg"),
#        help_text=("Allowed type - .mp3,.wav,.ogg"))


#    def audio_file_player(self):
#        '''audio player tag for admin '''
#        if self.audio_file:
#            file_url = settings.MEDIA_URL + str(self.audio_file)
#            player_string = '<audio src="%s" controls>Yout browser does not support the audio element.</audio>'%(file_url)
#            return player_string
#    audio_file_player.allow_tags = True
#    audio_file_player.short_description = ('Audio file player')








#
