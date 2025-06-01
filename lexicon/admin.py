# lexicon/admin.py
from django.contrib import admin
from .models import (
    Lema, Forma, TiposLemas, SubtiposLemas,
    Bibliografia, Autor, BibliografiaAutor,
    CamposSemanticos, Significados, Textos,
    LemasBibliografia, TextoBibliografia, AuxSignificadosBibliografia,
    Notas, LemBibNotas, TxtBibNotas,
    AccAuxCasus, AccAuxGeneros, AccAuxNum, AccAuxGradacion, AccAuxPersona,
    AccAdverbio, AccSustantivo, AccVerboFnom, AccVerbo, AccSignificados
)

# Registra tus modelos aquí. Cada modelo debe registrarse UNA SOLA VEZ.
admin.site.register(Lema)
admin.site.register(Forma)
admin.site.register(TiposLemas)
admin.site.register(SubtiposLemas)
admin.site.register(Bibliografia)
admin.site.register(Autor)
admin.site.register(BibliografiaAutor)
admin.site.register(CamposSemanticos)
admin.site.register(Significados)
admin.site.register(Textos)
admin.site.register(LemasBibliografia)
admin.site.register(TextoBibliografia)
admin.site.register(AuxSignificadosBibliografia)
admin.site.register(Notas)
admin.site.register(LemBibNotas)
admin.site.register(TxtBibNotas)
admin.site.register(AccAuxCasus)
admin.site.register(AccAuxGeneros)
admin.site.register(AccAuxNum)
admin.site.register(AccAuxGradacion)
admin.site.register(AccAuxPersona)
admin.site.register(AccAdverbio)
admin.site.register(AccSustantivo)
admin.site.register(AccVerboFnom)
admin.site.register(AccVerbo)
admin.site.register(AccSignificados)