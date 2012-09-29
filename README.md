# Entu

_Futuristic Data Management System with emphasis on educational institutions_


## Key features

* It stores data in Entities (objects) and Entities have (text, numeric, date, file, …) properties
* Entities are fully customizable
    * what properties to show as name, description, etc
    * what properties to show in relation table
    * what properties to use for search and sort
    * allowed child Entities
    * what kind of custom actions it supports
    * ...
* Properties are fully customizable
    * label
    * description
    * data type
    * multiplicity
    * visibility in public search
    * ...
* In addition to stored properties, there are calculated properties to calculate/show Entity's (or related Entity's) properties
* Property can store one or multiple values
* Entities can be related with each other by system relations (child, seeder, leecher) or by custom ones
* User authentication is delegated to Google, Facebook, Twitter, MS Live or other providers
* Users have explicit rights (viewer, editor, owner) for every Entity - there are no roles


## Screenshot

![Screenshot](https://raw.github.com/argoroots/Entu/master/static/images/screenshot.png "Screenshot")


## Dependencies

* [MySQL](http://www.mysql.com/)
* [Python](http://www.python.org/)
    * [Tornado](http://www.tornadoweb.org)
    * [python-mysqldb](http://mysql-python.sourceforge.net)
    * [python-magic](https://github.com/ahupp/python-magic)
    * [python-suds](https://fedorahosted.org/suds/)
    * [python-markdown2](https://github.com/trentm/python-markdown2)
    * [tornadomail](https://github.com/equeny/tornadomail)
    * [xmltodict](https://github.com/martinblech/xmltodict)
    * [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup)


## Used libraries/add-ons

* [Bootstrap](http://twitter.github.com/bootstrap/) + [Font Awesome](http://fortawesome.github.com/Font-Awesome/)
* [jQuery](http://jquery.com/) + [jQuery UI](http://jqueryui.com/)
* [Elastic](http://unwrongest.com/projects/elastic/)
* [Datejs](http://www.datejs.com/)


## ToDo

* Calculation (formula) fields
* Show Entity.displaycount
* Show all entities in search (not first 303)
* Replace [tornadomail](https://github.com/equeny/tornadomail) with better email library
* Custom Entity actions
* Favorite entities
* Recently viewed/changed entities
* Separate login page
* Invite person to become user
* Customizable table fields by user (visibility, sort)
* Find duplicate Entities and propose merger
* Option to ask permission (send message to owner) to Entity if access denied
* Relation definition based Entity.displaytable
* ...
