"""Test for my functions.
"""

from functions import find_actor, prepare_concatenate_string
from classes import AddFilm
import pandas as pd
import csv

def test_find_actor():   
    not_in_list = find_actor('Julia Guglielmo')
    assert not_in_list == 'This actor is not featured in any films in the list.'
    
    in_list = find_actor('owen teague')
    
    #ChatGPT helped to debug assert isinstance and assert 'Kingdom'
    assert isinstance(in_list, pd.DataFrame)
    assert 'Kingdom of the Planet of the Apes' in in_list['Title'].tolist()   
    
def test_add_to_movies_csv():                
    beetlejuice = AddFilm(title = "Beetlejuice", 
                      genre = "Fantasy, Comedy", 
                      year = "1988", 
                     cast = "Michael Keaton, Geena Davis, Alec Baldwin, Winona Ryder, Catherine O'Hara",
                     director = "Tim Burton")
    
    beetlejuice.add_to_movies_csv('../movies.csv')

    #ChatGPT helped me to/learn how to create this test 
    with open('../movies.csv', 'r') as movies_file:
        reader = csv.reader(movies_file)
        rows = list(reader)
        expected_row = ["Beetlejuice", "Fantasy, Comedy", "1988", "Michael Keaton, Geena Davis, Alec Baldwin, Winona Ryder, Catherine O'Hara", "Tim Burton"]
        assert rows[-1] == expected_row
        
def test_prepare_concatenate_string():
   
    assert type(prepare_concatenate_string('Search by ACTOR!!!')) == str
    assert prepare_concatenate_string('Search by ACTOR!!!') == 'search by actor'
