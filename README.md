# Laura Erickson's For the Birds

A birder's portfolio and resource for helping birds.


## Dependencies

Python version is listed in `runtime.txt`.

Package dependencies are listed in `requirements.txt`.


## Database

[Here](https://www.lucidchart.com/documents/view/49ce06b3-0dbd-4cee-8b7c-758e195b583a)
is the database schema on Lucidchart.


## Code

Django/Python. Scripts live in the standard location (an app's management/commands).

CSS is in [SASS](http://sass-lang.com/). Run
`sass -wc --style compressed website/static/stylesheets/styles.sass`
to compile.

Javascript is in [CoffeeScript](http://coffeescript.org/). Run
`coffee --compile website/static/js/*.coffee`
to compile (assuming coffee is installed).

To set up the project for gulping (assuming [Gulp.js](http://gulpjs.com/)
is installed on the system), run the following in the project root
to install project-specific gulp packages in a git-ignored directory called
`node_modules`:

```
npm install --dev-save gulp
npm install --dev-save gulp-util
npm install --dev-save gulp-plumber
npm install --dev-save gulp-ruby-sass
npm install --dev-save gulp-coffee
```


## Migration from old sources
Query to extract Bird-Of-The-Week name from url:

> SELECT species_list.scientific_name, TRIM(TRAILING ".html" FROM
>   SUBSTR(link.link, LOCATE("botw/", link.link) + 5))
> FROM link
> LEFT JOIN species_list ON link.species_id = species_list.id
> WHERE link LIKE "%/botw/%"
