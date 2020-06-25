var gulp = require('gulp');
var sass = require('gulp-sass');

sass.compiler = require('node-sass');

var watchFiles = '**/*.sass';
var inputFile = 'website/static/stylesheets/styles.sass';
var outputDirectory = 'website/static/stylesheets/';

var compileCSS = function () {
  return gulp.src(inputFile)
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(gulp.dest(outputDirectory));
}

gulp.task('default', function () {
  gulp.watch(watchFiles, compileCSS);
});
