# lexicon/models.py
from django.db import models

# ----------------------------------------------------
# 1. Tablas Auxiliares (ACC AUX) - Tablas de "lookup"
# ----------------------------------------------------

class AccAuxCasus(models.Model):
    # PK ID Caso LONG -> Django usa 'id' por defecto como PK. Si tu esquema lo requiere explícitamente, puedes usar:
    # id_caso = models.BigAutoField(primary_key=True)
    caso = models.CharField(max_length=25) # Case CHAR(25)

    def __str__(self):
        return self.caso

    class Meta:
        verbose_name = "Auxiliar de Caso"
        verbose_name_plural = "Auxiliares de Casos"

class AccAuxGeneros(models.Model):
    # PK ID Genero LONG
    genero = models.CharField(max_length=25) # Asumo CHAR(25) por analogía con Casus

    def __str__(self):
        return self.genero

    class Meta:
        verbose_name = "Auxiliar de Género"
        verbose_name_plural = "Auxiliares de Géneros"

class AccAuxNum(models.Model):
    # PK ID Numero LONG
    numero = models.CharField(max_length=25) # Asumo CHAR(25) por analogía

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name = "Auxiliar de Número"
        verbose_name_plural = "Auxiliares de Números"

class AccAuxGradacion(models.Model):
    # PK ID Gradacion LONG
    gradacion = models.CharField(max_length=25) # Gradación CHAR(25)

    def __str__(self):
        return self.gradacion

    class Meta:
        verbose_name = "Auxiliar de Gradación"
        verbose_name_plural = "Auxiliares de Gradaciones"

class AccAuxPersona(models.Model):
    # PK ID Persona LONG (no está explícitamente en el PDF, pero es común en morfología verbal/pronominal)
    persona = models.CharField(max_length=25) # Asumo CHAR(25)

    def __str__(self):
        return self.persona

    class Meta:
        verbose_name = "Auxiliar de Persona"
        verbose_name_plural = "Auxiliares de Personas"

# ----------------------------------------------------
# 2. Tablas Principales y de Clasificación
# ----------------------------------------------------

class TiposLemas(models.Model):
    # PK ID Tipo Lema LONG
    tipo_lema = models.CharField(max_length=35) # Tipo lema CHAR(35)

    def __str__(self):
        return self.tipo_lema

    class Meta:
        verbose_name = "Tipo de Lema"
        verbose_name_plural = "Tipos de Lemas"

class SubtiposLemas(models.Model):
    # PK ID Subtipo Lemas LONG
    subtipo_lema = models.CharField(max_length=35) # Subtipo lemas CHAR(35)
    # FK1 ID Tipo Lema LONG
    tipo_lema = models.ForeignKey(TiposLemas, on_delete=models.CASCADE)

    def __str__(self):
        return self.subtipo_lema

    class Meta:
        verbose_name = "Subtipo de Lema"
        verbose_name_plural = "Subtipos de Lemas"

class Lema(models.Model):
    # PK IDLema LONG
    lema = models.CharField(max_length=150) # Lema CHAR(150)
    observaciones = models.TextField(blank=True, null=True) # Observaciones LONGTEXT
    # FK1 ID Subtipo Lemas LONG
    subtipo_lema = models.ForeignKey(SubtiposLemas, on_delete=models.SET_NULL, null=True, blank=True)
    # Usamos SET_NULL para que si se borra un subtipo, los lemas asociados no se borren, solo se ponga null el campo.

    def __str__(self):
        return self.lema

    class Meta:
        verbose_name = "Lema"
        verbose_name_plural = "Lemas"

class Forma(models.Model):
    # PK IDForma LONG
    forma = models.CharField(max_length=50) # Forma CHAR(50)
    # FK1 IDLema LONG
    lema = models.ForeignKey(Lema, on_delete=models.CASCADE) # Relación Many-to-one con Lema
    observaciones = models.TextField(blank=True, null=True) # Observaciones LONGTEXT

    def __str__(self):
        return self.forma

    class Meta:
        verbose_name = "Forma"
        verbose_name_plural = "Formas"

class CamposSemanticos(models.Model):
    # PK ID Campo Semantico LONG
    campo_semantico = models.CharField(max_length=75) # Asumo CHAR(75)

    def __str__(self):
        return self.campo_semantico

    class Meta:
        verbose_name = "Campo Semántico"
        verbose_name_plural = "Campos Semánticos"

class Significados(models.Model):
    # PK ID Significado LONG
    significado = models.CharField(max_length=75) # Significado CHAR(75)
    # FK3 ID Campo semantico LONG
    campo_semantico = models.ForeignKey(CamposSemanticos, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.significado

    class Meta:
        verbose_name = "Significado"
        verbose_name_plural = "Significados"

class Textos(models.Model):
    # PK ID Texto LONG
    texto = models.TextField() # Texto LONGTEXT

    def __str__(self):
        return f"Texto {self.pk}" # O alguna parte del texto si no es demasiado largo

    class Meta:
        verbose_name = "Texto"
        verbose_name_plural = "Textos"

# ----------------------------------------------------
# 3. Tablas de Bibliografía (y sus relaciones)
# ----------------------------------------------------

class Bibliografia(models.Model):
    # PK ID Bibliografia LONG
    titulo = models.CharField(max_length=150) # Titulo CHAR(150)
    colacion = models.TextField(blank=True, null=True) # Colación LONGTEXT
    observaciones = models.TextField(blank=True, null=True) # Observaciones LONGTEXT

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Bibliografía"
        verbose_name_plural = "Bibliografías"

class Autor(models.Model):
    # Asumo una tabla de Autor basada en la relación BibliografiaAutores
    # PK ID Autor LONG
    autor = models.CharField(max_length=75) # Asumo CHAR(75)

    def __str__(self):
        return self.autor

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

class BibliografiaAutor(models.Model):
    # PK FK1 ID Bibliografia LONG
    bibliografia = models.ForeignKey(Bibliografia, on_delete=models.CASCADE)
    # PK FK2 ID Autor LONG
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    # Puedes añadir un campo 'posicion' si lo necesitas para la relación específica (no lo veo en el esquema de la relación, pero sí en AUX Significados Biografía)
    # posicion = models.CharField(max_length=10, blank=True, null=True) # Si hubiera un campo Posición en esta tabla intermedia

    class Meta:
        unique_together = ('bibliografia', 'autor') # Evita duplicados en la relación
        verbose_name = "Autor de Bibliografía"
        verbose_name_plural = "Autores de Bibliografía"

# ----------------------------------------------------
# 4. Tablas de Relación M:N explícitas (a través de modelos)
# ----------------------------------------------------

class LemasBibliografia(models.Model):
    # PK ID LEM-BIB LONG (Django autogenera PK. Podemos usar id_lem_bib si queremos nombrar la PK)
    # FK1 ID Lema LONG
    lema = models.ForeignKey(Lema, on_delete=models.CASCADE)
    # FK2 ID Bibliografia LONG
    bibliografia = models.ForeignKey(Bibliografia, on_delete=models.CASCADE)
    posicion = models.TextField(blank=True, null=True) # Posición LONGTEXT

    class Meta:
        unique_together = ('lema', 'bibliografia')
        verbose_name = "Lema en Bibliografía"
        verbose_name_plural = "Lemas en Bibliografía"

class TextoBibliografia(models.Model):
    # PK ID TXT-BIB LONG
    # FK1 ID Text LONG
    texto = models.ForeignKey(Textos, on_delete=models.CASCADE)
    # FK2 ID Bibliografia LONG
    bibliografia = models.ForeignKey(Bibliografia, on_delete=models.CASCADE)
    posicion = models.TextField(blank=True, null=True) # Posición (asumo LONGTEXT por el esquema)

    class Meta:
        unique_together = ('texto', 'bibliografia')
        verbose_name = "Texto en Bibliografía"
        verbose_name_plural = "Textos en Bibliografía"

class AuxSignificadosBibliografia(models.Model):
    significado = models.ForeignKey(Significados, on_delete=models.CASCADE)
    bibliografia = models.ForeignKey(Bibliografia, on_delete=models.CASCADE)
    posicion = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        unique_together = ('significado', 'bibliografia')
        verbose_name = "Significado en Bibliografía"
        verbose_name_plural = "Significados en Bibliografía"
        
        
class Notas(models.Model):
    # PK ID Nota LONG
    notas = models.TextField() # Notas LONGTEXT

    def __str__(self):
        return f"Nota {self.pk}"

    class Meta:
        verbose_name = "Nota"
        verbose_name_plural = "Notas"

class LemBibNotas(models.Model):
    # PK, FK1 ID LEM-BIB LONG
    lem_bib = models.ForeignKey('LemasBibliografia', on_delete=models.CASCADE)
    # PK, FK2 ID Nota LONG
    nota = models.ForeignKey(Notas, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('lem_bib', 'nota')
        verbose_name = "Nota de Lema-Bibliografía"
        verbose_name_plural = "Notas de Lema-Bibliografía"

class TxtBibNotas(models.Model):
    # PK, FK1 ID Nota LONG
    nota = models.ForeignKey(Notas, on_delete=models.CASCADE)
    # PK, FK2 ID TXT BIB LONG
    txt_bib = models.ForeignKey('TextoBibliografia', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('nota', 'txt_bib')
        verbose_name = "Nota de Texto-Bibliografía"
        verbose_name_plural = "Notas de Texto-Bibliografía"

# ----------------------------------------------------
# 6. Tablas de Acentuación/Morfología (ACC ADVE, ACC Sustantivo, ACC Verbo FNOM, etc.)
# ----------------------------------------------------
# Estas tablas son más complejas por las múltiples FK y PK compuestas.
# Se traducen como modelos que tienen claves foráneas a las tablas auxiliares (Casus, Generos, Num, Gradacion, Persona).
# Y también a las tablas principales (Forma, Lema, etc.).

# ACC Adverbio: PK,FK2 ID Forma LONG, PK,FK3 ID Gradación LONG
class AccAdverbio(models.Model):
    forma = models.ForeignKey('Forma', on_delete=models.CASCADE)
    gradacion = models.ForeignKey('AccAuxGradacion', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('forma', 'gradacion')
        verbose_name = "Acentuación Adverbio"
        verbose_name_plural = "Acentuaciones Adverbios"

# ACC Sustantivo: PK,FK4 ID Forma LONG, ID Genero LONG, ID Caso LONG, ID Numero LONG
class AccSustantivo(models.Model):
    forma = models.ForeignKey('Forma', on_delete=models.CASCADE)
    genero = models.ForeignKey('AccAuxGeneros', on_delete=models.CASCADE)
    caso = models.ForeignKey('AccAuxCasus', on_delete=models.CASCADE)
    numero = models.ForeignKey('AccAuxNum', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('forma', 'genero', 'caso', 'numero')
        verbose_name = "Acentuación Sustantivo"
        verbose_name_plural = "Acentuaciones Sustantivos"

# ACC Verbo FNOM: PK,FK1 ID Forma LONG, PK2 ID Caso LONG, FK3 ID Género LONG, FK4 ID Número LONG
class AccVerboFnom(models.Model):
    forma = models.ForeignKey('Forma', on_delete=models.CASCADE)
    caso = models.ForeignKey('AccAuxCasus', on_delete=models.CASCADE)
    genero = models.ForeignKey('AccAuxGeneros', on_delete=models.CASCADE)
    numero = models.ForeignKey('AccAuxNum', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('forma', 'caso', 'genero', 'numero')
        verbose_name = "Acentuación Verbo F. No Personal"
        verbose_name_plural = "Acentuaciones Verbos F. No Personales"

# ACC Verbo: PK,FK5 ID Forma LONG, Genero LONG, FK ID Caso LONG, ID Numero LONG, FK4 ID Gradación LONG
class AccVerbo(models.Model):
    forma = models.ForeignKey('Forma', on_delete=models.CASCADE)
    genero = models.ForeignKey('AccAuxGeneros', on_delete=models.CASCADE, null=True, blank=True)
    caso = models.ForeignKey('AccAuxCasus', on_delete=models.CASCADE, null=True, blank=True)
    numero = models.ForeignKey('AccAuxNum', on_delete=models.CASCADE, null=True, blank=True)
    gradacion = models.ForeignKey('AccAuxGradacion', on_delete=models.CASCADE, null=True, blank=True)
    persona = models.ForeignKey('AccAuxPersona', on_delete=models.CASCADE, null=True, blank=True) # Añadido campo Persona

    class Meta:
        # unique_together será más complejo aquí si hay campos opcionales que a veces son parte de la PK
        # Si la PK no es solo la forma, sino la forma + sus características morfológicas, entonces:
        unique_together = ('forma', 'genero', 'caso', 'numero', 'gradacion', 'persona')
        # Si algún campo es Nulo, unique_together puede no funcionar como esperas para la PK.
        # Aquí asumimos que todos estos campos formarán parte de la clave única cuando no sean nulos.
        # En MySQL, UNIQUE KEYs pueden tener NULLs, pero solo un NULL por campo en la combinación.

        verbose_name = "Acentuación Verbo"
        verbose_name_plural = "Acentuaciones Verbos"

# ACC Significado: PK ID AUX Significado LONG, FK2 ID Forma LONG, FK3 ID Texto LONG
class AccSignificados(models.Model):
    significado = models.ForeignKey('Significados', on_delete=models.CASCADE)
    forma = models.ForeignKey('Forma', on_delete=models.CASCADE)
    texto = models.ForeignKey('Textos', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('significado', 'forma', 'texto')
        verbose_name = "Acentuación Significado"
        verbose_name_plural = "Acentuaciones Significados"
