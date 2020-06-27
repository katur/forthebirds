var gulp = require('gulp');
var sass = require('gulp-sass');
var hash = require('gulp-hash');

sass.compiler = require('node-sass');

var watchFiles = '**/*.sass';
var inputFilename = 'styles';
var inputFile = 'website/static/stylesheets/' + inputFilename + '.sass';
var outputDirectory = 'website/static/stylesheets/';
var outputFile = outputDirectory + inputFilename + '.css';

var compileCSS = function () {
  return gulp.src(inputFile)
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(gulp.dest(outputDirectory));
}

var makeHash = function () {
  return gulp.src(outputFile)
    .pipe(hash({
      template: '<%= hash %>',
    }))
    .pipe(hash.manifest('forthebirds/static_asset_hashes.json'))
    .pipe(gulp.dest('.'));
}

gulp.task('default', function () {
  gulp.watch(watchFiles, compileCSS);
  gulp.watch(outputFile, makeHash);
});
