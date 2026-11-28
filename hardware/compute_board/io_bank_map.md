# SCH-1 RK3576 I/O bank map

Voltages and source rails are from the revised SCH-1 Fusion netlist. Peripheral muxes marked planned are assignments for the later memory and peripheral sheets. Ball names follow the RK3576 symbol and EVB.

| Bank | Supply ball(s) | Voltage | SCH-1 source | Signals or planned peripherals | Reference |
| --- | --- | --- | --- | --- | --- |
| PMUIO0 | 2K11 | 1.8 V | `VCC_1V8_S3`, U2 BUCK8 | Wired I2C1_M0 SCL/SDA (1T22/1T23) to RK806 through R1122/R1123. R5/R6 pull up to the PMIC's 1.8 V `VCCA1V8_PLDO6_S3`. PMIC power control and interrupt use this bank. | EVB PDF pp. 6 and 11, U1000D, R1122/R1123 |
| PMUIO1 | 1U20 | 3.3 V | `VCC_3V3_S3`, U2 BUCK4 | Wired UART0_M0 debug TX/RX (1U24/AA28) to TP1/TP2 via R9906/R9905. The pads are for a 3.3 V logic adapter. | EVB PDF pp. 6, 11 and 27 |
| VCCIO0 | 1J20 | 1.8 V | `VCC_1V8_S0`, U9 switched from BUCK8 | Planned eMMC bus for the eMCP (D0–D7, CMD, CLK, STRB, RSTn). I/O VCCQ is 1.8 V. The eMMC core has a separate 3.3 V VCC supply. | EVB PDF pp. 6 and 13, U1000C, C1308. HDG §2.1.11.1 |
| VCCIO1 | 2A8 | 3.3 V nominal | `VCCIO_SD_S0`, U2 PLDO5 | SDMMC0 bank. No peripheral assigned in SCH-1. | EVB PDF pp. 6 and 13, U1000C, C1309 |
| VCCIO2 | 2A2 | 1.8 V | `VCC_1V8_S0`, U9 switched from BUCK8 | Planned I²S on SAI1_M0. BCLK 1C6, LRCK 1B6, SDO0 A7, SDI0 1A6. | EVB PDF pp. 5, 6 and 18, U1000F, SAI1_M0 mux |
| VCCIO3 | 2B10 | 1.8 V | `VCCIO_WL`, through R2427 (0 Ω) from `VCC_1V8_S3` | Planned RTL8723DS SDMMC1_M0. D0–D3 A28/B27/1A23/A27, CMD B26, CLK 1B22. The radio's 3.3 V supply and its 1.8 V SDIO signaling use separate rails. | EVB PDF pp. 6, 18 and 22, U1000G, C1801, R2427/C2423. RTL8723DS-CG DS §§7.4.1–7.4.2 |
| VCCIO4 | 2A7 | 3.3 V | `VCC_3V3_S0`, U8 switched from BUCK4 | No peripheral assigned in SCH-1. | EVB PDF pp. 6 and 19, U1000H, C1901 |
| VCCIO5 | 2A4, 2A5 | 1.8 V | `VCC_1V8_S0`, U9 switched from BUCK8 | Planned IMX708 control on I2C4_M3 for CSI0, SCL 1E9 and SDA 1D12, with pull-ups to 1.8 V. | EVB PDF pp. 6 and 19, U1000I, C1903, I2C4_M3_MIPI_CSI0 |
| VCCIO6 | 2N3 | 3.3 V | `VCC_3V3_S0`, U8 switched from BUCK4 | No peripheral assigned in SCH-1. | EVB PDF pp. 6 and 18, U1000J, C1802 |
| VCCIO7 | 2M3 | 1.8 V | `VCC_1V8_S0`, U9 switched from BUCK8 | GPIO4_D0/D1 available. UFS is unused and neither pin is assigned. | EVB PDF pp. 6 and 13, U1000K, C1300. HDG §2.1.11.1 |

SW1 MaskROM is wired to RK3576 SARADC_IN0 (A25) via R18. SW2 is wired to RK806 PWRON (pin 4) via R9006. Both keys use dedicated inputs outside the GPIO banks. (EVB PDF pp. 11, 21 and 26.)

The planned 1.8 V peripheral signals in the table all use 1.8 V banks. The audio interconnect lists a 3.3 V feed. An INMP441 powered directly from it requires a logic-high input of at least 2.31 V (0.7 × VDD). For the later audio sheet, the 1.8 V SAI1 assignment requires a 1.8 V microphone rail or translation at the microphone interface. The microphone rail and camera reset/power-down GPIO assignments are **UNVERIFIED** for that sheet. (INMP441 DS p. 5, Digital Input. Project component specification §8.)

SCH-2 Y3 records a 1.8 V INMP441 supply for the future audio sheet, matching the 1.8 V SAI1_M0 bank. (INMP441 DS p. 5.)
