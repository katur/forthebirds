# Laura Erickson's For the Birds

A birder's portfolio and resources for learning about and helping birds.


## Installation

1. Install the version Python listed in `runtime.txt`
1. Create a virtual environment for the project with `mkvirtualenv forthebirds`
1. Install the python dependencies with `pip install -r requirements.txt`
1. Add your `localsettings.py` file (see `forthebirds/localsettings.sample.py`)
1. Start the site with the command `./manage.py runserver`


## Database Schema

[Click here](https://www.lucidchart.com/documents/view/a75393ca-f3ce-45e0-8658-e901ae2e41a0)
to view on Lucidchart.

[Click here](https://www.lucidchart.com/publicSegments/view/a3c5059c-139e-40a8-ad5c-bdfdad791a14/image.pdf)
to download PDF.


## Code

Django/Python. Scripts live in the standard location
(`appname/management/commands`).

Javascript uses [jQuery](https://jquery.com).

CSS is written in [SASS](http://sass-lang.com), and uses
[gulp](gulpfile.js) to automate the compilation of SASS in development.
Assuming you have [NPM](https://www.npmjs.com/get-npm), install the
project's dependencies--listed in [package.json](package.json)--
by running the following in the project root:
```
npm install --dev-save
```

And to start the gulp build script, run the following in the project root:
```
npx gulp
```
