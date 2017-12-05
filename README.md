# FSND-1st-Project:
Full Stack Nanodegree 1st project

This repository is for the first project in the Full Stack Nanodegree program. It is a python progran that creates a small website that shows a list of moveies and show their trailers. The repository contains 5 files as follows:

1-README.md: The README file

2-entertainment_center.py: The python file were innces of class 'Movie' are created and the 'open_movies_page' function is called

3-media.py: The module where class 'Movie' is located

4-fresh_tomatoes.py The module used to create the website using the function 'open_movies_page'

5-fresh_tomatoes.html: the website html file created by the 'open_movies_page' function

# Usage:
In the 'entertainment_center.py' file, you begin by creating the 'Movie' instances of your choosing as follows:
  
  my_movie = media.Movie(move_title,
                         movie_storyline,
                         movie_poster,
                         movie_trailer)
                         
After creating the 'Movie' instances you need, add them to a list. Then you can call the 'open_movies_page' function with the list of movies as its argument. The function will then create a HTML file in the same directory called 'fresh_tomatoes.html' and it will open it on your browser.

# Notes:
For the program to work correctly, you have to have all the .py file in this repository in one directory. 'fresh_tomatoes.py' was provided by Udacity, and to customize it a bit I change the title of the website to 'Moe's Tomotoes Movie Trailers' :)
