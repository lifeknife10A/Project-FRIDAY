# SCH-3 preflight sources

| Requirement | Source reviewed |
| --- | --- |
| Camera schematic | [Raspberry Pi RP-008969-SD Rev R1, pp. 1–2](../../docs/datasheets/Raspberry%20Pi%20Camera%20Module%203%20Schematic.pdf) |
| Camera assembly | [Raspberry Pi Camera Module 3 Sensor Assembly, pp. 2–5](../../docs/datasheets/Raspberry%20Pi%20Camera%20Module%203%20Sensor%20Assembly.pdf) |
| DF37 receptacle | [Hirose DF37NC-30DS-0.4V(51) English reference drawing, pp. 1–3](https://www.hirose.com/en/product/p/CL0684-3313-5-51/documents?path=%2Fapi%2Fv1%2Fproducts%2FCL0684-3313-5-51%2Fdocuments%2Fdrawing_2d%2Fcontent%3Flang%3DEN) · [Hirose DF37 catalog, p. 3](../../docs/datasheets/Hirose_DF37_Series.pdf#page=3) |
| Catalog mating plug | [Hirose DF37C-30DP-0.4V(51) English reference drawing, pp. 1–3](https://www.hirose.com/en/product/p/CL0684-3026-3-51/documents?path=%2Fapi%2Fv1%2Fproducts%2FCL0684-3026-3-51%2Fdocuments%2Fdrawing_2d%2Fcontent%3Flang%3DEN) · [Hirose DF37 catalog, p. 6](../../docs/datasheets/Hirose_DF37_Series.pdf#page=6) |
| DVDD buck and inductor | [Diodes AP3429/A, pp. 1–2, 5, 8–10](../../docs/datasheets/Diodes_AP3429.pdf) · [Coilcraft XFL4020, p. 1](../../docs/datasheets/Coilcraft_XFL4020.pdf) |
| AVDD/AFVDD and DOVDD LDO | [Diodes AP7331, pp. 1–4, 8–11](../../docs/datasheets/Diodes_AP7331.pdf) |
| MCLK oscillator | [SiTime SiT1602B, pp. 2–4, 12–13](../../docs/datasheets/SiTime_SiT1602B.pdf) |
| POR and host enable | [TI TPS386000, pp. 4–8 and 25–29](../../docs/datasheets/TI_TPS386000.pdf) · [TI SN74LV1T34, pp. 3, 6 and 11](../../docs/datasheets/TI_SN74LV1T34.pdf) |
| CSI chokes | [Murata DLP11SN900HL2L, pp. 1–2 and 5](../../docs/datasheets/Murata_DLP11SN900HL2L.pdf) |
| Microphones | [TDK InvenSense INMP441, pp. 5, 8, 11–12 and 15–17](../../docs/datasheets/INMP441%20Datasheet.pdf) |
| I²C timing | [NXP UM10204 Rev 7, pp. 42–43, 50](../../docs/datasheets/NXP_UM10204.pdf) |

The required documents were available through the listed sources. The manufacturer drawing endpoints were accessible through web lookup. Direct download returned HTTP 403 in the workspace, so the repository copy is the public Hirose catalog containing the exact receptacle and plug drawings. The checked text showed ordinary copyright and reference notices. No confidential PDFs were added.

Git had a clean working tree and an empty stash at entry. The Fusion MCP open-document read passed. Existing open Fusion documents belonged to earlier rounds. SCH-3 uses script-driven capture and export.
