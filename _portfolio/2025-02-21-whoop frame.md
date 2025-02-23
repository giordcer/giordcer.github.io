---
title: "Modular 75mm Whoop Frame"
date: 2023-10-01
layout: post
---
The point of this project was to get my tiny whoop quad flying again, since the injection molded frames I ordered were taking far too long to arrive. 

## Frame

This project was a quick one, whipped up in Onshape. One problem from the injection molded Mobula 7 frame I was trying to solve was that the ducts were prone to breakage while the rest of the frame was still flyable. As such, I designed this frame in two parts so that the ducts could be interchanged from the rest of the frame. Also, this allows for a ductless configuration, which should elicit better flight characteristics.

![Whoop frame](/assets/frame.jpg)

The battery is to be attached by hair tie or rubber band below the flight controller. Four 16mm M2 bolts hold the whole thing together and give the rubber band something to hook on to.

## Lens Hood

I also designed a swappable lens hood to shield the camera from impact. Once I lost my second camera I knew something had to be done to protect it. This one is meant to attach to the stock Mobula 7 canopy with adhesive. Hot glue would be best since it can be cleaned off easily, but all I have is some gelatinous CA, which is what the residue is on the canopy.

![Lens hood after a particularly hard impact](/assets/hood_afterimpact.JPEG)\
*The lens hood did its job during a particularly hard impact onto tile. Shown on an injection molded frame.*

![Lens hood in CAD](/assets/hood.jpg)\
*Lens hood in CAD. I modeled the Mobula 7 canopy in Onshape in order to get a perfect fit.*

## Conclusion
When printed in PETG, this frame is heavier than a proper injection molded frame. However, when no frames are available, this one can be printed quickly and many spares can be made. This is also a great way to convert a whoop to a ductless format -- something I'll be trying when the snow melts. 

**Side note**: I made my own 2.4GHz antenna for this quad after the stock one broke off the flight controller PCB. I actually get better reception with this monopole wire than with the stock SMD helical antenna. The green wire is just visible behind the canopy in the image above.

The antenna can be made by cutting some thin gauge wire to the quarter wavelength of 2.4GHz: 31.25mm. Solid core wire is better than stranded. The wire is soldered directly to the antenna pad on the PCB. Performance would be improved if I soldered an identical wire to the antenna ground pads and oriented it at 90 degrees from the active element.

[Onshape Link](https://cad.onshape.com/documents/4826809f162368ac13344eab/w/c70d77fcc150a07869bcd544/e/41a74c3dc87d9fa099b05880)