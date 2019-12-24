# Sample-API

In the past i did a job interview test that was a small and simple example of a REST api. After reading a bit about clean code and clean architecture i found myself wondering how to implement some of the principles of the books in python and choose to make this software again using so that i could tinker a bit with it...

The requirements of the software where:
* You will implement a REST API to save, retrieve and delete records of planets of star wars.
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

Let's try to separate the program in a four layer topology


Main Layer - Will be responsible for receiving the call and passing data to the Bussiness Layer. In this layer we will also ask for the instatiation of a DAL class.

Data Layer - Will be responsible for recovering the data to form the entities from the datasources.

Bussiness Layer - will be responsible for being called by the Main Layer and receive a class representing the Database where it will either save, search or delete.

Entity Layer - Will represent the entities used by the system which the data layer will be responsible for fetching

## Entities

- Planet

### Planet
Planet will be an entity composed of Name, Climate, Terrain, Number of Movies and ID. 

This decision is a bit critical because from the Data viewpoint it will return a Planet Object... But the BasicPlanet record will not have the number of movies, this field will be recovered from a external source.

In an analogy to a real world scenario the manager would ask for the data of a single planet, one clerk would go fetch the local data of this record, but he also wants to cross reference it so he will also call his friend elsewhere and asak for the number of movies.

## Use Cases

Each use case will be a specific function on our system in the format (obligatory_input, *optional_input) # output:
- Search by Name (name_string, queryable, *page, *records_per_page) # GetPlanetsResponse
- Get All (queryable, *page, *records_per_page) # GetPlanetsResponse
- Get by ID (id, queryable) # GetPlanetsResponse
- Create Planet (name, climate, terrain, queryable) # CreatePlanetResponse
- Delete Planet (id, queryable) # DeletePlanetsResponse

The Queryable class(es) are abstract class(es) which will get the needed data for the use cases

Also the following DTO classes will be needed:
- GetPlanetsResponse
- CreatePlanetResponse
- DeletePlanetsResponse
- PlanetResponse

These classes will return the affected planet(s), if any, and a Status. The Status is an Integer that may be used by the Main layer to ask the Data Layer about what to show to the user/client.

 


