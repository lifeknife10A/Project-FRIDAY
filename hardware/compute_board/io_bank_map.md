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

## SCH-4b inter-board and audio assignments

The accepted SCH-2 rails supply these interfaces. GPIO selections are for the SCH-4b compute sheet and its firmware pinmux only.

| Bank or domain | Ball(s) | Supply | SCH-4b function | Source |
| --- | --- | --- | --- | --- |
| CSI0 DCPHY | AK20 / AL20, AK21 / AL21, AK22 / AL22 | Dedicated CSI0 PHY domains from SCH-1 | D0 P/N, D1 P/N and CLK P/N on J5. CSI1–4 and other CSI0 lanes retain their baseline state. | RK3576 DS §2, ball list |
| VCCIO5 | 1E9, 1D12 | 1.8 V `VCC_1V8_S0` | I2C4_M3 SCL/SDA on J5. Open drain, pull-ups only on SCH-3 bridge to local DOVDD. | EVB PDF p. 19, U1000I |
| VCCIO5 | 1D7, 1D9 | 1.8 V `VCC_1V8_S0` | GPIO3_C6 requests CAM_ENABLE through the local 1.8 V buffer. GPIO3_C4 authorizes the USB charge branch through its buffer. Both have 100 kΩ pulldowns at the GPIO. | EVB PDF p. 19, U1000I and RK3576 DS §2 |
| VCCIO2 | 1C6, 1B6, A7, 1A6 | 1.8 V `VCC_1V8_S0` | SAI1_M0 BCLK, LRCK, SDO0 and SDI0. BCLK/LRCK have 22 Ω source damping. SDO0 feeds both amps. SDI0 comes from the bridge mics. | EVB PDF p. 18, U1000F and RK3576 HDG audio routing |
| VCCIO2 | 1D6, 1C5 | 1.8 V `VCC_1V8_S0` | GPIO4_A2 drives SD_MODE_L through J6. GPIO4_A4 drives the right amp selector. High enables the assigned channel. Low or high-impedance shuts down. | EVB PDF p. 18, U1000F and RK3576 DS §2 |
| VCCIO7 | 1AD2, AK4 | 1.8 V `VCC_1V8_S0` | GPIO4_D0 / GPIO4_D1 read DOCK_DET / CHG_STAT on J6. A 10 kΩ pull-up per pin is on compute. | EVB PDF p. 13, U1000K, and auxiliary interconnect CSV |
| PMUIO0 | 1U21 | 1.8 V `VCC_1V8_S3` | GPIO0_A7 drives a local N-FET open-drain sink. GPIO high pulls J6 CHG_EN low. A 4.7 kΩ pull-up to the PMU I/O supply releases the line. | EVB PDF p. 11, U1000D, and auxiliary interconnect CSV |
| SARADC | 1B19 | 1.8 V `SARADC_AVDD1V8` | SARADC_IN2 pack monitor through a filtered high-value divider and powered-off isolation switch. A25 boot input keeps its existing role. | RK3576 DS §§2, 3.2 and 3.9, HDG PDF pp. 85–86 |
