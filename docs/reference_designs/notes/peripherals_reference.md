# Peripherals Reference: Wi-Fi/BT, Camera CSI, and USB-C

This note synthesizes peripheral circuit implementations from the triaged reference designs (ArmSoM Sige5, ArmSoM CM5-IO, Bit-Brick K1, DshanPI-A1) to guide upcoming schematic rounds (SCH-3 Camera/Bridge, SCH-4 Wireless/Audio).

---

## 1. Wi-Fi / Bluetooth Subsystem (SDIO 3.0 + UART)

### 1.1 Reference Circuits & Citations
- **ArmSoM Sige5:** Sheet 17 (`RK3576-Schematics/Sige5/armsom-sige5-1v3_Sch.pdf`, p.17) — SDIO Wi-Fi 6 / BT 5.2 module (AP6275P / RTL8852BS / RTL8723DS pin-compatible footprint).
- **Bit-Brick K1 SBC:** Sheet 24 (`Bit-Brick-K1/Circuit Diagram Files for Bit-Brick K1 SBC.pdf`, p.24) — On-board Wi-Fi/BT module with 2.4G/5G antenna connector.
- **DshanPI-A1:** Sheet 36 (`RK3576-Schematics/DshanPI-A1/DshanPi-A1-RK3576-SCH_V1.1.pdf`, p.36) — Standard SDIO Wi-Fi + UART Bluetooth implementation.

### 1.2 Interface Architecture & Wiring
- **Wi-Fi SDIO 3.0 Bus:**
  - Pins: `SDIO_CLK`, `SDIO_CMD`, `SDIO_D0`, `SDIO_D1`, `SDIO_D2`, `SDIO_D3` connected to RK3576 SDIO controller.
  - Power: IO voltage domain is `VCCIO_SD_S0` (switches between 3.3V and 1.8V for high-speed SDR104 mode).
  - Decoupling: 0 Ω or 22 Ω series resistor on `SDIO_CLK`; 10 kΩ pull-ups on CMD and D[3:0].
- **Bluetooth Interface:**
  - UART: 4-wire high-speed UART (`UART_TX`, `UART_RX`, `UART_RTS`, `UART_CTS`) connected to RK3576 UART bus.
  - Audio/Voice (optional): I2S / PCM interface for Bluetooth SCO voice audio (`BT_PCM_CLK`, `BT_PCM_IN`, `BT_PCM_OUT`, `BT_PCM_SYNC`).
- **Control & Clocks:**
  - `WL_REG_ON` (GPIO control from PMU/SoC to enable Wi-Fi power domain).
  - `BT_REG_ON` (GPIO control from PMU/SoC to enable BT power domain).
  - `WL_WAKE_HOST` & `BT_WAKE_HOST` (Interrupt inputs to wake SoC from deep sleep).
  - 32.768 kHz RTC clock input (`CLK32K_OUT` / `32KOUT_RTC2WIFI`).
- **Power Rails:**
  - Module core supply: `VCC_3V3_S0` (requires 10 µF + 100 nF local decoupling).
  - I/O voltage: `VCC_1V8_S0` or `VCCIO_SD_S0`.
  - RF Output: 50 Ω matched microstrip route to U.FL antenna connector (`J12` U.FL-R-SMT-1).

---

## 2. Camera MIPI CSI Subsystem

### 2.1 Reference Circuits & Citations
- **ArmSoM Sige5:** Sheet 11 (`armsom-sige5-1v3_Sch.pdf`, p.11) & Sheet 23 (p.23) — Dual MIPI CSI interfaces (CAM0 2-lane, CAM1 4-lane).
- **ArmSoM CM5-IO:** Sheet 5 (`ArmSoM-CM5-IO-1V1_sch.pdf`, p.5) & Sheet 7 (p.7) — MIPI CSI camera FPC connectors.
- **Bit-Brick K1 SBC:** Sheet 17 (`Circuit Diagram Files for Bit-Brick K1 SBC.pdf`, p.17) — MIPI CSI 24-pin connector.
- **DshanPI-A1:** Sheet 31 & 32 (`DshanPi-A1-RK3576-SCH_V1.1.pdf`, pp. 31-32) — Dual camera CSI interfaces.

### 2.2 Interface Architecture & Wiring
- **Differential Pairs:**
  - Data lanes: `MIPI_CSI_D0_P/N`, `MIPI_CSI_D1_P/N` (for 2-lane), and `D2_P/N`, `D3_P/N` (for 4-lane).
  - Clock lanes: `MIPI_CSI_CLK_P/N`.
  - Impedance: 100 Ω differential impedance target.
- **Control & Sync Signals:**
  - I2C Bus: `I2C_SCL`, `I2C_SDA` with 2.2 kΩ pull-up resistors to `VCC_1V8_S0`.
  - Reset & Power Down: `CAM_RST_L` and `CAM_PDN_H` (GPIOs from RK3576).
  - Master Clock: `MCLK` (24 MHz / 27 MHz clock from SoC to sensor).
- **Power Delivery to Camera Modules (e.g. Raspberry Pi Camera Module 3 / IMX708):**
  - `AVDD` (Analog): 2.80 V (via discrete low-noise LDO).
  - `DVDD` (Digital Core): 1.20 V / 1.05 V (via discrete buck/LDO).
  - `DOVDD` (I/O): 1.80 V (from `VCC_1V8_S0`).

---

## 3. USB-C & USB 2.0 OTG Reference Circuits

### 3.1 Reference Circuits & Citations
- **ArmSoM Sige5:** Sheet 22 (`armsom-sige5-1v3_Sch.pdf`, p.22) — Type-C and USB 2.0 Host/OTG ports.
- **Bit-Brick K1 SBC:** Sheet 21 (`Circuit Diagram Files for Bit-Brick K1 SBC.pdf`, p.21) — USB 2.0 Type-C interface.
- **DshanPI-A1:** Sheet 30 (`DshanPi-A1-RK3576-SCH_V1.1.pdf`, p.30) — USB 2.0 OTG port with ESD protection.

### 3.2 Interface Architecture & Wiring
- **Type-C Configuration Channel (CC):**
  - `CC1` and `CC2` pins on Type-C receptacle terminated with 5.1 kΩ ±1% pull-down resistors to GND (R1 and R2 on FRIDAY SCH-1).
  - Configures the port as a standard Upstream Facing Port (UFP / Sink), requesting 5V from any standard USB host or USB PD source without needing a complex PD controller IC.
- **VBUS Protection & Switching:**
  - VBUS TVS diode (e.g. SMBJ5.0A or ESD5641D) for surge clamping.
  - VBUS detection resistor divider (10 kΩ / 15 kΩ) into SoC SARADC for cable attachment sensing.
  - Power muxing via TPS2121 to safely isolate battery power from USB VBUS.
- **High-Speed USB 2.0 Data (D+ / D-):**
  - Ultra-low capacitance ESD protection diode array (USBLC6-2SC6, Cj < 1.0 pF) connected on D+ and D- to prevent signal distortion.
  - 90 Ω differential impedance routing directly to RK3576 `USB20_OTG0_DP` and `USB20_OTG0_DM`.
