---
title: "Migrating from Apple Notes to Obsidian"
date: 2025-03-22
layout: post
order: 2
---
Apple notes are a problem for me -- I love the app, it works really well with almost all of my devices & in the browser, but they are locked in: Apple provides no easy way to bulk export thousands of notes. What if Apple were to go bankrupt and all my Apple devices were smashed in a meteorite impact? So, I was pleased to find out that migrating from Apple Notes to Obsidian has become easy.

The Obsidian team provides a plugin called "Importer" that makes migrating from other notes apps very easy. One thing that I was very pleased with is that it works with Apple notes on Mac. There are other services which aim to export Apple notes from Mac, but when I looked into them, they all seemed hacky. A concern I had with converting the Apple notes format to Markdown was that Apple notes can have drawings, a feature which I have been a heavy user of. I did migrate my most of my handwritten notes to Goodnotes (for a variety of reasons), but a large portion of my Apple notes are still handwritten.

In this article I am going to walk through how I did it. In another article I will discuss Obsidian data sync between platforms.

## Migration Steps

1. Download Obsidian for Mac.
The only platform which can migrate Apple Notes to Obsidian is on Mac. This is because iOS apps are highly sandboxed with no access to system files. Macs do not have this problem.
2. Install the "Importer" community plugin.
Even though it is a community plugin, it is developed by the Obsidian team.
3. Follow the on-screen steps. It runs relatively quickly.

## Notes
- I did get a ton of errors, I think related to some drawings. I did not care to go through my hundreds of handwritten pages to determine which ones failed to import, but most seem to have made it.
- The images from your Apple Notes all dump into the Obsidian vault root directory. 
	- This is due to the way Markdown files handle images.
	- I cleaned them up into an "images" folder and the links to their respective notes were not broken.
