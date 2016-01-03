## General
- add word count and character count to text boxes in Admin

## Header
- add chickadees

## Birds
- allow additional photos (slideshow)
- ament main photo url to be flickr ID, and use flickr API to access

## Book
- rename publisher to published_by

## Radio
- BUG: item.clean() throwing exception on initial save; research how to do this better
- research whether podcast should be .xml, .rss, or no extension
- better player that allows jumping

## Webpage
- add image captions from img alt text (with javascript)
- tile layout
- markdown image styling (LCR, wrap/nowrap, etc)
- rebuild existing static pages

## Research
- BUG: slugs not working nested under categories
- add unique_together constraint to category and slug

## Add highly managed slugs to:
- Book
- SpeakingProgram
- WebPage

## Add less managed slugs to:
- Article
- RadioProgram

## Stuff regarding old lauraerickson.com
- hardcode request redirects for popular pages
- for other requests, catchall to old.lauraerickson.com
