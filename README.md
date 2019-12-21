# Sample-API

In the past i did a job interview test that was a small and simple example of a REST api. After reading a bit about clean code and clean architecture i found myself wondering how to implement some of the principles of the books in python and choose to make this software again using so that i could tinker a bit with it...

The requirements of the software where:
* You will implement a REST API to save retrieve and delete records of planets of star wars.
* There will be a database where you will save the information that you will receive through POST.
* The information received from a caller will be the Name, the Terrain and the Climate.
* Whenerver you returned a Planet you should also return the queryable ID and the number of movies it was in this number may be calculated from swapi.
* The API will accept a GET call that will return a list of planets.
* The API will accept a GET call with an ID for a specific planet that will return this planet.
* The API will accept a GET call to search for a given planet by Name.
* The API will accept a POST request containing only the Name, the Terrain and the Climate and save this planet to the database.
* The API will accept a DELETE request to remove a given planet from the DataBase.

# Analysis

The requirements tell of a variety of needs, the main ones which are IO related, we're talking about receiving/accepting data and writing/reading from database and APIs.

So let's try to find the main core rules of the application without looking for database or library, for now.

We have three functions that must fetch zero or more planets:
    One will return an unfiltered list of planets
    One will return a filtered list
    One that will return only one planet

    Every one of those functions will return planets with: Name, Climate, Terrain, Number of Movies and ID

We also have an insert function that will receive a planet with: Name, Climate, Terrain, it may return the saved planet

We also have an delete function that will receive an ID and delete that planet if it exists

Let's try to separate the program in a three layer topology

Entry Layer/Main Layer - Will be responsible for receiving the call and passing data to the Bussiness Layer. In this layer we will also ask for the instatiation of a DAL class.

Bussiness Layer - will be responsible for being called by the Entry Layer and receive a class representing the Database where it will either save, search or delete.

Data Layer - This will implement the methods for search, save, delete defined on the bussiness layer.

