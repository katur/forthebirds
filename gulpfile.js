var gulp = require('gulp');
var util = require('gulp-util');
var plumber = require('gulp-plumber');
var sass = require('gulp-ruby-sass');

var sassMain = 'website/static/stylesheets/styles.sass';
var cssDir = 'website/static/stylesheets/';

gulp.task('default', function() {
  gulp.run('compileSass')
  gulp.watch('**/*.sass', ['compileSass']);
});

gulp.task('compileSass', function() {
  return sass(sassMain)
    .on('error', sass.logError)
    .pipe(gulp.dest(cssDir));
});
