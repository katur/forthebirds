## General
- add word count and character count to text boxes in Admin

## Header
- add chickadee drawings

## Birds
- modify main photo url to be flickr ID, and use flickr API to access
- allow additional photos (slideshow)

## Radio
- BUG: item.clean() throwing exception on initial save; research how to do
  this better (with item.save() instead?)
- research whether podcast should be .xml, .rss, or no extension
- find better audio player that allows jumping

## Webpage
- add image captions from img alt text (with javascript)
- minimal markdown image styling (center everything, min height, min width)
- advanced markdown image styling (LCR, wrap/nowrap, etc)
- rebuild existing static pages (tribute pages, birds of iraq, etc)
- show all miscellany as tiles with background image

## Finalize URL schemes. This includes:

  Highly curated slug-only URLs on:
  - Book
  - SpeakingProgram
  - WebPage

  id followed by optional slug on:
  - Article
  - RadioProgram

  id only on:
  - ResearchCategory and Research

## Stuff regarding old lauraerickson.com
- hardcode request redirects for popular pages
- for other requests, catchall to old.lauraerickson.com
