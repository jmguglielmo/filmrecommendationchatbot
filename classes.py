"""Classes used throughout project"""

import csv

class AddFilm:

    def __init__ (self, title, genre, year, cast, director):
    
        self.title = title
        self.genre = genre
        self.year = year
        self.cast = cast
        self.director = director
    
    def add_to_movies_csv(self, csv_title):
        
        """
        Adds information about a movie to a new row in a preexisting csv file. 
    
        Parameters
        ----------
        csv_title : str
                The title of the csv that will be appended.
    
        Returns: None    
        """
        
        #mode='a' opens the file so it will be ready to be appended
        #use of ChatGPT to learn how to do this
        with open(csv_title, mode='a', newline='') as film_dataframe:
            new_film = csv.writer(film_dataframe)
            new_film.writerow([self.title, self.genre, 
                           self.year, self.cast, self.director])
                 
    def append_lists(self):
        
        """
        Adds information about a movie to preexisting and corresponding lists. 
    
        Checks if the genre/year/actor/director is already in the preexisting 
        and corresponding lists. If they are not already there, the information
        will be added. If it is already there, a message will print saying so.
        
        Returns: None    
        """
        
        if self.genre not in functions.genre_in:
            new_genre = functions.prepare_text(self.genre)
            functions.genre_in.append(new_genre)
        else:
            print('Genre already in genre_in.')
            
        if self.year not in functions.year_in:
            functions.year_in.append(self.year)
        else:
            print('Year already in year_in.')
            
        if self.cast not in functions.cast_in:
            new_cast = functions.prepare_text(self.cast)
            functions.cast_in.append(new_cast)
        else:
            print('Cast already in cast_in.')
            
        if self.director not in functions.director_in:
            new_director = functions.prepare_text(self.director)
            functions.director_in.append(new_director)
        else:
            print('Director already in director_in.')
          
