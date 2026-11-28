<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="9.6.2">
  <drawing>
    <settings>
      <setting alwaysvectorfont="no" />
      <setting verticaltext="up" />
    </settings>
    <grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="yes" altdistance="0.01" altunitdist="inch" altunit="inch" />
    <layers>
      <layer number="1" name="Top" color="4" fill="1" visible="yes" active="yes" />
      <layer number="16" name="Bottom" color="1" fill="1" visible="yes" active="yes" />
      <layer number="17" name="Pads" color="2" fill="1" visible="yes" active="yes" />
      <layer number="18" name="Vias" color="2" fill="1" visible="yes" active="yes" />
      <layer number="19" name="Unrouted" color="6" fill="1" visible="yes" active="yes" />
      <layer number="20" name="Dimension" color="15" fill="1" visible="yes" active="yes" />
      <layer number="21" name="tPlace" color="7" fill="1" visible="yes" active="yes" />
      <layer number="22" name="bPlace" color="7" fill="1" visible="yes" active="yes" />
      <layer number="23" name="tOrigins" color="15" fill="1" visible="yes" active="yes" />
      <layer number="24" name="bOrigins" color="15" fill="1" visible="yes" active="yes" />
      <layer number="25" name="tNames" color="7" fill="1" visible="yes" active="yes" />
      <layer number="26" name="bNames" color="7" fill="1" visible="yes" active="yes" />
      <layer number="27" name="tValues" color="7" fill="1" visible="yes" active="yes" />
      <layer number="28" name="bValues" color="7" fill="1" visible="yes" active="yes" />
      <layer number="29" name="tStop" color="7" fill="3" visible="yes" active="yes" />
      <layer number="30" name="bStop" color="7" fill="6" visible="no" active="yes" />
      <layer number="31" name="tCream" color="7" fill="4" visible="yes" active="yes" />
      <layer number="32" name="bCream" color="7" fill="5" visible="no" active="yes" />
      <layer number="39" name="tKeepout" color="4" fill="11" visible="yes" active="yes" />
      <layer number="40" name="bKeepout" color="1" fill="11" visible="yes" active="yes" />
      <layer number="41" name="tRestrict" color="4" fill="10" visible="yes" active="yes" />
      <layer number="42" name="bRestrict" color="1" fill="10" visible="yes" active="yes" />
      <layer number="43" name="vRestrict" color="2" fill="10" visible="yes" active="yes" />
      <layer number="44" name="Drills" color="7" fill="1" visible="no" active="yes" />
      <layer number="45" name="Holes" color="7" fill="1" visible="no" active="yes" />
      <layer number="46" name="Milling" color="3" fill="1" visible="no" active="yes" />
      <layer number="47" name="Measures" color="7" fill="1" visible="no" active="yes" />
      <layer number="48" name="Document" color="7" fill="1" visible="yes" active="yes" />
      <layer number="49" name="Reference" color="7" fill="1" visible="yes" active="yes" />
      <layer number="51" name="tDocu" color="7" fill="1" visible="yes" active="yes" />
      <layer number="52" name="bDocu" color="7" fill="1" visible="yes" active="yes" />
      <layer number="88" name="SimResults" color="9" fill="1" visible="yes" active="yes" />
      <layer number="89" name="SimProbes" color="9" fill="1" visible="yes" active="yes" />
      <layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes" />
      <layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes" />
      <layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes" />
      <layer number="93" name="Pins" color="2" fill="1" visible="yes" active="yes" />
      <layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes" />
      <layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes" />
      <layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes" />
      <layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes" />
      <layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes" />
    </layers>
    <schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
      <libraries>
        <library name="FRIDAY_SCH1_Support">
          <packages>
            <package name="R0201">
              <smd name="1" x="-0.3" y="0" dx="0.32" dy="0.32" layer="1" />
              <smd name="2" x="0.3" y="0" dx="0.32" dy="0.32" layer="1" />
              <wire x1="-0.35" y1="-0.2" x2="0.35" y2="-0.2" width="0.127" layer="21" />
              <wire x1="0.35" y1="-0.2" x2="0.35" y2="0.2" width="0.127" layer="21" />
              <wire x1="0.35" y1="0.2" x2="-0.35" y2="0.2" width="0.127" layer="21" />
              <wire x1="-0.35" y1="0.2" x2="-0.35" y2="-0.2" width="0.127" layer="21" />
              <text x="-0.35" y="0.6000000000000001" size="0.8" layer="25">&gt;NAME</text>
              <text x="-0.35" y="-1.3" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="R0402">
              <smd name="1" x="-0.5" y="0" dx="0.55" dy="0.6" layer="1" />
              <smd name="2" x="0.5" y="0" dx="0.55" dy="0.6" layer="1" />
              <wire x1="-0.6" y1="-0.35" x2="0.6" y2="-0.35" width="0.127" layer="21" />
              <wire x1="0.6" y1="-0.35" x2="0.6" y2="0.35" width="0.127" layer="21" />
              <wire x1="0.6" y1="0.35" x2="-0.6" y2="0.35" width="0.127" layer="21" />
              <wire x1="-0.6" y1="0.35" x2="-0.6" y2="-0.35" width="0.127" layer="21" />
              <text x="-0.6" y="0.75" size="0.8" layer="25">&gt;NAME</text>
              <text x="-0.6" y="-1.4500000000000002" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="R0603">
              <smd name="1" x="-0.8" y="0" dx="0.9" dy="0.95" layer="1" />
              <smd name="2" x="0.8" y="0" dx="0.9" dy="0.95" layer="1" />
              <wire x1="-0.9" y1="-0.5" x2="0.9" y2="-0.5" width="0.127" layer="21" />
              <wire x1="0.9" y1="-0.5" x2="0.9" y2="0.5" width="0.127" layer="21" />
              <wire x1="0.9" y1="0.5" x2="-0.9" y2="0.5" width="0.127" layer="21" />
              <wire x1="-0.9" y1="0.5" x2="-0.9" y2="-0.5" width="0.127" layer="21" />
              <text x="-0.9" y="0.9" size="0.8" layer="25">&gt;NAME</text>
              <text x="-0.9" y="-1.6" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="C0201">
              <smd name="1" x="-0.3" y="0" dx="0.32" dy="0.32" layer="1" />
              <smd name="2" x="0.3" y="0" dx="0.32" dy="0.32" layer="1" />
              <wire x1="-0.35" y1="-0.2" x2="0.35" y2="-0.2" width="0.127" layer="21" />
              <wire x1="0.35" y1="-0.2" x2="0.35" y2="0.2" width="0.127" layer="21" />
              <wire x1="0.35" y1="0.2" x2="-0.35" y2="0.2" width="0.127" layer="21" />
              <wire x1="-0.35" y1="0.2" x2="-0.35" y2="-0.2" width="0.127" layer="21" />
              <text x="-0.35" y="0.6000000000000001" size="0.8" layer="25">&gt;NAME</text>
              <text x="-0.35" y="-1.3" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="C0402">
              <smd name="1" x="-0.5" y="0" dx="0.55" dy="0.6" layer="1" />
              <smd name="2" x="0.5" y="0" dx="0.55" dy="0.6" layer="1" />
              <wire x1="-0.6" y1="-0.35" x2="0.6" y2="-0.35" width="0.127" layer="21" />
              <wire x1="0.6" y1="-0.35" x2="0.6" y2="0.35" width="0.127" layer="21" />
              <wire x1="0.6" y1="0.35" x2="-0.6" y2="0.35" width="0.127" layer="21" />
              <wire x1="-0.6" y1="0.35" x2="-0.6" y2="-0.35" width="0.127" layer="21" />
              <text x="-0.6" y="0.75" size="0.8" layer="25">&gt;NAME</text>
              <text x="-0.6" y="-1.4500000000000002" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="C0402_BGA">
              <smd name="1" x="-0.5" y="0" dx="0.55" dy="0.6" layer="1" />
              <smd name="2" x="0.5" y="0" dx="0.55" dy="0.6" layer="1" />
              <wire x1="-0.6" y1="-0.35" x2="0.6" y2="-0.35" width="0.127" layer="21" />
              <wire x1="0.6" y1="-0.35" x2="0.6" y2="0.35" width="0.127" layer="21" />
              <wire x1="0.6" y1="0.35" x2="-0.6" y2="0.35" width="0.127" layer="21" />
              <wire x1="-0.6" y1="0.35" x2="-0.6" y2="-0.35" width="0.127" layer="21" />
              <text x="-0.6" y="0.75" size="0.8" layer="25">&gt;NAME</text>
              <text x="-0.6" y="-1.4500000000000002" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="C0603">
              <smd name="1" x="-0.8" y="0" dx="0.9" dy="0.95" layer="1" />
              <smd name="2" x="0.8" y="0" dx="0.9" dy="0.95" layer="1" />
              <wire x1="-0.9" y1="-0.5" x2="0.9" y2="-0.5" width="0.127" layer="21" />
              <wire x1="0.9" y1="-0.5" x2="0.9" y2="0.5" width="0.127" layer="21" />
              <wire x1="0.9" y1="0.5" x2="-0.9" y2="0.5" width="0.127" layer="21" />
              <wire x1="-0.9" y1="0.5" x2="-0.9" y2="-0.5" width="0.127" layer="21" />
              <text x="-0.9" y="0.9" size="0.8" layer="25">&gt;NAME</text>
              <text x="-0.9" y="-1.6" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="C0805">
              <smd name="1" x="-0.95" y="0" dx="1.1" dy="1.35" layer="1" />
              <smd name="2" x="0.95" y="0" dx="1.1" dy="1.35" layer="1" />
              <wire x1="-1.1" y1="-0.7" x2="1.1" y2="-0.7" width="0.127" layer="21" />
              <wire x1="1.1" y1="-0.7" x2="1.1" y2="0.7" width="0.127" layer="21" />
              <wire x1="1.1" y1="0.7" x2="-1.1" y2="0.7" width="0.127" layer="21" />
              <wire x1="-1.1" y1="0.7" x2="-1.1" y2="-0.7" width="0.127" layer="21" />
              <text x="-1.1" y="1.1" size="0.8" layer="25">&gt;NAME</text>
              <text x="-1.1" y="-1.8" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="IND_2016">
              <smd name="1" x="-0.7" y="0" dx="0.8" dy="1.6" layer="1" />
              <smd name="2" x="0.7" y="0" dx="0.8" dy="1.6" layer="1" />
              <wire x1="-1.1" y1="-0.9" x2="1.1" y2="-0.9" width="0.127" layer="21" />
              <wire x1="1.1" y1="-0.9" x2="1.1" y2="0.9" width="0.127" layer="21" />
              <wire x1="1.1" y1="0.9" x2="-1.1" y2="0.9" width="0.127" layer="21" />
              <wire x1="-1.1" y1="0.9" x2="-1.1" y2="-0.9" width="0.127" layer="21" />
              <text x="-1.1" y="1.3" size="0.8" layer="25">&gt;NAME</text>
              <text x="-1.1" y="-2.0" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="IND_2520">
              <smd name="1" x="-0.9" y="0" dx="0.95" dy="2.0" layer="1" />
              <smd name="2" x="0.9" y="0" dx="0.95" dy="2.0" layer="1" />
              <wire x1="-1.35" y1="-1.1" x2="1.35" y2="-1.1" width="0.127" layer="21" />
              <wire x1="1.35" y1="-1.1" x2="1.35" y2="1.1" width="0.127" layer="21" />
              <wire x1="1.35" y1="1.1" x2="-1.35" y2="1.1" width="0.127" layer="21" />
              <wire x1="-1.35" y1="1.1" x2="-1.35" y2="-1.1" width="0.127" layer="21" />
              <text x="-1.35" y="1.5" size="0.8" layer="25">&gt;NAME</text>
              <text x="-1.35" y="-2.2" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="IND_4040">
              <smd name="1" x="-1.45" y="0" dx="1.3" dy="3.6" layer="1" />
              <smd name="2" x="1.45" y="0" dx="1.3" dy="3.6" layer="1" />
              <wire x1="-2.2" y1="-2.2" x2="2.2" y2="-2.2" width="0.127" layer="21" />
              <wire x1="2.2" y1="-2.2" x2="2.2" y2="2.2" width="0.127" layer="21" />
              <wire x1="2.2" y1="2.2" x2="-2.2" y2="2.2" width="0.127" layer="21" />
              <wire x1="-2.2" y1="2.2" x2="-2.2" y2="-2.2" width="0.127" layer="21" />
              <text x="-2.2" y="2.6" size="0.8" layer="25">&gt;NAME</text>
              <text x="-2.2" y="-3.3000000000000003" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="SOD-323">
              <smd name="1" x="-1.05" y="0" dx="0.85" dy="0.85" layer="1" />
              <smd name="2" x="1.05" y="0" dx="0.85" dy="0.85" layer="1" />
              <wire x1="-1.1" y1="-0.7" x2="1.1" y2="-0.7" width="0.127" layer="21" />
              <wire x1="1.1" y1="-0.7" x2="1.1" y2="0.7" width="0.127" layer="21" />
              <wire x1="1.1" y1="0.7" x2="-1.1" y2="0.7" width="0.127" layer="21" />
              <wire x1="-1.1" y1="0.7" x2="-1.1" y2="-0.7" width="0.127" layer="21" />
              <text x="-1.1" y="1.1" size="0.8" layer="25">&gt;NAME</text>
              <text x="-1.1" y="-1.8" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="DFN1006-2">
              <smd name="1" x="-0.35" y="0" dx="0.4" dy="0.6" layer="1" />
              <smd name="2" x="0.35" y="0" dx="0.4" dy="0.6" layer="1" />
              <wire x1="-0.6" y1="-0.4" x2="0.6" y2="-0.4" width="0.127" layer="21" />
              <wire x1="0.6" y1="-0.4" x2="0.6" y2="0.4" width="0.127" layer="21" />
              <wire x1="0.6" y1="0.4" x2="-0.6" y2="0.4" width="0.127" layer="21" />
              <wire x1="-0.6" y1="0.4" x2="-0.6" y2="-0.4" width="0.127" layer="21" />
              <text x="-0.6" y="0.8" size="0.8" layer="25">&gt;NAME</text>
              <text x="-0.6" y="-1.5" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="BATT_PADS_2PIN">
              <smd name="1" x="-2.0" y="0" dx="2.5" dy="3.0" layer="1" />
              <smd name="2" x="2.0" y="0" dx="2.5" dy="3.0" layer="1" />
              <wire x1="-3.5" y1="-2.0" x2="3.5" y2="-2.0" width="0.127" layer="21" />
              <wire x1="3.5" y1="-2.0" x2="3.5" y2="2.0" width="0.127" layer="21" />
              <wire x1="3.5" y1="2.0" x2="-3.5" y2="2.0" width="0.127" layer="21" />
              <wire x1="-3.5" y1="2.0" x2="-3.5" y2="-2.0" width="0.127" layer="21" />
              <text x="-3.5" y="2.4" size="0.8" layer="25">&gt;NAME</text>
              <text x="-3.5" y="-3.1" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="TP_1MM">
              <smd name="1" x="0" y="0" dx="1.0" dy="1.0" layer="1" />
              <wire x1="-0.7" y1="-0.7" x2="0.7" y2="-0.7" width="0.127" layer="21" />
              <wire x1="0.7" y1="-0.7" x2="0.7" y2="0.7" width="0.127" layer="21" />
              <wire x1="0.7" y1="0.7" x2="-0.7" y2="0.7" width="0.127" layer="21" />
              <wire x1="-0.7" y1="0.7" x2="-0.7" y2="-0.7" width="0.127" layer="21" />
              <text x="-0.7" y="1.1" size="0.8" layer="25">&gt;NAME</text>
              <text x="-0.7" y="-1.8" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="SOT-23-5">
              <smd name="1" x="-1.2" y="0.95" dx="1.0" dy="0.55" layer="1" />
              <smd name="2" x="-1.2" y="0" dx="1.0" dy="0.55" layer="1" />
              <smd name="3" x="-1.2" y="-0.95" dx="1.0" dy="0.55" layer="1" />
              <smd name="4" x="1.2" y="-0.95" dx="1.0" dy="0.55" layer="1" />
              <smd name="5" x="1.2" y="0.95" dx="1.0" dy="0.55" layer="1" />
              <wire x1="-1.6" y1="-1.6" x2="1.6" y2="-1.6" width="0.127" layer="21" />
              <wire x1="1.6" y1="-1.6" x2="1.6" y2="1.6" width="0.127" layer="21" />
              <wire x1="1.6" y1="1.6" x2="-1.6" y2="1.6" width="0.127" layer="21" />
              <wire x1="-1.6" y1="1.6" x2="-1.6" y2="-1.6" width="0.127" layer="21" />
              <text x="-1.6" y="2.0" size="0.8" layer="25">&gt;NAME</text>
              <text x="-1.6" y="-2.7" size="0.8" layer="27">&gt;VALUE</text>
            </package>
            <package name="WLCSP-4">
              <smd name="A1" x="-0.2" y="0.2" dx="0.25" dy="0.25" layer="1" />
              <smd name="A2" x="0.2" y="0.2" dx="0.25" dy="0.25" layer="1" />
              <smd name="B1" x="-0.2" y="-0.2" dx="0.25" dy="0.25" layer="1" />
              <smd name="B2" x="0.2" y="-0.2" dx="0.25" dy="0.25" layer="1" />
              <wire x1="-0.45" y1="-0.45" x2="0.45" y2="-0.45" width="0.127" layer="21" />
              <wire x1="0.45" y1="-0.45" x2="0.45" y2="0.45" width="0.127" layer="21" />
              <wire x1="0.45" y1="0.45" x2="-0.45" y2="0.45" width="0.127" layer="21" />
              <wire x1="-0.45" y1="0.45" x2="-0.45" y2="-0.45" width="0.127" layer="21" />
              <text x="-0.45" y="0.8500000000000001" size="0.8" layer="25">&gt;NAME</text>
              <text x="-0.45" y="-1.55" size="0.8" layer="27">&gt;VALUE</text>
            </package>
          </packages>
          <symbols>
            <symbol name="RES">
              <wire x1="-2.54" y1="0" x2="-2.032" y2="0.889" width="0.254" layer="94" />
              <wire x1="-2.032" y1="0.889" x2="-1.016" y2="-0.889" width="0.254" layer="94" />
              <wire x1="-1.016" y1="-0.889" x2="0" y2="0.889" width="0.254" layer="94" />
              <wire x1="0" y1="0.889" x2="1.016" y2="-0.889" width="0.254" layer="94" />
              <wire x1="1.016" y1="-0.889" x2="2.032" y2="0.889" width="0.254" layer="94" />
              <wire x1="2.032" y1="0.889" x2="2.54" y2="0" width="0.254" layer="94" />
              <pin name="1" x="-5.08" y="0" visible="off" length="short" direction="pas" />
              <pin name="2" x="5.08" y="0" visible="off" length="short" direction="pas" rot="R180" />
              <text x="-2.54" y="1.4" size="1.27" layer="95">&gt;NAME</text>
              <text x="-2.54" y="-2.8" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="CAP">
              <wire x1="-0.635" y1="-1.905" x2="-0.635" y2="1.905" width="0.254" layer="94" />
              <wire x1="0.635" y1="-1.905" x2="0.635" y2="1.905" width="0.254" layer="94" />
              <wire x1="-2.54" y1="0" x2="-0.635" y2="0" width="0.254" layer="94" />
              <wire x1="0.635" y1="0" x2="2.54" y2="0" width="0.254" layer="94" />
              <pin name="1" x="-5.08" y="0" visible="off" length="short" direction="pas" />
              <pin name="2" x="5.08" y="0" visible="off" length="short" direction="pas" rot="R180" />
              <text x="-2.54" y="2.2" size="1.27" layer="95">&gt;NAME</text>
              <text x="-2.54" y="-3.6" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="IND">
              <wire x1="-2.54" y1="0" x2="-1.27" y2="0" width="0.254" layer="94" curve="-180" />
              <wire x1="-1.27" y1="0" x2="0" y2="0" width="0.254" layer="94" curve="-180" />
              <wire x1="0" y1="0" x2="1.27" y2="0" width="0.254" layer="94" curve="-180" />
              <wire x1="1.27" y1="0" x2="2.54" y2="0" width="0.254" layer="94" curve="-180" />
              <pin name="1" x="-5.08" y="0" visible="off" length="short" direction="pas" />
              <pin name="2" x="5.08" y="0" visible="off" length="short" direction="pas" rot="R180" />
              <text x="-2.54" y="1.778" size="1.27" layer="95">&gt;NAME</text>
              <text x="-2.54" y="-2.54" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="SCHOTTKY">
              <wire x1="-1.27" y1="1.27" x2="1.27" y2="0" width="0.254" layer="94" />
              <wire x1="1.27" y1="0" x2="-1.27" y2="-1.27" width="0.254" layer="94" />
              <wire x1="-1.27" y1="-1.27" x2="-1.27" y2="1.27" width="0.254" layer="94" />
              <wire x1="1.27" y1="1.27" x2="1.27" y2="-1.27" width="0.254" layer="94" />
              <pin name="1" x="-5.08" y="0" visible="off" length="short" direction="pas" />
              <pin name="2" x="5.08" y="0" visible="off" length="short" direction="pas" rot="R180" />
              <text x="-2.54" y="1.9" size="1.27" layer="95">&gt;NAME</text>
              <text x="-2.54" y="-3.2" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="TVS_UNI">
              <wire x1="-1.27" y1="1.27" x2="1.27" y2="0" width="0.254" layer="94" />
              <wire x1="1.27" y1="0" x2="-1.27" y2="-1.27" width="0.254" layer="94" />
              <wire x1="-1.27" y1="-1.27" x2="-1.27" y2="1.27" width="0.254" layer="94" />
              <wire x1="1.27" y1="1.27" x2="1.27" y2="-1.27" width="0.254" layer="94" />
              <pin name="1" x="-5.08" y="0" visible="off" length="short" direction="pas" />
              <pin name="2" x="5.08" y="0" visible="off" length="short" direction="pas" rot="R180" />
              <text x="-2.54" y="1.9" size="1.27" layer="95">&gt;NAME</text>
              <text x="-2.54" y="-3.2" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="BATT_2P">
              <wire x1="-5.08" y1="5.08" x2="5.08" y2="5.08" width="0.254" layer="94" />
              <wire x1="5.08" y1="5.08" x2="5.08" y2="-5.08" width="0.254" layer="94" />
              <wire x1="5.08" y1="-5.08" x2="-5.08" y2="-5.08" width="0.254" layer="94" />
              <wire x1="-5.08" y1="-5.08" x2="-5.08" y2="5.08" width="0.254" layer="94" />
              <pin name="VBAT+" x="10.16" y="2.54" length="middle" direction="pas" rot="R180" />
              <pin name="GND" x="10.16" y="-2.54" length="middle" direction="pas" rot="R180" />
              <text x="-5.08" y="5.842" size="1.524" layer="95">&gt;NAME</text>
              <text x="-5.08" y="-7.366" size="1.524" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="TP_1MM">
              <circle x="0" y="0" radius="1.016" width="0.254" layer="94" />
              <pin name="1" x="-5.08" y="0" visible="off" length="short" direction="pas" />
              <text x="-1.27" y="1.778" size="1.27" layer="95">&gt;NAME</text>
              <text x="-1.27" y="-2.794" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="TMI3112H">
              <wire x1="-10.16" y1="7.62" x2="10.16" y2="7.62" width="0.254" layer="94" />
              <wire x1="10.16" y1="7.62" x2="10.16" y2="-7.62" width="0.254" layer="94" />
              <wire x1="10.16" y1="-7.62" x2="-10.16" y2="-7.62" width="0.254" layer="94" />
              <wire x1="-10.16" y1="-7.62" x2="-10.16" y2="7.62" width="0.254" layer="94" />
              <pin name="IN" x="-15.24" y="5.08" length="middle" direction="pwr" />
              <pin name="EN" x="-15.24" y="0" length="middle" direction="in" />
              <pin name="GND" x="-15.24" y="-5.08" length="middle" direction="pwr" />
              <pin name="LX" x="15.24" y="5.08" length="middle" direction="out" rot="R180" />
              <pin name="FB" x="15.24" y="-2.54" length="middle" direction="in" rot="R180" />
              <text x="-10.16" y="8.382" size="1.524" layer="95">&gt;NAME</text>
              <text x="-10.16" y="-9.906" size="1.524" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="CW3301">
              <wire x1="-10.16" y1="7.62" x2="10.16" y2="7.62" width="0.254" layer="94" />
              <wire x1="10.16" y1="7.62" x2="10.16" y2="-7.62" width="0.254" layer="94" />
              <wire x1="10.16" y1="-7.62" x2="-10.16" y2="-7.62" width="0.254" layer="94" />
              <wire x1="-10.16" y1="-7.62" x2="-10.16" y2="7.62" width="0.254" layer="94" />
              <pin name="IN" x="-15.24" y="5.08" length="middle" direction="in" />
              <pin name="ON" x="-15.24" y="-2.54" length="middle" direction="in" />
              <pin name="OUT" x="15.24" y="5.08" length="middle" direction="out" rot="R180" />
              <pin name="GND" x="15.24" y="-2.54" length="middle" direction="pwr" rot="R180" />
              <text x="-10.16" y="8.382" size="1.524" layer="95">&gt;NAME</text>
              <text x="-10.16" y="-9.906" size="1.524" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="A3_FRAME">
              <frame x1="0" y1="0" x2="419.1" y2="297.18" columns="8" rows="6" layer="94" border-left="yes" border-top="yes" border-right="yes" border-bottom="yes" />
            </symbol>
            <symbol name="A1_FRAME">
              <frame x1="0" y1="0" x2="840.74" y2="594.36" columns="8" rows="6" layer="94" border-left="yes" border-top="yes" border-right="yes" border-bottom="yes" />
            </symbol>
            <symbol name="A0_FRAME">
              <frame x1="0" y1="0" x2="1188.72" y2="840.74" columns="8" rows="6" layer="94" border-left="yes" border-top="yes" border-right="yes" border-bottom="yes" />
            </symbol>
            <symbol name="DDR_PLL_AVDD1V8">
              <pin name="DDR_PLL_AVDD1V8" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="GND">
              <pin name="GND" x="0" y="2.54" visible="off" length="short" direction="sup" rot="R270" />
              <wire x1="-1.905" y1="0" x2="1.905" y2="0" width="0.254" layer="94" />
              <wire x1="-1.27" y1="-0.762" x2="1.27" y2="-0.762" width="0.254" layer="94" />
              <wire x1="-0.635" y1="-1.524" x2="0.635" y2="-1.524" width="0.254" layer="94" />
            </symbol>
            <symbol name="MIPI_DCPHY_AVDD">
              <pin name="MIPI_DCPHY_AVDD" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="OSC_1V8">
              <pin name="OSC_1V8" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="SARADC_AVDD1V8">
              <pin name="SARADC_AVDD1V8" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VBAT_2S_IN">
              <pin name="VBAT_2S_IN" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VBAT_BUCK_5V">
              <pin name="VBAT_BUCK_5V" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VBUS_5V">
              <pin name="VBUS_5V" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VCC5V0_SYS_S5">
              <pin name="VCC5V0_SYS_S5" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VCCA1V8_PLDO2_S0">
              <pin name="VCCA1V8_PLDO2_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VCCA1V8_PLDO6_S3">
              <pin name="VCCA1V8_PLDO6_S3" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VCCA_1V8_S0">
              <pin name="VCCA_1V8_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VCCA_3V3_S0">
              <pin name="VCCA_3V3_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VCCIO_SD_S0">
              <pin name="VCCIO_SD_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VCC_1V1_NLDO_S3">
              <pin name="VCC_1V1_NLDO_S3" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VCC_1V8_S0">
              <pin name="VCC_1V8_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VCC_1V8_S3">
              <pin name="VCC_1V8_S3" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VCC_2V0_PLDO_S3">
              <pin name="VCC_2V0_PLDO_S3" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VCC_3V3_S0">
              <pin name="VCC_3V3_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VCC_3V3_S3">
              <pin name="VCC_3V3_S3" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VDD2_DDR_S3">
              <pin name="VDD2_DDR_S3" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VDDA0V75_HDMI_S0">
              <pin name="VDDA0V75_HDMI_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VDDA_0V75_S0">
              <pin name="VDDA_0V75_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VDDA_0V85_S0">
              <pin name="VDDA_0V85_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VDDA_1V2_S0">
              <pin name="VDDA_1V2_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VDDA_DDR_PLL_S0">
              <pin name="VDDA_DDR_PLL_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VDDQ_DDR_S0">
              <pin name="VDDQ_DDR_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VDD_0V75_S3">
              <pin name="VDD_0V75_S3" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VDD_CPU_BIG_S0">
              <pin name="VDD_CPU_BIG_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VDD_CPU_LIT_S0">
              <pin name="VDD_CPU_LIT_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VDD_DDR_S0">
              <pin name="VDD_DDR_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VDD_GPU_S0">
              <pin name="VDD_GPU_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VDD_LOGIC_S0">
              <pin name="VDD_LOGIC_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="VDD_NPU_S0">
              <pin name="VDD_NPU_S0" x="0" y="-2.54" visible="off" length="short" direction="pas" rot="R90" />
              <wire x1="-1.27" y1="0" x2="1.27" y2="0" width="0.3048" layer="94" />
              <text x="-1.27" y="0.635" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
          </symbols>
          <devicesets>
            <deviceset name="DDR_PLL_AVDD1V8" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="DDR_PLL_AVDD1V8" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="GND" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="GND" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="MIPI_DCPHY_AVDD" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="MIPI_DCPHY_AVDD" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="OSC_1V8" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="OSC_1V8" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="SARADC_AVDD1V8" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="SARADC_AVDD1V8" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VBAT_2S_IN" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VBAT_2S_IN" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VBAT_BUCK_5V" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VBAT_BUCK_5V" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VBUS_5V" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VBUS_5V" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VCC5V0_SYS_S5" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VCC5V0_SYS_S5" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VCCA1V8_PLDO2_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VCCA1V8_PLDO2_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VCCA1V8_PLDO6_S3" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VCCA1V8_PLDO6_S3" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VCCA_1V8_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VCCA_1V8_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VCCA_3V3_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VCCA_3V3_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VCCIO_SD_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VCCIO_SD_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VCC_1V1_NLDO_S3" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VCC_1V1_NLDO_S3" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VCC_1V8_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VCC_1V8_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VCC_1V8_S3" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VCC_1V8_S3" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VCC_2V0_PLDO_S3" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VCC_2V0_PLDO_S3" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VCC_3V3_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VCC_3V3_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VCC_3V3_S3" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VCC_3V3_S3" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VDD2_DDR_S3" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VDD2_DDR_S3" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VDDA0V75_HDMI_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VDDA0V75_HDMI_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VDDA_0V75_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VDDA_0V75_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VDDA_0V85_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VDDA_0V85_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VDDA_1V2_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VDDA_1V2_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VDDA_DDR_PLL_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VDDA_DDR_PLL_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VDDQ_DDR_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VDDQ_DDR_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VDD_0V75_S3" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VDD_0V75_S3" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VDD_CPU_BIG_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VDD_CPU_BIG_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VDD_CPU_LIT_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VDD_CPU_LIT_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VDD_DDR_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VDD_DDR_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VDD_GPU_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VDD_GPU_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VDD_LOGIC_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VDD_LOGIC_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="VDD_NPU_S0" prefix="PWR">
              <gates>
                <gate name="G$1" symbol="VDD_NPU_S0" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="R_0402" prefix="R" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="RES" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="R0402">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="R_0201" prefix="R" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="RES" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="R0201">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="R_0603" prefix="R" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="RES" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="R0603">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="C_0201" prefix="C" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="CAP" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="C0201">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="C_0402" prefix="C" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="CAP" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="C0402">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="C_0402_BGA" prefix="C" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="CAP" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="C0402_BGA">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="C_0603" prefix="C" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="CAP" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="C0603">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="C_0805" prefix="C" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="CAP" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="C0805">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="IND_2016" prefix="L" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="IND" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="IND_2016">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="IND_2520" prefix="L" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="IND" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="IND_2520">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="IND_4040" prefix="L" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="IND" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="IND_4040">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="B5819WS" prefix="D" uservalue="no">
              <gates>
                <gate name="G$1" symbol="SCHOTTKY" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="SOD-323">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="TVS_VBUS" prefix="D" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="TVS_UNI" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="SOD-323">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="PSUR1610DNV07" prefix="D" uservalue="no">
              <gates>
                <gate name="G$1" symbol="TVS_UNI" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="DFN1006-2">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="BATT_PADS_2PIN" prefix="J" uservalue="no">
              <gates>
                <gate name="G$1" symbol="BATT_2P" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="BATT_PADS_2PIN">
                  <connects>
                    <connect gate="G$1" pin="VBAT+" pad="1" />
                    <connect gate="G$1" pin="GND" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="TP_1MM" prefix="TP" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="TP_1MM" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="TP_1MM">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="TMI3112H" prefix="U" uservalue="no">
              <gates>
                <gate name="G$1" symbol="TMI3112H" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="SOT-23-5">
                  <connects>
                    <connect gate="G$1" pin="EN" pad="1" />
                    <connect gate="G$1" pin="GND" pad="2" />
                    <connect gate="G$1" pin="LX" pad="3" />
                    <connect gate="G$1" pin="IN" pad="4" />
                    <connect gate="G$1" pin="FB" pad="5" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="CW3301" prefix="U" uservalue="no">
              <gates>
                <gate name="G$1" symbol="CW3301" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="WLCSP-4">
                  <connects>
                    <connect gate="G$1" pin="OUT" pad="A1" />
                    <connect gate="G$1" pin="IN" pad="A2" />
                    <connect gate="G$1" pin="GND" pad="B1" />
                    <connect gate="G$1" pin="ON" pad="B2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="A3_FRAME" prefix="FRAME">
              <gates>
                <gate name="G$1" symbol="A3_FRAME" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="A1_FRAME" prefix="FRAME">
              <gates>
                <gate name="G$1" symbol="A1_FRAME" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
            <deviceset name="A0_FRAME" prefix="FRAME">
              <gates>
                <gate name="G$1" symbol="A0_FRAME" x="0" y="0" />
              </gates>
              <devices>
                <device name="" />
              </devices>
            </deviceset>
          </devicesets>
        </library>
        <library name="FH12-24S-0.5SH_55_">
          <packages>
            <package name="HRS_FH12-24S-0.5SH(55)">
              <wire x1="7.55" y1="-3.45" x2="-7.55" y2="-3.45" width="0.127" layer="21" />
              <wire x1="-7.55" y1="0.97" x2="-7.55" y2="2.15" width="0.127" layer="21" />
              <wire x1="-7.55" y1="2.15" x2="-6.22" y2="2.15" width="0.127" layer="21" />
              <wire x1="8.8" y1="-3.7" x2="-8.8" y2="-3.7" width="0.05" layer="39" />
              <wire x1="-8.8" y1="-3.7" x2="-8.8" y2="3.7" width="0.05" layer="39" />
              <wire x1="-8.8" y1="3.7" x2="8.8" y2="3.7" width="0.05" layer="39" />
              <wire x1="8.8" y1="3.7" x2="8.8" y2="-3.7" width="0.05" layer="39" />
              <circle x="-5.75" y="3.9" radius="0.1" width="0.2" layer="21" />
              <text x="-8.62167" y="4.29517" size="1.27212" layer="25">&gt;NAME</text>
              <text x="-8.62006" y="-5.2916" size="1.27007" layer="27">&gt;VALUE</text>
              <rectangle x1="5.625" y1="2.15" x2="5.875" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="5.125" y1="2.15" x2="5.375" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="4.625" y1="2.15" x2="4.875" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="4.125" y1="2.15" x2="4.375" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="3.625" y1="2.15" x2="3.875" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="3.125" y1="2.15" x2="3.375" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="2.625" y1="2.15" x2="2.875" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="2.125" y1="2.15" x2="2.375" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="1.625" y1="2.15" x2="1.875" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="1.125" y1="2.15" x2="1.375" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="0.625" y1="2.15" x2="0.875" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="0.125" y1="2.15" x2="0.375" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="-0.375" y1="2.15" x2="-0.125" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="-0.875" y1="2.15" x2="-0.625" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="-1.375" y1="2.15" x2="-1.125" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="-1.875" y1="2.15" x2="-1.625" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="-2.375" y1="2.15" x2="-2.125" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="-2.875" y1="2.15" x2="-2.625" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="-3.375" y1="2.15" x2="-3.125" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="-3.875" y1="2.15" x2="-3.625" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="-4.375" y1="2.15" x2="-4.125" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="-4.875" y1="2.15" x2="-4.625" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="-5.375" y1="2.15" x2="-5.125" y2="3.45" layer="31" rot="R180" />
              <rectangle x1="-5.875" y1="2.15" x2="-5.625" y2="3.45" layer="31" rot="R180" />
              <wire x1="-7.55" y1="2.15" x2="7.55" y2="2.15" width="0.127" layer="51" />
              <wire x1="7.55" y1="0.97" x2="7.55" y2="2.15" width="0.127" layer="21" />
              <wire x1="6.22" y1="2.15" x2="7.55" y2="2.15" width="0.127" layer="21" />
              <wire x1="7.55" y1="-3.45" x2="-7.55" y2="-3.45" width="0.127" layer="51" />
              <wire x1="7.55" y1="2.15" x2="7.55" y2="-3.45" width="0.127" layer="51" />
              <wire x1="-7.55" y1="-3.45" x2="-7.55" y2="2.15" width="0.127" layer="51" />
              <wire x1="7.55" y1="-3.45" x2="7.55" y2="-1.87" width="0.127" layer="21" />
              <wire x1="-7.55" y1="-3.45" x2="-7.55" y2="-1.87" width="0.127" layer="21" />
              <circle x="-5.75" y="3.9" radius="0.1" width="0.2" layer="51" />
              <smd name="1" x="-5.75" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="2" x="-5.25" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="3" x="-4.75" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="4" x="-4.25" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="5" x="-3.75" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="6" x="-3.25" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="7" x="-2.75" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="8" x="-2.25" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="9" x="-1.75" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="10" x="-1.25" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="11" x="-0.75" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="12" x="-0.25" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="13" x="0.25" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="14" x="0.75" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="15" x="1.25" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="16" x="1.75" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="17" x="2.25" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="18" x="2.75" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="19" x="3.25" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="20" x="3.75" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="21" x="4.25" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="22" x="4.75" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="23" x="5.25" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="24" x="5.75" y="2.8" dx="0.3" dy="1.3" layer="1" cream="no" />
              <smd name="P1" x="7.65" y="-0.45" dx="1.8" dy="2.2" layer="1" />
              <smd name="P2" x="-7.65" y="-0.45" dx="1.8" dy="2.2" layer="1" />
            </package>
          </packages>
          <symbols>
            <symbol name="FH12-24S-0.5SH(55)">
              <wire x1="-5.08" y1="35.56" x2="-5.08" y2="-33.02" width="0.254" layer="94" />
              <wire x1="-5.08" y1="-33.02" x2="5.08" y2="-33.02" width="0.254" layer="94" />
              <wire x1="5.08" y1="-33.02" x2="5.08" y2="35.56" width="0.254" layer="94" />
              <wire x1="5.08" y1="35.56" x2="-5.08" y2="35.56" width="0.254" layer="94" />
              <text x="-5.08" y="36.1117" size="1.778" layer="95">&gt;NAME</text>
              <text x="-5.08" y="-35.6278" size="1.778" layer="96">&gt;VALUE</text>
              <pin name="1" x="-10.16" y="33.02" length="middle" direction="pas" />
              <pin name="2" x="-10.16" y="30.48" length="middle" direction="pas" />
              <pin name="3" x="-10.16" y="27.94" length="middle" direction="pas" />
              <pin name="4" x="-10.16" y="25.4" length="middle" direction="pas" />
              <pin name="5" x="-10.16" y="22.86" length="middle" direction="pas" />
              <pin name="6" x="-10.16" y="20.32" length="middle" direction="pas" />
              <pin name="7" x="-10.16" y="17.78" length="middle" direction="pas" />
              <pin name="8" x="-10.16" y="15.24" length="middle" direction="pas" />
              <pin name="9" x="-10.16" y="12.7" length="middle" direction="pas" />
              <pin name="10" x="-10.16" y="10.16" length="middle" direction="pas" />
              <pin name="11" x="-10.16" y="7.62" length="middle" direction="pas" />
              <pin name="12" x="-10.16" y="5.08" length="middle" direction="pas" />
              <pin name="13" x="-10.16" y="2.54" length="middle" direction="pas" />
              <pin name="14" x="-10.16" y="0" length="middle" direction="pas" />
              <pin name="15" x="-10.16" y="-2.54" length="middle" direction="pas" />
              <pin name="16" x="-10.16" y="-5.08" length="middle" direction="pas" />
              <pin name="17" x="-10.16" y="-7.62" length="middle" direction="pas" />
              <pin name="18" x="-10.16" y="-10.16" length="middle" direction="pas" />
              <pin name="19" x="-10.16" y="-12.7" length="middle" direction="pas" />
              <pin name="20" x="-10.16" y="-15.24" length="middle" direction="pas" />
              <pin name="21" x="-10.16" y="-17.78" length="middle" direction="pas" />
              <pin name="22" x="-10.16" y="-20.32" length="middle" direction="pas" />
              <pin name="23" x="-10.16" y="-22.86" length="middle" direction="pas" />
              <pin name="24" x="-10.16" y="-25.4" length="middle" direction="pas" />
              <pin name="SHIELD" x="-10.16" y="-30.48" length="middle" direction="pas" />
            </symbol>
          </symbols>
          <devicesets>
            <deviceset name="FH12-24S-0.5SH(55)" prefix="J">
              <gates>
                <gate name="G$1" symbol="FH12-24S-0.5SH(55)" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="HRS_FH12-24S-0.5SH(55)">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="10" pad="10" />
                    <connect gate="G$1" pin="11" pad="11" />
                    <connect gate="G$1" pin="12" pad="12" />
                    <connect gate="G$1" pin="13" pad="13" />
                    <connect gate="G$1" pin="14" pad="14" />
                    <connect gate="G$1" pin="15" pad="15" />
                    <connect gate="G$1" pin="16" pad="16" />
                    <connect gate="G$1" pin="17" pad="17" />
                    <connect gate="G$1" pin="18" pad="18" />
                    <connect gate="G$1" pin="19" pad="19" />
                    <connect gate="G$1" pin="2" pad="2" />
                    <connect gate="G$1" pin="20" pad="20" />
                    <connect gate="G$1" pin="21" pad="21" />
                    <connect gate="G$1" pin="22" pad="22" />
                    <connect gate="G$1" pin="23" pad="23" />
                    <connect gate="G$1" pin="24" pad="24" />
                    <connect gate="G$1" pin="3" pad="3" />
                    <connect gate="G$1" pin="4" pad="4" />
                    <connect gate="G$1" pin="5" pad="5" />
                    <connect gate="G$1" pin="6" pad="6" />
                    <connect gate="G$1" pin="7" pad="7" />
                    <connect gate="G$1" pin="8" pad="8" />
                    <connect gate="G$1" pin="9" pad="9" />
                    <connect gate="G$1" pin="SHIELD" pad="P1 P2" />
                  </connects>
                  <technologies>
                    <technology name="">
                      <attribute name="DATASHEET_URL" value="https://s3.amazonaws.com/snapeda/datasheet/FH12-24S-05SH-55-_Hirose.pdf" />
                      <attribute name="DESCRIPTION" value="24 Position FFC, FPC Connector Contacts, Bottom 0.020&quot; (0.50mm) Surface Mount, Right Angle" />
                      <attribute name="MANUFACTURER" value="Hirose" />
                      <attribute name="MAXIMUM_PACKAGE_HEIGHT" value="2.2mm" />
                      <attribute name="MPN" value="FH12-24S-0.5SH(55)" />
                      <attribute name="SOURCE_URL" value="https://www.snapeda.com/parts/FH12-24S-0.5SH(55)/Hirose+Electric+Co+Ltd/view-part/" />
                      <attribute name="STANDARD" value="Manufacturer recommendations" />
                    </technology>
                  </technologies>
                </device>
              </devices>
            </deviceset>
          </devicesets>
        </library>
        <library name="DF37NC-30DS-0.4V_51_">
          <packages>
            <package name="HRS_DF37NC-30DS-0.4V(51)">
              <wire x1="4.11" y1="-1.16" x2="-4.11" y2="-1.16" width="0.127" layer="51" />
              <wire x1="-4.11" y1="-1.16" x2="-4.11" y2="1.16" width="0.127" layer="51" />
              <wire x1="-4.11" y1="1.16" x2="4.11" y2="1.16" width="0.127" layer="51" />
              <wire x1="4.11" y1="1.16" x2="4.11" y2="-1.16" width="0.127" layer="51" />
              <wire x1="-4.11" y1="-1.16" x2="-4.11" y2="1.16" width="0.127" layer="21" />
              <wire x1="4.11" y1="1.16" x2="4.11" y2="-1.16" width="0.127" layer="21" />
              <wire x1="-4.11" y1="1.16" x2="-3.235" y2="1.16" width="0.127" layer="21" />
              <wire x1="3.235" y1="1.16" x2="4.11" y2="1.16" width="0.127" layer="21" />
              <wire x1="3.235" y1="-1.16" x2="4.11" y2="-1.16" width="0.127" layer="21" />
              <wire x1="-3.235" y1="-1.16" x2="-4.11" y2="-1.16" width="0.127" layer="21" />
              <wire x1="-4.36" y1="-2.02" x2="-4.36" y2="2.02" width="0.05" layer="39" />
              <wire x1="-4.36" y1="2.02" x2="4.36" y2="2.02" width="0.05" layer="39" />
              <wire x1="4.36" y1="2.02" x2="4.36" y2="-2.02" width="0.05" layer="39" />
              <wire x1="4.36" y1="-2.02" x2="-4.36" y2="-2.02" width="0.05" layer="39" />
              <text x="-4.36" y="2.09" size="0.8" layer="25">&gt;NAME</text>
              <text x="-4.36" y="-3.34" size="0.8" layer="27">&gt;VALUE</text>
              <circle x="2.8" y="-2.214" radius="0.05" width="0.1" layer="21" />
              <circle x="2.8" y="-2.214" radius="0.05" width="0.1" layer="51" />
              <rectangle x1="-0.115" y1="1.14" x2="0.115" y2="1.77" layer="31" />
              <rectangle x1="0.285" y1="1.14" x2="0.515" y2="1.77" layer="31" />
              <rectangle x1="0.685" y1="1.14" x2="0.915" y2="1.77" layer="31" />
              <rectangle x1="-0.515" y1="1.14" x2="-0.285" y2="1.77" layer="31" />
              <rectangle x1="-0.915" y1="1.14" x2="-0.685" y2="1.77" layer="31" />
              <rectangle x1="-0.115" y1="-1.77" x2="0.115" y2="-1.14" layer="31" />
              <rectangle x1="-0.515" y1="-1.77" x2="-0.285" y2="-1.14" layer="31" />
              <rectangle x1="-0.915" y1="-1.77" x2="-0.685" y2="-1.14" layer="31" />
              <rectangle x1="0.285" y1="-1.77" x2="0.515" y2="-1.14" layer="31" />
              <rectangle x1="0.685" y1="-1.77" x2="0.915" y2="-1.14" layer="31" />
              <rectangle x1="-0.165" y1="0.96" x2="0.165" y2="1.69" layer="29" />
              <rectangle x1="0.235" y1="0.96" x2="0.565" y2="1.69" layer="29" />
              <rectangle x1="0.635" y1="0.96" x2="0.965" y2="1.69" layer="29" />
              <rectangle x1="-0.565" y1="0.96" x2="-0.235" y2="1.69" layer="29" />
              <rectangle x1="-0.965" y1="0.96" x2="-0.635" y2="1.69" layer="29" />
              <rectangle x1="-0.165" y1="-1.69" x2="0.165" y2="-0.96" layer="29" />
              <rectangle x1="0.235" y1="-1.69" x2="0.565" y2="-0.96" layer="29" />
              <rectangle x1="0.635" y1="-1.69" x2="0.965" y2="-0.96" layer="29" />
              <rectangle x1="-0.565" y1="-1.69" x2="-0.235" y2="-0.96" layer="29" />
              <rectangle x1="-0.965" y1="-1.69" x2="-0.635" y2="-0.96" layer="29" />
              <rectangle x1="1.885" y1="1.14" x2="2.115" y2="1.77" layer="31" />
              <rectangle x1="2.285" y1="1.14" x2="2.515" y2="1.77" layer="31" />
              <rectangle x1="2.685" y1="1.14" x2="2.915" y2="1.77" layer="31" />
              <rectangle x1="1.485" y1="1.14" x2="1.715" y2="1.77" layer="31" />
              <rectangle x1="1.085" y1="1.14" x2="1.315" y2="1.77" layer="31" />
              <rectangle x1="1.885" y1="-1.77" x2="2.115" y2="-1.14" layer="31" />
              <rectangle x1="1.485" y1="-1.77" x2="1.715" y2="-1.14" layer="31" />
              <rectangle x1="1.085" y1="-1.77" x2="1.315" y2="-1.14" layer="31" />
              <rectangle x1="2.285" y1="-1.77" x2="2.515" y2="-1.14" layer="31" />
              <rectangle x1="2.685" y1="-1.77" x2="2.915" y2="-1.14" layer="31" />
              <rectangle x1="1.835" y1="0.96" x2="2.165" y2="1.69" layer="29" />
              <rectangle x1="2.235" y1="0.96" x2="2.565" y2="1.69" layer="29" />
              <rectangle x1="2.635" y1="0.96" x2="2.965" y2="1.69" layer="29" />
              <rectangle x1="1.435" y1="0.96" x2="1.765" y2="1.69" layer="29" />
              <rectangle x1="1.035" y1="0.96" x2="1.365" y2="1.69" layer="29" />
              <rectangle x1="1.835" y1="-1.69" x2="2.165" y2="-0.96" layer="29" />
              <rectangle x1="2.235" y1="-1.69" x2="2.565" y2="-0.96" layer="29" />
              <rectangle x1="2.635" y1="-1.69" x2="2.965" y2="-0.96" layer="29" />
              <rectangle x1="1.435" y1="-1.69" x2="1.765" y2="-0.96" layer="29" />
              <rectangle x1="1.035" y1="-1.69" x2="1.365" y2="-0.96" layer="29" />
              <rectangle x1="-2.115" y1="1.14" x2="-1.885" y2="1.77" layer="31" />
              <rectangle x1="-1.715" y1="1.14" x2="-1.485" y2="1.77" layer="31" />
              <rectangle x1="-1.315" y1="1.14" x2="-1.085" y2="1.77" layer="31" />
              <rectangle x1="-2.515" y1="1.14" x2="-2.285" y2="1.77" layer="31" />
              <rectangle x1="-2.915" y1="1.14" x2="-2.685" y2="1.77" layer="31" />
              <rectangle x1="-2.115" y1="-1.77" x2="-1.885" y2="-1.14" layer="31" />
              <rectangle x1="-2.515" y1="-1.77" x2="-2.285" y2="-1.14" layer="31" />
              <rectangle x1="-2.915" y1="-1.77" x2="-2.685" y2="-1.14" layer="31" />
              <rectangle x1="-1.715" y1="-1.77" x2="-1.485" y2="-1.14" layer="31" />
              <rectangle x1="-1.315" y1="-1.77" x2="-1.085" y2="-1.14" layer="31" />
              <rectangle x1="-2.165" y1="0.96" x2="-1.835" y2="1.69" layer="29" />
              <rectangle x1="-1.765" y1="0.96" x2="-1.435" y2="1.69" layer="29" />
              <rectangle x1="-1.365" y1="0.96" x2="-1.035" y2="1.69" layer="29" />
              <rectangle x1="-2.565" y1="0.96" x2="-2.235" y2="1.69" layer="29" />
              <rectangle x1="-2.965" y1="0.96" x2="-2.635" y2="1.69" layer="29" />
              <rectangle x1="-2.165" y1="-1.69" x2="-1.835" y2="-0.96" layer="29" />
              <rectangle x1="-1.765" y1="-1.69" x2="-1.435" y2="-0.96" layer="29" />
              <rectangle x1="-1.365" y1="-1.69" x2="-1.035" y2="-0.96" layer="29" />
              <rectangle x1="-2.565" y1="-1.69" x2="-2.235" y2="-0.96" layer="29" />
              <rectangle x1="-2.965" y1="-1.69" x2="-2.635" y2="-0.96" layer="29" />
              <smd name="01" x="2.8" y="-1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="02" x="2.8" y="1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="03" x="2.4" y="-1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="04" x="2.4" y="1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="05" x="2" y="-1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="06" x="2" y="1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="07" x="1.6" y="-1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="08" x="1.6" y="1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="09" x="1.2" y="-1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="10" x="1.2" y="1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="11" x="0.8" y="-1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="12" x="0.8" y="1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="13" x="0.4" y="-1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="14" x="0.4" y="1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="15" x="0" y="-1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="16" x="0" y="1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="17" x="-0.4" y="-1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="18" x="-0.4" y="1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="19" x="-0.8" y="-1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="20" x="-0.8" y="1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="21" x="-1.2" y="-1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="22" x="-1.2" y="1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="23" x="-1.6" y="-1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="24" x="-1.6" y="1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="25" x="-2" y="-1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="26" x="-2" y="1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="27" x="-2.4" y="-1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="28" x="-2.4" y="1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="29" x="-2.8" y="-1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
              <smd name="30" x="-2.8" y="1.325" dx="0.23" dy="0.63" layer="1" stop="no" cream="no" />
            </package>
          </packages>
          <symbols>
            <symbol name="DF37NC-30DS-0.4V(51)">
              <wire x1="-7.62" y1="17.78" x2="-6.35" y2="17.78" width="0.254" layer="94" />
              <wire x1="-5.715" y1="17.145" x2="-5.715" y2="18.415" width="0.254" layer="94" curve="-180" />
              <wire x1="7.62" y1="17.78" x2="6.35" y2="17.78" width="0.254" layer="94" />
              <wire x1="5.715" y1="18.415" x2="5.715" y2="17.145" width="0.254" layer="94" curve="-180" />
              <wire x1="-7.62" y1="15.24" x2="-6.35" y2="15.24" width="0.254" layer="94" />
              <wire x1="-5.715" y1="14.605" x2="-5.715" y2="15.875" width="0.254" layer="94" curve="-180" />
              <wire x1="7.62" y1="15.24" x2="6.35" y2="15.24" width="0.254" layer="94" />
              <wire x1="5.715" y1="15.875" x2="5.715" y2="14.605" width="0.254" layer="94" curve="-180" />
              <wire x1="-7.62" y1="12.7" x2="-6.35" y2="12.7" width="0.254" layer="94" />
              <wire x1="-5.715" y1="12.065" x2="-5.715" y2="13.335" width="0.254" layer="94" curve="-180" />
              <wire x1="7.62" y1="12.7" x2="6.35" y2="12.7" width="0.254" layer="94" />
              <wire x1="5.715" y1="13.335" x2="5.715" y2="12.065" width="0.254" layer="94" curve="-180" />
              <wire x1="-7.62" y1="10.16" x2="-6.35" y2="10.16" width="0.254" layer="94" />
              <wire x1="-5.715" y1="9.525" x2="-5.715" y2="10.795" width="0.254" layer="94" curve="-180" />
              <wire x1="7.62" y1="10.16" x2="6.35" y2="10.16" width="0.254" layer="94" />
              <wire x1="5.715" y1="10.795" x2="5.715" y2="9.525" width="0.254" layer="94" curve="-180" />
              <wire x1="-7.62" y1="7.62" x2="-6.35" y2="7.62" width="0.254" layer="94" />
              <wire x1="-5.715" y1="6.985" x2="-5.715" y2="8.255" width="0.254" layer="94" curve="-180" />
              <wire x1="7.62" y1="7.62" x2="6.35" y2="7.62" width="0.254" layer="94" />
              <wire x1="5.715" y1="8.255" x2="5.715" y2="6.985" width="0.254" layer="94" curve="-180" />
              <wire x1="-7.62" y1="5.08" x2="-6.35" y2="5.08" width="0.254" layer="94" />
              <wire x1="-5.715" y1="4.445" x2="-5.715" y2="5.715" width="0.254" layer="94" curve="-180" />
              <wire x1="7.62" y1="5.08" x2="6.35" y2="5.08" width="0.254" layer="94" />
              <wire x1="5.715" y1="5.715" x2="5.715" y2="4.445" width="0.254" layer="94" curve="-180" />
              <wire x1="-7.62" y1="2.54" x2="-6.35" y2="2.54" width="0.254" layer="94" />
              <wire x1="-5.715" y1="1.905" x2="-5.715" y2="3.175" width="0.254" layer="94" curve="-180" />
              <wire x1="7.62" y1="2.54" x2="6.35" y2="2.54" width="0.254" layer="94" />
              <wire x1="5.715" y1="3.175" x2="5.715" y2="1.905" width="0.254" layer="94" curve="-180" />
              <wire x1="-7.62" y1="0" x2="-6.35" y2="0" width="0.254" layer="94" />
              <wire x1="-5.715" y1="-0.635" x2="-5.715" y2="0.635" width="0.254" layer="94" curve="-180" />
              <wire x1="7.62" y1="0" x2="6.35" y2="0" width="0.254" layer="94" />
              <wire x1="5.715" y1="0.635" x2="5.715" y2="-0.635" width="0.254" layer="94" curve="-180" />
              <wire x1="-7.62" y1="-2.54" x2="-6.35" y2="-2.54" width="0.254" layer="94" />
              <wire x1="-5.715" y1="-3.175" x2="-5.715" y2="-1.905" width="0.254" layer="94" curve="-180" />
              <wire x1="7.62" y1="-2.54" x2="6.35" y2="-2.54" width="0.254" layer="94" />
              <wire x1="5.715" y1="-1.905" x2="5.715" y2="-3.175" width="0.254" layer="94" curve="-180" />
              <wire x1="-7.62" y1="-5.08" x2="-6.35" y2="-5.08" width="0.254" layer="94" />
              <wire x1="-5.715" y1="-5.715" x2="-5.715" y2="-4.445" width="0.254" layer="94" curve="-180" />
              <wire x1="7.62" y1="-5.08" x2="6.35" y2="-5.08" width="0.254" layer="94" />
              <wire x1="5.715" y1="-4.445" x2="5.715" y2="-5.715" width="0.254" layer="94" curve="-180" />
              <wire x1="-7.62" y1="-7.62" x2="-6.35" y2="-7.62" width="0.254" layer="94" />
              <wire x1="-5.715" y1="-8.255" x2="-5.715" y2="-6.985" width="0.254" layer="94" curve="-180" />
              <wire x1="7.62" y1="-7.62" x2="6.35" y2="-7.62" width="0.254" layer="94" />
              <wire x1="5.715" y1="-6.985" x2="5.715" y2="-8.255" width="0.254" layer="94" curve="-180" />
              <wire x1="-7.62" y1="-10.16" x2="-6.35" y2="-10.16" width="0.254" layer="94" />
              <wire x1="-5.715" y1="-10.795" x2="-5.715" y2="-9.525" width="0.254" layer="94" curve="-180" />
              <wire x1="7.62" y1="-10.16" x2="6.35" y2="-10.16" width="0.254" layer="94" />
              <wire x1="5.715" y1="-9.525" x2="5.715" y2="-10.795" width="0.254" layer="94" curve="-180" />
              <wire x1="-7.62" y1="-12.7" x2="-6.35" y2="-12.7" width="0.254" layer="94" />
              <wire x1="-5.715" y1="-13.335" x2="-5.715" y2="-12.065" width="0.254" layer="94" curve="-180" />
              <wire x1="7.62" y1="-12.7" x2="6.35" y2="-12.7" width="0.254" layer="94" />
              <wire x1="5.715" y1="-12.065" x2="5.715" y2="-13.335" width="0.254" layer="94" curve="-180" />
              <wire x1="-7.62" y1="-15.24" x2="-6.35" y2="-15.24" width="0.254" layer="94" />
              <wire x1="-5.715" y1="-15.875" x2="-5.715" y2="-14.605" width="0.254" layer="94" curve="-180" />
              <wire x1="7.62" y1="-15.24" x2="6.35" y2="-15.24" width="0.254" layer="94" />
              <wire x1="5.715" y1="-14.605" x2="5.715" y2="-15.875" width="0.254" layer="94" curve="-180" />
              <wire x1="-7.62" y1="-17.78" x2="-6.35" y2="-17.78" width="0.254" layer="94" />
              <wire x1="-5.715" y1="-18.415" x2="-5.715" y2="-17.145" width="0.254" layer="94" curve="-180" />
              <wire x1="7.62" y1="-17.78" x2="6.35" y2="-17.78" width="0.254" layer="94" />
              <wire x1="5.715" y1="-17.145" x2="5.715" y2="-18.415" width="0.254" layer="94" curve="-180" />
              <wire x1="-7.62" y1="-20.32" x2="-7.62" y2="20.32" width="0.254" layer="94" />
              <wire x1="-7.62" y1="20.32" x2="7.62" y2="20.32" width="0.254" layer="94" />
              <wire x1="7.62" y1="20.32" x2="7.62" y2="-20.32" width="0.254" layer="94" />
              <wire x1="7.62" y1="-20.32" x2="-7.62" y2="-20.32" width="0.254" layer="94" />
              <text x="-7.62" y="20.828" size="1.778" layer="95">&gt;NAME</text>
              <text x="-7.62" y="-22.86" size="1.778" layer="96">&gt;VALUE</text>
              <pin name="01" x="-12.7" y="17.78" length="middle" direction="pas" />
              <pin name="02" x="12.7" y="17.78" length="middle" direction="pas" rot="R180" />
              <pin name="03" x="-12.7" y="15.24" length="middle" direction="pas" />
              <pin name="04" x="12.7" y="15.24" length="middle" direction="pas" rot="R180" />
              <pin name="05" x="-12.7" y="12.7" length="middle" direction="pas" />
              <pin name="06" x="12.7" y="12.7" length="middle" direction="pas" rot="R180" />
              <pin name="07" x="-12.7" y="10.16" length="middle" direction="pas" />
              <pin name="08" x="12.7" y="10.16" length="middle" direction="pas" rot="R180" />
              <pin name="09" x="-12.7" y="7.62" length="middle" direction="pas" />
              <pin name="10" x="12.7" y="7.62" length="middle" direction="pas" rot="R180" />
              <pin name="11" x="-12.7" y="5.08" length="middle" direction="pas" />
              <pin name="12" x="12.7" y="5.08" length="middle" direction="pas" rot="R180" />
              <pin name="13" x="-12.7" y="2.54" length="middle" direction="pas" />
              <pin name="14" x="12.7" y="2.54" length="middle" direction="pas" rot="R180" />
              <pin name="15" x="-12.7" y="0" length="middle" direction="pas" />
              <pin name="16" x="12.7" y="0" length="middle" direction="pas" rot="R180" />
              <pin name="17" x="-12.7" y="-2.54" length="middle" direction="pas" />
              <pin name="18" x="12.7" y="-2.54" length="middle" direction="pas" rot="R180" />
              <pin name="19" x="-12.7" y="-5.08" length="middle" direction="pas" />
              <pin name="20" x="12.7" y="-5.08" length="middle" direction="pas" rot="R180" />
              <pin name="21" x="-12.7" y="-7.62" length="middle" direction="pas" />
              <pin name="22" x="12.7" y="-7.62" length="middle" direction="pas" rot="R180" />
              <pin name="23" x="-12.7" y="-10.16" length="middle" direction="pas" />
              <pin name="24" x="12.7" y="-10.16" length="middle" direction="pas" rot="R180" />
              <pin name="25" x="-12.7" y="-12.7" length="middle" direction="pas" />
              <pin name="26" x="12.7" y="-12.7" length="middle" direction="pas" rot="R180" />
              <pin name="27" x="-12.7" y="-15.24" length="middle" direction="pas" />
              <pin name="28" x="12.7" y="-15.24" length="middle" direction="pas" rot="R180" />
              <pin name="29" x="-12.7" y="-17.78" length="middle" direction="pas" />
              <pin name="30" x="12.7" y="-17.78" length="middle" direction="pas" rot="R180" />
            </symbol>
          </symbols>
          <devicesets>
            <deviceset name="DF37NC-30DS-0.4V(51)" prefix="J">
              <gates>
                <gate name="G$1" symbol="DF37NC-30DS-0.4V(51)" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="HRS_DF37NC-30DS-0.4V(51)">
                  <connects>
                    <connect gate="G$1" pin="01" pad="01" />
                    <connect gate="G$1" pin="02" pad="02" />
                    <connect gate="G$1" pin="03" pad="03" />
                    <connect gate="G$1" pin="04" pad="04" />
                    <connect gate="G$1" pin="05" pad="05" />
                    <connect gate="G$1" pin="06" pad="06" />
                    <connect gate="G$1" pin="07" pad="07" />
                    <connect gate="G$1" pin="08" pad="08" />
                    <connect gate="G$1" pin="09" pad="09" />
                    <connect gate="G$1" pin="10" pad="10" />
                    <connect gate="G$1" pin="11" pad="11" />
                    <connect gate="G$1" pin="12" pad="12" />
                    <connect gate="G$1" pin="13" pad="13" />
                    <connect gate="G$1" pin="14" pad="14" />
                    <connect gate="G$1" pin="15" pad="15" />
                    <connect gate="G$1" pin="16" pad="16" />
                    <connect gate="G$1" pin="17" pad="17" />
                    <connect gate="G$1" pin="18" pad="18" />
                    <connect gate="G$1" pin="19" pad="19" />
                    <connect gate="G$1" pin="20" pad="20" />
                    <connect gate="G$1" pin="21" pad="21" />
                    <connect gate="G$1" pin="22" pad="22" />
                    <connect gate="G$1" pin="23" pad="23" />
                    <connect gate="G$1" pin="24" pad="24" />
                    <connect gate="G$1" pin="25" pad="25" />
                    <connect gate="G$1" pin="26" pad="26" />
                    <connect gate="G$1" pin="27" pad="27" />
                    <connect gate="G$1" pin="28" pad="28" />
                    <connect gate="G$1" pin="29" pad="29" />
                    <connect gate="G$1" pin="30" pad="30" />
                  </connects>
                  <technologies>
                    <technology name="">
                      <attribute name="DATASHEET_URL" value="https://s3.amazonaws.com/snapeda/datasheet/DF37NC-30DS-04V-51-_Hirose.pdf" />
                      <attribute name="DESCRIPTION" value="30 Position Connector Receptacle, Center Strip Contacts Surface Mount Gold" />
                      <attribute name="MANUFACTURER" value="Hirose" />
                      <attribute name="MAXIMUM_PACKAGE_HEIGHT" value="1.08mm" />
                      <attribute name="MPN" value="DF37NC-30DS-0.4V(51)" />
                      <attribute name="PARTREV" value="11.02.09" />
                      <attribute name="SOURCE_URL" value="https://www.snapeda.com/parts/DF37NC-30DS-0.4V(51)/Hirose/view-part/" />
                      <attribute name="STANDARD" value="Manufacturer Recommendations" />
                    </technology>
                  </technologies>
                </device>
              </devices>
            </deviceset>
          </devicesets>
        </library>
        <library name="INMP441">
          <packages>
            <package name="MIC_INMP441">
              <wire x1="-1.88" y1="2.39" x2="1.88" y2="2.39" width="0.127" layer="21" />
              <wire x1="-1.88" y1="-2.42" x2="1.88" y2="-2.42" width="0.127" layer="21" />
              <wire x1="-2.13" y1="2.61" x2="2.13" y2="2.61" width="0.05" layer="39" />
              <wire x1="2.13" y1="2.61" x2="2.13" y2="-2.61" width="0.05" layer="39" />
              <wire x1="-2.13" y1="2.61" x2="-2.13" y2="-2.61" width="0.05" layer="39" />
              <wire x1="-2.13" y1="-2.61" x2="2.13" y2="-2.61" width="0.05" layer="39" />
              <circle x="-2.4" y="1.87" radius="0.1" width="0.2" layer="21" />
              <circle x="-2.4" y="1.87" radius="0.1" width="0.2" layer="51" />
              <text x="-2.5" y="2.75" size="1.016" layer="25">&gt;NAME</text>
              <text x="-2.5" y="-2.75" size="1.016" layer="27" align="top-left">&gt;VALUE</text>
              <wire x1="-1.88" y1="2.36" x2="1.88" y2="2.36" width="0.127" layer="51" />
              <wire x1="1.88" y1="2.36" x2="1.88" y2="-2.36" width="0.127" layer="51" />
              <wire x1="-1.88" y1="2.36" x2="-1.88" y2="-2.36" width="0.127" layer="51" />
              <wire x1="-1.88" y1="-2.36" x2="1.88" y2="-2.36" width="0.127" layer="51" />
              <polygon width="0" layer="1">
                <vertex x="0" y="-1.77" />
                <vertex x="0" y="-2.07" curve="90" />
                <vertex x="0.78" y="-1.29" curve="90" />
                <vertex x="0" y="-0.51" />
                <vertex x="0" y="-0.81" curve="-90" />
                <vertex x="0.48" y="-1.29" curve="-90" />
              </polygon>
              <polygon width="0" layer="1">
                <vertex x="0" y="-0.81" />
                <vertex x="0" y="-0.51" curve="90" />
                <vertex x="-0.78" y="-1.29" curve="90" />
                <vertex x="0" y="-2.07" />
                <vertex x="0" y="-1.77" curve="-90" />
                <vertex x="-0.48" y="-1.29" curve="-90" />
              </polygon>
              <circle x="0" y="-1.29" radius="0.4" width="0.8" layer="29" />
              <rectangle x1="-1.605" y1="-1.455" x2="-1.055" y2="-1.105" layer="31" />
              <rectangle x1="-1.605" y1="-0.405" x2="-1.055" y2="-0.055" layer="31" />
              <rectangle x1="-1.605" y1="0.645" x2="-1.055" y2="0.995" layer="31" />
              <rectangle x1="-1.605" y1="1.695" x2="-1.055" y2="2.045" layer="31" />
              <rectangle x1="1.055" y1="-1.455" x2="1.605" y2="-1.105" layer="31" />
              <rectangle x1="1.055" y1="-0.405" x2="1.605" y2="-0.055" layer="31" />
              <rectangle x1="1.055" y1="0.645" x2="1.605" y2="0.995" layer="31" />
              <rectangle x1="1.055" y1="1.695" x2="1.605" y2="2.045" layer="31" />
              <polygon width="0" layer="31">
                <vertex x="-0.491438" y="-0.657141" />
                <vertex x="-0.293447" y="-0.855131" curve="-80" />
                <vertex x="0.371228" y="-0.918772" curve="-80" />
                <vertex x="0.434869" y="-1.58345" />
                <vertex x="0.632859" y="-1.78144" curve="85" />
                <vertex x="0.565684" y="-0.724316" curve="85" />
              </polygon>
              <polygon width="0" layer="31">
                <vertex x="0.491438" y="-1.92286" />
                <vertex x="0.293447" y="-1.72487" curve="-80" />
                <vertex x="-0.371228" y="-1.66123" curve="-80" />
                <vertex x="-0.434869" y="-0.996553" />
                <vertex x="-0.632859" y="-0.798562" curve="85" />
                <vertex x="-0.565684" y="-1.85568" curve="85" />
              </polygon>
              <smd name="1" x="-1.33" y="1.87" dx="0.6" dy="0.4" layer="1" cream="no" />
              <smd name="2" x="-1.33" y="0.82" dx="0.6" dy="0.4" layer="1" cream="no" />
              <smd name="9" x="1.33" y="1.87" dx="0.6" dy="0.4" layer="1" cream="no" />
              <smd name="8" x="1.33" y="0.82" dx="0.6" dy="0.4" layer="1" cream="no" />
              <smd name="5_1" x="-0.63" y="-1.29" dx="0.1" dy="0.1" layer="1" stop="no" cream="no" />
              <smd name="3" x="-1.33" y="-0.23" dx="0.6" dy="0.4" layer="1" cream="no" />
              <smd name="4" x="-1.33" y="-1.28" dx="0.6" dy="0.4" layer="1" cream="no" />
              <smd name="7" x="1.33" y="-0.23" dx="0.6" dy="0.4" layer="1" cream="no" />
              <smd name="6" x="1.33" y="-1.28" dx="0.6" dy="0.4" layer="1" cream="no" />
              <smd name="5_2" x="0.63" y="-1.29" dx="0.1" dy="0.1" layer="1" stop="no" cream="no" />
              <hole x="0" y="-1.29" drill="0.5" />
            </package>
          </packages>
          <symbols>
            <symbol name="INMP441">
              <wire x1="12.7" y1="-10.16" x2="-12.7" y2="-10.16" width="0.254" layer="94" />
              <wire x1="-12.7" y1="-10.16" x2="-12.7" y2="10.16" width="0.254" layer="94" />
              <wire x1="-12.7" y1="10.16" x2="12.7" y2="10.16" width="0.254" layer="94" />
              <wire x1="12.7" y1="10.16" x2="12.7" y2="-10.16" width="0.254" layer="94" />
              <text x="-12.7" y="10.795" size="1.778" layer="95">&gt;NAME</text>
              <text x="-12.7" y="-12.7" size="1.778" layer="96">&gt;VALUE</text>
              <pin name="SCK" x="17.78" y="2.54" length="middle" direction="in" function="clk" rot="R180" />
              <pin name="SD" x="17.78" y="-2.54" length="middle" rot="R180" />
              <pin name="VDD" x="17.78" y="7.62" length="middle" direction="pwr" rot="R180" />
              <pin name="GND" x="17.78" y="-7.62" length="middle" direction="pwr" rot="R180" />
              <pin name="L/R" x="-17.78" y="-2.54" length="middle" direction="in" />
              <pin name="WS" x="17.78" y="0" length="middle" direction="in" rot="R180" />
              <pin name="CHIPEN" x="-17.78" y="2.54" length="middle" direction="in" />
            </symbol>
          </symbols>
          <devicesets>
            <deviceset name="INMP441" prefix="MK">
              <gates>
                <gate name="G$1" symbol="INMP441" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="MIC_INMP441">
                  <connects>
                    <connect gate="G$1" pin="CHIPEN" pad="8" />
                    <connect gate="G$1" pin="GND" pad="5_1 5_2 6 9" />
                    <connect gate="G$1" pin="L/R" pad="4" />
                    <connect gate="G$1" pin="SCK" pad="1" />
                    <connect gate="G$1" pin="SD" pad="2" />
                    <connect gate="G$1" pin="VDD" pad="7" />
                    <connect gate="G$1" pin="WS" pad="3" />
                  </connects>
                  <technologies>
                    <technology name="">
                      <attribute name="DATASHEET_URL" value="https://s3.amazonaws.com/snapeda/datasheet/INMP441_TDK_InvenSense.pdf" />
                      <attribute name="DESCRIPTION" value="EVAL BOARD MEMS MIC INMP441" />
                      <attribute name="MANUFACTURER" value="TDK InvenSense" />
                      <attribute name="MAXIMUM_PACKAGE_HEIGHT" value="1.05 mm" />
                      <attribute name="MPN" value="INMP441" />
                      <attribute name="PARTREV" value="1.1" />
                      <attribute name="SOURCE_URL" value="https://www.snapeda.com/parts/INMP441/TDK/view-part/" />
                      <attribute name="STANDARD" value="Manufacturer Recommendations" />
                    </technology>
                  </technologies>
                </device>
              </devices>
            </deviceset>
          </devicesets>
        </library>
        <library name="FRIDAY_SCH3_Camera">
          <packages>
            <package name="TSOT25_AP3429">
              <wire x1="-1.45" y1="-0.8" x2="1.45" y2="-0.8" width="0.1524" layer="51" />
              <wire x1="1.45" y1="-0.8" x2="1.45" y2="0.8" width="0.1524" layer="51" />
              <wire x1="1.45" y1="0.8" x2="-1.45" y2="0.8" width="0.1524" layer="51" />
              <wire x1="-1.45" y1="0.8" x2="-1.45" y2="-0.8" width="0.1524" layer="51" />
              <wire x1="-1.7" y1="-1.05" x2="1.7" y2="-1.05" width="0.1524" layer="39" />
              <wire x1="1.7" y1="-1.05" x2="1.7" y2="1.05" width="0.1524" layer="39" />
              <wire x1="1.7" y1="1.05" x2="-1.7" y2="1.05" width="0.1524" layer="39" />
              <wire x1="-1.7" y1="1.05" x2="-1.7" y2="-1.05" width="0.1524" layer="39" />
              <text x="-1.45" y="1.15" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-0.95" y="-1.05" dx="0.65" dy="0.85" layer="1" cream="yes" />
              <smd name="2" x="0" y="-1.05" dx="0.65" dy="0.85" layer="1" cream="yes" />
              <smd name="3" x="0.95" y="-1.05" dx="0.65" dy="0.85" layer="1" cream="yes" />
              <smd name="4" x="0.95" y="1.05" dx="0.65" dy="0.85" layer="1" cream="yes" />
              <smd name="5" x="-0.95" y="1.05" dx="0.65" dy="0.85" layer="1" cream="yes" />
              <circle x="-1.4" y="-1.45" radius="0.1" width="0.15" layer="21" />
            </package>
            <package name="SOT25_AP7331">
              <wire x1="-1.45" y1="-0.8" x2="1.45" y2="-0.8" width="0.1524" layer="51" />
              <wire x1="1.45" y1="-0.8" x2="1.45" y2="0.8" width="0.1524" layer="51" />
              <wire x1="1.45" y1="0.8" x2="-1.45" y2="0.8" width="0.1524" layer="51" />
              <wire x1="-1.45" y1="0.8" x2="-1.45" y2="-0.8" width="0.1524" layer="51" />
              <wire x1="-1.7" y1="-1.05" x2="1.7" y2="-1.05" width="0.1524" layer="39" />
              <wire x1="1.7" y1="-1.05" x2="1.7" y2="1.05" width="0.1524" layer="39" />
              <wire x1="1.7" y1="1.05" x2="-1.7" y2="1.05" width="0.1524" layer="39" />
              <wire x1="-1.7" y1="1.05" x2="-1.7" y2="-1.05" width="0.1524" layer="39" />
              <text x="-1.45" y="1.15" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-0.95" y="-1.05" dx="0.65" dy="0.85" layer="1" cream="yes" />
              <smd name="2" x="0" y="-1.05" dx="0.65" dy="0.85" layer="1" cream="yes" />
              <smd name="3" x="0.95" y="-1.05" dx="0.65" dy="0.85" layer="1" cream="yes" />
              <smd name="4" x="0.95" y="1.05" dx="0.65" dy="0.85" layer="1" cream="yes" />
              <smd name="5" x="-0.95" y="1.05" dx="0.65" dy="0.85" layer="1" cream="yes" />
              <circle x="-1.4" y="-1.45" radius="0.1" width="0.15" layer="21" />
            </package>
            <package name="SOT23_DBV">
              <wire x1="-1.45" y1="-0.8" x2="1.45" y2="-0.8" width="0.1524" layer="51" />
              <wire x1="1.45" y1="-0.8" x2="1.45" y2="0.8" width="0.1524" layer="51" />
              <wire x1="1.45" y1="0.8" x2="-1.45" y2="0.8" width="0.1524" layer="51" />
              <wire x1="-1.45" y1="0.8" x2="-1.45" y2="-0.8" width="0.1524" layer="51" />
              <wire x1="-1.7" y1="-1.05" x2="1.7" y2="-1.05" width="0.1524" layer="39" />
              <wire x1="1.7" y1="-1.05" x2="1.7" y2="1.05" width="0.1524" layer="39" />
              <wire x1="1.7" y1="1.05" x2="-1.7" y2="1.05" width="0.1524" layer="39" />
              <wire x1="-1.7" y1="1.05" x2="-1.7" y2="-1.05" width="0.1524" layer="39" />
              <text x="-1.45" y="1.15" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-0.95" y="-1.05" dx="0.65" dy="0.85" layer="1" cream="yes" />
              <smd name="2" x="0" y="-1.05" dx="0.65" dy="0.85" layer="1" cream="yes" />
              <smd name="3" x="0.95" y="-1.05" dx="0.65" dy="0.85" layer="1" cream="yes" />
              <smd name="4" x="0.95" y="1.05" dx="0.65" dy="0.85" layer="1" cream="yes" />
              <smd name="5" x="-0.95" y="1.05" dx="0.65" dy="0.85" layer="1" cream="yes" />
              <circle x="-1.4" y="-1.45" radius="0.1" width="0.15" layer="21" />
            </package>
            <package name="XFL4020">
              <wire x1="-2.0" y1="-2.0" x2="2.0" y2="-2.0" width="0.1524" layer="51" />
              <wire x1="2.0" y1="-2.0" x2="2.0" y2="2.0" width="0.1524" layer="51" />
              <wire x1="2.0" y1="2.0" x2="-2.0" y2="2.0" width="0.1524" layer="51" />
              <wire x1="-2.0" y1="2.0" x2="-2.0" y2="-2.0" width="0.1524" layer="51" />
              <wire x1="-2.25" y1="-2.25" x2="2.25" y2="-2.25" width="0.1524" layer="39" />
              <wire x1="2.25" y1="-2.25" x2="2.25" y2="2.25" width="0.1524" layer="39" />
              <wire x1="2.25" y1="2.25" x2="-2.25" y2="2.25" width="0.1524" layer="39" />
              <wire x1="-2.25" y1="2.25" x2="-2.25" y2="-2.25" width="0.1524" layer="39" />
              <text x="-2.0" y="2.35" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-1.45" y="0" dx="1.6" dy="3.7" layer="1" cream="yes" />
              <smd name="2" x="1.45" y="0" dx="1.6" dy="3.7" layer="1" cream="yes" />
            </package>
            <package name="MLCC_1206">
              <wire x1="-1.6" y1="-0.8" x2="1.6" y2="-0.8" width="0.1524" layer="51" />
              <wire x1="1.6" y1="-0.8" x2="1.6" y2="0.8" width="0.1524" layer="51" />
              <wire x1="1.6" y1="0.8" x2="-1.6" y2="0.8" width="0.1524" layer="51" />
              <wire x1="-1.6" y1="0.8" x2="-1.6" y2="-0.8" width="0.1524" layer="51" />
              <wire x1="-1.85" y1="-1.05" x2="1.85" y2="-1.05" width="0.1524" layer="39" />
              <wire x1="1.85" y1="-1.05" x2="1.85" y2="1.05" width="0.1524" layer="39" />
              <wire x1="1.85" y1="1.05" x2="-1.85" y2="1.05" width="0.1524" layer="39" />
              <wire x1="-1.85" y1="1.05" x2="-1.85" y2="-1.05" width="0.1524" layer="39" />
              <text x="-1.6" y="1.15" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-1.4" y="0" dx="1.4" dy="1.8" layer="1" cream="yes" />
              <smd name="2" x="1.4" y="0" dx="1.4" dy="1.8" layer="1" cream="yes" />
            </package>
            <package name="SIT_2016_4">
              <wire x1="-1.0" y1="-0.8" x2="1.0" y2="-0.8" width="0.1524" layer="51" />
              <wire x1="1.0" y1="-0.8" x2="1.0" y2="0.8" width="0.1524" layer="51" />
              <wire x1="1.0" y1="0.8" x2="-1.0" y2="0.8" width="0.1524" layer="51" />
              <wire x1="-1.0" y1="0.8" x2="-1.0" y2="-0.8" width="0.1524" layer="51" />
              <wire x1="-1.25" y1="-1.05" x2="1.25" y2="-1.05" width="0.1524" layer="39" />
              <wire x1="1.25" y1="-1.05" x2="1.25" y2="1.05" width="0.1524" layer="39" />
              <wire x1="1.25" y1="1.05" x2="-1.25" y2="1.05" width="0.1524" layer="39" />
              <wire x1="-1.25" y1="1.05" x2="-1.25" y2="-1.05" width="0.1524" layer="39" />
              <text x="-1.0" y="1.15" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-0.7" y="-0.53" dx="0.72" dy="0.65" layer="1" cream="yes" />
              <smd name="2" x="0.7" y="-0.53" dx="0.72" dy="0.65" layer="1" cream="yes" />
              <smd name="3" x="0.7" y="0.53" dx="0.72" dy="0.65" layer="1" cream="yes" />
              <smd name="4" x="-0.7" y="0.53" dx="0.72" dy="0.65" layer="1" cream="yes" />
              <circle x="-1.21" y="-0.65" radius="0.1" width="0.15" layer="21" />
            </package>
            <package name="TI_RGP20">
              <wire x1="-2.0" y1="-2.0" x2="2.0" y2="-2.0" width="0.1524" layer="51" />
              <wire x1="2.0" y1="-2.0" x2="2.0" y2="2.0" width="0.1524" layer="51" />
              <wire x1="2.0" y1="2.0" x2="-2.0" y2="2.0" width="0.1524" layer="51" />
              <wire x1="-2.0" y1="2.0" x2="-2.0" y2="-2.0" width="0.1524" layer="51" />
              <wire x1="-2.25" y1="-2.25" x2="2.25" y2="-2.25" width="0.1524" layer="39" />
              <wire x1="2.25" y1="-2.25" x2="2.25" y2="2.25" width="0.1524" layer="39" />
              <wire x1="2.25" y1="2.25" x2="-2.25" y2="2.25" width="0.1524" layer="39" />
              <wire x1="-2.25" y1="2.25" x2="-2.25" y2="-2.25" width="0.1524" layer="39" />
              <text x="-2.0" y="2.35" size="0.8" layer="25">&gt;NAME</text>
              <smd name="EP" x="0" y="0" dx="2.5" dy="2.5" layer="1" cream="no" />
              <smd name="1" x="-1.95" y="1.0" dx="0.65" dy="0.27" layer="1" cream="yes" />
              <smd name="6" x="-1.0" y="-1.95" dx="0.27" dy="0.65" layer="1" cream="yes" />
              <smd name="11" x="1.95" y="-1.0" dx="0.65" dy="0.27" layer="1" cream="yes" />
              <smd name="16" x="1.0" y="1.95" dx="0.27" dy="0.65" layer="1" cream="yes" />
              <smd name="2" x="-1.95" y="0.5" dx="0.65" dy="0.27" layer="1" cream="yes" />
              <smd name="7" x="-0.5" y="-1.95" dx="0.27" dy="0.65" layer="1" cream="yes" />
              <smd name="12" x="1.95" y="-0.5" dx="0.65" dy="0.27" layer="1" cream="yes" />
              <smd name="17" x="0.5" y="1.95" dx="0.27" dy="0.65" layer="1" cream="yes" />
              <smd name="3" x="-1.95" y="0.0" dx="0.65" dy="0.27" layer="1" cream="yes" />
              <smd name="8" x="-0.0" y="-1.95" dx="0.27" dy="0.65" layer="1" cream="yes" />
              <smd name="13" x="1.95" y="-0.0" dx="0.65" dy="0.27" layer="1" cream="yes" />
              <smd name="18" x="0.0" y="1.95" dx="0.27" dy="0.65" layer="1" cream="yes" />
              <smd name="4" x="-1.95" y="-0.5" dx="0.65" dy="0.27" layer="1" cream="yes" />
              <smd name="9" x="0.5" y="-1.95" dx="0.27" dy="0.65" layer="1" cream="yes" />
              <smd name="14" x="1.95" y="0.5" dx="0.65" dy="0.27" layer="1" cream="yes" />
              <smd name="19" x="-0.5" y="1.95" dx="0.27" dy="0.65" layer="1" cream="yes" />
              <smd name="5" x="-1.95" y="-1.0" dx="0.65" dy="0.27" layer="1" cream="yes" />
              <smd name="10" x="1.0" y="-1.95" dx="0.27" dy="0.65" layer="1" cream="yes" />
              <smd name="15" x="1.95" y="1.0" dx="0.65" dy="0.27" layer="1" cream="yes" />
              <smd name="20" x="-1.0" y="1.95" dx="0.27" dy="0.65" layer="1" cream="yes" />
              <circle x="-2.25" y="1.3" radius="0.1" width="0.15" layer="21" />
            </package>
            <package name="DLP11SN_0504">
              <wire x1="-0.625" y1="-0.5" x2="0.625" y2="-0.5" width="0.1524" layer="51" />
              <wire x1="0.625" y1="-0.5" x2="0.625" y2="0.5" width="0.1524" layer="51" />
              <wire x1="0.625" y1="0.5" x2="-0.625" y2="0.5" width="0.1524" layer="51" />
              <wire x1="-0.625" y1="0.5" x2="-0.625" y2="-0.5" width="0.1524" layer="51" />
              <wire x1="-0.875" y1="-0.75" x2="0.875" y2="-0.75" width="0.1524" layer="39" />
              <wire x1="0.875" y1="-0.75" x2="0.875" y2="0.75" width="0.1524" layer="39" />
              <wire x1="0.875" y1="0.75" x2="-0.875" y2="0.75" width="0.1524" layer="39" />
              <wire x1="-0.875" y1="0.75" x2="-0.875" y2="-0.75" width="0.1524" layer="39" />
              <text x="-0.625" y="0.85" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-0.51" y="0.28" dx="0.39" dy="0.36" layer="1" cream="yes" />
              <smd name="2" x="0.51" y="0.28" dx="0.39" dy="0.36" layer="1" cream="yes" />
              <smd name="3" x="0.51" y="-0.28" dx="0.39" dy="0.36" layer="1" cream="yes" />
              <smd name="4" x="-0.51" y="-0.28" dx="0.39" dy="0.36" layer="1" cream="yes" />
            </package>
          </packages>
          <symbols>
            <symbol name="AP3429">
              <wire x1="-17.78" y1="-6.35" x2="17.78" y2="-6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-6.35" x2="17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="6.35" x2="-17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="6.35" x2="-17.78" y2="-6.35" width="0.1524" layer="94" />
              <text x="-17.78" y="7.619999999999999" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-8.89" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="VIN" x="-22.86" y="2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="EN" x="-22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="GND" x="-22.86" y="-2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="LX" x="22.86" y="1.27" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="FB" x="22.86" y="-1.27" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="AP7331">
              <wire x1="-17.78" y1="-6.35" x2="17.78" y2="-6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-6.35" x2="17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="6.35" x2="-17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="6.35" x2="-17.78" y2="-6.35" width="0.1524" layer="94" />
              <text x="-17.78" y="7.619999999999999" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-8.89" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="IN" x="-22.86" y="2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="EN" x="-22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="GND" x="-22.86" y="-2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="OUT" x="22.86" y="1.27" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="NC" x="22.86" y="-1.27" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="SN74LV1T34">
              <wire x1="-17.78" y1="-6.35" x2="17.78" y2="-6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-6.35" x2="17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="6.35" x2="-17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="6.35" x2="-17.78" y2="-6.35" width="0.1524" layer="94" />
              <text x="-17.78" y="7.619999999999999" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-8.89" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="A" x="-22.86" y="2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="VCC" x="-22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="GND" x="-22.86" y="-2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="Y" x="22.86" y="1.27" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="NC" x="22.86" y="-1.27" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="XFL4020">
              <pin name="1" x="-5.08" y="0.0" length="short" direction="pas" visible="off" rot="R0" />
              <pin name="2" x="5.08" y="0.0" length="short" direction="pas" visible="off" rot="R180" />
              <wire x1="-2.54" y1="1.27" x2="2.54" y2="1.27" width="0.1524" layer="94" />
              <wire x1="2.54" y1="1.27" x2="2.54" y2="-1.27" width="0.1524" layer="94" />
              <wire x1="2.54" y1="-1.27" x2="-2.54" y2="-1.27" width="0.1524" layer="94" />
              <wire x1="-2.54" y1="-1.27" x2="-2.54" y2="1.27" width="0.1524" layer="94" />
              <text x="-2.54" y="2.54" size="1.27" layer="95">&gt;NAME</text>
              <text x="-2.54" y="-3.81" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="C_1206">
              <pin name="1" x="-5.08" y="0.0" length="short" direction="pas" visible="off" rot="R0" />
              <pin name="2" x="5.08" y="0.0" length="short" direction="pas" visible="off" rot="R180" />
              <wire x1="-2.54" y1="1.27" x2="2.54" y2="1.27" width="0.1524" layer="94" />
              <wire x1="2.54" y1="1.27" x2="2.54" y2="-1.27" width="0.1524" layer="94" />
              <wire x1="2.54" y1="-1.27" x2="-2.54" y2="-1.27" width="0.1524" layer="94" />
              <wire x1="-2.54" y1="-1.27" x2="-2.54" y2="1.27" width="0.1524" layer="94" />
              <text x="-2.54" y="2.54" size="1.27" layer="95">&gt;NAME</text>
              <text x="-2.54" y="-3.81" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="SIT1602B">
              <wire x1="-17.78" y1="-6.35" x2="17.78" y2="-6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-6.35" x2="17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="6.35" x2="-17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="6.35" x2="-17.78" y2="-6.35" width="0.1524" layer="94" />
              <text x="-17.78" y="7.619999999999999" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-8.89" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="VDD" x="-22.86" y="2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="OE" x="-22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="GND" x="-22.86" y="-2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="CLK" x="22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="TPS386000">
              <wire x1="-17.78" y1="-16.51" x2="17.78" y2="-16.51" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-16.51" x2="17.78" y2="16.51" width="0.1524" layer="94" />
              <wire x1="17.78" y1="16.51" x2="-17.78" y2="16.51" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="16.51" x2="-17.78" y2="-16.51" width="0.1524" layer="94" />
              <text x="-17.78" y="17.78" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-19.05" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="VDD" x="-22.86" y="11.43" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="MR" x="-22.86" y="8.89" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="SENSE1" x="-22.86" y="6.35" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="SENSE2" x="-22.86" y="3.8099999999999996" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="SENSE3" x="-22.86" y="1.2699999999999996" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="SENSE4L" x="-22.86" y="-1.2699999999999996" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="SENSE4H" x="-22.86" y="-3.8100000000000005" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="GND" x="-22.86" y="-6.350000000000001" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="NC11" x="-22.86" y="-8.89" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="EP" x="-22.86" y="-11.43" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="RESET1" x="22.86" y="12.7" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="RESET2" x="22.86" y="10.16" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="RESET3" x="22.86" y="7.619999999999999" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="RESET4" x="22.86" y="5.079999999999999" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="CT1" x="22.86" y="2.539999999999999" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="CT2" x="22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="CT3" x="22.86" y="-2.540000000000001" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="CT4" x="22.86" y="-5.080000000000002" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="WDI" x="22.86" y="-7.620000000000001" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="WDO" x="22.86" y="-10.16" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="VREF" x="22.86" y="-12.7" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="DLP11SN900HL2L">
              <wire x1="-17.78" y1="-5.08" x2="17.78" y2="-5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-5.08" x2="17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="5.08" x2="-17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="5.08" x2="-17.78" y2="-5.08" width="0.1524" layer="94" />
              <text x="-17.78" y="6.35" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-7.62" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="FLEX_N" x="-22.86" y="1.27" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="FLEX_P" x="-22.86" y="-1.27" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="SENSOR_N" x="22.86" y="1.27" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="SENSOR_P" x="22.86" y="-1.27" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
          </symbols>
          <devicesets>
            <deviceset name="AP3429" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="AP3429" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="TSOT25_AP3429">
                  <connects>
                    <connect gate="G$1" pin="VIN" pad="4" />
                    <connect gate="G$1" pin="EN" pad="1" />
                    <connect gate="G$1" pin="GND" pad="2" />
                    <connect gate="G$1" pin="LX" pad="3" />
                    <connect gate="G$1" pin="FB" pad="5" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="AP7331" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="AP7331" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="SOT25_AP7331">
                  <connects>
                    <connect gate="G$1" pin="IN" pad="1" />
                    <connect gate="G$1" pin="EN" pad="3" />
                    <connect gate="G$1" pin="GND" pad="2" />
                    <connect gate="G$1" pin="OUT" pad="5" />
                    <connect gate="G$1" pin="NC" pad="4" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="SN74LV1T34" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="SN74LV1T34" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="SOT23_DBV">
                  <connects>
                    <connect gate="G$1" pin="A" pad="2" />
                    <connect gate="G$1" pin="VCC" pad="5" />
                    <connect gate="G$1" pin="GND" pad="3" />
                    <connect gate="G$1" pin="Y" pad="4" />
                    <connect gate="G$1" pin="NC" pad="1" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="XFL4020" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="XFL4020" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="XFL4020">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="C_1206" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="C_1206" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="MLCC_1206">
                  <connects>
                    <connect gate="G$1" pin="1" pad="1" />
                    <connect gate="G$1" pin="2" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="SIT1602B" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="SIT1602B" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="SIT_2016_4">
                  <connects>
                    <connect gate="G$1" pin="VDD" pad="4" />
                    <connect gate="G$1" pin="OE" pad="1" />
                    <connect gate="G$1" pin="GND" pad="2" />
                    <connect gate="G$1" pin="CLK" pad="3" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="TPS386000" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="TPS386000" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="TI_RGP20">
                  <connects>
                    <connect gate="G$1" pin="VDD" pad="14" />
                    <connect gate="G$1" pin="MR" pad="1" />
                    <connect gate="G$1" pin="SENSE1" pad="10" />
                    <connect gate="G$1" pin="SENSE2" pad="9" />
                    <connect gate="G$1" pin="SENSE3" pad="8" />
                    <connect gate="G$1" pin="SENSE4L" pad="7" />
                    <connect gate="G$1" pin="SENSE4H" pad="6" />
                    <connect gate="G$1" pin="GND" pad="12" />
                    <connect gate="G$1" pin="NC11" pad="11" />
                    <connect gate="G$1" pin="EP" pad="EP" />
                    <connect gate="G$1" pin="RESET1" pad="15" />
                    <connect gate="G$1" pin="RESET2" pad="16" />
                    <connect gate="G$1" pin="RESET3" pad="17" />
                    <connect gate="G$1" pin="RESET4" pad="18" />
                    <connect gate="G$1" pin="CT1" pad="5" />
                    <connect gate="G$1" pin="CT2" pad="4" />
                    <connect gate="G$1" pin="CT3" pad="3" />
                    <connect gate="G$1" pin="CT4" pad="2" />
                    <connect gate="G$1" pin="WDI" pad="20" />
                    <connect gate="G$1" pin="WDO" pad="19" />
                    <connect gate="G$1" pin="VREF" pad="13" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="DLP11SN900HL2L" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="DLP11SN900HL2L" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="DLP11SN_0504">
                  <connects>
                    <connect gate="G$1" pin="FLEX_N" pad="1" />
                    <connect gate="G$1" pin="FLEX_P" pad="4" />
                    <connect gate="G$1" pin="SENSOR_N" pad="2" />
                    <connect gate="G$1" pin="SENSOR_P" pad="3" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
          </devicesets>
        </library>
      </libraries>
      <attributes />
      <variantdefs>
        <variantdef name="default" />
      </variantdefs>
      <classes>
        <class number="0" name="default" width="0" drill="0" />
      </classes>
      <parts>
        <part name="FRAME1" library="FRIDAY_SCH1_Support" deviceset="A3_FRAME" device="" value="" />
        <part name="J2" library="FH12-24S-0.5SH_55_" deviceset="FH12-24S-0.5SH(55)" device="" value="FH12-24S-0.5SH(55)" />
        <part name="J1" library="DF37NC-30DS-0.4V_51_" deviceset="DF37NC-30DS-0.4V(51)" device="" value="DF37NC-30DS-0.4V(51)" />
        <part name="L2" library="FRIDAY_SCH3_Camera" deviceset="DLP11SN900HL2L" device="" value="DLP11SN900HL2L" />
        <part name="L3" library="FRIDAY_SCH3_Camera" deviceset="DLP11SN900HL2L" device="" value="DLP11SN900HL2L" />
        <part name="L4" library="FRIDAY_SCH3_Camera" deviceset="DLP11SN900HL2L" device="" value="DLP11SN900HL2L" />
        <part name="FRAME2" library="FRIDAY_SCH1_Support" deviceset="A3_FRAME" device="" value="" />
        <part name="U1" library="FRIDAY_SCH3_Camera" deviceset="AP3429" device="" value="AP3429KTTR-G1" />
        <part name="L1" library="FRIDAY_SCH3_Camera" deviceset="XFL4020" device="" value="XFL4020-222MEC 2.2uH" />
        <part name="U2" library="FRIDAY_SCH3_Camera" deviceset="AP7331" device="" value="AP7331-28WG-7" />
        <part name="U3" library="FRIDAY_SCH3_Camera" deviceset="AP7331" device="" value="AP7331-18WG-7" />
        <part name="U4" library="FRIDAY_SCH3_Camera" deviceset="SN74LV1T34" device="" value="SN74LV1T34DBVR" />
        <part name="R1" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="20k 0.1%" />
        <part name="R2" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="24k 0.1%" />
        <part name="R3" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="100k 1%" />
        <part name="R4" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="100k 1%" />
        <part name="C1" library="FRIDAY_SCH3_Camera" deviceset="C_1206" device="" value="22uF 10V X7R" />
        <part name="C2" library="FRIDAY_SCH3_Camera" deviceset="C_1206" device="" value="22uF 10V X7R" />
        <part name="C3" library="FRIDAY_SCH3_Camera" deviceset="C_1206" device="" value="22uF 10V X7R" />
        <part name="C4" library="FRIDAY_SCH1_Support" deviceset="C_0402" device="" value="330pF 25V C0G" />
        <part name="C5" library="FRIDAY_SCH1_Support" deviceset="C_0402" device="" value="1uF 16V X5R" />
        <part name="C6" library="FRIDAY_SCH1_Support" deviceset="C_0402" device="" value="1uF 16V X5R" />
        <part name="C7" library="FRIDAY_SCH1_Support" deviceset="C_0402" device="" value="1uF 16V X5R" />
        <part name="C8" library="FRIDAY_SCH1_Support" deviceset="C_0402" device="" value="1uF 16V X5R" />
        <part name="C9" library="FRIDAY_SCH1_Support" deviceset="C_0402" device="" value="100nF 16V X7R" />
        <part name="C10" library="FRIDAY_SCH1_Support" deviceset="C_0402" device="" value="1uF 16V X5R" />
        <part name="C11" library="FRIDAY_SCH1_Support" deviceset="C_0402" device="" value="1uF 16V X5R" />
        <part name="C12" library="FRIDAY_SCH1_Support" deviceset="C_0402" device="" value="100nF 25V X7R" />
        <part name="C13" library="FRIDAY_SCH1_Support" deviceset="C_0402" device="" value="1uF 16V X5R" />
        <part name="TP1" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="CAM_DVDD_1V1" />
        <part name="TP2" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="CAM_AVDD_AFVDD_2V8" />
        <part name="TP3" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="CAM_DOVDD_1V8" />
        <part name="FRAME3" library="FRIDAY_SCH1_Support" deviceset="A3_FRAME" device="" value="" />
        <part name="X1" library="FRIDAY_SCH3_Camera" deviceset="SIT1602B" device="" value="SIT1602BI-71-18E-24.000000D" />
        <part name="R5" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="22R 1%" />
        <part name="C14" library="FRIDAY_SCH1_Support" deviceset="C_0402" device="" value="1uF 16V X5R" />
        <part name="U5" library="FRIDAY_SCH3_Camera" deviceset="TPS386000" device="" value="TPS386000RGPR" />
        <part name="C15" library="FRIDAY_SCH1_Support" deviceset="C_0402" device="" value="100nF 16V X7R" />
        <part name="R6" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="15.4k 0.1%" />
        <part name="R7" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="10k 0.1%" />
        <part name="R8" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="32.4k 0.1%" />
        <part name="R9" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="10k 0.1%" />
        <part name="R10" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="54.9k 0.1%" />
        <part name="R11" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="10k 0.1%" />
        <part name="R12" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="10k 1%" />
        <part name="R13" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="0R DNP">
          <variant name="default" populate="no" />
        </part>
        <part name="R14" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="0R DNP">
          <variant name="default" populate="no" />
        </part>
        <part name="R15" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="2.2k 1%" />
        <part name="R16" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="2.2k 1%" />
        <part name="TP4" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="MCLK" />
        <part name="TP5" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="XCLR" />
        <part name="TP6" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="CAM_ENABLE" />
        <part name="TP7" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="HOST CLK RESERVED" />
        <part name="TP8" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="HOST RESET RESERVED" />
        <part name="TP9" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="CRADLE NTC RESERVED" />
        <part name="FRAME4" library="FRIDAY_SCH1_Support" deviceset="A3_FRAME" device="" value="" />
        <part name="MK1" library="INMP441" deviceset="INMP441" device="" value="INMP441" />
        <part name="C16" library="FRIDAY_SCH1_Support" deviceset="C_0402" device="" value="100nF 16V X7R" />
        <part name="MK2" library="INMP441" deviceset="INMP441" device="" value="INMP441" />
        <part name="C17" library="FRIDAY_SCH1_Support" deviceset="C_0402" device="" value="100nF 16V X7R" />
        <part name="R17" library="FRIDAY_SCH1_Support" deviceset="R_0402" device="" value="100k 1%" />
        <part name="TP10" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="MIC SD" />
      </parts>
      <sheets>
        <sheet>
          <plain>
            <text x="15.24" y="281.94" size="2.54" layer="94">FRIDAY / SCH-3 / CAMERA CONNECTORS AND CSI</text>
            <text x="15.24" y="274.32" size="1.78" layer="94">RP-008969-SD p.2 and FRIDAY interconnect | 2-lane D-PHY | DF37 hold</text>
            <text x="13.97" y="251.46" size="1.78" layer="94">J2 PCB view: pin 1 at negative X. Bottom contact; pin 1 mates to pin 1 at right board.</text>
            <text x="261.62" y="232.41" size="1.78" layer="94">J1 awaiting crosswalk. All 30 electrical contacts open.</text>
            <text x="14" y="109.22" size="1.78" layer="94">Place EMI filters near flex launch. Keep pair polarity and continuous return.</text>
            <text x="14" y="48.26" size="1.78" layer="94">Sensor-side choke nets end at L2-L4 until the tail orientation is proven.</text>
          </plain>
          <instances>
            <instance part="FRAME1" gate="G$1" x="0" y="0" smashed="yes" />
            <instance part="J2" gate="G$1" x="84.0" y="171.45" smashed="yes">
              <attribute name="NAME" x="78.92" y="207.56169999999997" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="78.92" y="135.82219999999998" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="J1" gate="G$1" x="323.85" y="174.0" smashed="yes">
              <attribute name="NAME" x="316.23" y="194.828" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="316.23" y="151.14" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="L2" gate="G$1" x="69.85" y="78.74" smashed="yes">
              <attribute name="NAME" x="52.06999999999999" y="85.08999999999999" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="52.06999999999999" y="71.11999999999999" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="L3" gate="G$1" x="205.74" y="78.74" smashed="yes">
              <attribute name="NAME" x="187.96" y="85.08999999999999" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="187.96" y="71.11999999999999" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="L4" gate="G$1" x="336.55" y="78.74" smashed="yes">
              <attribute name="NAME" x="318.77" y="85.08999999999999" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="318.77" y="71.11999999999999" size="1.27" layer="96" align="bottom-left" />
            </instance>
          </instances>
          <busses />
          <nets>
            <net name="GND" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="1" />
                <wire x1="73.84" y1="204.47" x2="56.06" y2="204.47" width="0.1524" layer="91" />
                <label x="56.06" y="204.47" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J2" gate="G$1" pin="4" />
                <wire x1="73.84" y1="196.85" x2="56.06" y2="196.85" width="0.1524" layer="91" />
                <label x="56.06" y="196.85" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J2" gate="G$1" pin="7" />
                <wire x1="73.84" y1="189.23" x2="56.06" y2="189.23" width="0.1524" layer="91" />
                <label x="56.06" y="189.23" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J2" gate="G$1" pin="10" />
                <wire x1="73.84" y1="181.61" x2="56.06" y2="181.61" width="0.1524" layer="91" />
                <label x="56.06" y="181.61" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J2" gate="G$1" pin="19" />
                <wire x1="73.84" y1="158.75" x2="56.06" y2="158.75" width="0.1524" layer="91" />
                <label x="56.06" y="158.75" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J2" gate="G$1" pin="21" />
                <wire x1="73.84" y1="153.67" x2="56.06" y2="153.67" width="0.1524" layer="91" />
                <label x="56.06" y="153.67" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CSI0_D0_N" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="2" />
                <wire x1="73.84" y1="201.93" x2="56.06" y2="201.93" width="0.1524" layer="91" />
                <label x="56.06" y="201.93" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="L2" gate="G$1" pin="FLEX_N" />
                <wire x1="46.99" y1="80.01" x2="29.21" y2="80.01" width="0.1524" layer="91" />
                <label x="29.21" y="80.01" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CSI0_D0_P" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="3" />
                <wire x1="73.84" y1="199.39" x2="56.06" y2="199.39" width="0.1524" layer="91" />
                <label x="56.06" y="199.39" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="L2" gate="G$1" pin="FLEX_P" />
                <wire x1="46.99" y1="77.47" x2="29.21" y2="77.47" width="0.1524" layer="91" />
                <label x="29.21" y="77.47" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CSI0_D1_N" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="5" />
                <wire x1="73.84" y1="194.31" x2="56.06" y2="194.31" width="0.1524" layer="91" />
                <label x="56.06" y="194.31" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="L3" gate="G$1" pin="FLEX_N" />
                <wire x1="182.88" y1="80.01" x2="165.10" y2="80.01" width="0.1524" layer="91" />
                <label x="165.10" y="80.01" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CSI0_D1_P" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="6" />
                <wire x1="73.84" y1="191.77" x2="56.06" y2="191.77" width="0.1524" layer="91" />
                <label x="56.06" y="191.77" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="L3" gate="G$1" pin="FLEX_P" />
                <wire x1="182.88" y1="77.47" x2="165.10" y2="77.47" width="0.1524" layer="91" />
                <label x="165.10" y="77.47" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CSI0_CLK_N" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="8" />
                <wire x1="73.84" y1="186.69" x2="56.06" y2="186.69" width="0.1524" layer="91" />
                <label x="56.06" y="186.69" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="L4" gate="G$1" pin="FLEX_N" />
                <wire x1="313.69" y1="80.01" x2="295.91" y2="80.01" width="0.1524" layer="91" />
                <label x="295.91" y="80.01" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CSI0_CLK_P" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="9" />
                <wire x1="73.84" y1="184.15" x2="56.06" y2="184.15" width="0.1524" layer="91" />
                <label x="56.06" y="184.15" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="L4" gate="G$1" pin="FLEX_P" />
                <wire x1="313.69" y1="77.47" x2="295.91" y2="77.47" width="0.1524" layer="91" />
                <label x="295.91" y="77.47" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="I2C_CAM_SCL" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="11" />
                <wire x1="73.84" y1="179.07" x2="56.06" y2="179.07" width="0.1524" layer="91" />
                <label x="56.06" y="179.07" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="I2C_CAM_SDA" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="12" />
                <wire x1="73.84" y1="176.53" x2="56.06" y2="176.53" width="0.1524" layer="91" />
                <label x="56.06" y="176.53" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_ENABLE" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="13" />
                <wire x1="73.84" y1="173.99" x2="56.06" y2="173.99" width="0.1524" layer="91" />
                <label x="56.06" y="173.99" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_RST_L_RESERVED" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="14" />
                <wire x1="73.84" y1="171.45" x2="56.06" y2="171.45" width="0.1524" layer="91" />
                <label x="56.06" y="171.45" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_MCLK_RESERVED" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="15" />
                <wire x1="73.84" y1="168.91" x2="56.06" y2="168.91" width="0.1524" layer="91" />
                <label x="56.06" y="168.91" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_CRADLE_NTC_RESERVED" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="16" />
                <wire x1="73.84" y1="166.37" x2="56.06" y2="166.37" width="0.1524" layer="91" />
                <label x="56.06" y="166.37" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="VCC_3V3_S3" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="17" />
                <wire x1="73.84" y1="163.83" x2="56.06" y2="163.83" width="0.1524" layer="91" />
                <label x="56.06" y="163.83" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J2" gate="G$1" pin="18" />
                <wire x1="73.84" y1="161.29" x2="56.06" y2="161.29" width="0.1524" layer="91" />
                <label x="56.06" y="161.29" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="VCC_1V8_S0" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="20" />
                <wire x1="73.84" y1="156.21" x2="56.06" y2="156.21" width="0.1524" layer="91" />
                <label x="56.06" y="156.21" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SAI1_BCLK_M0" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="22" />
                <wire x1="73.84" y1="151.13" x2="56.06" y2="151.13" width="0.1524" layer="91" />
                <label x="56.06" y="151.13" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SAI1_LRCK_M0" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="23" />
                <wire x1="73.84" y1="148.59" x2="56.06" y2="148.59" width="0.1524" layer="91" />
                <label x="56.06" y="148.59" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SAI1_SDI0_M0" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="24" />
                <wire x1="73.84" y1="146.05" x2="56.06" y2="146.05" width="0.1524" layer="91" />
                <label x="56.06" y="146.05" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CSI0_D0_N_SENSOR" class="0">
              <segment>
                <pinref part="L2" gate="G$1" pin="SENSOR_N" />
                <wire x1="92.71" y1="80.01" x2="97.79" y2="80.01" width="0.1524" layer="91" />
                <label x="97.79" y="80.01" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CSI0_D0_P_SENSOR" class="0">
              <segment>
                <pinref part="L2" gate="G$1" pin="SENSOR_P" />
                <wire x1="92.71" y1="77.47" x2="97.79" y2="77.47" width="0.1524" layer="91" />
                <label x="97.79" y="77.47" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CSI0_D1_N_SENSOR" class="0">
              <segment>
                <pinref part="L3" gate="G$1" pin="SENSOR_N" />
                <wire x1="228.60" y1="80.01" x2="233.68" y2="80.01" width="0.1524" layer="91" />
                <label x="233.68" y="80.01" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CSI0_D1_P_SENSOR" class="0">
              <segment>
                <pinref part="L3" gate="G$1" pin="SENSOR_P" />
                <wire x1="228.60" y1="77.47" x2="233.68" y2="77.47" width="0.1524" layer="91" />
                <label x="233.68" y="77.47" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CSI0_CLK_N_SENSOR" class="0">
              <segment>
                <pinref part="L4" gate="G$1" pin="SENSOR_N" />
                <wire x1="359.41" y1="80.01" x2="364.49" y2="80.01" width="0.1524" layer="91" />
                <label x="364.49" y="80.01" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CSI0_CLK_P_SENSOR" class="0">
              <segment>
                <pinref part="L4" gate="G$1" pin="SENSOR_P" />
                <wire x1="359.41" y1="77.47" x2="364.49" y2="77.47" width="0.1524" layer="91" />
                <label x="364.49" y="77.47" size="1.016" layer="95" />
              </segment>
            </net>
          </nets>
        </sheet>
        <sheet>
          <plain>
            <text x="15.24" y="281.94" size="2.54" layer="94">FRIDAY / SCH-3 / CAMERA POWER</text>
            <text x="15.24" y="274.32" size="1.78" layer="94">Common CAM_ENABLE sequencing per RP-008969-SD p.2 | Local camera DOVDD</text>
            <text x="15.24" y="151.13" size="1.78" layer="94">U2 2.8 V supplies AVDD and AFVDD, as on the Pi carrier. J1 is electrically parked.</text>
            <text x="15.24" y="33.02" size="1.78" layer="94">Input budget and load transient screen are in SCH-3_crossref.md.</text>
          </plain>
          <instances>
            <instance part="FRAME2" gate="G$1" x="0" y="0" smashed="yes" />
            <instance part="U1" gate="G$1" x="76.2" y="209.55" smashed="yes">
              <attribute name="NAME" x="58.42" y="217.17000000000002" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="58.42" y="200.66000000000003" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="L1" gate="G$1" x="172.72" y="218.44" smashed="yes">
              <attribute name="NAME" x="170.18" y="220.98" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="170.18" y="214.63" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="U2" gate="G$1" x="245.11" y="120.65" smashed="yes">
              <attribute name="NAME" x="227.33" y="128.27" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="227.33" y="111.76" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="U3" gate="G$1" x="245.11" y="70.0" smashed="yes">
              <attribute name="NAME" x="227.33" y="77.62" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="227.33" y="61.11" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="U4" gate="G$1" x="75.0" y="78.74" smashed="yes">
              <attribute name="NAME" x="57.22" y="86.36" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="57.22" y="69.85" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R1" gate="G$1" x="171.45" y="188.0" smashed="yes">
              <attribute name="NAME" x="168.91" y="189.4" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="168.91" y="185.2" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R2" gate="G$1" x="171.45" y="162.56" smashed="yes">
              <attribute name="NAME" x="168.91" y="163.96" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="168.91" y="159.76" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R3" gate="G$1" x="55.88" y="53.34" smashed="yes">
              <attribute name="NAME" x="53.34" y="54.74" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="53.34" y="50.540000000000006" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R4" gate="G$1" x="129.54" y="53.34" smashed="yes">
              <attribute name="NAME" x="126.99999999999999" y="54.74" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="126.99999999999999" y="50.540000000000006" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C1" gate="G$1" x="57.15" y="246.38" smashed="yes">
              <attribute name="NAME" x="54.61" y="248.92" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="54.61" y="242.57" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C2" gate="G$1" x="259.08" y="220.98" smashed="yes">
              <attribute name="NAME" x="256.53999999999996" y="223.51999999999998" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="256.53999999999996" y="217.17" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C3" gate="G$1" x="345.44" y="220.98" smashed="yes">
              <attribute name="NAME" x="342.9" y="223.51999999999998" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="342.9" y="217.17" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C4" gate="G$1" x="258.0" y="187.96" smashed="yes">
              <attribute name="NAME" x="255.46" y="190.16" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="255.46" y="184.36" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C5" gate="G$1" x="152.4" y="131.0" smashed="yes">
              <attribute name="NAME" x="149.86" y="133.2" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="149.86" y="127.4" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C6" gate="G$1" x="335.28" y="126.0" smashed="yes">
              <attribute name="NAME" x="332.73999999999995" y="128.2" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="332.73999999999995" y="122.4" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C7" gate="G$1" x="152.4" y="84.0" smashed="yes">
              <attribute name="NAME" x="149.86" y="86.2" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="149.86" y="80.4" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C8" gate="G$1" x="335.28" y="76.2" smashed="yes">
              <attribute name="NAME" x="332.73999999999995" y="78.4" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="332.73999999999995" y="72.60000000000001" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C9" gate="G$1" x="53.34" y="118.11" smashed="yes">
              <attribute name="NAME" x="50.800000000000004" y="120.31" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="50.800000000000004" y="114.51" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C10" gate="G$1" x="345.44" y="171.45" smashed="yes">
              <attribute name="NAME" x="342.9" y="173.64999999999998" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="342.9" y="167.85" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C11" gate="G$1" x="345.44" y="104.0" smashed="yes">
              <attribute name="NAME" x="342.9" y="106.2" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="342.9" y="100.4" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C12" gate="G$1" x="345.44" y="95.25" smashed="yes">
              <attribute name="NAME" x="342.9" y="97.45" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="342.9" y="91.65" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C13" gate="G$1" x="345.44" y="55.88" smashed="yes">
              <attribute name="NAME" x="342.9" y="58.080000000000005" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="342.9" y="52.28" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP1" gate="G$1" x="207.01" y="35.56" smashed="yes">
              <attribute name="NAME" x="205.73999999999998" y="37.338" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="205.73999999999998" y="32.766000000000005" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP2" gate="G$1" x="260.35" y="35.56" smashed="yes">
              <attribute name="NAME" x="259.08000000000004" y="37.338" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="259.08000000000004" y="32.766000000000005" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP3" gate="G$1" x="325.12" y="35.56" smashed="yes">
              <attribute name="NAME" x="323.85" y="37.338" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="323.85" y="32.766000000000005" size="1.27" layer="96" align="bottom-left" />
            </instance>
          </instances>
          <busses />
          <nets>
            <net name="VCC_3V3_S3" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="VIN" />
                <wire x1="53.34" y1="212.09" x2="35.56" y2="212.09" width="0.1524" layer="91" />
                <label x="35.56" y="212.09" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U2" gate="G$1" pin="IN" />
                <wire x1="222.25" y1="123.19" x2="204.47" y2="123.19" width="0.1524" layer="91" />
                <label x="204.47" y="123.19" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U3" gate="G$1" pin="IN" />
                <wire x1="222.25" y1="72.54" x2="204.47" y2="72.54" width="0.1524" layer="91" />
                <label x="204.47" y="72.54" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U4" gate="G$1" pin="VCC" />
                <wire x1="52.14" y1="78.74" x2="34.36" y2="78.74" width="0.1524" layer="91" />
                <label x="34.36" y="78.74" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C1" gate="G$1" pin="1" />
                <wire x1="52.07" y1="246.38" x2="34.29" y2="246.38" width="0.1524" layer="91" />
                <label x="34.29" y="246.38" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C5" gate="G$1" pin="1" />
                <wire x1="147.32" y1="131.00" x2="129.54" y2="131.00" width="0.1524" layer="91" />
                <label x="129.54" y="131.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C7" gate="G$1" pin="1" />
                <wire x1="147.32" y1="84.00" x2="129.54" y2="84.00" width="0.1524" layer="91" />
                <label x="129.54" y="84.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C9" gate="G$1" pin="1" />
                <wire x1="48.26" y1="118.11" x2="30.48" y2="118.11" width="0.1524" layer="91" />
                <label x="30.48" y="118.11" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_ENABLE_3V3" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="EN" />
                <wire x1="53.34" y1="209.55" x2="35.56" y2="209.55" width="0.1524" layer="91" />
                <label x="35.56" y="209.55" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U2" gate="G$1" pin="EN" />
                <wire x1="222.25" y1="120.65" x2="204.47" y2="120.65" width="0.1524" layer="91" />
                <label x="204.47" y="120.65" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U3" gate="G$1" pin="EN" />
                <wire x1="222.25" y1="70.00" x2="204.47" y2="70.00" width="0.1524" layer="91" />
                <label x="204.47" y="70.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U4" gate="G$1" pin="Y" />
                <wire x1="97.86" y1="80.01" x2="102.94" y2="80.01" width="0.1524" layer="91" />
                <label x="102.94" y="80.01" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R4" gate="G$1" pin="1" />
                <wire x1="124.46" y1="53.34" x2="106.68" y2="53.34" width="0.1524" layer="91" />
                <label x="106.68" y="53.34" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="GND" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="GND" />
                <wire x1="53.34" y1="207.01" x2="35.56" y2="207.01" width="0.1524" layer="91" />
                <label x="35.56" y="207.01" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U2" gate="G$1" pin="GND" />
                <wire x1="222.25" y1="118.11" x2="204.47" y2="118.11" width="0.1524" layer="91" />
                <label x="204.47" y="118.11" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U3" gate="G$1" pin="GND" />
                <wire x1="222.25" y1="67.46" x2="204.47" y2="67.46" width="0.1524" layer="91" />
                <label x="204.47" y="67.46" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U4" gate="G$1" pin="GND" />
                <wire x1="52.14" y1="76.20" x2="34.36" y2="76.20" width="0.1524" layer="91" />
                <label x="34.36" y="76.20" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R2" gate="G$1" pin="2" />
                <wire x1="176.53" y1="162.56" x2="181.61" y2="162.56" width="0.1524" layer="91" />
                <label x="181.61" y="162.56" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R3" gate="G$1" pin="2" />
                <wire x1="60.96" y1="53.34" x2="66.04" y2="53.34" width="0.1524" layer="91" />
                <label x="66.04" y="53.34" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R4" gate="G$1" pin="2" />
                <wire x1="134.62" y1="53.34" x2="139.70" y2="53.34" width="0.1524" layer="91" />
                <label x="139.70" y="53.34" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C1" gate="G$1" pin="2" />
                <wire x1="62.23" y1="246.38" x2="67.31" y2="246.38" width="0.1524" layer="91" />
                <label x="67.31" y="246.38" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C2" gate="G$1" pin="2" />
                <wire x1="264.16" y1="220.98" x2="269.24" y2="220.98" width="0.1524" layer="91" />
                <label x="269.24" y="220.98" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C3" gate="G$1" pin="2" />
                <wire x1="350.52" y1="220.98" x2="355.60" y2="220.98" width="0.1524" layer="91" />
                <label x="355.60" y="220.98" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C5" gate="G$1" pin="2" />
                <wire x1="157.48" y1="131.00" x2="162.56" y2="131.00" width="0.1524" layer="91" />
                <label x="162.56" y="131.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C6" gate="G$1" pin="2" />
                <wire x1="340.36" y1="126.00" x2="345.44" y2="126.00" width="0.1524" layer="91" />
                <label x="345.44" y="126.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C7" gate="G$1" pin="2" />
                <wire x1="157.48" y1="84.00" x2="162.56" y2="84.00" width="0.1524" layer="91" />
                <label x="162.56" y="84.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C8" gate="G$1" pin="2" />
                <wire x1="340.36" y1="76.20" x2="345.44" y2="76.20" width="0.1524" layer="91" />
                <label x="345.44" y="76.20" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C9" gate="G$1" pin="2" />
                <wire x1="58.42" y1="118.11" x2="63.50" y2="118.11" width="0.1524" layer="91" />
                <label x="63.50" y="118.11" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C10" gate="G$1" pin="2" />
                <wire x1="350.52" y1="171.45" x2="355.60" y2="171.45" width="0.1524" layer="91" />
                <label x="355.60" y="171.45" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C11" gate="G$1" pin="2" />
                <wire x1="350.52" y1="104.00" x2="355.60" y2="104.00" width="0.1524" layer="91" />
                <label x="355.60" y="104.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C12" gate="G$1" pin="2" />
                <wire x1="350.52" y1="95.25" x2="355.60" y2="95.25" width="0.1524" layer="91" />
                <label x="355.60" y="95.25" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C13" gate="G$1" pin="2" />
                <wire x1="350.52" y1="55.88" x2="355.60" y2="55.88" width="0.1524" layer="91" />
                <label x="355.60" y="55.88" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_DVDD_SW" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="LX" />
                <wire x1="99.06" y1="210.82" x2="104.14" y2="210.82" width="0.1524" layer="91" />
                <label x="104.14" y="210.82" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="L1" gate="G$1" pin="1" />
                <wire x1="167.64" y1="218.44" x2="149.86" y2="218.44" width="0.1524" layer="91" />
                <label x="149.86" y="218.44" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_DVDD_FB" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="FB" />
                <wire x1="99.06" y1="208.28" x2="104.14" y2="208.28" width="0.1524" layer="91" />
                <label x="104.14" y="208.28" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R1" gate="G$1" pin="2" />
                <wire x1="176.53" y1="188.00" x2="181.61" y2="188.00" width="0.1524" layer="91" />
                <label x="181.61" y="188.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R2" gate="G$1" pin="1" />
                <wire x1="166.37" y1="162.56" x2="148.59" y2="162.56" width="0.1524" layer="91" />
                <label x="148.59" y="162.56" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C4" gate="G$1" pin="2" />
                <wire x1="263.08" y1="187.96" x2="268.16" y2="187.96" width="0.1524" layer="91" />
                <label x="268.16" y="187.96" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_DVDD_1V1" class="0">
              <segment>
                <pinref part="L1" gate="G$1" pin="2" />
                <wire x1="177.80" y1="218.44" x2="182.88" y2="218.44" width="0.1524" layer="91" />
                <label x="182.88" y="218.44" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R1" gate="G$1" pin="1" />
                <wire x1="166.37" y1="188.00" x2="148.59" y2="188.00" width="0.1524" layer="91" />
                <label x="148.59" y="188.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C2" gate="G$1" pin="1" />
                <wire x1="254.00" y1="220.98" x2="236.22" y2="220.98" width="0.1524" layer="91" />
                <label x="236.22" y="220.98" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C3" gate="G$1" pin="1" />
                <wire x1="340.36" y1="220.98" x2="322.58" y2="220.98" width="0.1524" layer="91" />
                <label x="322.58" y="220.98" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C4" gate="G$1" pin="1" />
                <wire x1="252.92" y1="187.96" x2="235.14" y2="187.96" width="0.1524" layer="91" />
                <label x="235.14" y="187.96" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C10" gate="G$1" pin="1" />
                <wire x1="340.36" y1="171.45" x2="322.58" y2="171.45" width="0.1524" layer="91" />
                <label x="322.58" y="171.45" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP1" gate="G$1" pin="1" />
                <wire x1="201.93" y1="35.56" x2="184.15" y2="35.56" width="0.1524" layer="91" />
                <label x="184.15" y="35.56" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_AVDD_AFVDD_2V8" class="0">
              <segment>
                <pinref part="U2" gate="G$1" pin="OUT" />
                <wire x1="267.97" y1="121.92" x2="273.05" y2="121.92" width="0.1524" layer="91" />
                <label x="273.05" y="121.92" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C6" gate="G$1" pin="1" />
                <wire x1="330.20" y1="126.00" x2="312.42" y2="126.00" width="0.1524" layer="91" />
                <label x="312.42" y="126.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C11" gate="G$1" pin="1" />
                <wire x1="340.36" y1="104.00" x2="322.58" y2="104.00" width="0.1524" layer="91" />
                <label x="322.58" y="104.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C12" gate="G$1" pin="1" />
                <wire x1="340.36" y1="95.25" x2="322.58" y2="95.25" width="0.1524" layer="91" />
                <label x="322.58" y="95.25" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP2" gate="G$1" pin="1" />
                <wire x1="255.27" y1="35.56" x2="237.49" y2="35.56" width="0.1524" layer="91" />
                <label x="237.49" y="35.56" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_DOVDD_1V8" class="0">
              <segment>
                <pinref part="U3" gate="G$1" pin="OUT" />
                <wire x1="267.97" y1="71.27" x2="273.05" y2="71.27" width="0.1524" layer="91" />
                <label x="273.05" y="71.27" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C8" gate="G$1" pin="1" />
                <wire x1="330.20" y1="76.20" x2="312.42" y2="76.20" width="0.1524" layer="91" />
                <label x="312.42" y="76.20" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C13" gate="G$1" pin="1" />
                <wire x1="340.36" y1="55.88" x2="322.58" y2="55.88" width="0.1524" layer="91" />
                <label x="322.58" y="55.88" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP3" gate="G$1" pin="1" />
                <wire x1="320.04" y1="35.56" x2="302.26" y2="35.56" width="0.1524" layer="91" />
                <label x="302.26" y="35.56" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_ENABLE" class="0">
              <segment>
                <pinref part="U4" gate="G$1" pin="A" />
                <wire x1="52.14" y1="81.28" x2="34.36" y2="81.28" width="0.1524" layer="91" />
                <label x="34.36" y="81.28" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R3" gate="G$1" pin="1" />
                <wire x1="50.80" y1="53.34" x2="33.02" y2="53.34" width="0.1524" layer="91" />
                <label x="33.02" y="53.34" size="1.016" layer="95" />
              </segment>
            </net>
          </nets>
        </sheet>
        <sheet>
          <plain>
            <text x="15.24" y="281.94" size="2.54" layer="94">FRIDAY / SCH-3 / MCLK, RESET AND CAMERA CONTROL</text>
            <text x="15.24" y="274.32" size="1.78" layer="94">Local 24 MHz MCLK | Supervisor holds XCLR until all camera rails qualify</text>
            <text x="15.24" y="189.23" size="1.78" layer="94">U5 CT1-CT3 open select 14 ms minimum. Clock startup is 5 ms maximum at rated VDD.</text>
            <text x="15.24" y="32.0" size="1.78" layer="94">Host clock option requires removing R5 and revalidating reset timing. Host reset must be open drain.</text>
          </plain>
          <instances>
            <instance part="FRAME3" gate="G$1" x="0" y="0" smashed="yes" />
            <instance part="X1" gate="G$1" x="68.0" y="220.98" smashed="yes">
              <attribute name="NAME" x="50.22" y="228.6" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="50.22" y="212.08999999999997" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R5" gate="G$1" x="172.72" y="220.98" smashed="yes">
              <attribute name="NAME" x="170.18" y="222.38" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="170.18" y="218.17999999999998" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C14" gate="G$1" x="68" y="248.92" smashed="yes">
              <attribute name="NAME" x="65.46" y="251.11999999999998" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="65.46" y="245.32" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="U5" gate="G$1" x="210.82" y="133.35" smashed="yes">
              <attribute name="NAME" x="193.04" y="151.13" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="193.04" y="114.3" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C15" gate="G$1" x="277.0" y="174.0" smashed="yes">
              <attribute name="NAME" x="274.46" y="176.2" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="274.46" y="170.4" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R6" gate="G$1" x="51.0" y="154.94" smashed="yes">
              <attribute name="NAME" x="48.46" y="156.34" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="48.46" y="152.14" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R7" gate="G$1" x="117.0" y="154.94" smashed="yes">
              <attribute name="NAME" x="114.46" y="156.34" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="114.46" y="152.14" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R8" gate="G$1" x="51.0" y="125.73" smashed="yes">
              <attribute name="NAME" x="48.46" y="127.13000000000001" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="48.46" y="122.93" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R9" gate="G$1" x="117.0" y="125.73" smashed="yes">
              <attribute name="NAME" x="114.46" y="127.13000000000001" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="114.46" y="122.93" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R10" gate="G$1" x="51.0" y="96.52" smashed="yes">
              <attribute name="NAME" x="48.46" y="97.92" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="48.46" y="93.72" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R11" gate="G$1" x="117.0" y="96.52" smashed="yes">
              <attribute name="NAME" x="114.46" y="97.92" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="114.46" y="93.72" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R12" gate="G$1" x="320" y="135.89" smashed="yes">
              <attribute name="NAME" x="317.46" y="137.29" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="317.46" y="133.08999999999997" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R13" gate="G$1" x="320" y="218.44" smashed="yes">
              <attribute name="NAME" x="317.46" y="219.84" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="317.46" y="215.64" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R14" gate="G$1" x="320" y="110.49" smashed="yes">
              <attribute name="NAME" x="317.46" y="111.89" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="317.46" y="107.69" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R15" gate="G$1" x="94" y="56.0" smashed="yes">
              <attribute name="NAME" x="91.46" y="57.4" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="91.46" y="53.2" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R16" gate="G$1" x="175" y="56.0" smashed="yes">
              <attribute name="NAME" x="172.46" y="57.4" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="172.46" y="53.2" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP4" gate="G$1" x="227" y="246.38" smashed="yes">
              <attribute name="NAME" x="225.73" y="248.158" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="225.73" y="243.58599999999998" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP5" gate="G$1" x="291" y="76.2" smashed="yes">
              <attribute name="NAME" x="289.73" y="77.97800000000001" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="289.73" y="73.406" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP6" gate="G$1" x="365.76" y="76.2" smashed="yes">
              <attribute name="NAME" x="364.49" y="77.97800000000001" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="364.49" y="73.406" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP7" gate="G$1" x="336.55" y="246.38" smashed="yes">
              <attribute name="NAME" x="335.28000000000003" y="248.158" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="335.28000000000003" y="243.58599999999998" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP8" gate="G$1" x="265" y="49.5" smashed="yes">
              <attribute name="NAME" x="263.73" y="51.278" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="263.73" y="46.706" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP9" gate="G$1" x="349" y="49.5" smashed="yes">
              <attribute name="NAME" x="347.73" y="51.278" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="347.73" y="46.706" size="1.27" layer="96" align="bottom-left" />
            </instance>
          </instances>
          <busses />
          <nets>
            <net name="CAM_DOVDD_1V8" class="0">
              <segment>
                <pinref part="X1" gate="G$1" pin="VDD" />
                <wire x1="45.14" y1="223.52" x2="27.36" y2="223.52" width="0.1524" layer="91" />
                <label x="27.36" y="223.52" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="X1" gate="G$1" pin="OE" />
                <wire x1="45.14" y1="220.98" x2="27.36" y2="220.98" width="0.1524" layer="91" />
                <label x="27.36" y="220.98" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C14" gate="G$1" pin="1" />
                <wire x1="62.92" y1="248.92" x2="45.14" y2="248.92" width="0.1524" layer="91" />
                <label x="45.14" y="248.92" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R8" gate="G$1" pin="1" />
                <wire x1="45.92" y1="125.73" x2="28.14" y2="125.73" width="0.1524" layer="91" />
                <label x="28.14" y="125.73" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R12" gate="G$1" pin="1" />
                <wire x1="314.92" y1="135.89" x2="297.14" y2="135.89" width="0.1524" layer="91" />
                <label x="297.14" y="135.89" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R15" gate="G$1" pin="1" />
                <wire x1="88.92" y1="56.00" x2="71.14" y2="56.00" width="0.1524" layer="91" />
                <label x="71.14" y="56.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R16" gate="G$1" pin="1" />
                <wire x1="169.92" y1="56.00" x2="152.14" y2="56.00" width="0.1524" layer="91" />
                <label x="152.14" y="56.00" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="GND" class="0">
              <segment>
                <pinref part="X1" gate="G$1" pin="GND" />
                <wire x1="45.14" y1="218.44" x2="27.36" y2="218.44" width="0.1524" layer="91" />
                <label x="27.36" y="218.44" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C14" gate="G$1" pin="2" />
                <wire x1="73.08" y1="248.92" x2="78.16" y2="248.92" width="0.1524" layer="91" />
                <label x="78.16" y="248.92" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U5" gate="G$1" pin="SENSE4L" />
                <wire x1="187.96" y1="132.08" x2="170.18" y2="132.08" width="0.1524" layer="91" />
                <label x="170.18" y="132.08" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U5" gate="G$1" pin="SENSE4H" />
                <wire x1="187.96" y1="129.54" x2="170.18" y2="129.54" width="0.1524" layer="91" />
                <label x="170.18" y="129.54" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U5" gate="G$1" pin="WDI" />
                <wire x1="233.68" y1="125.73" x2="238.76" y2="125.73" width="0.1524" layer="91" />
                <label x="238.76" y="125.73" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U5" gate="G$1" pin="NC11" />
                <wire x1="187.96" y1="124.46" x2="170.18" y2="124.46" width="0.1524" layer="91" />
                <label x="170.18" y="124.46" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U5" gate="G$1" pin="GND" />
                <wire x1="187.96" y1="127.00" x2="170.18" y2="127.00" width="0.1524" layer="91" />
                <label x="170.18" y="127.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U5" gate="G$1" pin="EP" />
                <wire x1="187.96" y1="121.92" x2="170.18" y2="121.92" width="0.1524" layer="91" />
                <label x="170.18" y="121.92" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C15" gate="G$1" pin="2" />
                <wire x1="282.08" y1="174.00" x2="287.16" y2="174.00" width="0.1524" layer="91" />
                <label x="287.16" y="174.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R7" gate="G$1" pin="2" />
                <wire x1="122.08" y1="154.94" x2="127.16" y2="154.94" width="0.1524" layer="91" />
                <label x="127.16" y="154.94" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R9" gate="G$1" pin="2" />
                <wire x1="122.08" y1="125.73" x2="127.16" y2="125.73" width="0.1524" layer="91" />
                <label x="127.16" y="125.73" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R11" gate="G$1" pin="2" />
                <wire x1="122.08" y1="96.52" x2="127.16" y2="96.52" width="0.1524" layer="91" />
                <label x="127.16" y="96.52" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_MCLK_XO" class="0">
              <segment>
                <pinref part="X1" gate="G$1" pin="CLK" />
                <wire x1="90.86" y1="220.98" x2="95.94" y2="220.98" width="0.1524" layer="91" />
                <label x="95.94" y="220.98" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R5" gate="G$1" pin="1" />
                <wire x1="167.64" y1="220.98" x2="149.86" y2="220.98" width="0.1524" layer="91" />
                <label x="149.86" y="220.98" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="MCLK" class="0">
              <segment>
                <pinref part="R5" gate="G$1" pin="2" />
                <wire x1="177.80" y1="220.98" x2="182.88" y2="220.98" width="0.1524" layer="91" />
                <label x="182.88" y="220.98" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R13" gate="G$1" pin="2" />
                <wire x1="325.08" y1="218.44" x2="330.16" y2="218.44" width="0.1524" layer="91" />
                <label x="330.16" y="218.44" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP4" gate="G$1" pin="1" />
                <wire x1="221.92" y1="246.38" x2="204.14" y2="246.38" width="0.1524" layer="91" />
                <label x="204.14" y="246.38" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="VCC_3V3_S3" class="0">
              <segment>
                <pinref part="U5" gate="G$1" pin="VDD" />
                <wire x1="187.96" y1="144.78" x2="170.18" y2="144.78" width="0.1524" layer="91" />
                <label x="170.18" y="144.78" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C15" gate="G$1" pin="1" />
                <wire x1="271.92" y1="174.00" x2="254.14" y2="174.00" width="0.1524" layer="91" />
                <label x="254.14" y="174.00" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_ENABLE_3V3" class="0">
              <segment>
                <pinref part="U5" gate="G$1" pin="MR" />
                <wire x1="187.96" y1="142.24" x2="170.18" y2="142.24" width="0.1524" layer="91" />
                <label x="170.18" y="142.24" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="POR_SENSE_DVDD" class="0">
              <segment>
                <pinref part="U5" gate="G$1" pin="SENSE1" />
                <wire x1="187.96" y1="139.70" x2="170.18" y2="139.70" width="0.1524" layer="91" />
                <label x="170.18" y="139.70" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R6" gate="G$1" pin="2" />
                <wire x1="56.08" y1="154.94" x2="61.16" y2="154.94" width="0.1524" layer="91" />
                <label x="61.16" y="154.94" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R7" gate="G$1" pin="1" />
                <wire x1="111.92" y1="154.94" x2="94.14" y2="154.94" width="0.1524" layer="91" />
                <label x="94.14" y="154.94" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="POR_SENSE_DOVDD" class="0">
              <segment>
                <pinref part="U5" gate="G$1" pin="SENSE2" />
                <wire x1="187.96" y1="137.16" x2="170.18" y2="137.16" width="0.1524" layer="91" />
                <label x="170.18" y="137.16" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R8" gate="G$1" pin="2" />
                <wire x1="56.08" y1="125.73" x2="61.16" y2="125.73" width="0.1524" layer="91" />
                <label x="61.16" y="125.73" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R9" gate="G$1" pin="1" />
                <wire x1="111.92" y1="125.73" x2="94.14" y2="125.73" width="0.1524" layer="91" />
                <label x="94.14" y="125.73" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="POR_SENSE_AVDD" class="0">
              <segment>
                <pinref part="U5" gate="G$1" pin="SENSE3" />
                <wire x1="187.96" y1="134.62" x2="170.18" y2="134.62" width="0.1524" layer="91" />
                <label x="170.18" y="134.62" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R10" gate="G$1" pin="2" />
                <wire x1="56.08" y1="96.52" x2="61.16" y2="96.52" width="0.1524" layer="91" />
                <label x="61.16" y="96.52" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R11" gate="G$1" pin="1" />
                <wire x1="111.92" y1="96.52" x2="94.14" y2="96.52" width="0.1524" layer="91" />
                <label x="94.14" y="96.52" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="XCLR" class="0">
              <segment>
                <pinref part="U5" gate="G$1" pin="RESET1" />
                <wire x1="233.68" y1="146.05" x2="238.76" y2="146.05" width="0.1524" layer="91" />
                <label x="238.76" y="146.05" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U5" gate="G$1" pin="RESET2" />
                <wire x1="233.68" y1="143.51" x2="238.76" y2="143.51" width="0.1524" layer="91" />
                <label x="238.76" y="143.51" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U5" gate="G$1" pin="RESET3" />
                <wire x1="233.68" y1="140.97" x2="238.76" y2="140.97" width="0.1524" layer="91" />
                <label x="238.76" y="140.97" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R12" gate="G$1" pin="2" />
                <wire x1="325.08" y1="135.89" x2="330.16" y2="135.89" width="0.1524" layer="91" />
                <label x="330.16" y="135.89" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R14" gate="G$1" pin="2" />
                <wire x1="325.08" y1="110.49" x2="330.16" y2="110.49" width="0.1524" layer="91" />
                <label x="330.16" y="110.49" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP5" gate="G$1" pin="1" />
                <wire x1="285.92" y1="76.20" x2="268.14" y2="76.20" width="0.1524" layer="91" />
                <label x="268.14" y="76.20" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_DVDD_1V1" class="0">
              <segment>
                <pinref part="R6" gate="G$1" pin="1" />
                <wire x1="45.92" y1="154.94" x2="28.14" y2="154.94" width="0.1524" layer="91" />
                <label x="28.14" y="154.94" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_AVDD_AFVDD_2V8" class="0">
              <segment>
                <pinref part="R10" gate="G$1" pin="1" />
                <wire x1="45.92" y1="96.52" x2="28.14" y2="96.52" width="0.1524" layer="91" />
                <label x="28.14" y="96.52" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_MCLK_RESERVED" class="0">
              <segment>
                <pinref part="R13" gate="G$1" pin="1" />
                <wire x1="314.92" y1="218.44" x2="297.14" y2="218.44" width="0.1524" layer="91" />
                <label x="297.14" y="218.44" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP7" gate="G$1" pin="1" />
                <wire x1="331.47" y1="246.38" x2="313.69" y2="246.38" width="0.1524" layer="91" />
                <label x="313.69" y="246.38" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_RST_L_RESERVED" class="0">
              <segment>
                <pinref part="R14" gate="G$1" pin="1" />
                <wire x1="314.92" y1="110.49" x2="297.14" y2="110.49" width="0.1524" layer="91" />
                <label x="297.14" y="110.49" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP8" gate="G$1" pin="1" />
                <wire x1="259.92" y1="49.50" x2="242.14" y2="49.50" width="0.1524" layer="91" />
                <label x="242.14" y="49.50" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="I2C_CAM_SCL" class="0">
              <segment>
                <pinref part="R15" gate="G$1" pin="2" />
                <wire x1="99.08" y1="56.00" x2="104.16" y2="56.00" width="0.1524" layer="91" />
                <label x="104.16" y="56.00" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="I2C_CAM_SDA" class="0">
              <segment>
                <pinref part="R16" gate="G$1" pin="2" />
                <wire x1="180.08" y1="56.00" x2="185.16" y2="56.00" width="0.1524" layer="91" />
                <label x="185.16" y="56.00" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_ENABLE" class="0">
              <segment>
                <pinref part="TP6" gate="G$1" pin="1" />
                <wire x1="360.68" y1="76.20" x2="342.90" y2="76.20" width="0.1524" layer="91" />
                <label x="342.90" y="76.20" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CAM_CRADLE_NTC_RESERVED" class="0">
              <segment>
                <pinref part="TP9" gate="G$1" pin="1" />
                <wire x1="343.92" y1="49.50" x2="326.14" y2="49.50" width="0.1524" layer="91" />
                <label x="326.14" y="49.50" size="1.016" layer="95" />
              </segment>
            </net>
          </nets>
        </sheet>
        <sheet>
          <plain>
            <text x="15.24" y="281.94" size="2.54" layer="94">FRIDAY / SCH-3 / STEREO DIGITAL MICROPHONES</text>
            <text x="15.24" y="274.32" size="1.78" layer="94">Y3 | 1.8 V host I/O and microphone supplies | Common I2S data</text>
            <text x="15.24" y="246.38" size="1.78" layer="94">MK1 strap low = left. MK2 strap high = right. Host uses 64 BCLK periods per stereo frame.</text>
            <text x="15.24" y="82.55" size="1.78" layer="94">Bottom acoustic ports: align board and enclosure holes. Keep solder paste, adhesive and debris clear.</text>
            <text x="15.24" y="74.93" size="1.78" layer="94">Host BCLK and LRCK must remain idle while the common 1.8 V S0 domain is off.</text>
          </plain>
          <instances>
            <instance part="FRAME4" gate="G$1" x="0" y="0" smashed="yes" />
            <instance part="MK1" gate="G$1" x="101.6" y="192.0" smashed="yes">
              <attribute name="NAME" x="88.89999999999999" y="202.795" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="88.89999999999999" y="179.3" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C16" gate="G$1" x="101.6" y="152.4" smashed="yes">
              <attribute name="NAME" x="99.05999999999999" y="154.6" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="99.05999999999999" y="148.8" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="MK2" gate="G$1" x="280.67" y="192.0" smashed="yes">
              <attribute name="NAME" x="267.97" y="202.795" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="267.97" y="179.3" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C17" gate="G$1" x="280.67" y="152.4" smashed="yes">
              <attribute name="NAME" x="278.13" y="154.6" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="278.13" y="148.8" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R17" gate="G$1" x="101.6" y="112.0" smashed="yes">
              <attribute name="NAME" x="99.05999999999999" y="113.4" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="99.05999999999999" y="109.2" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP10" gate="G$1" x="224.79" y="112.0" smashed="yes">
              <attribute name="NAME" x="223.51999999999998" y="113.778" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="223.51999999999998" y="109.206" size="1.27" layer="96" align="bottom-left" />
            </instance>
          </instances>
          <busses />
          <nets>
            <net name="SAI1_BCLK_M0" class="0">
              <segment>
                <pinref part="MK1" gate="G$1" pin="SCK" />
                <wire x1="119.38" y1="194.54" x2="124.46" y2="194.54" width="0.1524" layer="91" />
                <label x="124.46" y="194.54" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="MK2" gate="G$1" pin="SCK" />
                <wire x1="298.45" y1="194.54" x2="303.53" y2="194.54" width="0.1524" layer="91" />
                <label x="303.53" y="194.54" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SAI1_LRCK_M0" class="0">
              <segment>
                <pinref part="MK1" gate="G$1" pin="WS" />
                <wire x1="119.38" y1="192.00" x2="124.46" y2="192.00" width="0.1524" layer="91" />
                <label x="124.46" y="192.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="MK2" gate="G$1" pin="WS" />
                <wire x1="298.45" y1="192.00" x2="303.53" y2="192.00" width="0.1524" layer="91" />
                <label x="303.53" y="192.00" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SAI1_SDI0_M0" class="0">
              <segment>
                <pinref part="MK1" gate="G$1" pin="SD" />
                <wire x1="119.38" y1="189.46" x2="124.46" y2="189.46" width="0.1524" layer="91" />
                <label x="124.46" y="189.46" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="MK2" gate="G$1" pin="SD" />
                <wire x1="298.45" y1="189.46" x2="303.53" y2="189.46" width="0.1524" layer="91" />
                <label x="303.53" y="189.46" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R17" gate="G$1" pin="1" />
                <wire x1="96.52" y1="112.00" x2="78.74" y2="112.00" width="0.1524" layer="91" />
                <label x="78.74" y="112.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP10" gate="G$1" pin="1" />
                <wire x1="219.71" y1="112.00" x2="201.93" y2="112.00" width="0.1524" layer="91" />
                <label x="201.93" y="112.00" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="VCC_1V8_S0" class="0">
              <segment>
                <pinref part="MK1" gate="G$1" pin="VDD" />
                <wire x1="119.38" y1="199.62" x2="124.46" y2="199.62" width="0.1524" layer="91" />
                <label x="124.46" y="199.62" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="MK1" gate="G$1" pin="CHIPEN" />
                <wire x1="83.82" y1="194.54" x2="66.04" y2="194.54" width="0.1524" layer="91" />
                <label x="66.04" y="194.54" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C16" gate="G$1" pin="1" />
                <wire x1="96.52" y1="152.40" x2="78.74" y2="152.40" width="0.1524" layer="91" />
                <label x="78.74" y="152.40" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="MK2" gate="G$1" pin="VDD" />
                <wire x1="298.45" y1="199.62" x2="303.53" y2="199.62" width="0.1524" layer="91" />
                <label x="303.53" y="199.62" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="MK2" gate="G$1" pin="CHIPEN" />
                <wire x1="262.89" y1="194.54" x2="245.11" y2="194.54" width="0.1524" layer="91" />
                <label x="245.11" y="194.54" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="MK2" gate="G$1" pin="L/R" />
                <wire x1="262.89" y1="189.46" x2="245.11" y2="189.46" width="0.1524" layer="91" />
                <label x="245.11" y="189.46" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C17" gate="G$1" pin="1" />
                <wire x1="275.59" y1="152.40" x2="257.81" y2="152.40" width="0.1524" layer="91" />
                <label x="257.81" y="152.40" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="GND" class="0">
              <segment>
                <pinref part="MK1" gate="G$1" pin="GND" />
                <wire x1="119.38" y1="184.38" x2="124.46" y2="184.38" width="0.1524" layer="91" />
                <label x="124.46" y="184.38" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="MK1" gate="G$1" pin="L/R" />
                <wire x1="83.82" y1="189.46" x2="66.04" y2="189.46" width="0.1524" layer="91" />
                <label x="66.04" y="189.46" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C16" gate="G$1" pin="2" />
                <wire x1="106.68" y1="152.40" x2="111.76" y2="152.40" width="0.1524" layer="91" />
                <label x="111.76" y="152.40" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="MK2" gate="G$1" pin="GND" />
                <wire x1="298.45" y1="184.38" x2="303.53" y2="184.38" width="0.1524" layer="91" />
                <label x="303.53" y="184.38" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C17" gate="G$1" pin="2" />
                <wire x1="285.75" y1="152.40" x2="290.83" y2="152.40" width="0.1524" layer="91" />
                <label x="290.83" y="152.40" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R17" gate="G$1" pin="2" />
                <wire x1="106.68" y1="112.00" x2="111.76" y2="112.00" width="0.1524" layer="91" />
                <label x="111.76" y="112.00" size="1.016" layer="95" />
              </segment>
            </net>
          </nets>
        </sheet>
      </sheets>
    </schematic>
  </drawing>
</eagle>
