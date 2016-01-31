# Laura Erickson's For the Birds

A birder's portfolio and resource for helping birds.


## Dependencies

Python version is listed in `runtime.txt`.

Package dependencies are listed in `requirements.txt`.

Due to a release issue with django-private-media, do these two steps for
Django 1.9 compatibility:
```
pip uninstall django-private-media
pip install git+https://github.com/RacingTadpole/django-private-media.git
```


## Database Schema

[Click here](https://www.lucidchart.com/documents/view/a75393ca-f3ce-45e0-8658-e901ae2e41a0)
to view on Lucidchart.

[Click here](https://www.lucidchart.com/publicSegments/view/a3c5059c-139e-40a8-ad5c-bdfdad791a14/image.pdf)
to download PDF.


## Code

Django/Python. Scripts live in the standard location (an app's management/commands).

CSS is in [SASS](http://sass-lang.com/).

Javascript is in [CoffeeScript](http://coffeescript.org/).

To compile both the CSS and Javascript, use gulp.
After installing [Gulp.js](http://gulpjs.com/),
run the following in the project root
to install project-specific gulp packages in a git-ignored directory called
`node_modules`:

```
npm install --dev-save gulp
npm install --dev-save gulp-util
npm install --dev-save gulp-plumber
npm install --dev-save gulp-ruby-sass
npm install --dev-save gulp-coffee
```

To compile, simply run `gulp` in the project root.
