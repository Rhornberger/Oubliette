## Table of contents

* [Oubliett](#Oubliette)
* [Inspiration](#Inspiration)
* [What will Oubliette become?](#What-will-Oubliette-become?)
* [Technologies used](#Technologies-used)
* [Setting up the enviroment](#Setting-up-the-enviroment)

## Oubliette

Oubliette is currently a basic quick reference for Tabletop Roleplaying games (specifically Pathfinder).


## Inspiration

Tabletop Roleplaying games are a process of collaborative story telling. A group of friends will get together, agree on a platform and general style of adventure. From there they take the skeleton of a story and together they decide what direction and details fill out that story through the process of game play. The world they choose to play in requires a very complex and vast set of rules that outlines and makes "real" this imaginary world. All players need to keep a running list of of the basic world rules and how that effects the character they are playing, the main purpose of Oubliette is to streamline the process of looking up that information and unbury a players lap from the mountain of books that tend to pile up as a player references and cross references the rules of a fantasy world. 

## What will Oubliette become?

Oubliette seeks to be a social media platform for Tabletop RPG enthusiasts that will allow playes to have easy access to the gameplay information as well as be able to start a Party page that will allow players to more easily share information between one another and keep journal logs of what has happened during each game sessions. This page will also allow Game Masters to make changes to charachter sheets and other pertinent game and player info.


## Technologies used 
This is a full stack project that was managed and built by Rhiannon Hornberger useing the following tech stack.
* Django
* Django Rest Framework
* Vue.js
* Axios 
* Html
* Bootstrap 4
* Vanilla CSS
* SqLite
* Custom Api 

## Setting up the enviroment

1. Clone the repo.
2. Set up your virtual environment.
    1. If you don't already have pip installed on your machine please see the installation instructions [here](https://pip.pypa.io/en/stable/installing/). 
    2. You can create your virtual enviroment using: `pip install -r requirements.txt`.
    3. Move into the virtual enviroment by (you will need to prepend this with one of the following: py, py -m, or python depending on what your computer set up is) `$ pipenv shell`.
    4. Once in the virtual enviroment do `pipenv sync --dev` (you can do this outside of the virtual enviroment by using `pipenv install --dev`).
3. You can now enjoy Oubliette.



