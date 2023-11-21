class Song:
    def __init__(self,num,name,artist,views,year,language,history=0):
        self.num = num
        self.name = name
        self.artist = artist
        self.views = views
        self.year = year
        self.language = language
        self.history = history
    
    def show(self):
        return f"""
    Número: {self.num}
    Nombre: {self.name}
    Artista: {self.artist}
    Reproducciones: {self.views}
    Año: {self.year}
    Idioma: {self.language}
    """
    def songName(self):
        return self.name
