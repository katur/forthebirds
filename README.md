# Laura Erickson's For the Birds

A birder's portfolio and resources for learning about and helping birds.


## Dependencies

Python version is listed in `runtime.txt`.

Package dependencies are listed in `requirements.txt`.
To install:

* clone the repo and cd in
* `python -m venv forthebirds-venv`
* `source forthebirds-venv/bin/activate`
* `pip install -r requirements.txt`


## Database Schema

[Click here](https://www.lucidchart.com/documents/view/a75393ca-f3ce-45e0-8658-e901ae2e41a0)
to view on Lucidchart.

[Click here](https://www.lucidchart.com/publicSegments/view/a3c5059c-139e-40a8-ad5c-bdfdad791a14/image.pdf)
to download PDF.


## Code

Django/Python. Scripts live in the standard location
(`appname/management/commands`).

Javascript uses [jQuery](https://jquery.com).

CSS is in [SASS](http://sass-lang.com).
[gulpfile.js](gulpfile.js) can be used to automate the compilation of
SASS in development.
To set up, assuming [Gulp.js](http://gulpjs.com) is installed on the
system, run the following in the project root (which will install the
dependencies---listed in [package.json](package.json)---in a git-ignored
directory called `node_modules`):
```
npm install --dev-save
```

And to start the gulp build script, run the following in the project root:
```
gulp
```
