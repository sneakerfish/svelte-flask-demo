# Svelte - Flask Demo

This project demonstrates the use of Svelte with Flask as a back-end server.  There will
be a simple database using MySQL on the back-end from the Flask server and database tables
will be modeled using SQLAlchemy. 

The application will manage todo items.  The user will be able to add, delete, and update
existing todo items.  

## Table of Contents


- [Introduction](#introduction)
- [Svelte front-end](#svelte-front-end)
- [Flask back-end](#flask-back-end)
- [Database](#database)

## Introduction

This is a demonstration of Svelte application with a Flask API
application as the back-end.  The API is connected to a MySQL
database.  The Svelte App, Flask API, and MySQL instance are provided
as a Docker Compose set of servers that run at the same time available
on different ports.

## Docker Compose

To get started, just clone the repository and then make sure Docker
desktop with the `docker` command available at the command line.  From
the directory where you cloned the repository, simply enter

```sh
docker compose up
```

and it should download and build everything.  You can see the empty
todo list by visiting the url `http://localhost:8080`. 

## Svelte front-end

The Svelte Front-end runs on port 8080.

## Flask back-end

The Flask Back-end runs on port 5000.  The application is run from the
`manage.py` file in the `api` root.

## Database

The database is MySQL and runs on its standard port of 3306.  The
database will have a single table called `todos`.