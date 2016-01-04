# TODO BEFORE FLIPPING SWITCH

## Header
- add chickadee drawings

## Radio
- BUG: item.clean() throwing exception on initial save, since audio file is not
  yet saved. research how to do this better (with item.save() instead?)
- research whether podcast should be .xml, .rss, or no extension

## Webpage
- add image captions from img alt text (with javascript)
- minimal markdown image styling (center everything, min height, min width)
- finalize Harry Potter page

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

## Redirection stuff
- hardcode 401 redirects for popular pages
- for other requests, catchall to v0.lauraerickson.com


# TODO AFTER FLIPPING SWITCH

## General
- add word count and character count to text boxes in Admin

## Birds
- modify main photo url to be flickr ID, and use flickr API to access
- allow additional photos (slideshow)

## Radio
- find better audio player that allows jumping

## Webpage
- advanced markdown image styling (LCR, wrap/nowrap, etc)
- rebuild all existing static pages (tribute pages, birds of iraq, etc)
- show all miscellany as tiles with background image

## Research
- rename Research to ResearchItem

## Images
- Standardize image model scheme (ABAFieldGuideImage vs UploadedImage vs
  Creation)
