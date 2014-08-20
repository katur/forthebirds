# Laura Erickson's For the Birds

A birder's portfolio and resource for helping birds.


## Dependencies

Python version is listed in `runtime.txt`.

Package dependencies are listed in `requirements.txt`.


## Database

[Here](https://www.lucidchart.com/documents/view/a75393ca-f3ce-45e0-8658-e901ae2e41a0)
is the database schema on Lucidchart.

[South](http://south.readthedocs.org/en/latest/) is used for database migrations.


## Code

Django/Python. Scripts live in the standard location (an app's management/commands).

CSS is in [SASS](http://sass-lang.com/). Run
`sass -wc --style compressed website/static/stylesheets/styles.sass`
to compile.

Javascript in [jQuery](http://jquery.com/).
