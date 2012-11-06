# Entu API

_API for Entu (Entu is futuristic object database framework) which lets you search, view, add and modify entities(objects)_


## Key functions
* Search for entities based on keywords, entity type and dataproperty. Possible to get all info about entity or only 'displayable'
* View all information about entity, by giving entity identification number.
* Add new entity by providing entity_definition_keyname or simply the type of new entity and optionally parent identification number.
* Modify existing entity properties or add new ones: API creates new property if given property_id = None, otherwise changes existing.
* User authentication is delegated to Facebook


## Screenshot

![Screenshot](http://math.ut.ee/~juliet91/screenshot.png "Screenshot")

### Dependencies:

* [MySQL 3.23+](http://www.mysql.com/)
* [Python 2.7x](http://www.python.org/)
  * [Tornado](http://www.tornadoweb.org/)
  * [python-mysqld](http://mysql-python.sourceforge.net/)
  * [python-magic](https://github.com/ahupp/python-magic)
  * [python-suds](https://fedorahosted.org/suds/)
  * [python-markdown2](https://github.com/trentm/python-markdown2)
  * [tornadomail](https://github.com/equeny/tornadomail)
  * [xmltodict](https://github.com/martinblech/xmltodict)
  * [Bautiful Soup](http://www.crummy.com/software/BeautifulSoup)
  * [virtualenv](http://www.virtualenv.org/en/latest/)
  * [Pip installs Python](http://www.pip-installer.org/en/latest/)

**Additional Debian dependencies:**
* libmysqlclient15-dev
* python-dev

***

### Recommended OS:

* Linux

**Reason:** original Entu database is run on Linux. Also the guide is focused on installation procedure in Debian distribution.

**Note 1:** Entu is unlikely to run on Windows since python-mysqld is made for POSIX system and is not promised to work by the mysqld author. Customization for Windows may exist.

**Note 2:** Working on Mac is untested.


## ToDo

* Add other authentication providers (Google, MS Live)
* ...
