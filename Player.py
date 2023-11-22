from Song import Song
class Player:
    def __init__(self,songs,playlist,history):
        self.songs = []
        self.playlist = []
        self.history = []
        
    def create_history(self):
        self.history = []
        for cancion in self.playlist:
            self.history.append({cancion:cancion.history})
        return self.history    
            
    def get_txt(self):
        
        Abrir = "canciones.txt"

        with open(Abrir) as fin:
            self.songs = [ linea.strip().split(',') for linea in fin ]
        print(self.songs)
        
        for i in self.songs:
            count = 0
            for j in i:
                if count == 0:
                    num = j
                    count = count + 1
                elif count == 1:
                    name = j
                    count = count + 1
                elif count == 2:
                    artist = j
                    count = count + 1
                elif count == 3:
                    views = j
                    count = count + 1
                elif count == 4:
                    year = j
                    count = count + 1
                elif count == 5:
                    language = j
                    count = count + 1
            new_song = Song(num,name,artist,views,year,language)
            self.playlist.append(new_song)
                
                    
                
                
    def menucito(self,options):
        print("----------------------------")
        for option in range(len(options)):
                print(f"{option+1} / {options[option]}")
                print("----------------------------")    
    def shows(self):
        print("----------------------------")
        for i in range(len(self.playlist)):
            print(f"{i+1}. {self.playlist[i].show()}")
            print("----------------------------")   
                       
    def pause(self):
        #Pausa activa que se usan en casi todos los metodos, así la pantalla se ve más organizada al hacerle run
        print("Toque cualquier botón para volver al menú")
        pause = input(" ")
        if pause == "":
         pass
        else:
         pass            
    def artist_filter(self):
        choice = input("Ingrese el artista para buscar las canciones: ")
        count = 0
        for artista in self.playlist:
            if artista.artist == choice:
                if count == 0:
                    print("Se encontraron las siguientes canciones: ")
                print(f"""
                -----------------------      
                   {artista.show()}
                -----------------------      
                      """)
            
                count = count +1
        if count == 0:
            print("Este artista no se encuentra en la playlist")
         
    def menu(self):
        Start = 0
        if Start == 0:
            self.get_txt()
            Start = Start+1
            print(self.songs)
        options = ["Agregar Canción","Buscar Canción", "Filtrar por Artista", "Reproducción","Ordenar" ,"Mostrar playlist", "Historial", "Salir"]
        choice = 0
        while choice != 8:
            print(f"""
                SPOTIFYTHON

                """)
            self.menucito(options)
            choice = input("Ingrese el número de la opción que desee: ")
            if choice == "1":
                self.new_song()
                self.pause()       
            elif choice == "2":
                self.search_song()
                self.pause()  
            elif choice == "3":
                self.artist_filter()
                self.pause()      
            elif choice == "4":
                self.reproductor()
            elif choice == "5":
                self.order()
                self.pause()  
            elif choice == "6":
                self.shows()
                self.pause()  
            elif choice == "7":
                self.pause()  
            elif choice == "8":
                print("Gracias por preferirnos")
                break
            else:
                print("Error, seleccione un número válido")
                self.pause()   
    def order(self):
        choice = input(f"""
            ¿Como desea ordenar su lista?            
        1.Por visualizaciones crecientes
        2.Por visualizaciones decrecientes
        3.Por orden alfabético reciente
        4.Por orden alfabético decrecientes
        5.Por número creciente
        6.Por número decreciente
        7.Volver al menú
        Ingrese el número de la opción que desee: """)   
        
        if choice == "1":
            playlisttemp = self.playlist
            for i in range(len(playlisttemp)-1):
                for j in range(len(playlisttemp)-1):
                    if int(playlisttemp[j].views) > int(playlisttemp[j+1].views):
                    
                        temp = playlisttemp[j].views
                        playlisttemp[j].views = playlisttemp[j+1].views
                        playlisttemp[j+1].views = temp
            for cancion in playlisttemp:
                print(f"""
                ---------------------------------      
                      {cancion.show()}
                ---------------------------------      
                      """)          
        elif choice == "2":
            playlisttemp = self.playlist
            for i in range(len(playlisttemp)-1):
                for j in range(len(playlisttemp)-1):
                    if int(playlisttemp[j].views) < int(playlisttemp[j+1].views):
                    
                        temp = playlisttemp[j].views
                        playlisttemp[j].views = playlisttemp[j+1].views
                        playlisttemp[j+1].views = temp
            for cancion in playlisttemp:
                print(f"""
                ---------------------------------      
                      {cancion.show()}
                ---------------------------------      
                      """) 
        elif choice == "3":
            playlisttemp = self.playlist
            for i in range(len(playlisttemp)-1):
                for j in range(len(playlisttemp)-1):
                    if playlisttemp[j].name.lower() > playlisttemp[j+1].name.lower():
                    
                        temp = playlisttemp[j].name
                        playlisttemp[j].name = playlisttemp[j+1].name
                        playlisttemp[j+1].name = temp
            for cancion in playlisttemp:
                print(f"""
                ---------------------------------      
                      {cancion.show()}
                ---------------------------------      
                      """) 
                    
        elif choice == "4":
            playlisttemp = self.playlist
            for i in range(len(playlisttemp)-1):
                for j in range(len(playlisttemp)-1):
                    if playlisttemp[j].name.lower() < playlisttemp[j+1].name.lower():
                    
                        temp = playlisttemp[j].name
                        playlisttemp[j].name = playlisttemp[j+1].name
                        playlisttemp[j+1].name = temp
            for cancion in playlisttemp:
                print(f"""
                ---------------------------------      
                      {cancion.show()}
                ---------------------------------      
                      """) 
        elif choice == "5":
            for cancion in self.playlist:
                print(f"""
                ---------------------------------      
                      {cancion.show()}
                ---------------------------------      
                      """) 
            
        elif choice == "6":
            playlisttemp = self.playlist
            playlisttemp.reverse()
            for cancion in playlisttemp:
                print(f"""
                ---------------------------------      
                      {cancion.show()}
                ---------------------------------      
                      """) 
                   
    def historial(self):
        pass           
    def search_song(self):    
        
        choice = input("Ingrese el nombre de la canción a buscar: ")
        count = 0
        for nombre in self.playlist:
            if nombre.name == choice:
                print("La canción se encuentra en la playlist")
                print(nombre.show())
                count = count +1
        if count == 0:
            print("Esta canción no se encuentra en la playlist")
            
    def new_song(self):            
        qty = (input("Cuántas canciones deseas agregar?: "))
        while any(chr.isalpha() for chr in qty) or not qty.isdigit():
            qty = input("Error! Ingrese un numero: ")
        qty = int(qty)
        for i in range(qty):
            #Validacion de nombre
            name=input("Ingrese el nombre de la canción (No debe tener números): ")
            name=name.lower()
            name=name.title()
            while any(chr.isdigit() for chr in name):
                name = input("Error! Ingrese el nombre de la canción (Recuerde que no puede tener números): ")
                name=name.lower()
                name=name.title()         
            
            artist = input("Ingrese el artista de la canción: ")    
            artist=artist.lower()
            artist=artist.title()
            while any(chr.isdigit() for chr in artist) or not artist.isalpha():
                name = input("Error! Ingrese el artista (Recuerde que no puede tener números): ")
                artist=artist.lower()
                artist=artist.title()
            
            views = input("Ingrese las reproducciones de la canción: ")
            while any(chr.isalpha() for chr in views) or not views.isdigit():
                 views = input("Error! Ingrese las reproducciones de la canción")
                                  
            year = input("Ingrese el año de la canción: ")
            while any(chr.isalpha() for chr in year) or not year.isdigit():
                 views = input("Error! Ingrese el año de la canción")
                 
            language = input("Ingrese el idioma de la canción: ")
            language=language.lower()
            language=language.title()
            while any(chr.isdigit() for chr in language) or not language.isalpha():
                language = input("Error! Ingrese el nombre de la canción (Recuerde que no puede tener números): ")
                language=language.lower()
                language=language.title()      
            
            num = len(self.playlist) + 1
            
            new_song = Song(num,name,artist,views,year,language)      
            self.playlist.append(new_song)
            print(f"Se ha añadido la canción: {name} ")
    
        
    def reproductor(self):
        count = 0
        inicio = 0
        bucle = 0
        self.playlist[inicio].history += 1
        print(f"""
        --------Reproduciendo-----
        
        {self.playlist[inicio].show()}
        
        --------------------------"""
        )
        while count == 0:
            choice = input(f"""
                       
        1-Siguiente Canción
        2-Reproducir en bucle
        3-Eliminar bucle
        4-Salir              
        Ingrese el número de la opción que desee: """)
            if choice == "1":
                print("@")
                inicio, count=self.next_song(inicio,bucle,count) 
            elif choice == "2":
                if bucle == 0:
                    bucle = 1
                    print("Se ha iniciado un bucle")
                else:
                    print("Ya hay un bucle activo")
            elif choice == "3":
                if bucle == 1:
                    bucle == 0
                else:
                    print("No hay bucles activos")
            elif choice == "4":
                self.history=self.create_history()
                count = 1
            else: 
                print("Por favor escoja una opcion")
                    
    
    def next_song(self, inicio,bucle,count):
        inicio = inicio + 1
        if inicio >= len(self.playlist) and bucle == 0:
            count = 1
            print("Se han reproducido todas las canciones, volviendo al menú...")
        if inicio >= len(self.playlist) and bucle == 1:
            inicio = 0
            print("Se han reproducido todas las canciones, reproduciendo desde el inicio")
        if count == 0:
            self.playlist[inicio].history += 1
            print(f"""
            --------Reproduciendo-----
            
            {self.playlist[inicio].show()}
            
            --------------------------"""
            )
        return inicio, count
       
                
        

            
            
