---
title: "Coffee Grinder Conversion"
date: 2023-10-01
layout: post
---
The point of this project was less to have an actual coffee grinder and more because I just wanted to build something. That being said, burr grinders (the typical hand crank grinder) have a much better grind quality than typical electric coffee grinders, which have blades like a blender. So, since electric burr grinders are rather expensive compared to their hand crank counterparts, I thought I would have a try at building one myself, using a hand crank grinder's burrs.

![Grinder CAD](/assets/grinder_CAD.jpg)

The project involved integrating a microcontroller, power supply, brushless motor, ESC, and reduction gearbox. 

## Requirements & Calculations
The coffee grinder core I chose to use for this project requires about 1.4 N*m of shaft torque to grind. This was measured using a kitchen scale and a known distance from the shaft. For an acceptable grind rate, I chose 80RPM as a target rotational velocity for the grinder. This means that the grinder requires about 12W of shaft power to operate. Gearbox losses are very significant with 3d printed gears, and especially the sliding contact gearboxes I have tried so far, so I chose a 16V, 32W power supply. I first tried a 12V, 36W power supply, but I wasn't using 3A of current, so I swapped it for the 16V one to get more RPMs. I am still not using the full 2A of rated current on that power supply.

I chose a brushless motor because I thought I might want to scrap this and turn it into a plane in the future.

I calculated the no-load motor RPM by putting a bunch of tape on one side of the motor to unbalance it. Then, I ran the motor with my 12V power supply (I didn't try this with the 16V one) and matched the pitch the motor vibrations made with a keyboard. The motor vibrated at an Ab2, which is 104Hz. 104Hz*60RPM/Hz gives a no-load motor angular velocity of 6240RPM. I wasn't interested in spending the time to solve the equations to figure out what the loaded RPM would be, but I assumed it would be 90% of the no-load RPM to calculate the required gear reduction.

To get an 80RPM (12W shaft power) output with a 5616RPM input, a gearbox with a ~80:1 reduction is required. It was very hard to find gearboxes that provide this amount of reduction in the form factor that I wanted. I started with a worm drive and currently the design uses a staged split ring planetary gearbox. In the future I will probably either design a true split ring Wolfrom drive (no sliding contact) or use 2 belts in series to provide the reduction needed, since this gearbox gets very warm and the PETG can soften too much when grinding light roasts. However, for darker roasts or shorter periods of time, this design works great.

## First Build

An early version of the coffee grinder used a worm drive, but suffered from vibration & the helical gear was prone to popping off the grinder shaft. However, its electronics enclosure was roomy despite how short & compact it was. I don't have a picture of it with the worm integrated. 

![Worm drive grinder](/assets/grinder_worm.JPEG)

## A New Design

After graduating, I lost my student Solidworks license and moved to Onshape. The first thing I designed was a new version of the grinder, using a split-ring gearbox I found on [Michael Rechtin's YouTube channel](https://www.youtube.com/watch?v=d9P5LBQqgFo):

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

[Onshape link](https://cad.onshape.com/documents/a8f6d220e42aa0f698fa49dd/w/ad4594e7f4a60be1f675f96d/e/5e049caf246cccc6c2610eea?renderMode=0&uiState=67bba943fd9b866452c4f9f6)

