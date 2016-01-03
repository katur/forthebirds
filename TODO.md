## General
- add word count and character count to text boxes in Admin

## Header
- add chickadees

## Birds
- allow additional photos (slideshow)
- ament main photo url to be flickr ID, and use flickr API to access

## Book
- publisher -> published_by

## Radio
- item.clean() not being run on save; research how to do this
- research whether podcast should be .xml, .rss, or no extension
- better player that allows jumping

## Webpage
- add image captions from img alt text (with javascript)
- tile layout
- markdown image styling (LCR, wrap/nowrap, etc)
- rebuild existing static pages

## Research
- add unique_together constraint to category and slug

## Add very managed slugs to:
- Book
- Research Category
- SpeakingProgram
- WebPage

## Add less managed slugs to:
- Article
- RadioProgram
- Research Item

## Stuff regarding old lauraerickson.com
- hardcode request redirects for popular pages
- for other requests, catchall to old.lauraerickson.com
