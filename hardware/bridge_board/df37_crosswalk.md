# DF37 crosswalk — UNPROVEN

[30-row logical crosswalk](df37_crosswalk.csv)

RP-008969-SD p. 2 identifies the camera module top-view corners as pins 1 and 15 above pins 30 and 16. The Hirose DF37 catalog p. 3 shows the exact receptacle and p. 6 shows its catalog mating plug. Both drawings describe these parts as unpolarized. The EAGLE footprint places pad 01 at (+2.8, −1.325) mm and pad 02 at (+2.8, +1.325) mm. Odd and even pad numbers occupy opposing rows. The Pi top view and the library therefore use different numbering conventions. [Pi schematic p. 2](../../docs/datasheets/Raspberry%20Pi%20Camera%20Module%203%20Schematic.pdf#page=2) · [Hirose DF37 pp. 3, 6](../../docs/datasheets/Hirose_DF37_Series.pdf#page=3) · [Library pad coordinates](../../libraries/DF37NC-30DS-0.4V_51_.lbr#L137)

The published Sensor Assembly drawing gives outline and tail dimensions. The missing evidence is a numbered contact-side view of the actual SA31VA30P factory tail tied to a mechanical landmark, together with registration to the carrier receptacle top view. The catalog pairing and library alone establish no mapping from the Pi logical numbers to those physical contacts. [Assembly pp. 4–5](../../docs/datasheets/Raspberry%20Pi%20Camera%20Module%203%20Sensor%20Assembly.pdf#page=4) · [Exact Hirose drawing links](SCH-3_sources.md)

**For Krishna.** Supply the actual SA31VA30P supplier connector/tail drawing showing all 30 contacts and a visible orientation landmark in the installed view, or supply an unpowered 30-contact continuity map against a genuine Camera Module 3 carrier, keyed to the carrier PCB face and the installed tail exit direction. The map needs an entry for each contact, including unconnected pins, and must distinguish 180° insertion. Verify the actual plug and intended receptacle seating before taking measurements.

**Capture consequence.** J1 remains completely unwired. Pi p. 2 ties logical 1 (AFVDD) and 10 (VA2V8) to 2.8 V, logical 3 (VO1V8) to local 1.8 V, and logical 4 (DVDD) and 11 (DVDD/GPIO) to 1.1 V. These are logical assignments pending contact proof. Pi's 600 mA core design ceiling still requires an actual current-sharing measurement at the factory contacts.
