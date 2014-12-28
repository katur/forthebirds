# Laura Erickson's For the Birds

A birder's portfolio and resource for helping birds.


## Dependencies

Python version is listed in `runtime.txt`.

Package dependencies are listed in `requirements.txt`.


## Database

[Here](https://www.lucidchart.com/documents/view/a75393ca-f3ce-45e0-8658-e901ae2e41a0)
is the database schema on Lucidchart.


## Code

Django/Python. Scripts live in the standard location (an app's management/commands).

CSS is in [SASS](http://sass-lang.com/). Run
`sass -wc --style compressed website/static/stylesheets/styles.sass`
to compile.

Javascript in [jQuery](http://jquery.com/).


## Migration from old sources
Query to extract Bird-Of-The-Week name from url:

> SELECT species_list.scientific_name, TRIM(TRAILING ".html" FROM
>   SUBSTR(link.link, LOCATE("botw/", link.link) + 5))
> FROM link
> LEFT JOIN species_list ON link.species_id = species_list.id
> WHERE link LIKE "%/botw/%"
