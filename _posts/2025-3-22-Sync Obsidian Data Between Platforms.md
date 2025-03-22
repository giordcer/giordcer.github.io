---
title: "Sync Obsidian Data Between Platforms"
date: 2025-03-22
layout: post
---
Data sync is very important to me. I want to work quickly and effectively at my desk and leave the house and pick up where I left off on the go. Here I'll discuss some different options, their pros and cons, and what I ended up going with.

## Ways to sync between Linux and other platforms
- rclone & iCloud integration
- Remotely Save plugin
- Obsidian Sync
- Github & Working Copy integration

### rclone & iCloud integration
My main desktop computer runs Linux, which means I cannot use iCloud drive, my cloud provider of choice. Apple provides no way to mount an iCloud Drive on the system the same way it works on Windows and Mac. Google Drive and MS OneDrive do support this, but I don't want those companies to have my data. Luckily a program called [rclone](https://rclone.org/) committed a feature to beta that integrates iCloud Drive.

I [[Set up rclone & iCloud Drive on a Linux machine]] successfully, but did not pursue this because of how Obsidian on iOS cannot access folders outside its sandbox.

### Remotely Save plugin

Remotely Save is a community plugin that providees the ability to use a number of different cloud providers to sync data between Obsidian instances. Primarily, it supports AWS S3-type bucket services, but it also supports other ones, like OneDrive and Webdav. 

One downside of this plugin is that true Git-style conflict resolution is a paid tier. However, conflict resolution in the style of "newer files survive" is free, and this is good enough for notes where I'm the only one editing them.

AWS S3 isn't free but it's [so cheap](https://aws.amazon.com/s3/pricing/) ($0.02/Gb/mo) that its true cost wasn't even worth calculating to me. It's so cheap, it's basically free. It also has a 12 month free trial with 5 free Gb. API calls do cost money but they are also incredibly cheap. 

Side note: Lex Fridman wasn't lying when he said the AWS interface is really bad.

### Obsidian Sync

Probably the nicest option is Obsidian Sync, as it "just works." I didn't try it because it costs $4 a month for 1Gb. Which is ridiculous. However if I didn't feel competent enough to try any other solutions I would use this. It is definitely the easiest way to sync and the funds go towards supporting the Obsidian team. 

### Github & Working Copy

I'm not going to get too into the weeds, but there is a way to use iOS automations and Obsidian plugins to automatically push and pull your vault to repository, which would be a free option, if the app that enables pushing to Git on iOS (Working Copy) weren't $20. 


## What I went with

I ended up choosing Remotely Save because of how cheap S3 is. The plugin has a lot of configuration, but it works well enough, and I haven't had any problems yet. 

My configuration uses AWS S3 well within the free tier. I have configured the plugin on all my devices to refresh the vault every minute, as well as when Obsidian is opened. 

