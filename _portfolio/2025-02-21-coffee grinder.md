---
title: "Coffee Grinder Conversion"
date: 2023-10-01
layout: post
---
The point of this project was less to have an actual coffee grinder and more because I just wanted to build something. That being said, burr grinders (the typical hand crank grinder) have a much better grind quality than typical electric coffee grinders, which have blades like a blender. So, since electric burr grinders are rather expensive compared to their hand crank counterparts, I thought I would have a try at building one myself, using a hand crank grinder's burrs.

The project involved integrating a microcontroller (ESP32), power supply, brushless motor, ESC, and reduction gearbox. 

## First Build

An early version of the coffee grinder used a worm drive, but suffered from vibration & the helical gear was prone to popping off the grinder shaft. However, its electronics enclosure was roomy despite how short & compact it was. I don't have a picture of it with the worm integrated. 

![Worm drive grinder](/assets/grinder_worm.JPEG)

## A New Design

After graduating, I lost my student Solidworks license and moved to Onshape. The first thing I designed was a new version of the grinder, using a split-ring gearbox:

![Split ring gearbox](/assets/grinder_gearbox_top.JPEG)

The gearbox had some problems at first, but I increased density in the finely pitched teeth by reprinting with a 0.2mm nozzle, which strengthened the teeth.

![planet printed with 0.4mm nozzle](/assets/grinder_0.4mm_gear.JPEG)\
*Tooth failure where the split rings meet the planet gears. Note the hollowness caused by the 0.4mm nozzle being too large to completely fill in the teeth.*
<br>

This new design resulted in a slimmer, taller grinder, but I was still able to pack the electronics into the new enclosure:

![loose electronics being flashed](/assets/grinder_flashingfirmware.JPEG)\
*Flashing firmware using PlatformIO. The microcontroller was used to send PWM signals to the ESC after it was turned on via switch. The whole thing was powered via 16v through the barrel jack.*
<br>

![Electronics crammed into enclosure](/assets/grinder_electronics.JPEG)\
*No wasted space: The width of the grinder body was designed to accommodate the ESC & ESP32 as well as the wires.*
<br>

Here's a video of the grinder in action:
<iframe width="560" height="315" src="https://www.youtube.com/embed/ECKTrz1fkBU?si=uUUsFpfrg9SYrXRJ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## Roadmap
In the future I plan to upgrade the gearbox to a version that does not involve sliding contact on the 3d printed gears to increase their lifespan. I could implement a Wolfrom drive or a belt-driven system. I could also use a stronger material or a material with a reduced friction coefficient, but I cannot print more exotic materials on this enclosure-less printer.



