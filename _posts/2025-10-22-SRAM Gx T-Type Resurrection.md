---
title: "SRAM T-Type Resurrection"
date: 2025-10-22
layout: post
order: 2
---

How to fix a dead Sram T-Type/Transmission derailleur. There is no official Sram process plan to do this repair. It will void your warranty. As far as I am aware, this will be the first full tutorial on the internet for this particular repair.

![IMG_3310.jpeg](/assets/IMG_3310.jpeg)
*Figure 1*
## Failure Analysis

**Symptoms**: No power. No LED, no shifting, side button does not respond. Battery is confirmed charged using multimeter. Shifting remote pod LED is functional and pod can be connected to via Bluetooth.

**Failure mode**: Pogo pins fail to extend and contact battery.

**Likely root cause**: Galvanic corrosion between pogo pin body and spring, due to water ingress during washing. As pictured in fig. 2, there is a gasket to prevent water and dust ingress, but it does not have a strong sealing pressure, so a jet of water from a hose was the likely source of the ingress.

![IMG_3297.jpeg](/assets/IMG_3297.jpeg)
*Figure 2: Faulty pogo pins*

## Repair
### Materials Needed
#### Tooling
- Soldering iron >400 C
- Third hand or vise
- Tweezers
- Needle nose pliers
- Wrenches:
	- Metric hex
	- Metric tamper-resistant hex
	- Torx wrenches
#### Consumables
- Solder
- Flux
Optional, but recommended:
- IPA 99% w/ brush
- Light grease
- Aluminum foil or wire
#### Replacement Parts
- 2x 6mm pogo pins
	- I sourced these from my old Sram AXS charger, because it was cheaper and faster to source a brand new charger from Amazon than it was to source pogo pins from Digikey or other similar supplier. See [[#Pogo Pin Sourcing]].
### Derailleur Disassembly

The derailleur requires a near complete disassembly to access the circuit board and replace the pogo pins.
0. Optional, but recommended: Move derailleur to most outboard position by forcing electrical contact using aluminum foil or wire. 
	1. The Sram process plan calls for this to take off the parallelogram, which you will need to do.
1. **Ensure battery is removed**.
2. **Remove rear wheel**.
	1. Use the derailleur lockout. Keep the derailleur cage locked for the duration of the repair.
3. **Remove derailleur from bicycle**. 
	1. Remove rear wheel, and uninstall derailleur from mount point.
	2. Fully liberate the derailleur from the bike by removing the inner derailleur cage, unthreading the chain. This step either saves you $30 or fits of rage from having to do this whole repair on the bike.
![IMG_3293.jpeg](/assets/IMG_3293.jpeg)
*Figure 3*
![IMG_3294.jpeg](/assets/IMG_3294.jpeg)
*Figure 4*
4. **Remove skid plate**.
	1. 1x coarse pitch screw, then snap off plastic skid plate.
	2. It's at this time I will inform you that this assembly is very complicated to reassemble and almost every fastener is unique. Keep everything organized: Keep fasteners with the parts they screw into. Keep parts in the same order you take them off the assembly.
5. **Remove both sides of the mount**. 
	1. 5x fine pitched screws.
	2. Don't lose the white bushing on one of the inserts on the gray side of the mount. Its place is as pictured in fig. 3.
![IMG_3295.jpeg](/assets/IMG_3295.jpeg)
*Figure 3*
6. **Remove outer linkage subassembly**.
	1. 2x finely pitched screws. The parallelogram linkage pivots are pins, so the top and bottom of the linkages will slide out of the pins, away from each other, after you remove the screws holding them together.
	2. Parallelogram linkage has a strong spring tension. Be prepared; do not pinch yourself.
	3. If needed use a soft pry tool to pop off the outer links.
![IMG_3300.jpeg](/assets/IMG_3300.jpeg)
*Figure 5*
7. **Remove inner links**.
	1. 2x Hex tamper-proof
	2. The inner links come off much like the outer links, but you will release the spring. It won't come all the way undone, let it relax slowly until it contacts the electronics housing.
	3. The only part connected to the gearbox is the arm originating from the electrical housing, which has a groove for the spring.
	4. Remove the bracket covering the electrical housing with the inner/upper link.
	5. Remove the cage/damper subassembly.
![IMG_3301 1.jpeg](/assets/IMG_3301%201.jpeg)
8. Remove the electrical housing lid.
	1. ESD sensitive operation.
	2. Pop off the plastic cover surrounding the button.
	3. 5x Torx
	4. Be careful to not introduce any FOD to the electrical housing gasket, or to the interior of the housing itself. Use IPA and a brush to clean if needed.
![IMG_3302.jpeg](/assets/IMG_3302.jpeg)
9. Remove PCB from housing.
	1. ESD sensitive operation.
	2. Unplug motor wires.
	3. Remove white motor bracket.
	4. Remove gaskets from pogo pins.
![IMG_3303.jpeg](/assets/IMG_3303.jpeg)
10. Remove pogo pins from PCB.
	1. ESD sensitive operation.
	2. I recommend using a high temp (~380 C) to get these off. They can soak quite a bit of heat before the solder melts, especially the negative pin.
![Pasted image 20251002220658.png](/assets/Pasted%20image%2020251002220658.png)

### Derailleur Reassembly
11. Reinstall new pogo pins.
	1. ESD sensitive operation.
	2. Be extremely careful to get them perfectly straight. Don't oversaturate the board with heat.
	3. A solid vice or third hand helps. I taped my third hand to the bench.
	4. Add additional solder if needed.
![Pasted image 20251002220955.png](/assets/Pasted%20image%2020251002220955.png)
12. Reinstall PCB & replace housing cover.
	1. ESD sensitive operation.
	2. Pogo pin gaskets, motor wires, motor bracket.
	3. Replace cover.
	4. Snap on plastic shield around button.
13. To reassemble: Perform disassembly steps in reverse.
### Pogo Pin Sourcing
It was cheaper and faster to source a brand new charger than it was to source two pogo pins from Digikey or Arrow. So, I ripped the pins out of this old charger:
![IMG_3298.jpeg](/assets/IMG_3298.jpeg)![IMG_3304.jpeg](/assets/IMG_3304.jpeg)