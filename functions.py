"""A collection of function for doing my project."""

import string
import random
import nltk
import pandas as pd

df = pd.read_csv('movies.csv')

#FROM A3: 
   
def remove_punctuation (input_string):
    
    """
    Takes an input string and removes the punctuation.
    
    Parameters
    ----------
    input_string : str
    
    Returns
    -------
    answer : str
        The result will be the same input string without any punctuation.   
        
    """
    
    out_string = ''
    
    for character in input_string:      
        if character not in string.punctuation:
            out_string = out_string + character         
    return out_string

def prepare_text(input_string): 
    
    """  
    Prepare an input string for processing.
    
    Parameters
    ----------
    input_string : str
    
    Returns
    -------
    answer : lst
        The result will be the same input string changed to lowercase, 
    without punctuation, and split up into a list.         
    """
    
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()   
    return out_list

def string_concatenator (string1, string2, separator): 
     
    """
    Concatenates two strings with a separator in between.
    
    Parameters
    ----------
    string1 : str
           First string to be concatenated.
    string2 : str
           Second string to be concatenated.
    separator : str
           The separator of the strings.
    
    Returns
    -------
    answer : str
        The result will string1 and string2 concatenated with the separator in between.   
            
    """
    
    output = string1 + separator + string2
    return output

def list_to_string (input_list, separator): 
     
    """
    Converts a list of strings to one string with a separator in between each.
    
    Parameters
    ----------
    input_list : lst
           List of strings to be concatenated.
    separator : str
           The separator of the strings.
    
    Returns
    -------
    answer : str
        The result will be a single string with the separator in between each word.   
    """
    
    output = input_list [0]
    for element in input_list[1:]:
        output = string_concatenator(output, element, separator) 
    return output

def end_chat (input_list): 
     
    """
    Check if 'quit' is part of the input list.
    
    Parameters
    ----------
    input_list : lst
           List of strings.
    
    Returns: 
    -------
    answer : bool
        The result will be True if quit is in the input_list and False if it isn't.       
    """
    
    if 'quit' in input_list:  
        output = True    
    else: 
        output = False    
    return output

#NEW CODE:

genre_in = ['music', 'comedy', 'adventure', 
            'animation', 'fantasy', 'drama', 
            'romance', 'family', 'crime', 'horror', 
            'documentary', 'science fiction', 'action']

director_in = ['george dunning', 'gil junger', 'alexander payne', 
                'griffin dunne','wes anderson', 'norman jewison', 
                'michael lehmann', 'cameron crowe', 'jonathan levine',
                'josh greenbaum', 'denny tedesco', 'tim burton', 
                'allan moyle', 'wes ball', 'steven spielberg', 
                'zelda williams', 'dean fleischer camp', 'jim jarmusch', 
                'hannah marks', 'harold ramis']

cast_in = ['paul angelis', 'john clive', 'dick emery', 
            'geoffrey hughes', 'julia stiles', 'heath ledger', 
             'joseph gordon-levitt', 'paul giamatti', 'dominic sessa', 
             "da'vine joy randolph", 'sandra bullock', 'nicole kidman',
             'stockard channing', 'dianne wiest', 'george clooney', 
             'meryl streep', 'jason schwartzman', 'cher', 'nicolas cage', 
             'winona ryder', 'christian slater', 'billy crudup', 
             'frances mcdormand', 'kate hudson', 'nicholas hoult', 
             'teresa palmer', 'john malkovich', 'kristen wiig', 
             'annie mumolo', 'jamie dornan', 'lou adler',  
             'herb alpert', 'hal blaine', 'ralph fiennes', 
             'f. murray abraham', 'tony revolori', 'saoirse ronan', 
             'johnny depp', 'helena bonham carter', 'emily watson', 
             'anthony lapaglia', 'liv tyler', 'renée zellweger', 
             'owen teague', 'freya allan', 'kevin durand', 'peter macon', 
             'harrison ford', 'karen allen', 'john rhys-davies', 
             'kathryn newton', 'cole sprouse', 'jenny slate', 
             'isabella rosselini', 'dean fleischer camp', 'bill murray', 
             'adam driver', 'tom waits', 'isabela merced', 
             'cree cicchino', 'felix mallard', 'henry thomas', 
           'drew barrymore', 'andie macdowell', 'chris elliot', 
           'stephen tobolowsky', 'michael keaton', 'geena davis', 
           "catherine o'hara", 'alec baldwin']

year_in = [1968, 1981, 1982, 1987, 1988, 
           1989, 1993, 1995, 1998, 1999, 
           2000, 2005, 2008, 2009, 2013, 
           2014, 2019, 2021, 2023, 2024]

def prepare_concatenate_string(input_string, separator = ' '): 
     
    """
    Takes an input string and removes the punctuation, 
    
    Parameters
    ----------
    input_string : str
    separator: str (optional)
    
    Returns
    -------
    answer : str
        The result will be the prepped and concatenated string.      
    """
    
    prepped_text = prepare_text(input_string)
    prepped_string = list_to_string(prepped_text, separator)
    return prepped_string

def find_genre(genre):
     
    """
    Takes an input genre and searches a DataFrame for corresponding films. 
    
    Parameters
    ----------
    director : str
    
    Returns
    -------
    answer : str
        The result will either be movie recommendations from the DataFrame 
        from that genre or that no films corresponds.   
    """
    
    if genre in genre_in: 
        result = df[df['Genre(s)'].str.contains(genre, case = False)]
        return result[['Title']]
    else:
        return 'Genre not included in film list.'

def find_actor(actor):
     
    """
    Takes an input actor and searches a DataFrame for corresponding films. 
    
    Parameters
    ----------
    director : str
    
    Returns
    -------
    answer : str
        The result will either be movie recommendations from the DataFrame
        from that actor or that no films corresponds.    
    """
    
    if actor in cast_in: 
        result = df[df['Cast'].str.contains(actor, case = False)]
        return result[['Title']]
    else:
        return 'This actor is not featured in any films in the list.'

def find_director(director):
     
    """
    Takes an input director and searches a DataFrame for corresponding films. 
    
    Parameters
    ----------
    director : str
    
    Returns
    -------
    answer : str
        The result will either be movie recommendations from the DataFrame
        from that director or that no films corresponds.    
    """
    
    if director in director_in: 
        result = df[df['Director'].str.contains(director, case = False)]
        return result[['Title']]
    else:
        return 'There are no films in the list from this director.'

def find_year(year):
     
    """
    Takes an input year and searches a DataFrame for corresponding films. 
    
    Parameters
    ----------
    year : int
    
    Returns
    -------
    answer : str
        The result will either be movie recommendations from the DataFrame
        from that year or that no films corresponds. 
    """  
    #ValueError suggested by ChatGPT
    try:
        year = int(year)
    except ValueError: 
        return "Please enter a year."
    
    if year in year_in: 
        result = df[df['Year'].isin([year])]
        return result[['Title']]
    else:
        return 'There are no films in the list from that year.'   
    
def chat_with_movie_recommender (): 
     
    """
    Movie recommendation chatbot. 
    
    The chatbot greets the user and asks what criteria they would like to
    search by: genre/actor/director/year. The chatbot will stop when 'quit' is
    the input. After the criteria is input, the user can input the name of the
    genre/actor/director/year they would like recommendations from.
        
    """
    
    print ('Hi! Welcome to the movie recommendation chatbot!')
    print ('Would you like to search by genre, actor, director, or year?')
    print ('Please say quit when you are done.')
    
    chat = True
    
    while chat:
        user_input = input('You: ').lower()
        
        #from chatbots assignment
        prepped_user_input = prepare_concatenate_string(user_input)
        
        if end_chat(prepped_user_input):
            out_input = 'Goodbye!'
            print(out_input)
            chat = False
            break
        
        #end of code from chatbots assignment
           
        #from ChatGPT to make sure loops will continue if category 
        #entered as a sentence
        category = None
        for word in ['genre', 'actor', 'director', 'year', 'thank you']:
            if word in prepped_user_input:
                category = word
                break
        #end of ChatGPT code
        
        if category:
            print('Please input ONLY the name of the genre/actor/director/year.')
            
            if category == 'genre':
                genre_input = input('Which genre would you like to watch?: ').lower()
                genre_film = find_genre(genre_input)
                print(genre_film)
        
            elif category == 'actor':
                actor_input = input('What is the name of the actor?: ').lower() 
                actor_in_film = find_actor(actor_input)
                print(actor_in_film)
        
            elif category == 'director':
                director_input = input('What is the name of the director?: ').lower()
                director_of_film = find_director(director_input)
                print(director_of_film)
             
            elif category == 'year':
                year_input = input('What year was the film released?: ')
                year_of_release = find_year(year_input)
                print(year_of_release) 
        
            elif category == 'thank you':    
                print ("You're welcome! :)")
            
        else:
            print ('Please select an option.')
        
