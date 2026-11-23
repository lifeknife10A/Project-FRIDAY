# DejaVu Sans Mono Font Specification

- **File**: `DejaVuSansMono.ttf`
- **Release Version**: 2.37 (official release: `https://github.com/dejavu-fonts/dejavu-fonts/releases/download/version_2_37/dejavu-fonts-ttf-2.37.tar.bz2`)
- **License**: Bitstream Vera Fonts License and DejaVu fonts license (permissive open-source, see `LICENSE`)
- **SHA256**: `b4a6c3e4faab8773f4ff761d56451646409f29abedd68f05d38c2df667d3c582`
- **Optical Calibration**:
  - In `plan.md` Gate 1, the Sony IMX415 sensor with 85° FoV at $D = 35\text{ cm}$ provides an analytic text resolution of $\mathbf{12.8\text{ px/char}}$ for $1.8\text{ mm}$ text height.
  - At TrueType font size $21\text{ pt}$, `DejaVuSansMono.ttf` has a measured character advance width of $\mathbf{13.00\text{ px/char}}$ (measured via PIL `ImageDraw.textbbox` and `ImageDraw.textlength`), exactly within the required $12.8 \pm 1.0\text{ px/char}$ window.
