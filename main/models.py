from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Audiofl(models.Model):
    descricao = models.TextField(verbose_name=u'Descrição')
    data_insercao = models.DateTimeField(verbose_name=u'Data de insercao',
                                         auto_now_add=True)
    # adicionar anexo, imagem, video, audio..
    foto = models.FileField(upload_to='audio_uploads',
                            blank=True,
                            null=True,
                            verbose_name=u'Foto')

