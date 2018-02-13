# Remake of music task.

#### Application installation

For development purposes just run:  `pip install -U -e .`

#### Set Virtual Enviroment

`pip install virtualenv`

#### Project Schema

___
Album | Artist | Country | Discovery | Like | Track
------------ | ------------- | ------------ | ------------- | ------------ | ------------
name | name | id | artist | track | name
artist | bio | name | order | user | artists
year | - | - | - | - | album
 -| - | - | - | - | path
 -| - | - | - | - | availiable_country

#### Project Tech Requires

- postgreSQL > 9.5
- python > 3.6
- django > 2.0
- DRF > 3.7
