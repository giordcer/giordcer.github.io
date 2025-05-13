---
title: "Retraction"
date: 2025-05-13
layout: post
---
#3dprinting
In OrcaSlicer, retraction speed and distance are set in the printer's settings.
# Ideal Retraction

| Filament              | Retraction Length \[mm] | Retraction Speed \[mm/s] | Deretraction Speed \[mm/s] | Notes                                                                                        |
| --------------------- | ----------------------- | ------------------------ | -------------------------- | -------------------------------------------------------------------------------------------- |
| PETG (Overture clear) | 5                       | 60                       | 40                         | 5mm is what I had in Cura, while the speeds are Orca defaults (Cura was at 50 mm/s for both) |


# Retraction Tests
## [[2025-03-30]]
### Part 1
0-2mm retraction, 20 steps, 0.1mm increment
Overture clear PETG, 255* hotend
![[Pasted image 20250330095940.jpg]]
- 0-1mm is totally unusable
- After 1mm retraction, things start to get better
- The best range was from step 13 to 16 (1.3mm to 1.6mm retraction)
- There was more stringing after 16mm retraction
	- Was this due to cavitation/ventilation within the nozzle, causing filament to linger around the nozzle opening?
		- Future Gio here: I still really don't know, but I'm also going to submit the possibility that the filament during that portion of the test had slightly different properties. Another test should confirm or disprove that hypothesis.
### Part 2
- Part 1 was wrong (I accidentally put 0.15 mm retraction in the slicer settings, and to top it off, I put in 15 mm retraction in this page's table.)
- Cura has pretty good performance with a retraction of 5mm. So I will keep that for now. 
- Cura's retraction speed is 50 mm/s for both the retract and the prime speed
	- I don't think this is default, I must have set this at some point. I know I altered the retraction distance.
- These settings will be Orcaslicer defaults for the time being.
# Future tests
- [ ] test from 2mm-7mm (Orcaslicer default is 4mm)