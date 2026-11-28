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
        <library name="FRIDAY_SCH4a_Power">
          <packages>
            <package name="QFN24_4X4_EP">
              <wire x1="-2.0" y1="-2.0" x2="2.0" y2="-2.0" width="0.1524" layer="51" />
              <wire x1="2.0" y1="-2.0" x2="2.0" y2="2.0" width="0.1524" layer="51" />
              <wire x1="2.0" y1="2.0" x2="-2.0" y2="2.0" width="0.1524" layer="51" />
              <wire x1="-2.0" y1="2.0" x2="-2.0" y2="-2.0" width="0.1524" layer="51" />
              <wire x1="-2.25" y1="-2.25" x2="2.25" y2="-2.25" width="0.1524" layer="39" />
              <wire x1="2.25" y1="-2.25" x2="2.25" y2="2.25" width="0.1524" layer="39" />
              <wire x1="2.25" y1="2.25" x2="-2.25" y2="2.25" width="0.1524" layer="39" />
              <wire x1="-2.25" y1="2.25" x2="-2.25" y2="-2.25" width="0.1524" layer="39" />
              <text x="-2.0" y="2.35" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-1.92" y="1.25" dx="0.7" dy="0.27" layer="1" cream="yes" />
              <smd name="7" x="-1.25" y="-1.92" dx="0.27" dy="0.7" layer="1" cream="yes" />
              <smd name="13" x="1.92" y="-1.25" dx="0.7" dy="0.27" layer="1" cream="yes" />
              <smd name="19" x="1.25" y="1.92" dx="0.27" dy="0.7" layer="1" cream="yes" />
              <smd name="2" x="-1.92" y="0.75" dx="0.7" dy="0.27" layer="1" cream="yes" />
              <smd name="8" x="-0.75" y="-1.92" dx="0.27" dy="0.7" layer="1" cream="yes" />
              <smd name="14" x="1.92" y="-0.75" dx="0.7" dy="0.27" layer="1" cream="yes" />
              <smd name="20" x="0.75" y="1.92" dx="0.27" dy="0.7" layer="1" cream="yes" />
              <smd name="3" x="-1.92" y="0.25" dx="0.7" dy="0.27" layer="1" cream="yes" />
              <smd name="9" x="-0.25" y="-1.92" dx="0.27" dy="0.7" layer="1" cream="yes" />
              <smd name="15" x="1.92" y="-0.25" dx="0.7" dy="0.27" layer="1" cream="yes" />
              <smd name="21" x="0.25" y="1.92" dx="0.27" dy="0.7" layer="1" cream="yes" />
              <smd name="4" x="-1.92" y="-0.25" dx="0.7" dy="0.27" layer="1" cream="yes" />
              <smd name="10" x="0.25" y="-1.92" dx="0.27" dy="0.7" layer="1" cream="yes" />
              <smd name="16" x="1.92" y="0.25" dx="0.7" dy="0.27" layer="1" cream="yes" />
              <smd name="22" x="-0.25" y="1.92" dx="0.27" dy="0.7" layer="1" cream="yes" />
              <smd name="5" x="-1.92" y="-0.75" dx="0.7" dy="0.27" layer="1" cream="yes" />
              <smd name="11" x="0.75" y="-1.92" dx="0.27" dy="0.7" layer="1" cream="yes" />
              <smd name="17" x="1.92" y="0.75" dx="0.7" dy="0.27" layer="1" cream="yes" />
              <smd name="23" x="-0.75" y="1.92" dx="0.27" dy="0.7" layer="1" cream="yes" />
              <smd name="6" x="-1.92" y="-1.25" dx="0.7" dy="0.27" layer="1" cream="yes" />
              <smd name="12" x="1.25" y="-1.92" dx="0.27" dy="0.7" layer="1" cream="yes" />
              <smd name="18" x="1.92" y="1.25" dx="0.7" dy="0.27" layer="1" cream="yes" />
              <smd name="24" x="-1.25" y="1.92" dx="0.27" dy="0.7" layer="1" cream="yes" />
              <smd name="EP" x="0" y="0" dx="2.5" dy="2.5" layer="1" cream="no" />
              <circle x="-2.18" y="1.9" radius="0.12" width="0.15" layer="21" />
            </package>
            <package name="SOT23_6">
              <wire x1="-1.45" y1="-0.8" x2="1.45" y2="-0.8" width="0.1524" layer="51" />
              <wire x1="1.45" y1="-0.8" x2="1.45" y2="0.8" width="0.1524" layer="51" />
              <wire x1="1.45" y1="0.8" x2="-1.45" y2="0.8" width="0.1524" layer="51" />
              <wire x1="-1.45" y1="0.8" x2="-1.45" y2="-0.8" width="0.1524" layer="51" />
              <wire x1="-1.7" y1="-1.05" x2="1.7" y2="-1.05" width="0.1524" layer="39" />
              <wire x1="1.7" y1="-1.05" x2="1.7" y2="1.05" width="0.1524" layer="39" />
              <wire x1="1.7" y1="1.05" x2="-1.7" y2="1.05" width="0.1524" layer="39" />
              <wire x1="-1.7" y1="1.05" x2="-1.7" y2="-1.05" width="0.1524" layer="39" />
              <text x="-1.45" y="1.15" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-0.95" y="-1.12" dx="0.58" dy="0.95" layer="1" cream="yes" />
              <smd name="6" x="-0.95" y="1.12" dx="0.58" dy="0.95" layer="1" cream="yes" />
              <smd name="2" x="0.0" y="-1.12" dx="0.58" dy="0.95" layer="1" cream="yes" />
              <smd name="5" x="0.0" y="1.12" dx="0.58" dy="0.95" layer="1" cream="yes" />
              <smd name="3" x="0.95" y="-1.12" dx="0.58" dy="0.95" layer="1" cream="yes" />
              <smd name="4" x="0.95" y="1.12" dx="0.58" dy="0.95" layer="1" cream="yes" />
            </package>
            <package name="AOS_DFN2X5A">
              <wire x1="-1.0" y1="-2.5" x2="1.0" y2="-2.5" width="0.1524" layer="51" />
              <wire x1="1.0" y1="-2.5" x2="1.0" y2="2.5" width="0.1524" layer="51" />
              <wire x1="1.0" y1="2.5" x2="-1.0" y2="2.5" width="0.1524" layer="51" />
              <wire x1="-1.0" y1="2.5" x2="-1.0" y2="-2.5" width="0.1524" layer="51" />
              <wire x1="-1.25" y1="-2.75" x2="1.25" y2="-2.75" width="0.1524" layer="39" />
              <wire x1="1.25" y1="-2.75" x2="1.25" y2="2.75" width="0.1524" layer="39" />
              <wire x1="1.25" y1="2.75" x2="-1.25" y2="2.75" width="0.1524" layer="39" />
              <wire x1="-1.25" y1="2.75" x2="-1.25" y2="-2.75" width="0.1524" layer="39" />
              <text x="-1.0" y="2.85" size="0.8" layer="25">&gt;NAME</text>
              <smd name="EP" x="0" y="0" dx="1.8" dy="2.77" layer="1" cream="no" />
              <smd name="G1" x="-0.5" y="-2.25" dx="0.25" dy="0.6" layer="1" cream="yes" />
              <smd name="S1B" x="0.0" y="-2.25" dx="0.25" dy="0.6" layer="1" cream="yes" />
              <smd name="S1A" x="0.5" y="-2.25" dx="0.25" dy="0.6" layer="1" cream="yes" />
              <smd name="S2A" x="-0.5" y="2.25" dx="0.25" dy="0.6" layer="1" cream="yes" />
              <smd name="S2B" x="0.0" y="2.25" dx="0.25" dy="0.6" layer="1" cream="yes" />
              <smd name="G2" x="0.5" y="2.25" dx="0.25" dy="0.6" layer="1" cream="yes" />
              <circle x="-1.15" y="-2.45" radius="0.12" width="0.15" layer="21" />
            </package>
            <package name="TI_RPW0010A">
              <wire x1="-1.0" y1="-1.0" x2="1.0" y2="-1.0" width="0.1524" layer="51" />
              <wire x1="1.0" y1="-1.0" x2="1.0" y2="1.0" width="0.1524" layer="51" />
              <wire x1="1.0" y1="1.0" x2="-1.0" y2="1.0" width="0.1524" layer="51" />
              <wire x1="-1.0" y1="1.0" x2="-1.0" y2="-1.0" width="0.1524" layer="51" />
              <wire x1="-1.25" y1="-1.25" x2="1.25" y2="-1.25" width="0.1524" layer="39" />
              <wire x1="1.25" y1="-1.25" x2="1.25" y2="1.25" width="0.1524" layer="39" />
              <wire x1="1.25" y1="1.25" x2="-1.25" y2="1.25" width="0.1524" layer="39" />
              <wire x1="-1.25" y1="1.25" x2="-1.25" y2="-1.25" width="0.1524" layer="39" />
              <text x="-1.0" y="1.35" size="0.8" layer="25">&gt;NAME</text>
              <smd name="5" x="-0.25" y="0" dx="0.3" dy="2.4" layer="1" cream="yes" />
              <smd name="6" x="0.25" y="0" dx="0.3" dy="2.4" layer="1" cream="yes" />
              <smd name="1" x="-0.9" y="0.7" dx="0.6" dy="0.3" layer="1" cream="yes" />
              <smd name="10" x="0.9" y="0.7" dx="0.6" dy="0.3" layer="1" cream="yes" />
              <smd name="2" x="-0.9" y="0.225" dx="0.6" dy="0.25" layer="1" cream="yes" />
              <smd name="9" x="0.9" y="0.225" dx="0.6" dy="0.25" layer="1" cream="yes" />
              <smd name="3" x="-0.9" y="-0.225" dx="0.6" dy="0.25" layer="1" cream="yes" />
              <smd name="8" x="0.9" y="-0.225" dx="0.6" dy="0.25" layer="1" cream="yes" />
              <smd name="4" x="-0.9" y="-0.7" dx="0.6" dy="0.3" layer="1" cream="yes" />
              <smd name="7" x="0.9" y="-0.7" dx="0.6" dy="0.3" layer="1" cream="yes" />
              <circle x="-1.14" y="0.72" radius="0.11" width="0.15" layer="21" />
            </package>
            <package name="SOT23_3">
              <wire x1="-1.45" y1="-0.675" x2="1.45" y2="-0.675" width="0.1524" layer="51" />
              <wire x1="1.45" y1="-0.675" x2="1.45" y2="0.675" width="0.1524" layer="51" />
              <wire x1="1.45" y1="0.675" x2="-1.45" y2="0.675" width="0.1524" layer="51" />
              <wire x1="-1.45" y1="0.675" x2="-1.45" y2="-0.675" width="0.1524" layer="51" />
              <wire x1="-1.7" y1="-0.925" x2="1.7" y2="-0.925" width="0.1524" layer="39" />
              <wire x1="1.7" y1="-0.925" x2="1.7" y2="0.925" width="0.1524" layer="39" />
              <wire x1="1.7" y1="0.925" x2="-1.7" y2="0.925" width="0.1524" layer="39" />
              <wire x1="-1.7" y1="0.925" x2="-1.7" y2="-0.925" width="0.1524" layer="39" />
              <text x="-1.45" y="1.025" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-0.95" y="-1.0" dx="0.68" dy="0.9" layer="1" cream="yes" />
              <smd name="2" x="0.95" y="-1.0" dx="0.68" dy="0.9" layer="1" cream="yes" />
              <smd name="3" x="0" y="1.0" dx="0.68" dy="0.9" layer="1" cream="yes" />
            </package>
            <package name="DIODES_SOT23">
              <wire x1="-1.45" y1="-0.65" x2="1.45" y2="-0.65" width="0.1524" layer="51" />
              <wire x1="1.45" y1="-0.65" x2="1.45" y2="0.65" width="0.1524" layer="51" />
              <wire x1="1.45" y1="0.65" x2="-1.45" y2="0.65" width="0.1524" layer="51" />
              <wire x1="-1.45" y1="0.65" x2="-1.45" y2="-0.65" width="0.1524" layer="51" />
              <wire x1="-1.7" y1="-0.9" x2="1.7" y2="-0.9" width="0.1524" layer="39" />
              <wire x1="1.7" y1="-0.9" x2="1.7" y2="0.9" width="0.1524" layer="39" />
              <wire x1="1.7" y1="0.9" x2="-1.7" y2="0.9" width="0.1524" layer="39" />
              <wire x1="-1.7" y1="0.9" x2="-1.7" y2="-0.9" width="0.1524" layer="39" />
              <text x="-1.45" y="1.0" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-0.95" y="-1.0" dx="0.8" dy="0.9" layer="1" cream="yes" />
              <smd name="2" x="0.95" y="-1.0" dx="0.8" dy="0.9" layer="1" cream="yes" />
              <smd name="3" x="0" y="1.0" dx="1.35" dy="0.9" layer="1" cream="yes" />
            </package>
            <package name="NANO2_2410">
              <wire x1="-3.05" y1="-1.345" x2="3.05" y2="-1.345" width="0.1524" layer="51" />
              <wire x1="3.05" y1="-1.345" x2="3.05" y2="1.345" width="0.1524" layer="51" />
              <wire x1="3.05" y1="1.345" x2="-3.05" y2="1.345" width="0.1524" layer="51" />
              <wire x1="-3.05" y1="1.345" x2="-3.05" y2="-1.345" width="0.1524" layer="51" />
              <wire x1="-3.3" y1="-1.595" x2="3.3" y2="-1.595" width="0.1524" layer="39" />
              <wire x1="3.3" y1="-1.595" x2="3.3" y2="1.595" width="0.1524" layer="39" />
              <wire x1="3.3" y1="1.595" x2="-3.3" y2="1.595" width="0.1524" layer="39" />
              <wire x1="-3.3" y1="1.595" x2="-3.3" y2="-1.595" width="0.1524" layer="39" />
              <text x="-3.05" y="1.6949999999999998" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-2.445" y="0" dx="2.16" dy="3.15" layer="1" cream="yes" />
              <smd name="2" x="2.445" y="0" dx="2.16" dy="3.15" layer="1" cream="yes" />
            </package>
            <package name="XAL5030">
              <wire x1="-2.74" y1="-2.64" x2="2.74" y2="-2.64" width="0.1524" layer="51" />
              <wire x1="2.74" y1="-2.64" x2="2.74" y2="2.64" width="0.1524" layer="51" />
              <wire x1="2.74" y1="2.64" x2="-2.74" y2="2.64" width="0.1524" layer="51" />
              <wire x1="-2.74" y1="2.64" x2="-2.74" y2="-2.64" width="0.1524" layer="51" />
              <wire x1="-2.99" y1="-2.89" x2="2.99" y2="-2.89" width="0.1524" layer="39" />
              <wire x1="2.99" y1="-2.89" x2="2.99" y2="2.89" width="0.1524" layer="39" />
              <wire x1="2.99" y1="2.89" x2="-2.99" y2="2.89" width="0.1524" layer="39" />
              <wire x1="-2.99" y1="2.89" x2="-2.99" y2="-2.89" width="0.1524" layer="39" />
              <text x="-2.74" y="2.99" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-1.94" y="0" dx="1.52" dy="4.7" layer="1" cream="yes" />
              <smd name="2" x="1.94" y="0" dx="1.52" dy="4.7" layer="1" cream="yes" />
            </package>
            <package name="SOD123FL">
              <wire x1="-1.425" y1="-0.9" x2="1.425" y2="-0.9" width="0.1524" layer="51" />
              <wire x1="1.425" y1="-0.9" x2="1.425" y2="0.9" width="0.1524" layer="51" />
              <wire x1="1.425" y1="0.9" x2="-1.425" y2="0.9" width="0.1524" layer="51" />
              <wire x1="-1.425" y1="0.9" x2="-1.425" y2="-0.9" width="0.1524" layer="51" />
              <wire x1="-1.675" y1="-1.15" x2="1.675" y2="-1.15" width="0.1524" layer="39" />
              <wire x1="1.675" y1="-1.15" x2="1.675" y2="1.15" width="0.1524" layer="39" />
              <wire x1="1.675" y1="1.15" x2="-1.675" y2="1.15" width="0.1524" layer="39" />
              <wire x1="-1.675" y1="1.15" x2="-1.675" y2="-1.15" width="0.1524" layer="39" />
              <text x="-1.425" y="1.25" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-1.39" y="0" dx="1.0" dy="1.6" layer="1" cream="yes" />
              <smd name="2" x="1.39" y="0" dx="1.0" dy="1.6" layer="1" cream="yes" />
              <circle x="-2.1" y="0.82" radius="0.1" width="0.15" layer="21" />
            </package>
            <package name="C_1206">
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
            <package name="VISHAY_WSK2512">
              <wire x1="-3.175" y1="-1.59" x2="3.175" y2="-1.59" width="0.1524" layer="51" />
              <wire x1="3.175" y1="-1.59" x2="3.175" y2="1.59" width="0.1524" layer="51" />
              <wire x1="3.175" y1="1.59" x2="-3.175" y2="1.59" width="0.1524" layer="51" />
              <wire x1="-3.175" y1="1.59" x2="-3.175" y2="-1.59" width="0.1524" layer="51" />
              <wire x1="-3.425" y1="-1.84" x2="3.425" y2="-1.84" width="0.1524" layer="39" />
              <wire x1="3.425" y1="-1.84" x2="3.425" y2="1.84" width="0.1524" layer="39" />
              <wire x1="3.425" y1="1.84" x2="-3.425" y2="1.84" width="0.1524" layer="39" />
              <wire x1="-3.425" y1="1.84" x2="-3.425" y2="-1.84" width="0.1524" layer="39" />
              <text x="-3.175" y="1.94" size="0.8" layer="25">&gt;NAME</text>
              <smd name="P1" x="-3.0" y="0" dx="2.29" dy="3.3" layer="1" cream="yes" />
              <smd name="P2" x="3.0" y="0" dx="2.29" dy="3.3" layer="1" cream="yes" />
              <smd name="K1" x="-1.08" y="1.27" dx="0.76" dy="0.76" layer="1" cream="yes" />
              <smd name="K2" x="1.08" y="1.27" dx="0.76" dy="0.76" layer="1" cream="yes" />
            </package>
            <package name="CELL_TABS">
              <wire x1="-3.55" y1="-1.5" x2="3.55" y2="-1.5" width="0.1524" layer="51" />
              <wire x1="3.55" y1="-1.5" x2="3.55" y2="1.5" width="0.1524" layer="51" />
              <wire x1="3.55" y1="1.5" x2="-3.55" y2="1.5" width="0.1524" layer="51" />
              <wire x1="-3.55" y1="1.5" x2="-3.55" y2="-1.5" width="0.1524" layer="51" />
              <wire x1="-3.8" y1="-1.75" x2="3.8" y2="-1.75" width="0.1524" layer="39" />
              <wire x1="3.8" y1="-1.75" x2="3.8" y2="1.75" width="0.1524" layer="39" />
              <wire x1="3.8" y1="1.75" x2="-3.8" y2="1.75" width="0.1524" layer="39" />
              <wire x1="-3.8" y1="1.75" x2="-3.8" y2="-1.75" width="0.1524" layer="39" />
              <text x="-3.55" y="1.85" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-2.3" y="0" dx="2.5" dy="3.0" layer="1" cream="no" />
              <smd name="2" x="2.3" y="0" dx="2.5" dy="3.0" layer="1" cream="no" />
              <hole x="-2.3" y="-3.3" drill="1.1" />
              <hole x="2.3" y="-3.3" drill="1.1" />
            </package>
            <package name="HARNESS_PADS">
              <wire x1="-3.55" y1="-1.5" x2="3.55" y2="-1.5" width="0.1524" layer="51" />
              <wire x1="3.55" y1="-1.5" x2="3.55" y2="1.5" width="0.1524" layer="51" />
              <wire x1="3.55" y1="1.5" x2="-3.55" y2="1.5" width="0.1524" layer="51" />
              <wire x1="-3.55" y1="1.5" x2="-3.55" y2="-1.5" width="0.1524" layer="51" />
              <wire x1="-3.8" y1="-1.75" x2="3.8" y2="-1.75" width="0.1524" layer="39" />
              <wire x1="3.8" y1="-1.75" x2="3.8" y2="1.75" width="0.1524" layer="39" />
              <wire x1="3.8" y1="1.75" x2="-3.8" y2="1.75" width="0.1524" layer="39" />
              <wire x1="-3.8" y1="1.75" x2="-3.8" y2="-1.75" width="0.1524" layer="39" />
              <text x="-3.55" y="1.85" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-2.3" y="0" dx="2.5" dy="3.0" layer="1" cream="no" />
              <smd name="2" x="2.3" y="0" dx="2.5" dy="3.0" layer="1" cream="no" />
            </package>
            <package name="NTC_PADS">
              <wire x1="-2.045" y1="-1.0" x2="2.045" y2="-1.0" width="0.1524" layer="51" />
              <wire x1="2.045" y1="-1.0" x2="2.045" y2="1.0" width="0.1524" layer="51" />
              <wire x1="2.045" y1="1.0" x2="-2.045" y2="1.0" width="0.1524" layer="51" />
              <wire x1="-2.045" y1="1.0" x2="-2.045" y2="-1.0" width="0.1524" layer="51" />
              <wire x1="-2.295" y1="-1.25" x2="2.295" y2="-1.25" width="0.1524" layer="39" />
              <wire x1="2.295" y1="-1.25" x2="2.295" y2="1.25" width="0.1524" layer="39" />
              <wire x1="2.295" y1="1.25" x2="-2.295" y2="1.25" width="0.1524" layer="39" />
              <wire x1="-2.295" y1="1.25" x2="-2.295" y2="-1.25" width="0.1524" layer="39" />
              <text x="-2.045" y="1.35" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-1.27" y="0" dx="1.55" dy="2.0" layer="1" cream="no" />
              <smd name="2" x="1.27" y="0" dx="1.55" dy="2.0" layer="1" cream="no" />
            </package>
            <package name="EDAC_MAGNETIC_3POS">
              <wire x1="-10.65" y1="-2.3" x2="10.65" y2="-2.3" width="0.1524" layer="51" />
              <wire x1="10.65" y1="-2.3" x2="10.65" y2="2.3" width="0.1524" layer="51" />
              <wire x1="10.65" y1="2.3" x2="-10.65" y2="2.3" width="0.1524" layer="51" />
              <wire x1="-10.65" y1="2.3" x2="-10.65" y2="-2.3" width="0.1524" layer="51" />
              <wire x1="-10.9" y1="-2.55" x2="10.9" y2="-2.55" width="0.1524" layer="39" />
              <wire x1="10.9" y1="-2.55" x2="10.9" y2="2.55" width="0.1524" layer="39" />
              <wire x1="10.9" y1="2.55" x2="-10.9" y2="2.55" width="0.1524" layer="39" />
              <wire x1="-10.9" y1="2.55" x2="-10.9" y2="-2.55" width="0.1524" layer="39" />
              <text x="-10.65" y="2.65" size="0.8" layer="25">&gt;NAME</text>
              <pad name="1" x="-2.7" y="0" drill="0.85" diameter="1.65" />
              <pad name="2" x="0.0" y="0" drill="0.85" diameter="1.65" />
              <pad name="3" x="2.7" y="0" drill="0.85" diameter="1.65" />
              <circle x="-3.85" y="0" radius="0.2" width="0.15" layer="21" />
            </package>
          </packages>
          <symbols>
            <symbol name="IP2326_NPD">
              <wire x1="-17.78" y1="-17.78" x2="17.78" y2="-17.78" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-17.78" x2="17.78" y2="17.78" width="0.1524" layer="94" />
              <wire x1="17.78" y1="17.78" x2="-17.78" y2="17.78" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="17.78" x2="-17.78" y2="-17.78" width="0.1524" layer="94" />
              <text x="-17.78" y="19.05" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-20.32" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="VIN" x="-22.86" y="13.97" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="EN" x="-22.86" y="11.43" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="ISET" x="-22.86" y="8.89" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="VSET" x="-22.86" y="6.3500000000000005" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="CON_SEL" x="-22.86" y="3.8100000000000005" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="TIME_SET" x="-22.86" y="1.2700000000000014" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="VIN_UVSET" x="-22.86" y="-1.2699999999999996" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="VIN_OVSET" x="-22.86" y="-3.8100000000000005" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="NTC" x="-22.86" y="-6.35" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="DM" x="-22.86" y="-8.889999999999999" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="DP" x="-22.86" y="-11.429999999999998" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="LED" x="-22.86" y="-13.97" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="BST" x="22.86" y="10.16" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="LX" x="22.86" y="7.62" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="VSYS" x="22.86" y="5.08" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="VOUT" x="22.86" y="2.54" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="VBATM" x="22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="VBAT_GND" x="22.86" y="-2.539999999999999" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="PGND" x="22.86" y="-5.08" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="EP" x="22.86" y="-7.620000000000001" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="BAT_STAT" x="22.86" y="-10.16" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="HY2120_CB">
              <wire x1="-17.78" y1="-6.35" x2="17.78" y2="-6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-6.35" x2="17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="6.35" x2="-17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="6.35" x2="-17.78" y2="-6.35" width="0.1524" layer="94" />
              <text x="-17.78" y="7.619999999999999" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-8.89" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="VDD" x="-22.86" y="2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="VC" x="-22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="VSS" x="-22.86" y="-2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="OD" x="22.86" y="2.54" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="OC" x="22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="CS" x="22.86" y="-2.54" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="AON5816">
              <wire x1="-17.78" y1="-6.35" x2="17.78" y2="-6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-6.35" x2="17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="6.35" x2="-17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="6.35" x2="-17.78" y2="-6.35" width="0.1524" layer="94" />
              <text x="-17.78" y="7.619999999999999" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-8.89" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="G1" x="-22.86" y="2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="S1" x="-22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="D1_D2" x="-22.86" y="-2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="G2" x="22.86" y="1.27" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="S2" x="22.86" y="-1.27" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="TPS259470">
              <wire x1="-17.78" y1="-8.89" x2="17.78" y2="-8.89" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-8.89" x2="17.78" y2="8.89" width="0.1524" layer="94" />
              <wire x1="17.78" y1="8.89" x2="-17.78" y2="8.89" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="8.89" x2="-17.78" y2="-8.89" width="0.1524" layer="94" />
              <text x="-17.78" y="10.16" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-11.43" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="IN" x="-22.86" y="5.08" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="EN_UVLO" x="-22.86" y="2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="OVLO" x="-22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="GND" x="-22.86" y="-2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="AUXOFF" x="-22.86" y="-5.08" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="OUT" x="22.86" y="5.08" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="ILM" x="22.86" y="2.54" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="DVDT" x="22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="ITIMER" x="22.86" y="-2.54" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="FLT" x="22.86" y="-5.08" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="AO3401A">
              <wire x1="-17.78" y1="-5.08" x2="17.78" y2="-5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-5.08" x2="17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="5.08" x2="-17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="5.08" x2="-17.78" y2="-5.08" width="0.1524" layer="94" />
              <text x="-17.78" y="6.35" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-7.62" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="D" x="-22.86" y="1.27" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="G" x="-22.86" y="-1.27" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="S" x="22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="DMN2058U">
              <wire x1="-17.78" y1="-5.08" x2="17.78" y2="-5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-5.08" x2="17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="5.08" x2="-17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="5.08" x2="-17.78" y2="-5.08" width="0.1524" layer="94" />
              <text x="-17.78" y="6.35" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-7.62" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="G" x="-22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="D" x="22.86" y="1.27" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="S" x="22.86" y="-1.27" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="NANO2_FUSE">
              <pin name="1" x="-5.08" y="0.0" length="short" direction="pas" visible="off" rot="R0" />
              <pin name="2" x="5.08" y="0.0" length="short" direction="pas" visible="off" rot="R180" />
              <wire x1="-2.54" y1="1.27" x2="2.54" y2="1.27" width="0.1524" layer="94" />
              <wire x1="2.54" y1="1.27" x2="2.54" y2="-1.27" width="0.1524" layer="94" />
              <wire x1="2.54" y1="-1.27" x2="-2.54" y2="-1.27" width="0.1524" layer="94" />
              <wire x1="-2.54" y1="-1.27" x2="-2.54" y2="1.27" width="0.1524" layer="94" />
              <text x="-2.54" y="2.54" size="1.27" layer="95">&gt;NAME</text>
              <text x="-2.54" y="-3.81" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="INDUCTOR">
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
            <symbol name="R_1206">
              <pin name="1" x="-5.08" y="0.0" length="short" direction="pas" visible="off" rot="R0" />
              <pin name="2" x="5.08" y="0.0" length="short" direction="pas" visible="off" rot="R180" />
              <wire x1="-2.54" y1="1.27" x2="2.54" y2="1.27" width="0.1524" layer="94" />
              <wire x1="2.54" y1="1.27" x2="2.54" y2="-1.27" width="0.1524" layer="94" />
              <wire x1="2.54" y1="-1.27" x2="-2.54" y2="-1.27" width="0.1524" layer="94" />
              <wire x1="-2.54" y1="-1.27" x2="-2.54" y2="1.27" width="0.1524" layer="94" />
              <text x="-2.54" y="2.54" size="1.27" layer="95">&gt;NAME</text>
              <text x="-2.54" y="-3.81" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="SMF_TVS">
              <pin name="K" x="-5.08" y="0.0" length="short" direction="pas" visible="off" rot="R0" />
              <pin name="A" x="5.08" y="0.0" length="short" direction="pas" visible="off" rot="R180" />
              <wire x1="-2.54" y1="1.27" x2="2.54" y2="1.27" width="0.1524" layer="94" />
              <wire x1="2.54" y1="1.27" x2="2.54" y2="-1.27" width="0.1524" layer="94" />
              <wire x1="2.54" y1="-1.27" x2="-2.54" y2="-1.27" width="0.1524" layer="94" />
              <wire x1="-2.54" y1="-1.27" x2="-2.54" y2="1.27" width="0.1524" layer="94" />
              <text x="-2.54" y="2.54" size="1.27" layer="95">&gt;NAME</text>
              <text x="-2.54" y="-3.81" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="WSK2512">
              <wire x1="-17.78" y1="-5.08" x2="17.78" y2="-5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-5.08" x2="17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="5.08" x2="-17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="5.08" x2="-17.78" y2="-5.08" width="0.1524" layer="94" />
              <text x="-17.78" y="6.35" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-7.62" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="I_MINUS" x="-22.86" y="1.27" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="S_MINUS" x="-22.86" y="-1.27" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="I_PLUS" x="22.86" y="1.27" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="S_PLUS" x="22.86" y="-1.27" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="CELL_TABS">
              <wire x1="-17.78" y1="-5.08" x2="17.78" y2="-5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-5.08" x2="17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="5.08" x2="-17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="5.08" x2="-17.78" y2="-5.08" width="0.1524" layer="94" />
              <text x="-17.78" y="6.35" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-7.62" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="POS" x="-22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="NEG" x="22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="HARNESS_PADS">
              <wire x1="-17.78" y1="-5.08" x2="17.78" y2="-5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-5.08" x2="17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="5.08" x2="-17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="5.08" x2="-17.78" y2="-5.08" width="0.1524" layer="94" />
              <text x="-17.78" y="6.35" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-7.62" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="POS" x="-22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="NEG" x="22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="PACK_NTC">
              <pin name="1" x="-5.08" y="0.0" length="short" direction="pas" visible="off" rot="R0" />
              <pin name="2" x="5.08" y="0.0" length="short" direction="pas" visible="off" rot="R180" />
              <wire x1="-2.54" y1="1.27" x2="2.54" y2="1.27" width="0.1524" layer="94" />
              <wire x1="2.54" y1="1.27" x2="2.54" y2="-1.27" width="0.1524" layer="94" />
              <wire x1="2.54" y1="-1.27" x2="-2.54" y2="-1.27" width="0.1524" layer="94" />
              <wire x1="-2.54" y1="-1.27" x2="-2.54" y2="1.27" width="0.1524" layer="94" />
              <text x="-2.54" y="2.54" size="1.27" layer="95">&gt;NAME</text>
              <text x="-2.54" y="-3.81" size="1.27" layer="96">&gt;VALUE</text>
            </symbol>
            <symbol name="MAGNETIC_POGO">
              <wire x1="-17.78" y1="-6.35" x2="17.78" y2="-6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-6.35" x2="17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="6.35" x2="-17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="6.35" x2="-17.78" y2="-6.35" width="0.1524" layer="94" />
              <text x="-17.78" y="7.619999999999999" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-8.89" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="VBUS" x="-22.86" y="2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="GND" x="-22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="DET" x="-22.86" y="-2.54" length="middle" direction="pas" visible="pin" rot="R0" />
            </symbol>
          </symbols>
          <devicesets>
            <deviceset name="IP2326_NPD" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="IP2326_NPD" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="QFN24_4X4_EP">
                  <connects>
                    <connect gate="G$1" pin="VIN" pad="13" />
                    <connect gate="G$1" pin="EN" pad="12" />
                    <connect gate="G$1" pin="ISET" pad="11" />
                    <connect gate="G$1" pin="VSET" pad="3" />
                    <connect gate="G$1" pin="CON_SEL" pad="10" />
                    <connect gate="G$1" pin="TIME_SET" pad="7" />
                    <connect gate="G$1" pin="VIN_UVSET" pad="8" />
                    <connect gate="G$1" pin="VIN_OVSET" pad="9" />
                    <connect gate="G$1" pin="NTC" pad="4" />
                    <connect gate="G$1" pin="DM" pad="1" />
                    <connect gate="G$1" pin="DP" pad="2" />
                    <connect gate="G$1" pin="LED" pad="6" />
                    <connect gate="G$1" pin="BST" pad="14" />
                    <connect gate="G$1" pin="LX" pad="15 16 17" />
                    <connect gate="G$1" pin="VSYS" pad="19 20" />
                    <connect gate="G$1" pin="VOUT" pad="21 22" />
                    <connect gate="G$1" pin="VBATM" pad="23" />
                    <connect gate="G$1" pin="VBAT_GND" pad="24" />
                    <connect gate="G$1" pin="PGND" pad="18" />
                    <connect gate="G$1" pin="EP" pad="EP" />
                    <connect gate="G$1" pin="BAT_STAT" pad="5" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="HY2120_CB" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="HY2120_CB" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="SOT23_6">
                  <connects>
                    <connect gate="G$1" pin="VDD" pad="5" />
                    <connect gate="G$1" pin="VC" pad="4" />
                    <connect gate="G$1" pin="VSS" pad="6" />
                    <connect gate="G$1" pin="OD" pad="1" />
                    <connect gate="G$1" pin="OC" pad="2" />
                    <connect gate="G$1" pin="CS" pad="3" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="AON5816" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="AON5816" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="AOS_DFN2X5A">
                  <connects>
                    <connect gate="G$1" pin="G1" pad="G1" />
                    <connect gate="G$1" pin="S1" pad="S1A S1B" />
                    <connect gate="G$1" pin="D1_D2" pad="EP" />
                    <connect gate="G$1" pin="G2" pad="G2" />
                    <connect gate="G$1" pin="S2" pad="S2A S2B" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="TPS259470" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="TPS259470" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="TI_RPW0010A">
                  <connects>
                    <connect gate="G$1" pin="IN" pad="5" />
                    <connect gate="G$1" pin="EN_UVLO" pad="1" />
                    <connect gate="G$1" pin="OVLO" pad="2" />
                    <connect gate="G$1" pin="GND" pad="8" />
                    <connect gate="G$1" pin="AUXOFF" pad="3" />
                    <connect gate="G$1" pin="OUT" pad="6" />
                    <connect gate="G$1" pin="ILM" pad="9" />
                    <connect gate="G$1" pin="DVDT" pad="7" />
                    <connect gate="G$1" pin="ITIMER" pad="10" />
                    <connect gate="G$1" pin="FLT" pad="4" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="AO3401A" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="AO3401A" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="SOT23_3">
                  <connects>
                    <connect gate="G$1" pin="D" pad="3" />
                    <connect gate="G$1" pin="G" pad="1" />
                    <connect gate="G$1" pin="S" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="DMN2058U" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="DMN2058U" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="DIODES_SOT23">
                  <connects>
                    <connect gate="G$1" pin="G" pad="1" />
                    <connect gate="G$1" pin="D" pad="3" />
                    <connect gate="G$1" pin="S" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="NANO2_FUSE" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="NANO2_FUSE" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="NANO2_2410">
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
            <deviceset name="INDUCTOR" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="INDUCTOR" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="XAL5030">
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
                <device name="" package="C_1206">
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
            <deviceset name="R_1206" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="R_1206" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="C_1206">
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
            <deviceset name="SMF_TVS" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="SMF_TVS" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="SOD123FL">
                  <connects>
                    <connect gate="G$1" pin="K" pad="1" />
                    <connect gate="G$1" pin="A" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="WSK2512" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="WSK2512" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="VISHAY_WSK2512">
                  <connects>
                    <connect gate="G$1" pin="I_MINUS" pad="P1" />
                    <connect gate="G$1" pin="S_MINUS" pad="K1" />
                    <connect gate="G$1" pin="I_PLUS" pad="P2" />
                    <connect gate="G$1" pin="S_PLUS" pad="K2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="CELL_TABS" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="CELL_TABS" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="CELL_TABS">
                  <connects>
                    <connect gate="G$1" pin="POS" pad="1" />
                    <connect gate="G$1" pin="NEG" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="HARNESS_PADS" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="HARNESS_PADS" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="HARNESS_PADS">
                  <connects>
                    <connect gate="G$1" pin="POS" pad="1" />
                    <connect gate="G$1" pin="NEG" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="PACK_NTC" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="PACK_NTC" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="NTC_PADS">
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
            <deviceset name="MAGNETIC_POGO" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="MAGNETIC_POGO" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="EDAC_MAGNETIC_3POS">
                  <connects>
                    <connect gate="G$1" pin="VBUS" pad="1" />
                    <connect gate="G$1" pin="GND" pad="2" />
                    <connect gate="G$1" pin="DET" pad="3" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
          </devicesets>
        </library>
        <library name="MAX98357AETE_T">
          <packages>
            <package name="QFN50P300X300X80-17N">
              <rectangle x1="-0.35" y1="-0.35" x2="0.35" y2="0.35" layer="31" />
              <text x="-2.34" y="-3.105" size="1.27" layer="27" align="top-left">&gt;VALUE</text>
              <text x="-2.34" y="3.105" size="1.27" layer="25">&gt;NAME</text>
              <circle x="-2.475" y="0.75" radius="0.1" width="0.2" layer="21" />
              <circle x="-2.475" y="0.75" radius="0.1" width="0.2" layer="51" />
              <wire x1="1.5" y1="-1.5" x2="-1.5" y2="-1.5" width="0.127" layer="51" />
              <wire x1="1.5" y1="1.5" x2="-1.5" y2="1.5" width="0.127" layer="51" />
              <wire x1="1.5" y1="-1.5" x2="1.5" y2="1.5" width="0.127" layer="51" />
              <wire x1="-1.5" y1="-1.5" x2="-1.5" y2="1.5" width="0.127" layer="51" />
              <wire x1="1.5" y1="-1.5" x2="1.205" y2="-1.5" width="0.127" layer="21" />
              <wire x1="1.5" y1="1.5" x2="1.205" y2="1.5" width="0.127" layer="21" />
              <wire x1="-1.5" y1="-1.5" x2="-1.205" y2="-1.5" width="0.127" layer="21" />
              <wire x1="-1.5" y1="1.5" x2="-1.205" y2="1.5" width="0.127" layer="21" />
              <wire x1="1.5" y1="-1.5" x2="1.5" y2="-1.205" width="0.127" layer="21" />
              <wire x1="1.5" y1="1.5" x2="1.5" y2="1.205" width="0.127" layer="21" />
              <wire x1="-1.5" y1="-1.5" x2="-1.5" y2="-1.205" width="0.127" layer="21" />
              <wire x1="-1.5" y1="1.5" x2="-1.5" y2="1.205" width="0.127" layer="21" />
              <wire x1="-2.105" y1="-2.105" x2="2.105" y2="-2.105" width="0.05" layer="39" />
              <wire x1="-2.105" y1="2.105" x2="2.105" y2="2.105" width="0.05" layer="39" />
              <wire x1="-2.105" y1="-2.105" x2="-2.105" y2="2.105" width="0.05" layer="39" />
              <wire x1="2.105" y1="-2.105" x2="2.105" y2="2.105" width="0.05" layer="39" />
              <smd name="5" x="-0.75" y="-1.435" dx="0.27" dy="0.84" layer="1" roundness="25" />
              <smd name="6" x="-0.25" y="-1.435" dx="0.27" dy="0.84" layer="1" roundness="25" />
              <smd name="7" x="0.25" y="-1.435" dx="0.27" dy="0.84" layer="1" roundness="25" />
              <smd name="8" x="0.75" y="-1.435" dx="0.27" dy="0.84" layer="1" roundness="25" />
              <smd name="13" x="0.75" y="1.435" dx="0.27" dy="0.84" layer="1" roundness="25" />
              <smd name="14" x="0.25" y="1.435" dx="0.27" dy="0.84" layer="1" roundness="25" />
              <smd name="15" x="-0.25" y="1.435" dx="0.27" dy="0.84" layer="1" roundness="25" />
              <smd name="16" x="-0.75" y="1.435" dx="0.27" dy="0.84" layer="1" roundness="25" />
              <smd name="1" x="-1.435" y="0.75" dx="0.84" dy="0.27" layer="1" roundness="25" />
              <smd name="2" x="-1.435" y="0.25" dx="0.84" dy="0.27" layer="1" roundness="25" />
              <smd name="3" x="-1.435" y="-0.25" dx="0.84" dy="0.27" layer="1" roundness="25" />
              <smd name="4" x="-1.435" y="-0.75" dx="0.84" dy="0.27" layer="1" roundness="25" />
              <smd name="9" x="1.435" y="-0.75" dx="0.84" dy="0.27" layer="1" roundness="25" />
              <smd name="10" x="1.435" y="-0.25" dx="0.84" dy="0.27" layer="1" roundness="25" />
              <smd name="11" x="1.435" y="0.25" dx="0.84" dy="0.27" layer="1" roundness="25" />
              <smd name="12" x="1.435" y="0.75" dx="0.84" dy="0.27" layer="1" roundness="25" />
              <smd name="17" x="0" y="0" dx="1.1" dy="1.1" layer="1" cream="no" />
            </package>
          </packages>
          <symbols>
            <symbol name="MAX98357AETE+T">
              <wire x1="-12.7" y1="15.24" x2="12.7" y2="15.24" width="0.41" layer="94" />
              <wire x1="12.7" y1="15.24" x2="12.7" y2="-15.24" width="0.41" layer="94" />
              <wire x1="12.7" y1="-15.24" x2="-12.7" y2="-15.24" width="0.41" layer="94" />
              <wire x1="-12.7" y1="-15.24" x2="-12.7" y2="15.24" width="0.41" layer="94" />
              <text x="-12.7" y="16.24" size="2.0828" layer="95" ratio="10" rot="SR0">&gt;NAME</text>
              <text x="-12.7" y="-19.24" size="2.0828" layer="96" ratio="10" rot="SR0">&gt;VALUE</text>
              <pin name="BCLK" x="-17.78" y="7.62" length="middle" direction="in" function="clk" />
              <pin name="DIN" x="-17.78" y="5.08" length="middle" direction="in" />
              <pin name="GAIN_SLOT" x="-17.78" y="2.54" length="middle" direction="in" />
              <pin name="LRCLK" x="-17.78" y="0" length="middle" direction="in" function="clk" />
              <pin name="SD_MODE" x="-17.78" y="-2.54" length="middle" direction="in" />
              <pin name="VDD" x="17.78" y="12.7" length="middle" direction="pwr" rot="R180" />
              <pin name="OUTN" x="17.78" y="7.62" length="middle" direction="out" rot="R180" />
              <pin name="OUTP" x="17.78" y="5.08" length="middle" direction="out" rot="R180" />
              <pin name="EP" x="17.78" y="-10.16" length="middle" direction="pwr" rot="R180" />
              <pin name="GND" x="17.78" y="-12.7" length="middle" direction="pwr" rot="R180" />
            </symbol>
          </symbols>
          <devicesets>
            <deviceset name="MAX98357AETE+T" prefix="U">
              <gates>
                <gate name="G$1" symbol="MAX98357AETE+T" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="QFN50P300X300X80-17N">
                  <connects>
                    <connect gate="G$1" pin="BCLK" pad="16" />
                    <connect gate="G$1" pin="DIN" pad="1" />
                    <connect gate="G$1" pin="EP" pad="17" />
                    <connect gate="G$1" pin="GAIN_SLOT" pad="2" />
                    <connect gate="G$1" pin="GND" pad="3 11 15" />
                    <connect gate="G$1" pin="LRCLK" pad="14" />
                    <connect gate="G$1" pin="OUTN" pad="10" />
                    <connect gate="G$1" pin="OUTP" pad="9" />
                    <connect gate="G$1" pin="SD_MODE" pad="4" />
                    <connect gate="G$1" pin="VDD" pad="7 8" />
                  </connects>
                  <technologies>
                    <technology name="">
                      <attribute name="DATASHEET_URL" value="https://s3.amazonaws.com/snapeda/datasheet/MAX98357AETE_T_Maxim_Integrated_Products.pdf" />
                      <attribute name="DESCRIPTION" value="Audio Amp Speaker 1-CH Mono 3.2W Class-D 16-Pin TQFN EP T/R" />
                      <attribute name="MANUFACTURER" value="Analog Devices" />
                      <attribute name="MPN" value="MAX98357AETE+T" />
                      <attribute name="Package" value="TQFN-16 Maxim" />
                      <attribute name="SOURCE_URL" value="https://www.snapeda.com/parts/MAX98357AETE+T/Analog+Devices/view-part/" />
                    </technology>
                  </technologies>
                </device>
              </devices>
            </deviceset>
          </devicesets>
        </library>
        <library name="FRIDAY_SCH4b_Audio">
          <packages>
            <package name="SOT23_3">
              <wire x1="-1.45" y1="-0.675" x2="1.45" y2="-0.675" width="0.1524" layer="51" />
              <wire x1="1.45" y1="-0.675" x2="1.45" y2="0.675" width="0.1524" layer="51" />
              <wire x1="1.45" y1="0.675" x2="-1.45" y2="0.675" width="0.1524" layer="51" />
              <wire x1="-1.45" y1="0.675" x2="-1.45" y2="-0.675" width="0.1524" layer="51" />
              <wire x1="-1.7" y1="-0.925" x2="1.7" y2="-0.925" width="0.1524" layer="39" />
              <wire x1="1.7" y1="-0.925" x2="1.7" y2="0.925" width="0.1524" layer="39" />
              <wire x1="1.7" y1="0.925" x2="-1.7" y2="0.925" width="0.1524" layer="39" />
              <wire x1="-1.7" y1="0.925" x2="-1.7" y2="-0.925" width="0.1524" layer="39" />
              <text x="-1.45" y="1.025" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-0.95" y="-1.0" dx="0.68" dy="0.9" layer="1" cream="yes" />
              <smd name="2" x="0.95" y="-1.0" dx="0.68" dy="0.9" layer="1" cream="yes" />
              <smd name="3" x="0" y="1.0" dx="0.68" dy="0.9" layer="1" cream="yes" />
            </package>
            <package name="DIODES_SOT23">
              <wire x1="-1.45" y1="-0.65" x2="1.45" y2="-0.65" width="0.1524" layer="51" />
              <wire x1="1.45" y1="-0.65" x2="1.45" y2="0.65" width="0.1524" layer="51" />
              <wire x1="1.45" y1="0.65" x2="-1.45" y2="0.65" width="0.1524" layer="51" />
              <wire x1="-1.45" y1="0.65" x2="-1.45" y2="-0.65" width="0.1524" layer="51" />
              <wire x1="-1.7" y1="-0.9" x2="1.7" y2="-0.9" width="0.1524" layer="39" />
              <wire x1="1.7" y1="-0.9" x2="1.7" y2="0.9" width="0.1524" layer="39" />
              <wire x1="1.7" y1="0.9" x2="-1.7" y2="0.9" width="0.1524" layer="39" />
              <wire x1="-1.7" y1="0.9" x2="-1.7" y2="-0.9" width="0.1524" layer="39" />
              <text x="-1.45" y="1.0" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-0.95" y="-1.0" dx="0.8" dy="0.9" layer="1" cream="yes" />
              <smd name="2" x="0.95" y="-1.0" dx="0.8" dy="0.9" layer="1" cream="yes" />
              <smd name="3" x="0" y="1.0" dx="1.35" dy="0.9" layer="1" cream="yes" />
            </package>
            <package name="C_1206">
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
            <package name="TI_DBV_SOT23_5">
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
            </package>
            <package name="FRIDAY_SPEAKER_SOLDER_LANDS">
              <wire x1="-3.1" y1="-1.4" x2="3.1" y2="-1.4" width="0.1524" layer="51" />
              <wire x1="3.1" y1="-1.4" x2="3.1" y2="1.4" width="0.1524" layer="51" />
              <wire x1="3.1" y1="1.4" x2="-3.1" y2="1.4" width="0.1524" layer="51" />
              <wire x1="-3.1" y1="1.4" x2="-3.1" y2="-1.4" width="0.1524" layer="51" />
              <wire x1="-3.35" y1="-1.65" x2="3.35" y2="-1.65" width="0.1524" layer="39" />
              <wire x1="3.35" y1="-1.65" x2="3.35" y2="1.65" width="0.1524" layer="39" />
              <wire x1="3.35" y1="1.65" x2="-3.35" y2="1.65" width="0.1524" layer="39" />
              <wire x1="-3.35" y1="1.65" x2="-3.35" y2="-1.65" width="0.1524" layer="39" />
              <text x="-3.1" y="1.75" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-1.9" y="0" dx="2.4" dy="2.8" layer="1" cream="no" />
              <smd name="2" x="1.9" y="0" dx="2.4" dy="2.8" layer="1" cream="no" />
            </package>
            <package name="POWERPAK_1212_8SCD">
              <wire x1="-1.65" y1="-1.65" x2="1.65" y2="-1.65" width="0.1524" layer="51" />
              <wire x1="1.65" y1="-1.65" x2="1.65" y2="1.65" width="0.1524" layer="51" />
              <wire x1="1.65" y1="1.65" x2="-1.65" y2="1.65" width="0.1524" layer="51" />
              <wire x1="-1.65" y1="1.65" x2="-1.65" y2="-1.65" width="0.1524" layer="51" />
              <wire x1="-1.9" y1="-1.9" x2="1.9" y2="-1.9" width="0.1524" layer="39" />
              <wire x1="1.9" y1="-1.9" x2="1.9" y2="1.9" width="0.1524" layer="39" />
              <wire x1="1.9" y1="1.9" x2="-1.9" y2="1.9" width="0.1524" layer="39" />
              <wire x1="-1.9" y1="1.9" x2="-1.9" y2="-1.9" width="0.1524" layer="39" />
              <text x="-1.65" y="2.0" size="0.8" layer="25">&gt;NAME</text>
              <smd name="1" x="-1.305" y="0.9750000000000001" dx="1.29" dy="0.4" layer="1" cream="yes" />
              <smd name="2" x="-1.305" y="0.325" dx="1.29" dy="0.4" layer="1" cream="yes" />
              <smd name="3" x="-1.305" y="-0.325" dx="1.29" dy="0.4" layer="1" cream="yes" />
              <smd name="4" x="-1.305" y="-0.9750000000000001" dx="1.29" dy="0.4" layer="1" cream="yes" />
              <smd name="S1_78" x="0.6" y="0.82" dx="1.64" dy="1.35" layer="1" cream="no" stop="no" />
              <smd name="S2_56" x="0.6" y="-0.82" dx="1.64" dy="1.35" layer="1" cream="no" stop="no" />
              <circle x="-1.95" y="1.44" radius="0.1" width="0.15" layer="21" />
              <polygon width="0.05" layer="1">
                <vertex x="1.95" y="0.532" />
                <vertex x="1.5" y="0.532" />
                <vertex x="1.5" y="0.763" />
                <vertex x="1.95" y="0.763" />
                <vertex x="1.95" y="1.184" />
                <vertex x="1.5" y="1.184" />
                <vertex x="1.5" y="1.499" />
                <vertex x="0.04" y="1.499" />
                <vertex x="0.04" y="1.698" />
                <vertex x="-0.26" y="1.698" />
                <vertex x="-0.26" y="0.116" />
                <vertex x="1.95" y="0.116" />
              </polygon>
              <polygon width="0.05" layer="29">
                <vertex x="1.95" y="0.532" />
                <vertex x="1.5" y="0.532" />
                <vertex x="1.5" y="0.763" />
                <vertex x="1.95" y="0.763" />
                <vertex x="1.95" y="1.184" />
                <vertex x="1.5" y="1.184" />
                <vertex x="1.5" y="1.499" />
                <vertex x="0.04" y="1.499" />
                <vertex x="0.04" y="1.698" />
                <vertex x="-0.26" y="1.698" />
                <vertex x="-0.26" y="0.116" />
                <vertex x="1.95" y="0.116" />
              </polygon>
              <rectangle x1="-0.19" y1="0.24" x2="1.37" y2="1.39" layer="31" />
              <rectangle x1="1.49" y1="0.18" x2="1.88" y2="0.47" layer="31" />
              <rectangle x1="1.49" y1="0.84" x2="1.88" y2="1.1" layer="31" />
              <polygon width="0.05" layer="1">
                <vertex x="1.95" y="-0.532" />
                <vertex x="1.5" y="-0.532" />
                <vertex x="1.5" y="-0.763" />
                <vertex x="1.95" y="-0.763" />
                <vertex x="1.95" y="-1.184" />
                <vertex x="1.5" y="-1.184" />
                <vertex x="1.5" y="-1.499" />
                <vertex x="0.04" y="-1.499" />
                <vertex x="0.04" y="-1.698" />
                <vertex x="-0.26" y="-1.698" />
                <vertex x="-0.26" y="-0.116" />
                <vertex x="1.95" y="-0.116" />
              </polygon>
              <polygon width="0.05" layer="29">
                <vertex x="1.95" y="-0.532" />
                <vertex x="1.5" y="-0.532" />
                <vertex x="1.5" y="-0.763" />
                <vertex x="1.95" y="-0.763" />
                <vertex x="1.95" y="-1.184" />
                <vertex x="1.5" y="-1.184" />
                <vertex x="1.5" y="-1.499" />
                <vertex x="0.04" y="-1.499" />
                <vertex x="0.04" y="-1.698" />
                <vertex x="-0.26" y="-1.698" />
                <vertex x="-0.26" y="-0.116" />
                <vertex x="1.95" y="-0.116" />
              </polygon>
              <rectangle x1="-0.19" y1="-1.39" x2="1.37" y2="-0.24" layer="31" />
              <rectangle x1="1.49" y1="-0.47" x2="1.88" y2="-0.18" layer="31" />
              <rectangle x1="1.49" y1="-1.1" x2="1.88" y2="-0.84" layer="31" />
            </package>
          </packages>
          <symbols>
            <symbol name="AO3401A">
              <wire x1="-17.78" y1="-5.08" x2="17.78" y2="-5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-5.08" x2="17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="5.08" x2="-17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="5.08" x2="-17.78" y2="-5.08" width="0.1524" layer="94" />
              <text x="-17.78" y="6.35" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-7.62" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="D" x="-22.86" y="1.27" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="G" x="-22.86" y="-1.27" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="S" x="22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="DMN2058U">
              <wire x1="-17.78" y1="-5.08" x2="17.78" y2="-5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-5.08" x2="17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="5.08" x2="-17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="5.08" x2="-17.78" y2="-5.08" width="0.1524" layer="94" />
              <text x="-17.78" y="6.35" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-7.62" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="G" x="-22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="D" x="22.86" y="1.27" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="S" x="22.86" y="-1.27" length="middle" direction="pas" visible="pin" rot="R180" />
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
            <symbol name="TLV7041">
              <wire x1="-17.78" y1="-7.62" x2="17.78" y2="-7.62" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-7.62" x2="17.78" y2="7.62" width="0.1524" layer="94" />
              <wire x1="17.78" y1="7.62" x2="-17.78" y2="7.62" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="7.62" x2="-17.78" y2="-7.62" width="0.1524" layer="94" />
              <text x="-17.78" y="8.89" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-10.16" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="IN+" x="-22.86" y="3.81" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="IN-" x="-22.86" y="1.27" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="VCC" x="-22.86" y="-1.27" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="GND" x="-22.86" y="-3.81" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="OUT" x="22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="BTL_SPEAKER">
              <wire x1="-17.78" y1="-5.08" x2="17.78" y2="-5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-5.08" x2="17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="17.78" y1="5.08" x2="-17.78" y2="5.08" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="5.08" x2="-17.78" y2="-5.08" width="0.1524" layer="94" />
              <text x="-17.78" y="6.35" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-7.62" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="SPK_P" x="-22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="SPK_N" x="22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
            <symbol name="SISF04DN">
              <wire x1="-17.78" y1="-6.35" x2="17.78" y2="-6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="-6.35" x2="17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="17.78" y1="6.35" x2="-17.78" y2="6.35" width="0.1524" layer="94" />
              <wire x1="-17.78" y1="6.35" x2="-17.78" y2="-6.35" width="0.1524" layer="94" />
              <text x="-17.78" y="7.619999999999999" size="1.27" layer="95">&gt;NAME</text>
              <text x="-17.78" y="-8.89" size="1.27" layer="96">&gt;VALUE</text>
              <pin name="G1" x="-22.86" y="2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="S1" x="-22.86" y="0.0" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="D1_D2" x="-22.86" y="-2.54" length="middle" direction="pas" visible="pin" rot="R0" />
              <pin name="G2" x="22.86" y="1.27" length="middle" direction="pas" visible="pin" rot="R180" />
              <pin name="S2" x="22.86" y="-1.27" length="middle" direction="pas" visible="pin" rot="R180" />
            </symbol>
          </symbols>
          <devicesets>
            <deviceset name="AO3401A" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="AO3401A" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="SOT23_3">
                  <connects>
                    <connect gate="G$1" pin="D" pad="3" />
                    <connect gate="G$1" pin="G" pad="1" />
                    <connect gate="G$1" pin="S" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="DMN2058U" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="DMN2058U" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="DIODES_SOT23">
                  <connects>
                    <connect gate="G$1" pin="G" pad="1" />
                    <connect gate="G$1" pin="D" pad="3" />
                    <connect gate="G$1" pin="S" pad="2" />
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
                <device name="" package="C_1206">
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
            <deviceset name="TLV7041" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="TLV7041" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="TI_DBV_SOT23_5">
                  <connects>
                    <connect gate="G$1" pin="IN+" pad="3" />
                    <connect gate="G$1" pin="IN-" pad="4" />
                    <connect gate="G$1" pin="VCC" pad="5" />
                    <connect gate="G$1" pin="GND" pad="2" />
                    <connect gate="G$1" pin="OUT" pad="1" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="BTL_SPEAKER" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="BTL_SPEAKER" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="FRIDAY_SPEAKER_SOLDER_LANDS">
                  <connects>
                    <connect gate="G$1" pin="SPK_P" pad="1" />
                    <connect gate="G$1" pin="SPK_N" pad="2" />
                  </connects>
                  <technologies>
                    <technology name="" />
                  </technologies>
                </device>
              </devices>
            </deviceset>
            <deviceset name="SISF04DN" uservalue="yes">
              <gates>
                <gate name="G$1" symbol="SISF04DN" x="0" y="0" />
              </gates>
              <devices>
                <device name="" package="POWERPAK_1212_8SCD">
                  <connects>
                    <connect gate="G$1" pin="G1" pad="1" />
                    <connect gate="G$1" pin="S1" pad="S1_78" />
                    <connect gate="G$1" pin="D1_D2" pad="2 3" />
                    <connect gate="G$1" pin="G2" pad="4" />
                    <connect gate="G$1" pin="S2" pad="S2_56" />
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
      <variantdefs />
      <classes>
        <class number="0" name="default" width="0" drill="0" />
      </classes>
      <parts>
        <part name="FRAME1" library="FRIDAY_SCH1_Support" deviceset="A3_FRAME" device="" value="" />
        <part name="BT1" library="FRIDAY_SCH4a_Power" deviceset="CELL_TABS" device="" value="UPPER 1S POUCH TABS" />
        <part name="BT2" library="FRIDAY_SCH4a_Power" deviceset="CELL_TABS" device="" value="LOWER 1S POUCH TABS" />
        <part name="F1" library="FRIDAY_SCH4a_Power" deviceset="NANO2_FUSE" device="" value="0451002.MRL 2A" />
        <part name="J2" library="FRIDAY_SCH4a_Power" deviceset="HARNESS_PADS" device="" value="D16 KEYED HARNESS PADS" />
        <part name="U2" library="FRIDAY_SCH4a_Power" deviceset="HY2120_CB" device="" value="HY2120-CB" />
        <part name="Q1" library="FRIDAY_SCH4b_Audio" deviceset="SISF04DN" device="" value="SiSF04DN-T1-GE3" />
        <part name="RS1" library="FRIDAY_SCH4a_Power" deviceset="WSK2512" device="" value="WSK2512R0200FEA 20mR 1W" />
        <part name="R1" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="330R" />
        <part name="R2" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="330R" />
        <part name="R3" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="2k" />
        <part name="C1" library="FRIDAY_SCH1_Support" deviceset="C_0603" device="" value="100nF 25V" />
        <part name="C2" library="FRIDAY_SCH1_Support" deviceset="C_0603" device="" value="100nF 25V" />
        <part name="TP1" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="PACK+ (PROTECTED)" />
        <part name="TP2" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="PACK- (PROTECTED)" />
        <part name="TP3" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="CELL_MID" />
        <part name="TP4" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="SHUNT K-" />
        <part name="TP5" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="SHUNT K+" />
        <part name="FRAME2" library="FRIDAY_SCH1_Support" deviceset="A3_FRAME" device="" value="" />
        <part name="U1" library="FRIDAY_SCH4a_Power" deviceset="IP2326_NPD" device="" value="IP2326_NPD" />
        <part name="Q2" library="FRIDAY_SCH4a_Power" deviceset="AO3401A" device="" value="AO3401A" />
        <part name="R4" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="0.5R 5%" />
        <part name="R5" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="450k 1%" />
        <part name="R6" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="120k 1%" />
        <part name="R7" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="68k 1%" />
        <part name="R8" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="82k 1%" />
        <part name="R9" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="5.1k 5%" />
        <part name="R10" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="3.1M 5%" />
        <part name="R11" library="FRIDAY_SCH4a_Power" deviceset="R_1206" device="" value="120R 1% 0.25W" />
        <part name="TH1" library="FRIDAY_SCH4a_Power" deviceset="PACK_NTC" device="" value="HNT-GR1 100k B4100" />
        <part name="L1" library="FRIDAY_SCH4a_Power" deviceset="INDUCTOR" device="" value="XAL5030-222MEC 2.2uH" />
        <part name="C3" library="FRIDAY_SCH4a_Power" deviceset="C_1206" device="" value="10uF 25V X7R" />
        <part name="C4" library="FRIDAY_SCH4a_Power" deviceset="C_1206" device="" value="10uF 25V X7R" />
        <part name="C5" library="FRIDAY_SCH1_Support" deviceset="C_0603" device="" value="100nF 25V X7R" />
        <part name="C6" library="FRIDAY_SCH4a_Power" deviceset="C_1206" device="" value="22uF 25V X7R" />
        <part name="C7" library="FRIDAY_SCH4a_Power" deviceset="C_1206" device="" value="22uF 25V X7R" />
        <part name="C8" library="FRIDAY_SCH4a_Power" deviceset="C_1206" device="" value="10uF 25V X7R" />
        <part name="C9" library="FRIDAY_SCH4a_Power" deviceset="C_1206" device="" value="10uF 25V X7R" />
        <part name="C10" library="FRIDAY_SCH1_Support" deviceset="C_0603" device="" value="100nF 25V X7R" />
        <part name="C11" library="FRIDAY_SCH1_Support" deviceset="C_0603" device="" value="100nF 25V X7R" />
        <part name="TP7" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="CHARGER SW" />
        <part name="TP8" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="PACK NTC" />
        <part name="FRAME3" library="FRIDAY_SCH1_Support" deviceset="A3_FRAME" device="" value="" />
        <part name="J1" library="FRIDAY_SCH4a_Power" deviceset="MAGNETIC_POGO" device="" value="EDAC 686E0321250110E" />
        <part name="U3" library="FRIDAY_SCH4a_Power" deviceset="TPS259470" device="" value="TPS259470ARPW" />
        <part name="R12" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="374k 1%" />
        <part name="R13" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="150k 1%" />
        <part name="R14" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="365k 1%" />
        <part name="R15" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="100k 1%" />
        <part name="R16" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="6.04k 1%" />
        <part name="D1" library="FRIDAY_SCH4a_Power" deviceset="SMF_TVS" device="" value="SMF6.0A" />
        <part name="C12" library="FRIDAY_SCH1_Support" deviceset="C_0603" device="" value="1uF 25V X7R" />
        <part name="C13" library="FRIDAY_SCH1_Support" deviceset="C_0603" device="" value="1nF 25V C0G" />
        <part name="U4" library="FRIDAY_SCH4a_Power" deviceset="TPS259470" device="" value="TPS259470ARPW" />
        <part name="R17" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="374k 1%" />
        <part name="R18" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="150k 1%" />
        <part name="R19" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="365k 1%" />
        <part name="R20" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="100k 1%" />
        <part name="R21" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="6.04k 1%" />
        <part name="D2" library="FRIDAY_SCH4a_Power" deviceset="SMF_TVS" device="" value="SMF6.0A" />
        <part name="C14" library="FRIDAY_SCH1_Support" deviceset="C_0603" device="" value="1uF 25V X7R" />
        <part name="C15" library="FRIDAY_SCH1_Support" deviceset="C_0603" device="" value="1nF 25V C0G" />
        <part name="TP6" library="FRIDAY_SCH1_Support" deviceset="TP_1MM" device="" value="VBUS OR" />
        <part name="FRAME4" library="FRIDAY_SCH1_Support" deviceset="A3_FRAME" device="" value="" />
        <part name="J3" library="FH12-24S-0.5SH_55_" deviceset="FH12-24S-0.5SH(55)" device="" value="FH12-24S-0.5SH(55)" />
        <part name="Q3" library="FRIDAY_SCH4a_Power" deviceset="DMN2058U" device="" value="DMN2058U-7" />
        <part name="R22" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="47k 1%" />
        <part name="R23" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="100k 1%" />
        <part name="Q4" library="FRIDAY_SCH4a_Power" deviceset="DMN2058U" device="" value="DMN2058U-7" />
        <part name="R24" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="4.7k 1%" />
        <part name="R25" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="1M 1%" />
        <part name="Q5" library="FRIDAY_SCH4a_Power" deviceset="DMN2058U" device="" value="DMN2058U-7" />
        <part name="R26" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="4.7k 1%" />
        <part name="R27" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="1M 1%" />
        <part name="R28" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="5.1k 1%" />
        <part name="FRAME5" library="FRIDAY_SCH1_Support" deviceset="A3_FRAME" device="" value="" />
        <part name="U5" library="MAX98357AETE_T" deviceset="MAX98357AETE+T" device="" value="MAX98357AETE+T" />
        <part name="J4" library="FRIDAY_SCH4b_Audio" deviceset="BTL_SPEAKER" device="" value="1510 / 8 ohm assumed" />
        <part name="U6" library="FRIDAY_SCH4b_Audio" deviceset="TLV7041" device="" value="TLV7041DBVR" />
        <part name="Q6" library="FRIDAY_SCH4b_Audio" deviceset="AO3401A" device="" value="AO3401A" />
        <part name="R29" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="1k 1%" />
        <part name="R30" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="100k 1%" />
        <part name="R31" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="100k 1%" />
        <part name="R32" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="1k 1%" />
        <part name="R33" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="4.7k 1%" />
        <part name="R34" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="100k 1%" />
        <part name="R35" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="56k 1%" />
        <part name="R36" library="FRIDAY_SCH1_Support" deviceset="R_0603" device="" value="10k 1%" />
        <part name="C16" library="FRIDAY_SCH1_Support" deviceset="C_0603" device="" value="100nF 16V X7R" />
        <part name="C17" library="FRIDAY_SCH1_Support" deviceset="C_0805" device="" value="10uF 16V X7R" />
        <part name="C18" library="FRIDAY_SCH1_Support" deviceset="C_0603" device="" value="100nF 16V X7R" />
        <part name="C19" library="FRIDAY_SCH4b_Audio" deviceset="C_1206" device="" value="22uF 16V X7R" />
      </parts>
      <sheets>
        <sheet>
          <plain>
            <text x="15.24" y="281.94" size="2.54" layer="94">FRIDAY / SCH-4a / LEFT TEMPLE PACK AND PROTECTION</text>
            <text x="15.24" y="274.32" size="1.78" layer="94">D16/D17 | Both cells local | Generic tab pads | Bench qualification pending</text>
            <text x="15.24" y="255.27" size="1.78" layer="94">BT1 / BT2 tabs solder locally. Fit strain relief to the final cell and frame before assembly.</text>
            <text x="15.24" y="247.65" size="1.78" layer="94">J2 pad 1 positive, pad 2 protected return. Use a keyed two-lead harness. No cell-midpoint crossing.</text>
            <text x="15.24" y="176.53" size="1.78" layer="94">U2 CS observes the drop across both protection FETs and RS1. Do not bond any raw cell return to enclosure or flex.</text>
          </plain>
          <instances>
            <instance part="FRAME1" gate="G$1" x="0" y="0" smashed="yes" />
            <instance part="BT1" gate="G$1" x="76.2" y="220.98" smashed="yes">
              <attribute name="NAME" x="58.42" y="227.32999999999998" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="58.42" y="213.35999999999999" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="BT2" gate="G$1" x="76.2" y="193.04" smashed="yes">
              <attribute name="NAME" x="58.42" y="199.39" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="58.42" y="185.42" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="F1" gate="G$1" x="198.12" y="220.98" smashed="yes">
              <attribute name="NAME" x="195.58" y="223.51999999999998" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="195.58" y="217.17" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="J2" gate="G$1" x="319.05" y="220.98" smashed="yes">
              <attribute name="NAME" x="301.27" y="227.32999999999998" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="301.27" y="213.35999999999999" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="U2" gate="G$1" x="76.2" y="137.16" smashed="yes">
              <attribute name="NAME" x="58.42" y="144.78" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="58.42" y="128.26999999999998" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="Q1" gate="G$1" x="198.12" y="137.16" smashed="yes">
              <attribute name="NAME" x="180.34" y="144.78" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="180.34" y="128.26999999999998" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="RS1" gate="G$1" x="319.05" y="137.16" smashed="yes">
              <attribute name="NAME" x="301.27" y="143.51" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="301.27" y="129.54" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R1" gate="G$1" x="50.8" y="98.24" smashed="yes">
              <attribute name="NAME" x="48.26" y="99.64" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="48.26" y="95.44" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R2" gate="G$1" x="129.54" y="98.24" smashed="yes">
              <attribute name="NAME" x="126.99999999999999" y="99.64" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="126.99999999999999" y="95.44" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R3" gate="G$1" x="210.82" y="98.24" smashed="yes">
              <attribute name="NAME" x="208.28" y="99.64" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="208.28" y="95.44" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C1" gate="G$1" x="50.8" y="72.39" smashed="yes">
              <attribute name="NAME" x="48.26" y="74.59" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="48.26" y="68.79" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C2" gate="G$1" x="129.54" y="72.39" smashed="yes">
              <attribute name="NAME" x="126.99999999999999" y="74.59" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="126.99999999999999" y="68.79" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP1" gate="G$1" x="48.26" y="46.99" smashed="yes">
              <attribute name="NAME" x="46.989999999999995" y="48.768" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="46.989999999999995" y="44.196000000000005" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP2" gate="G$1" x="121.92" y="46.99" smashed="yes">
              <attribute name="NAME" x="120.65" y="48.768" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="120.65" y="44.196000000000005" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP3" gate="G$1" x="195.58" y="46.99" smashed="yes">
              <attribute name="NAME" x="194.31" y="48.768" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="194.31" y="44.196000000000005" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP4" gate="G$1" x="269.24" y="46.99" smashed="yes">
              <attribute name="NAME" x="267.97" y="48.768" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="267.97" y="44.196000000000005" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP5" gate="G$1" x="342.9" y="46.99" smashed="yes">
              <attribute name="NAME" x="341.63" y="48.768" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="341.63" y="44.196000000000005" size="1.27" layer="96" align="bottom-left" />
            </instance>
          </instances>
          <busses />
          <nets>
            <net name="CELL_POS" class="0">
              <segment>
                <pinref part="BT1" gate="G$1" pin="POS" />
                <wire x1="53.34" y1="220.98" x2="35.56" y2="220.98" width="0.1524" layer="91" />
                <label x="35.56" y="220.98" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="F1" gate="G$1" pin="1" />
                <wire x1="193.04" y1="220.98" x2="175.26" y2="220.98" width="0.1524" layer="91" />
                <label x="175.26" y="220.98" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R1" gate="G$1" pin="1" />
                <wire x1="45.72" y1="98.24" x2="27.94" y2="98.24" width="0.1524" layer="91" />
                <label x="27.94" y="98.24" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CELL_MID" class="0">
              <segment>
                <pinref part="BT1" gate="G$1" pin="NEG" />
                <wire x1="99.06" y1="220.98" x2="104.14" y2="220.98" width="0.1524" layer="91" />
                <label x="104.14" y="220.98" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="BT2" gate="G$1" pin="POS" />
                <wire x1="53.34" y1="193.04" x2="35.56" y2="193.04" width="0.1524" layer="91" />
                <label x="35.56" y="193.04" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R2" gate="G$1" pin="1" />
                <wire x1="124.46" y1="98.24" x2="106.68" y2="98.24" width="0.1524" layer="91" />
                <label x="106.68" y="98.24" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP3" gate="G$1" pin="1" />
                <wire x1="190.50" y1="46.99" x2="172.72" y2="46.99" width="0.1524" layer="91" />
                <label x="172.72" y="46.99" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CELL_NEG" class="0">
              <segment>
                <pinref part="BT2" gate="G$1" pin="NEG" />
                <wire x1="99.06" y1="193.04" x2="104.14" y2="193.04" width="0.1524" layer="91" />
                <label x="104.14" y="193.04" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U2" gate="G$1" pin="VSS" />
                <wire x1="53.34" y1="134.62" x2="35.56" y2="134.62" width="0.1524" layer="91" />
                <label x="35.56" y="134.62" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="Q1" gate="G$1" pin="S1" />
                <wire x1="175.26" y1="137.16" x2="157.48" y2="137.16" width="0.1524" layer="91" />
                <label x="157.48" y="137.16" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C1" gate="G$1" pin="2" />
                <wire x1="55.88" y1="72.39" x2="60.96" y2="72.39" width="0.1524" layer="91" />
                <label x="60.96" y="72.39" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C2" gate="G$1" pin="2" />
                <wire x1="134.62" y1="72.39" x2="139.70" y2="72.39" width="0.1524" layer="91" />
                <label x="139.70" y="72.39" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="PACK+_PROT" class="0">
              <segment>
                <pinref part="F1" gate="G$1" pin="2" />
                <wire x1="203.20" y1="220.98" x2="208.28" y2="220.98" width="0.1524" layer="91" />
                <label x="208.28" y="220.98" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J2" gate="G$1" pin="POS" />
                <wire x1="296.19" y1="220.98" x2="278.41" y2="220.98" width="0.1524" layer="91" />
                <label x="278.41" y="220.98" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP1" gate="G$1" pin="1" />
                <wire x1="43.18" y1="46.99" x2="25.40" y2="46.99" width="0.1524" layer="91" />
                <label x="25.40" y="46.99" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="PACK-_PROT" class="0">
              <segment>
                <pinref part="J2" gate="G$1" pin="NEG" />
                <wire x1="341.91" y1="220.98" x2="346.99" y2="220.98" width="0.1524" layer="91" />
                <label x="346.99" y="220.98" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="RS1" gate="G$1" pin="I_PLUS" />
                <wire x1="341.91" y1="138.43" x2="346.99" y2="138.43" width="0.1524" layer="91" />
                <label x="346.99" y="138.43" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R3" gate="G$1" pin="1" />
                <wire x1="205.74" y1="98.24" x2="187.96" y2="98.24" width="0.1524" layer="91" />
                <label x="187.96" y="98.24" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP2" gate="G$1" pin="1" />
                <wire x1="116.84" y1="46.99" x2="99.06" y2="46.99" width="0.1524" layer="91" />
                <label x="99.06" y="46.99" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="PROTECT_VDD" class="0">
              <segment>
                <pinref part="U2" gate="G$1" pin="VDD" />
                <wire x1="53.34" y1="139.70" x2="35.56" y2="139.70" width="0.1524" layer="91" />
                <label x="35.56" y="139.70" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R1" gate="G$1" pin="2" />
                <wire x1="55.88" y1="98.24" x2="60.96" y2="98.24" width="0.1524" layer="91" />
                <label x="60.96" y="98.24" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C1" gate="G$1" pin="1" />
                <wire x1="45.72" y1="72.39" x2="27.94" y2="72.39" width="0.1524" layer="91" />
                <label x="27.94" y="72.39" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="PROTECT_VC" class="0">
              <segment>
                <pinref part="U2" gate="G$1" pin="VC" />
                <wire x1="53.34" y1="137.16" x2="35.56" y2="137.16" width="0.1524" layer="91" />
                <label x="35.56" y="137.16" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R2" gate="G$1" pin="2" />
                <wire x1="134.62" y1="98.24" x2="139.70" y2="98.24" width="0.1524" layer="91" />
                <label x="139.70" y="98.24" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C2" gate="G$1" pin="1" />
                <wire x1="124.46" y1="72.39" x2="106.68" y2="72.39" width="0.1524" layer="91" />
                <label x="106.68" y="72.39" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="DISCHARGE_GATE" class="0">
              <segment>
                <pinref part="U2" gate="G$1" pin="OD" />
                <wire x1="99.06" y1="139.70" x2="104.14" y2="139.70" width="0.1524" layer="91" />
                <label x="104.14" y="139.70" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="Q1" gate="G$1" pin="G1" />
                <wire x1="175.26" y1="139.70" x2="157.48" y2="139.70" width="0.1524" layer="91" />
                <label x="157.48" y="139.70" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CHARGE_GATE" class="0">
              <segment>
                <pinref part="U2" gate="G$1" pin="OC" />
                <wire x1="99.06" y1="137.16" x2="104.14" y2="137.16" width="0.1524" layer="91" />
                <label x="104.14" y="137.16" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="Q1" gate="G$1" pin="G2" />
                <wire x1="220.98" y1="138.43" x2="226.06" y2="138.43" width="0.1524" layer="91" />
                <label x="226.06" y="138.43" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="PROTECT_CS" class="0">
              <segment>
                <pinref part="U2" gate="G$1" pin="CS" />
                <wire x1="99.06" y1="134.62" x2="104.14" y2="134.62" width="0.1524" layer="91" />
                <label x="104.14" y="134.62" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R3" gate="G$1" pin="2" />
                <wire x1="215.90" y1="98.24" x2="220.98" y2="98.24" width="0.1524" layer="91" />
                <label x="220.98" y="98.24" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="FET_COMMON_DRAIN" class="0">
              <segment>
                <pinref part="Q1" gate="G$1" pin="D1_D2" />
                <wire x1="175.26" y1="134.62" x2="157.48" y2="134.62" width="0.1524" layer="91" />
                <label x="157.48" y="134.62" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SHUNT_FET_SIDE" class="0">
              <segment>
                <pinref part="Q1" gate="G$1" pin="S2" />
                <wire x1="220.98" y1="135.89" x2="226.06" y2="135.89" width="0.1524" layer="91" />
                <label x="226.06" y="135.89" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="RS1" gate="G$1" pin="I_MINUS" />
                <wire x1="296.19" y1="138.43" x2="278.41" y2="138.43" width="0.1524" layer="91" />
                <label x="278.41" y="138.43" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SHUNT_K-" class="0">
              <segment>
                <pinref part="RS1" gate="G$1" pin="S_MINUS" />
                <wire x1="296.19" y1="135.89" x2="278.41" y2="135.89" width="0.1524" layer="91" />
                <label x="278.41" y="135.89" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP4" gate="G$1" pin="1" />
                <wire x1="264.16" y1="46.99" x2="246.38" y2="46.99" width="0.1524" layer="91" />
                <label x="246.38" y="46.99" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SHUNT_K+" class="0">
              <segment>
                <pinref part="RS1" gate="G$1" pin="S_PLUS" />
                <wire x1="341.91" y1="135.89" x2="346.99" y2="135.89" width="0.1524" layer="91" />
                <label x="346.99" y="135.89" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP5" gate="G$1" pin="1" />
                <wire x1="337.82" y1="46.99" x2="320.04" y2="46.99" width="0.1524" layer="91" />
                <label x="320.04" y="46.99" size="1.016" layer="95" />
              </segment>
            </net>
          </nets>
        </sheet>
        <sheet>
          <plain>
            <text x="15.24" y="281.94" size="2.54" layer="94">FRIDAY / SCH-4a / 2S BOOST CHARGER AND INTEGRATED BALANCE</text>
            <text x="15.24" y="274.32" size="1.78" layer="94">Injoinic IP2326 V1.6 pp. 2, 9-15 | Fixed 5 V source | 8.4 V and 0.20 A nominal</text>
            <text x="15.24" y="58.42" size="1.78" layer="94">U1 VSET / CON_SEL open: 8.4 V nominal / 2S. OVSET open: 8.75 V internal backup.</text>
            <text x="15.24" y="33.02" size="1.78" layer="94">U1 DM / DP open for fixed 5 V. Right USB data stays on the compute board.</text>
          </plain>
          <instances>
            <instance part="FRAME2" gate="G$1" x="0" y="0" smashed="yes" />
            <instance part="U1" gate="G$1" x="146.05" y="179.07" smashed="yes">
              <attribute name="NAME" x="128.27" y="198.12" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="128.27" y="158.75" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="Q2" gate="G$1" x="270.51" y="126.43" smashed="yes">
              <attribute name="NAME" x="252.73" y="132.78" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="252.73" y="118.81" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R4" gate="G$1" x="55.88" y="226.06" smashed="yes">
              <attribute name="NAME" x="53.34" y="227.46" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="53.34" y="223.26" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R5" gate="G$1" x="55.88" y="165.1" smashed="yes">
              <attribute name="NAME" x="53.34" y="166.5" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="53.34" y="162.29999999999998" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R6" gate="G$1" x="55.88" y="139.7" smashed="yes">
              <attribute name="NAME" x="53.34" y="141.1" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="53.34" y="136.89999999999998" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R7" gate="G$1" x="55.88" y="114.3" smashed="yes">
              <attribute name="NAME" x="53.34" y="115.7" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="53.34" y="111.5" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R8" gate="G$1" x="55.88" y="76.2" smashed="yes">
              <attribute name="NAME" x="53.34" y="77.60000000000001" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="53.34" y="73.4" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R9" gate="G$1" x="228.6" y="86.36" smashed="yes">
              <attribute name="NAME" x="226.06" y="87.76" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="226.06" y="83.56" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R10" gate="G$1" x="302.26" y="86.36" smashed="yes">
              <attribute name="NAME" x="299.71999999999997" y="87.76" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="299.71999999999997" y="83.56" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R11" gate="G$1" x="363.22" y="126.43" smashed="yes">
              <attribute name="NAME" x="360.68" y="128.97" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="360.68" y="122.62" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TH1" gate="G$1" x="139.7" y="76.2" smashed="yes">
              <attribute name="NAME" x="137.16" y="78.74000000000001" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="137.16" y="72.39" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="L1" gate="G$1" x="157.48" y="226.06" smashed="yes">
              <attribute name="NAME" x="154.94" y="228.6" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="154.94" y="222.25" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C3" gate="G$1" x="53.34" y="251.46" smashed="yes">
              <attribute name="NAME" x="50.800000000000004" y="254.0" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="50.800000000000004" y="247.65" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C4" gate="G$1" x="153.67" y="251.46" smashed="yes">
              <attribute name="NAME" x="151.13" y="254.0" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="151.13" y="247.65" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C5" gate="G$1" x="245.11" y="251.46" smashed="yes">
              <attribute name="NAME" x="242.57000000000002" y="253.66" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="242.57000000000002" y="247.86" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C6" gate="G$1" x="238.76" y="226.06" smashed="yes">
              <attribute name="NAME" x="236.22" y="228.6" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="236.22" y="222.25" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C7" gate="G$1" x="331.47" y="226.06" smashed="yes">
              <attribute name="NAME" x="328.93" y="228.6" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="328.93" y="222.25" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C8" gate="G$1" x="238.76" y="199.39" smashed="yes">
              <attribute name="NAME" x="236.22" y="201.92999999999998" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="236.22" y="195.57999999999998" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C9" gate="G$1" x="331.47" y="199.39" smashed="yes">
              <attribute name="NAME" x="328.93" y="201.92999999999998" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="328.93" y="195.57999999999998" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C10" gate="G$1" x="238.76" y="171.45" smashed="yes">
              <attribute name="NAME" x="236.22" y="173.64999999999998" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="236.22" y="167.85" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C11" gate="G$1" x="331.47" y="171.45" smashed="yes">
              <attribute name="NAME" x="328.93" y="173.64999999999998" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="328.93" y="167.85" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP7" gate="G$1" x="157.48" y="45.72" smashed="yes">
              <attribute name="NAME" x="156.20999999999998" y="47.498" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="156.20999999999998" y="42.926" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP8" gate="G$1" x="80.01" y="45.72" smashed="yes">
              <attribute name="NAME" x="78.74000000000001" y="47.498" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="78.74000000000001" y="42.926" size="1.27" layer="96" align="bottom-left" />
            </instance>
          </instances>
          <busses />
          <nets>
            <net name="CHARGER_VIN" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="VIN" />
                <wire x1="123.19" y1="193.04" x2="105.41" y2="193.04" width="0.1524" layer="91" />
                <label x="105.41" y="193.04" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R4" gate="G$1" pin="2" />
                <wire x1="60.96" y1="226.06" x2="66.04" y2="226.06" width="0.1524" layer="91" />
                <label x="66.04" y="226.06" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C4" gate="G$1" pin="1" />
                <wire x1="148.59" y1="251.46" x2="130.81" y2="251.46" width="0.1524" layer="91" />
                <label x="130.81" y="251.46" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CHARGER_RUN" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="EN" />
                <wire x1="123.19" y1="190.50" x2="105.41" y2="190.50" width="0.1524" layer="91" />
                <label x="105.41" y="190.50" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CHARGER_ISET" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="ISET" />
                <wire x1="123.19" y1="187.96" x2="105.41" y2="187.96" width="0.1524" layer="91" />
                <label x="105.41" y="187.96" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R5" gate="G$1" pin="1" />
                <wire x1="50.80" y1="165.10" x2="33.02" y2="165.10" width="0.1524" layer="91" />
                <label x="33.02" y="165.10" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CHARGER_TIME" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="TIME_SET" />
                <wire x1="123.19" y1="180.34" x2="105.41" y2="180.34" width="0.1524" layer="91" />
                <label x="105.41" y="180.34" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R6" gate="G$1" pin="1" />
                <wire x1="50.80" y1="139.70" x2="33.02" y2="139.70" width="0.1524" layer="91" />
                <label x="33.02" y="139.70" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CHARGER_UVSET" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="VIN_UVSET" />
                <wire x1="123.19" y1="177.80" x2="105.41" y2="177.80" width="0.1524" layer="91" />
                <label x="105.41" y="177.80" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R7" gate="G$1" pin="1" />
                <wire x1="50.80" y1="114.30" x2="33.02" y2="114.30" width="0.1524" layer="91" />
                <label x="33.02" y="114.30" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CHARGER_NTC" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="NTC" />
                <wire x1="123.19" y1="172.72" x2="105.41" y2="172.72" width="0.1524" layer="91" />
                <label x="105.41" y="172.72" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R8" gate="G$1" pin="1" />
                <wire x1="50.80" y1="76.20" x2="33.02" y2="76.20" width="0.1524" layer="91" />
                <label x="33.02" y="76.20" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TH1" gate="G$1" pin="1" />
                <wire x1="134.62" y1="76.20" x2="116.84" y2="76.20" width="0.1524" layer="91" />
                <label x="116.84" y="76.20" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP8" gate="G$1" pin="1" />
                <wire x1="74.93" y1="45.72" x2="57.15" y2="45.72" width="0.1524" layer="91" />
                <label x="57.15" y="45.72" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CHARGER_BST" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="BST" />
                <wire x1="168.91" y1="189.23" x2="173.99" y2="189.23" width="0.1524" layer="91" />
                <label x="173.99" y="189.23" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C5" gate="G$1" pin="1" />
                <wire x1="240.03" y1="251.46" x2="222.25" y2="251.46" width="0.1524" layer="91" />
                <label x="222.25" y="251.46" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CHARGER_SW" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="LX" />
                <wire x1="168.91" y1="186.69" x2="173.99" y2="186.69" width="0.1524" layer="91" />
                <label x="173.99" y="186.69" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="L1" gate="G$1" pin="2" />
                <wire x1="162.56" y1="226.06" x2="167.64" y2="226.06" width="0.1524" layer="91" />
                <label x="167.64" y="226.06" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C5" gate="G$1" pin="2" />
                <wire x1="250.19" y1="251.46" x2="255.27" y2="251.46" width="0.1524" layer="91" />
                <label x="255.27" y="251.46" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP7" gate="G$1" pin="1" />
                <wire x1="152.40" y1="45.72" x2="134.62" y2="45.72" width="0.1524" layer="91" />
                <label x="134.62" y="45.72" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CHARGER_VSYS" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="VSYS" />
                <wire x1="168.91" y1="184.15" x2="173.99" y2="184.15" width="0.1524" layer="91" />
                <label x="173.99" y="184.15" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C6" gate="G$1" pin="1" />
                <wire x1="233.68" y1="226.06" x2="215.90" y2="226.06" width="0.1524" layer="91" />
                <label x="215.90" y="226.06" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C7" gate="G$1" pin="1" />
                <wire x1="326.39" y1="226.06" x2="308.61" y2="226.06" width="0.1524" layer="91" />
                <label x="308.61" y="226.06" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="PACK+_PROT" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="VOUT" />
                <wire x1="168.91" y1="181.61" x2="173.99" y2="181.61" width="0.1524" layer="91" />
                <label x="173.99" y="181.61" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C8" gate="G$1" pin="1" />
                <wire x1="233.68" y1="199.39" x2="215.90" y2="199.39" width="0.1524" layer="91" />
                <label x="215.90" y="199.39" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C9" gate="G$1" pin="1" />
                <wire x1="326.39" y1="199.39" x2="308.61" y2="199.39" width="0.1524" layer="91" />
                <label x="308.61" y="199.39" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C10" gate="G$1" pin="1" />
                <wire x1="233.68" y1="171.45" x2="215.90" y2="171.45" width="0.1524" layer="91" />
                <label x="215.90" y="171.45" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CHARGER_VBATM" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="VBATM" />
                <wire x1="168.91" y1="179.07" x2="173.99" y2="179.07" width="0.1524" layer="91" />
                <label x="173.99" y="179.07" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R11" gate="G$1" pin="2" />
                <wire x1="368.30" y1="126.43" x2="373.38" y2="126.43" width="0.1524" layer="91" />
                <label x="373.38" y="126.43" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C11" gate="G$1" pin="1" />
                <wire x1="326.39" y1="171.45" x2="308.61" y2="171.45" width="0.1524" layer="91" />
                <label x="308.61" y="171.45" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="PACK-_PROT" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="VBAT_GND" />
                <wire x1="168.91" y1="176.53" x2="173.99" y2="176.53" width="0.1524" layer="91" />
                <label x="173.99" y="176.53" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U1" gate="G$1" pin="PGND" />
                <wire x1="168.91" y1="173.99" x2="173.99" y2="173.99" width="0.1524" layer="91" />
                <label x="173.99" y="173.99" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U1" gate="G$1" pin="EP" />
                <wire x1="168.91" y1="171.45" x2="173.99" y2="171.45" width="0.1524" layer="91" />
                <label x="173.99" y="171.45" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R5" gate="G$1" pin="2" />
                <wire x1="60.96" y1="165.10" x2="66.04" y2="165.10" width="0.1524" layer="91" />
                <label x="66.04" y="165.10" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R6" gate="G$1" pin="2" />
                <wire x1="60.96" y1="139.70" x2="66.04" y2="139.70" width="0.1524" layer="91" />
                <label x="66.04" y="139.70" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R7" gate="G$1" pin="2" />
                <wire x1="60.96" y1="114.30" x2="66.04" y2="114.30" width="0.1524" layer="91" />
                <label x="66.04" y="114.30" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R8" gate="G$1" pin="2" />
                <wire x1="60.96" y1="76.20" x2="66.04" y2="76.20" width="0.1524" layer="91" />
                <label x="66.04" y="76.20" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R9" gate="G$1" pin="2" />
                <wire x1="233.68" y1="86.36" x2="238.76" y2="86.36" width="0.1524" layer="91" />
                <label x="238.76" y="86.36" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TH1" gate="G$1" pin="2" />
                <wire x1="144.78" y1="76.20" x2="149.86" y2="76.20" width="0.1524" layer="91" />
                <label x="149.86" y="76.20" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C3" gate="G$1" pin="2" />
                <wire x1="58.42" y1="251.46" x2="63.50" y2="251.46" width="0.1524" layer="91" />
                <label x="63.50" y="251.46" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C4" gate="G$1" pin="2" />
                <wire x1="158.75" y1="251.46" x2="163.83" y2="251.46" width="0.1524" layer="91" />
                <label x="163.83" y="251.46" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C6" gate="G$1" pin="2" />
                <wire x1="243.84" y1="226.06" x2="248.92" y2="226.06" width="0.1524" layer="91" />
                <label x="248.92" y="226.06" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C7" gate="G$1" pin="2" />
                <wire x1="336.55" y1="226.06" x2="341.63" y2="226.06" width="0.1524" layer="91" />
                <label x="341.63" y="226.06" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C8" gate="G$1" pin="2" />
                <wire x1="243.84" y1="199.39" x2="248.92" y2="199.39" width="0.1524" layer="91" />
                <label x="248.92" y="199.39" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C9" gate="G$1" pin="2" />
                <wire x1="336.55" y1="199.39" x2="341.63" y2="199.39" width="0.1524" layer="91" />
                <label x="341.63" y="199.39" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C10" gate="G$1" pin="2" />
                <wire x1="243.84" y1="171.45" x2="248.92" y2="171.45" width="0.1524" layer="91" />
                <label x="248.92" y="171.45" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C11" gate="G$1" pin="2" />
                <wire x1="336.55" y1="171.45" x2="341.63" y2="171.45" width="0.1524" layer="91" />
                <label x="341.63" y="171.45" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CHARGER_BAT_STAT" class="0">
              <segment>
                <pinref part="U1" gate="G$1" pin="BAT_STAT" />
                <wire x1="168.91" y1="168.91" x2="173.99" y2="168.91" width="0.1524" layer="91" />
                <label x="173.99" y="168.91" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CELL_MID" class="0">
              <segment>
                <pinref part="Q2" gate="G$1" pin="D" />
                <wire x1="247.65" y1="127.70" x2="229.87" y2="127.70" width="0.1524" layer="91" />
                <label x="229.87" y="127.70" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="MIDPOINT_SWITCHED" class="0">
              <segment>
                <pinref part="Q2" gate="G$1" pin="S" />
                <wire x1="293.37" y1="126.43" x2="298.45" y2="126.43" width="0.1524" layer="91" />
                <label x="298.45" y="126.43" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R10" gate="G$1" pin="2" />
                <wire x1="307.34" y1="86.36" x2="312.42" y2="86.36" width="0.1524" layer="91" />
                <label x="312.42" y="86.36" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R11" gate="G$1" pin="1" />
                <wire x1="358.14" y1="126.43" x2="340.36" y2="126.43" width="0.1524" layer="91" />
                <label x="340.36" y="126.43" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="BALANCE_GATE" class="0">
              <segment>
                <pinref part="Q2" gate="G$1" pin="G" />
                <wire x1="247.65" y1="125.16" x2="229.87" y2="125.16" width="0.1524" layer="91" />
                <label x="229.87" y="125.16" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R9" gate="G$1" pin="1" />
                <wire x1="223.52" y1="86.36" x2="205.74" y2="86.36" width="0.1524" layer="91" />
                <label x="205.74" y="86.36" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R10" gate="G$1" pin="1" />
                <wire x1="297.18" y1="86.36" x2="279.40" y2="86.36" width="0.1524" layer="91" />
                <label x="279.40" y="86.36" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="VBUS_OR" class="0">
              <segment>
                <pinref part="R4" gate="G$1" pin="1" />
                <wire x1="50.80" y1="226.06" x2="33.02" y2="226.06" width="0.1524" layer="91" />
                <label x="33.02" y="226.06" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="L1" gate="G$1" pin="1" />
                <wire x1="152.40" y1="226.06" x2="134.62" y2="226.06" width="0.1524" layer="91" />
                <label x="134.62" y="226.06" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C3" gate="G$1" pin="1" />
                <wire x1="48.26" y1="251.46" x2="30.48" y2="251.46" width="0.1524" layer="91" />
                <label x="30.48" y="251.46" size="1.016" layer="95" />
              </segment>
            </net>
          </nets>
        </sheet>
        <sheet>
          <plain>
            <text x="15.24" y="281.94" size="2.54" layer="94">FRIDAY / SCH-4a / POGO AND USB INPUT OR</text>
            <text x="15.24" y="274.32" size="1.78" layer="94">D16 | Two independent reverse-blocking eFuses | Each branch has TVS, UVLO, OVLO and current limit</text>
            <text x="16.51" y="259.08" size="1.78" layer="94">J1 top view pin 1 VBUS, pin 2 protected GND, pin 3 DET. Dock is the source for VBUS and DET.</text>
            <text x="16.51" y="208.28" size="1.78" layer="94">U3 and U4 outputs join at VBUS_OR. Their always-on reverse blockers oppose flow toward either input.</text>
          </plain>
          <instances>
            <instance part="FRAME3" gate="G$1" x="0" y="0" smashed="yes" />
            <instance part="J1" gate="G$1" x="76.2" y="237.49" smashed="yes">
              <attribute name="NAME" x="58.42" y="245.11" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="58.42" y="228.60000000000002" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="U3" gate="G$1" x="180.34" y="164.08" smashed="yes">
              <attribute name="NAME" x="162.56" y="174.24" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="162.56" y="152.65" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R12" gate="G$1" x="55.88" y="176.78" smashed="yes">
              <attribute name="NAME" x="53.34" y="178.18" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="53.34" y="173.98" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R13" gate="G$1" x="55.88" y="153.92000000000002" smashed="yes">
              <attribute name="NAME" x="53.34" y="155.32000000000002" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="53.34" y="151.12" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R14" gate="G$1" x="298.45" y="188.21" smashed="yes">
              <attribute name="NAME" x="295.90999999999997" y="189.61" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="295.90999999999997" y="185.41" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R15" gate="G$1" x="298.45" y="166.62" smashed="yes">
              <attribute name="NAME" x="295.90999999999997" y="168.02" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="295.90999999999997" y="163.82" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R16" gate="G$1" x="298.45" y="143.76000000000002" smashed="yes">
              <attribute name="NAME" x="295.90999999999997" y="145.16000000000003" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="295.90999999999997" y="140.96" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="D1" gate="G$1" x="55.88" y="131.06" smashed="yes">
              <attribute name="NAME" x="53.34" y="133.6" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="53.34" y="127.25" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C12" gate="G$1" x="182.88" y="131.06" smashed="yes">
              <attribute name="NAME" x="180.34" y="133.26" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="180.34" y="127.46000000000001" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C13" gate="G$1" x="298.45" y="125.98000000000002" smashed="yes">
              <attribute name="NAME" x="295.90999999999997" y="128.18" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="295.90999999999997" y="122.38000000000002" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="U4" gate="G$1" x="180.34" y="77.47" smashed="yes">
              <attribute name="NAME" x="162.56" y="87.63" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="162.56" y="66.03999999999999" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R17" gate="G$1" x="55.88" y="90.17" smashed="yes">
              <attribute name="NAME" x="53.34" y="91.57000000000001" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="53.34" y="87.37" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R18" gate="G$1" x="55.88" y="67.31" smashed="yes">
              <attribute name="NAME" x="53.34" y="68.71000000000001" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="53.34" y="64.51" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R19" gate="G$1" x="298.45" y="101.6" smashed="yes">
              <attribute name="NAME" x="295.90999999999997" y="103.0" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="295.90999999999997" y="98.8" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R20" gate="G$1" x="298.45" y="80.01" smashed="yes">
              <attribute name="NAME" x="295.90999999999997" y="81.41000000000001" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="295.90999999999997" y="77.21000000000001" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R21" gate="G$1" x="298.45" y="57.15" smashed="yes">
              <attribute name="NAME" x="295.90999999999997" y="58.55" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="295.90999999999997" y="54.35" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="D2" gate="G$1" x="55.88" y="44.449999999999996" smashed="yes">
              <attribute name="NAME" x="53.34" y="46.989999999999995" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="53.34" y="40.63999999999999" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C14" gate="G$1" x="182.88" y="44.449999999999996" smashed="yes">
              <attribute name="NAME" x="180.34" y="46.65" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="180.34" y="40.849999999999994" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C15" gate="G$1" x="298.45" y="39.37" smashed="yes">
              <attribute name="NAME" x="295.90999999999997" y="41.57" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="295.90999999999997" y="35.769999999999996" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="TP6" gate="G$1" x="298.45" y="237.49" smashed="yes">
              <attribute name="NAME" x="297.18" y="239.268" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="297.18" y="234.696" size="1.27" layer="96" align="bottom-left" />
            </instance>
          </instances>
          <busses />
          <nets>
            <net name="POGO_VBUS_IN" class="0">
              <segment>
                <pinref part="J1" gate="G$1" pin="VBUS" />
                <wire x1="53.34" y1="240.03" x2="35.56" y2="240.03" width="0.1524" layer="91" />
                <label x="35.56" y="240.03" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U3" gate="G$1" pin="IN" />
                <wire x1="157.48" y1="169.16" x2="139.70" y2="169.16" width="0.1524" layer="91" />
                <label x="139.70" y="169.16" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R12" gate="G$1" pin="1" />
                <wire x1="50.80" y1="176.78" x2="33.02" y2="176.78" width="0.1524" layer="91" />
                <label x="33.02" y="176.78" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R14" gate="G$1" pin="1" />
                <wire x1="293.37" y1="188.21" x2="275.59" y2="188.21" width="0.1524" layer="91" />
                <label x="275.59" y="188.21" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="D1" gate="G$1" pin="K" />
                <wire x1="50.80" y1="131.06" x2="33.02" y2="131.06" width="0.1524" layer="91" />
                <label x="33.02" y="131.06" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C12" gate="G$1" pin="1" />
                <wire x1="177.80" y1="131.06" x2="160.02" y2="131.06" width="0.1524" layer="91" />
                <label x="160.02" y="131.06" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="PACK-_PROT" class="0">
              <segment>
                <pinref part="J1" gate="G$1" pin="GND" />
                <wire x1="53.34" y1="237.49" x2="35.56" y2="237.49" width="0.1524" layer="91" />
                <label x="35.56" y="237.49" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U3" gate="G$1" pin="GND" />
                <wire x1="157.48" y1="161.54" x2="139.70" y2="161.54" width="0.1524" layer="91" />
                <label x="139.70" y="161.54" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R13" gate="G$1" pin="2" />
                <wire x1="60.96" y1="153.92" x2="66.04" y2="153.92" width="0.1524" layer="91" />
                <label x="66.04" y="153.92" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R15" gate="G$1" pin="2" />
                <wire x1="303.53" y1="166.62" x2="308.61" y2="166.62" width="0.1524" layer="91" />
                <label x="308.61" y="166.62" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R16" gate="G$1" pin="2" />
                <wire x1="303.53" y1="143.76" x2="308.61" y2="143.76" width="0.1524" layer="91" />
                <label x="308.61" y="143.76" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="D1" gate="G$1" pin="A" />
                <wire x1="60.96" y1="131.06" x2="66.04" y2="131.06" width="0.1524" layer="91" />
                <label x="66.04" y="131.06" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C12" gate="G$1" pin="2" />
                <wire x1="187.96" y1="131.06" x2="193.04" y2="131.06" width="0.1524" layer="91" />
                <label x="193.04" y="131.06" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C13" gate="G$1" pin="2" />
                <wire x1="303.53" y1="125.98" x2="308.61" y2="125.98" width="0.1524" layer="91" />
                <label x="308.61" y="125.98" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U4" gate="G$1" pin="GND" />
                <wire x1="157.48" y1="74.93" x2="139.70" y2="74.93" width="0.1524" layer="91" />
                <label x="139.70" y="74.93" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R18" gate="G$1" pin="2" />
                <wire x1="60.96" y1="67.31" x2="66.04" y2="67.31" width="0.1524" layer="91" />
                <label x="66.04" y="67.31" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R20" gate="G$1" pin="2" />
                <wire x1="303.53" y1="80.01" x2="308.61" y2="80.01" width="0.1524" layer="91" />
                <label x="308.61" y="80.01" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R21" gate="G$1" pin="2" />
                <wire x1="303.53" y1="57.15" x2="308.61" y2="57.15" width="0.1524" layer="91" />
                <label x="308.61" y="57.15" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="D2" gate="G$1" pin="A" />
                <wire x1="60.96" y1="44.45" x2="66.04" y2="44.45" width="0.1524" layer="91" />
                <label x="66.04" y="44.45" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C14" gate="G$1" pin="2" />
                <wire x1="187.96" y1="44.45" x2="193.04" y2="44.45" width="0.1524" layer="91" />
                <label x="193.04" y="44.45" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C15" gate="G$1" pin="2" />
                <wire x1="303.53" y1="39.37" x2="308.61" y2="39.37" width="0.1524" layer="91" />
                <label x="308.61" y="39.37" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="POGO_DET_RAW" class="0">
              <segment>
                <pinref part="J1" gate="G$1" pin="DET" />
                <wire x1="53.34" y1="234.95" x2="35.56" y2="234.95" width="0.1524" layer="91" />
                <label x="35.56" y="234.95" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="VBUS_OR" class="0">
              <segment>
                <pinref part="U3" gate="G$1" pin="OUT" />
                <wire x1="203.20" y1="169.16" x2="208.28" y2="169.16" width="0.1524" layer="91" />
                <label x="208.28" y="169.16" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U4" gate="G$1" pin="OUT" />
                <wire x1="203.20" y1="82.55" x2="208.28" y2="82.55" width="0.1524" layer="91" />
                <label x="208.28" y="82.55" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="TP6" gate="G$1" pin="1" />
                <wire x1="293.37" y1="237.49" x2="275.59" y2="237.49" width="0.1524" layer="91" />
                <label x="275.59" y="237.49" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="POGO_UVLO" class="0">
              <segment>
                <pinref part="U3" gate="G$1" pin="EN_UVLO" />
                <wire x1="157.48" y1="166.62" x2="139.70" y2="166.62" width="0.1524" layer="91" />
                <label x="139.70" y="166.62" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R12" gate="G$1" pin="2" />
                <wire x1="60.96" y1="176.78" x2="66.04" y2="176.78" width="0.1524" layer="91" />
                <label x="66.04" y="176.78" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R13" gate="G$1" pin="1" />
                <wire x1="50.80" y1="153.92" x2="33.02" y2="153.92" width="0.1524" layer="91" />
                <label x="33.02" y="153.92" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="POGO_OVLO" class="0">
              <segment>
                <pinref part="U3" gate="G$1" pin="OVLO" />
                <wire x1="157.48" y1="164.08" x2="139.70" y2="164.08" width="0.1524" layer="91" />
                <label x="139.70" y="164.08" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R14" gate="G$1" pin="2" />
                <wire x1="303.53" y1="188.21" x2="308.61" y2="188.21" width="0.1524" layer="91" />
                <label x="308.61" y="188.21" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R15" gate="G$1" pin="1" />
                <wire x1="293.37" y1="166.62" x2="275.59" y2="166.62" width="0.1524" layer="91" />
                <label x="275.59" y="166.62" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="POGO_DVDT" class="0">
              <segment>
                <pinref part="U3" gate="G$1" pin="DVDT" />
                <wire x1="203.20" y1="164.08" x2="208.28" y2="164.08" width="0.1524" layer="91" />
                <label x="208.28" y="164.08" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C13" gate="G$1" pin="1" />
                <wire x1="293.37" y1="125.98" x2="275.59" y2="125.98" width="0.1524" layer="91" />
                <label x="275.59" y="125.98" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="POGO_ILM" class="0">
              <segment>
                <pinref part="U3" gate="G$1" pin="ILM" />
                <wire x1="203.20" y1="166.62" x2="208.28" y2="166.62" width="0.1524" layer="91" />
                <label x="208.28" y="166.62" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R16" gate="G$1" pin="1" />
                <wire x1="293.37" y1="143.76" x2="275.59" y2="143.76" width="0.1524" layer="91" />
                <label x="275.59" y="143.76" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="VBUS_5V_CHG" class="0">
              <segment>
                <pinref part="U4" gate="G$1" pin="IN" />
                <wire x1="157.48" y1="82.55" x2="139.70" y2="82.55" width="0.1524" layer="91" />
                <label x="139.70" y="82.55" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R17" gate="G$1" pin="1" />
                <wire x1="50.80" y1="90.17" x2="33.02" y2="90.17" width="0.1524" layer="91" />
                <label x="33.02" y="90.17" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R19" gate="G$1" pin="1" />
                <wire x1="293.37" y1="101.60" x2="275.59" y2="101.60" width="0.1524" layer="91" />
                <label x="275.59" y="101.60" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="D2" gate="G$1" pin="K" />
                <wire x1="50.80" y1="44.45" x2="33.02" y2="44.45" width="0.1524" layer="91" />
                <label x="33.02" y="44.45" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C14" gate="G$1" pin="1" />
                <wire x1="177.80" y1="44.45" x2="160.02" y2="44.45" width="0.1524" layer="91" />
                <label x="160.02" y="44.45" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="USB_UVLO" class="0">
              <segment>
                <pinref part="U4" gate="G$1" pin="EN_UVLO" />
                <wire x1="157.48" y1="80.01" x2="139.70" y2="80.01" width="0.1524" layer="91" />
                <label x="139.70" y="80.01" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R17" gate="G$1" pin="2" />
                <wire x1="60.96" y1="90.17" x2="66.04" y2="90.17" width="0.1524" layer="91" />
                <label x="66.04" y="90.17" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R18" gate="G$1" pin="1" />
                <wire x1="50.80" y1="67.31" x2="33.02" y2="67.31" width="0.1524" layer="91" />
                <label x="33.02" y="67.31" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="USB_OVLO" class="0">
              <segment>
                <pinref part="U4" gate="G$1" pin="OVLO" />
                <wire x1="157.48" y1="77.47" x2="139.70" y2="77.47" width="0.1524" layer="91" />
                <label x="139.70" y="77.47" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R19" gate="G$1" pin="2" />
                <wire x1="303.53" y1="101.60" x2="308.61" y2="101.60" width="0.1524" layer="91" />
                <label x="308.61" y="101.60" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R20" gate="G$1" pin="1" />
                <wire x1="293.37" y1="80.01" x2="275.59" y2="80.01" width="0.1524" layer="91" />
                <label x="275.59" y="80.01" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="USB_DVDT" class="0">
              <segment>
                <pinref part="U4" gate="G$1" pin="DVDT" />
                <wire x1="203.20" y1="77.47" x2="208.28" y2="77.47" width="0.1524" layer="91" />
                <label x="208.28" y="77.47" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C15" gate="G$1" pin="1" />
                <wire x1="293.37" y1="39.37" x2="275.59" y2="39.37" width="0.1524" layer="91" />
                <label x="275.59" y="39.37" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="USB_ILM" class="0">
              <segment>
                <pinref part="U4" gate="G$1" pin="ILM" />
                <wire x1="203.20" y1="80.01" x2="208.28" y2="80.01" width="0.1524" layer="91" />
                <label x="208.28" y="80.01" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R21" gate="G$1" pin="1" />
                <wire x1="293.37" y1="57.15" x2="275.59" y2="57.15" width="0.1524" layer="91" />
                <label x="275.59" y="57.15" size="1.016" layer="95" />
              </segment>
            </net>
          </nets>
        </sheet>
        <sheet>
          <plain>
            <text x="15.24" y="281.94" size="2.54" layer="94">FRIDAY / SCH-4a / AUXILIARY FLEX AND 1.8 V CONTROL</text>
            <text x="15.24" y="274.32" size="1.78" layer="94">Existing audio assignments pass through the interface. Audio circuitry is in SCH-4b.</text>
            <text x="15.24" y="254.0" size="1.78" layer="94">J3 pin 1 as marked at the contact row. Fit pin 1 to pin 1 with the contact side per the interconnect drawing.</text>
            <text x="15.24" y="246.38" size="1.78" layer="94">Right pulls DOCK_DET and CHG_STAT to VCCIO7 1.8 V. Both left outputs are open drain.</text>
            <text x="15.24" y="45.72" size="1.78" layer="94">CHG_EN low requests charge. An unpowered or unplugged right side defaults to local charging.</text>
            <text x="15.24" y="38.1" size="1.78" layer="94">AUX and pogo ground join only PACK-_PROT. PACK- harness stays the main load-current return.</text>
          </plain>
          <instances>
            <instance part="FRAME4" gate="G$1" x="0" y="0" smashed="yes" />
            <instance part="J3" gate="G$1" x="95.25" y="161.29" smashed="yes">
              <attribute name="NAME" x="90.17" y="197.4017" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="90.17" y="125.66219999999998" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="Q3" gate="G$1" x="269.24" y="200.66" smashed="yes">
              <attribute name="NAME" x="251.46" y="207.01" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="251.46" y="193.04" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R22" gate="G$1" x="185.42" y="212.09" smashed="yes">
              <attribute name="NAME" x="182.88" y="213.49" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="182.88" y="209.29" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R23" gate="G$1" x="185.42" y="189.23" smashed="yes">
              <attribute name="NAME" x="182.88" y="190.63" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="182.88" y="186.42999999999998" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="Q4" gate="G$1" x="269.24" y="139.7" smashed="yes">
              <attribute name="NAME" x="251.46" y="146.04999999999998" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="251.46" y="132.07999999999998" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R24" gate="G$1" x="185.42" y="151.13" smashed="yes">
              <attribute name="NAME" x="182.88" y="152.53" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="182.88" y="148.32999999999998" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R25" gate="G$1" x="185.42" y="128.26999999999998" smashed="yes">
              <attribute name="NAME" x="182.88" y="129.67" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="182.88" y="125.46999999999998" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="Q5" gate="G$1" x="269.24" y="78.74" smashed="yes">
              <attribute name="NAME" x="251.46" y="85.08999999999999" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="251.46" y="71.11999999999999" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R26" gate="G$1" x="185.42" y="90.16999999999999" smashed="yes">
              <attribute name="NAME" x="182.88" y="91.57" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="182.88" y="87.36999999999999" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R27" gate="G$1" x="185.42" y="67.31" smashed="yes">
              <attribute name="NAME" x="182.88" y="68.71000000000001" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="182.88" y="64.51" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R28" gate="G$1" x="342.9" y="78.74" smashed="yes">
              <attribute name="NAME" x="340.35999999999996" y="80.14" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="340.35999999999996" y="75.94" size="1.27" layer="96" align="bottom-left" />
            </instance>
          </instances>
          <busses />
          <nets>
            <net name="PACK-_PROT" class="0">
              <segment>
                <pinref part="J3" gate="G$1" pin="1" />
                <wire x1="85.09" y1="194.31" x2="67.31" y2="194.31" width="0.1524" layer="91" />
                <label x="67.31" y="194.31" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J3" gate="G$1" pin="4" />
                <wire x1="85.09" y1="186.69" x2="67.31" y2="186.69" width="0.1524" layer="91" />
                <label x="67.31" y="186.69" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J3" gate="G$1" pin="6" />
                <wire x1="85.09" y1="181.61" x2="67.31" y2="181.61" width="0.1524" layer="91" />
                <label x="67.31" y="181.61" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J3" gate="G$1" pin="11" />
                <wire x1="85.09" y1="168.91" x2="67.31" y2="168.91" width="0.1524" layer="91" />
                <label x="67.31" y="168.91" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J3" gate="G$1" pin="14" />
                <wire x1="85.09" y1="161.29" x2="67.31" y2="161.29" width="0.1524" layer="91" />
                <label x="67.31" y="161.29" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J3" gate="G$1" pin="18" />
                <wire x1="85.09" y1="151.13" x2="67.31" y2="151.13" width="0.1524" layer="91" />
                <label x="67.31" y="151.13" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J3" gate="G$1" pin="22" />
                <wire x1="85.09" y1="140.97" x2="67.31" y2="140.97" width="0.1524" layer="91" />
                <label x="67.31" y="140.97" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J3" gate="G$1" pin="23" />
                <wire x1="85.09" y1="138.43" x2="67.31" y2="138.43" width="0.1524" layer="91" />
                <label x="67.31" y="138.43" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J3" gate="G$1" pin="24" />
                <wire x1="85.09" y1="135.89" x2="67.31" y2="135.89" width="0.1524" layer="91" />
                <label x="67.31" y="135.89" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J3" gate="G$1" pin="SHIELD" />
                <wire x1="85.09" y1="130.81" x2="67.31" y2="130.81" width="0.1524" layer="91" />
                <label x="67.31" y="130.81" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="Q3" gate="G$1" pin="S" />
                <wire x1="292.10" y1="199.39" x2="297.18" y2="199.39" width="0.1524" layer="91" />
                <label x="297.18" y="199.39" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R23" gate="G$1" pin="2" />
                <wire x1="190.50" y1="189.23" x2="195.58" y2="189.23" width="0.1524" layer="91" />
                <label x="195.58" y="189.23" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="Q4" gate="G$1" pin="S" />
                <wire x1="292.10" y1="138.43" x2="297.18" y2="138.43" width="0.1524" layer="91" />
                <label x="297.18" y="138.43" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R25" gate="G$1" pin="2" />
                <wire x1="190.50" y1="128.27" x2="195.58" y2="128.27" width="0.1524" layer="91" />
                <label x="195.58" y="128.27" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="Q5" gate="G$1" pin="S" />
                <wire x1="292.10" y1="77.47" x2="297.18" y2="77.47" width="0.1524" layer="91" />
                <label x="297.18" y="77.47" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R27" gate="G$1" pin="2" />
                <wire x1="190.50" y1="67.31" x2="195.58" y2="67.31" width="0.1524" layer="91" />
                <label x="195.58" y="67.31" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="VCC5V0_SYS_S5_AMP" class="0">
              <segment>
                <pinref part="J3" gate="G$1" pin="2" />
                <wire x1="85.09" y1="191.77" x2="67.31" y2="191.77" width="0.1524" layer="91" />
                <label x="67.31" y="191.77" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J3" gate="G$1" pin="3" />
                <wire x1="85.09" y1="189.23" x2="67.31" y2="189.23" width="0.1524" layer="91" />
                <label x="67.31" y="189.23" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SAI1_BCLK_M0" class="0">
              <segment>
                <pinref part="J3" gate="G$1" pin="5" />
                <wire x1="85.09" y1="184.15" x2="67.31" y2="184.15" width="0.1524" layer="91" />
                <label x="67.31" y="184.15" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SAI1_LRCK_M0" class="0">
              <segment>
                <pinref part="J3" gate="G$1" pin="7" />
                <wire x1="85.09" y1="179.07" x2="67.31" y2="179.07" width="0.1524" layer="91" />
                <label x="67.31" y="179.07" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SAI1_SDO0_M0" class="0">
              <segment>
                <pinref part="J3" gate="G$1" pin="8" />
                <wire x1="85.09" y1="176.53" x2="67.31" y2="176.53" width="0.1524" layer="91" />
                <label x="67.31" y="176.53" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SD_MODE_L" class="0">
              <segment>
                <pinref part="J3" gate="G$1" pin="9" />
                <wire x1="85.09" y1="173.99" x2="67.31" y2="173.99" width="0.1524" layer="91" />
                <label x="67.31" y="173.99" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="DOCK_DET" class="0">
              <segment>
                <pinref part="J3" gate="G$1" pin="10" />
                <wire x1="85.09" y1="171.45" x2="67.31" y2="171.45" width="0.1524" layer="91" />
                <label x="67.31" y="171.45" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="Q3" gate="G$1" pin="D" />
                <wire x1="292.10" y1="201.93" x2="297.18" y2="201.93" width="0.1524" layer="91" />
                <label x="297.18" y="201.93" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CHG_STAT" class="0">
              <segment>
                <pinref part="J3" gate="G$1" pin="12" />
                <wire x1="85.09" y1="166.37" x2="67.31" y2="166.37" width="0.1524" layer="91" />
                <label x="67.31" y="166.37" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="Q4" gate="G$1" pin="D" />
                <wire x1="292.10" y1="140.97" x2="297.18" y2="140.97" width="0.1524" layer="91" />
                <label x="297.18" y="140.97" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CHG_EN" class="0">
              <segment>
                <pinref part="J3" gate="G$1" pin="13" />
                <wire x1="85.09" y1="163.83" x2="67.31" y2="163.83" width="0.1524" layer="91" />
                <label x="67.31" y="163.83" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R26" gate="G$1" pin="1" />
                <wire x1="180.34" y1="90.17" x2="162.56" y2="90.17" width="0.1524" layer="91" />
                <label x="162.56" y="90.17" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="VBUS_5V_CHG" class="0">
              <segment>
                <pinref part="J3" gate="G$1" pin="19" />
                <wire x1="85.09" y1="148.59" x2="67.31" y2="148.59" width="0.1524" layer="91" />
                <label x="67.31" y="148.59" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J3" gate="G$1" pin="20" />
                <wire x1="85.09" y1="146.05" x2="67.31" y2="146.05" width="0.1524" layer="91" />
                <label x="67.31" y="146.05" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J3" gate="G$1" pin="21" />
                <wire x1="85.09" y1="143.51" x2="67.31" y2="143.51" width="0.1524" layer="91" />
                <label x="67.31" y="143.51" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="DETECT_GATE" class="0">
              <segment>
                <pinref part="Q3" gate="G$1" pin="G" />
                <wire x1="246.38" y1="200.66" x2="228.60" y2="200.66" width="0.1524" layer="91" />
                <label x="228.60" y="200.66" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R22" gate="G$1" pin="2" />
                <wire x1="190.50" y1="212.09" x2="195.58" y2="212.09" width="0.1524" layer="91" />
                <label x="195.58" y="212.09" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R23" gate="G$1" pin="1" />
                <wire x1="180.34" y1="189.23" x2="162.56" y2="189.23" width="0.1524" layer="91" />
                <label x="162.56" y="189.23" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="POGO_DET_RAW" class="0">
              <segment>
                <pinref part="R22" gate="G$1" pin="1" />
                <wire x1="180.34" y1="212.09" x2="162.56" y2="212.09" width="0.1524" layer="91" />
                <label x="162.56" y="212.09" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="STATUS_GATE" class="0">
              <segment>
                <pinref part="Q4" gate="G$1" pin="G" />
                <wire x1="246.38" y1="139.70" x2="228.60" y2="139.70" width="0.1524" layer="91" />
                <label x="228.60" y="139.70" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R24" gate="G$1" pin="2" />
                <wire x1="190.50" y1="151.13" x2="195.58" y2="151.13" width="0.1524" layer="91" />
                <label x="195.58" y="151.13" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R25" gate="G$1" pin="1" />
                <wire x1="180.34" y1="128.27" x2="162.56" y2="128.27" width="0.1524" layer="91" />
                <label x="162.56" y="128.27" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CHARGER_BAT_STAT" class="0">
              <segment>
                <pinref part="R24" gate="G$1" pin="1" />
                <wire x1="180.34" y1="151.13" x2="162.56" y2="151.13" width="0.1524" layer="91" />
                <label x="162.56" y="151.13" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="ENABLE_GATE" class="0">
              <segment>
                <pinref part="Q5" gate="G$1" pin="G" />
                <wire x1="246.38" y1="78.74" x2="228.60" y2="78.74" width="0.1524" layer="91" />
                <label x="228.60" y="78.74" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R26" gate="G$1" pin="2" />
                <wire x1="190.50" y1="90.17" x2="195.58" y2="90.17" width="0.1524" layer="91" />
                <label x="195.58" y="90.17" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R27" gate="G$1" pin="1" />
                <wire x1="180.34" y1="67.31" x2="162.56" y2="67.31" width="0.1524" layer="91" />
                <label x="162.56" y="67.31" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="CHARGER_RUN" class="0">
              <segment>
                <pinref part="Q5" gate="G$1" pin="D" />
                <wire x1="292.10" y1="80.01" x2="297.18" y2="80.01" width="0.1524" layer="91" />
                <label x="297.18" y="80.01" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R28" gate="G$1" pin="2" />
                <wire x1="347.98" y1="78.74" x2="353.06" y2="78.74" width="0.1524" layer="91" />
                <label x="353.06" y="78.74" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="VBUS_OR" class="0">
              <segment>
                <pinref part="R28" gate="G$1" pin="1" />
                <wire x1="337.82" y1="78.74" x2="320.04" y2="78.74" width="0.1524" layer="91" />
                <label x="320.04" y="78.74" size="1.016" layer="95" />
              </segment>
            </net>
          </nets>
        </sheet>
        <sheet>
          <plain>
            <text x="15.24" y="281.94" size="2.54" layer="94">FRIDAY / SCH-4b / LEFT TEMPLE AUDIO</text>
            <text x="15.24" y="274.32" size="1.78" layer="94">J3 pins 2–3 switched 5 V, 5/7/8 SAI1, 9 channel enable</text>
            <text x="15.24" y="63" size="1.78" layer="94">0.8 W into assumed 8 ohms is a software and bench limit. GAIN_SLOT is set to +3 dB.</text>
            <text x="15.24" y="53" size="1.78" layer="94">Local BTL speaker pair. Verify &gt;10 uH voice-coil inductance and emissions.</text>
            <text x="15.24" y="43" size="1.78" layer="94">Host low or high-Z shuts down. Host high selects the fitted channel through the local rail.</text>
          </plain>
          <instances>
            <instance part="FRAME5" gate="G$1" x="0" y="0" smashed="yes" />
            <instance part="U5" gate="G$1" x="183" y="200.66" smashed="yes">
              <attribute name="NAME" x="170.3" y="216.9" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="170.3" y="181.42" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="J4" gate="G$1" x="332" y="200.66" smashed="yes">
              <attribute name="NAME" x="314.22" y="207.01" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="314.22" y="193.04" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="U6" gate="G$1" x="120" y="117" smashed="yes">
              <attribute name="NAME" x="102.22" y="125.89" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="102.22" y="106.84" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="Q6" gate="G$1" x="252" y="117" smashed="yes">
              <attribute name="NAME" x="234.22" y="123.35" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="234.22" y="109.38" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R29" gate="G$1" x="51" y="139" smashed="yes">
              <attribute name="NAME" x="48.46" y="140.4" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="48.46" y="136.2" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R30" gate="G$1" x="51" y="94" smashed="yes">
              <attribute name="NAME" x="48.46" y="95.4" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="48.46" y="91.2" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R31" gate="G$1" x="191" y="144" smashed="yes">
              <attribute name="NAME" x="188.46" y="145.4" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="188.46" y="141.2" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R32" gate="G$1" x="330" y="112" smashed="yes">
              <attribute name="NAME" x="327.46" y="113.4" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="327.46" y="109.2" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R33" gate="G$1" x="330" y="81" smashed="yes">
              <attribute name="NAME" x="327.46" y="82.4" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="327.46" y="78.2" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R34" gate="G$1" x="62" y="183" smashed="yes">
              <attribute name="NAME" x="59.46" y="184.4" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="59.46" y="180.2" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R35" gate="G$1" x="114" y="83" smashed="yes">
              <attribute name="NAME" x="111.46" y="84.4" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="111.46" y="80.2" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="R36" gate="G$1" x="184" y="83" smashed="yes">
              <attribute name="NAME" x="181.46" y="84.4" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="181.46" y="80.2" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C16" gate="G$1" x="187" y="246" smashed="yes">
              <attribute name="NAME" x="184.46" y="248.2" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="184.46" y="242.4" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C17" gate="G$1" x="259" y="246" smashed="yes">
              <attribute name="NAME" x="256.46" y="248.2" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="256.46" y="242.4" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C18" gate="G$1" x="65" y="246" smashed="yes">
              <attribute name="NAME" x="62.46" y="248.2" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="62.46" y="242.4" size="1.27" layer="96" align="bottom-left" />
            </instance>
            <instance part="C19" gate="G$1" x="335" y="246" smashed="yes">
              <attribute name="NAME" x="332.46" y="248.54" size="1.27" layer="95" align="bottom-left" />
              <attribute name="VALUE" x="332.46" y="242.19" size="1.27" layer="96" align="bottom-left" />
            </instance>
          </instances>
          <busses />
          <nets>
            <net name="VCC5V0_SYS_S5_AMP" class="0">
              <segment>
                <pinref part="U5" gate="G$1" pin="VDD" />
                <wire x1="200.78" y1="213.36" x2="205.86" y2="213.36" width="0.1524" layer="91" />
                <label x="205.86" y="213.36" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U6" gate="G$1" pin="VCC" />
                <wire x1="97.14" y1="115.73" x2="79.36" y2="115.73" width="0.1524" layer="91" />
                <label x="79.36" y="115.73" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="Q6" gate="G$1" pin="S" />
                <wire x1="274.86" y1="117.00" x2="279.94" y2="117.00" width="0.1524" layer="91" />
                <label x="279.94" y="117.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R31" gate="G$1" pin="1" />
                <wire x1="185.92" y1="144.00" x2="168.14" y2="144.00" width="0.1524" layer="91" />
                <label x="168.14" y="144.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R34" gate="G$1" pin="1" />
                <wire x1="56.92" y1="183.00" x2="39.14" y2="183.00" width="0.1524" layer="91" />
                <label x="39.14" y="183.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R35" gate="G$1" pin="1" />
                <wire x1="108.92" y1="83.00" x2="91.14" y2="83.00" width="0.1524" layer="91" />
                <label x="91.14" y="83.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C16" gate="G$1" pin="1" />
                <wire x1="181.92" y1="246.00" x2="164.14" y2="246.00" width="0.1524" layer="91" />
                <label x="164.14" y="246.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C17" gate="G$1" pin="1" />
                <wire x1="253.92" y1="246.00" x2="236.14" y2="246.00" width="0.1524" layer="91" />
                <label x="236.14" y="246.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C18" gate="G$1" pin="1" />
                <wire x1="59.92" y1="246.00" x2="42.14" y2="246.00" width="0.1524" layer="91" />
                <label x="42.14" y="246.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C19" gate="G$1" pin="1" />
                <wire x1="329.92" y1="246.00" x2="312.14" y2="246.00" width="0.1524" layer="91" />
                <label x="312.14" y="246.00" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="PACK-_PROT" class="0">
              <segment>
                <pinref part="U5" gate="G$1" pin="GND" />
                <wire x1="200.78" y1="187.96" x2="205.86" y2="187.96" width="0.1524" layer="91" />
                <label x="205.86" y="187.96" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U5" gate="G$1" pin="EP" />
                <wire x1="200.78" y1="190.50" x2="205.86" y2="190.50" width="0.1524" layer="91" />
                <label x="205.86" y="190.50" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="U6" gate="G$1" pin="GND" />
                <wire x1="97.14" y1="113.19" x2="79.36" y2="113.19" width="0.1524" layer="91" />
                <label x="79.36" y="113.19" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R30" gate="G$1" pin="2" />
                <wire x1="56.08" y1="94.00" x2="61.16" y2="94.00" width="0.1524" layer="91" />
                <label x="61.16" y="94.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R33" gate="G$1" pin="2" />
                <wire x1="335.08" y1="81.00" x2="340.16" y2="81.00" width="0.1524" layer="91" />
                <label x="340.16" y="81.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R36" gate="G$1" pin="2" />
                <wire x1="189.08" y1="83.00" x2="194.16" y2="83.00" width="0.1524" layer="91" />
                <label x="194.16" y="83.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C16" gate="G$1" pin="2" />
                <wire x1="192.08" y1="246.00" x2="197.16" y2="246.00" width="0.1524" layer="91" />
                <label x="197.16" y="246.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C17" gate="G$1" pin="2" />
                <wire x1="264.08" y1="246.00" x2="269.16" y2="246.00" width="0.1524" layer="91" />
                <label x="269.16" y="246.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C18" gate="G$1" pin="2" />
                <wire x1="70.08" y1="246.00" x2="75.16" y2="246.00" width="0.1524" layer="91" />
                <label x="75.16" y="246.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="C19" gate="G$1" pin="2" />
                <wire x1="340.08" y1="246.00" x2="345.16" y2="246.00" width="0.1524" layer="91" />
                <label x="345.16" y="246.00" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="AMP_L_SD_MODE" class="0">
              <segment>
                <pinref part="U5" gate="G$1" pin="SD_MODE" />
                <wire x1="165.22" y1="198.12" x2="147.44" y2="198.12" width="0.1524" layer="91" />
                <label x="147.44" y="198.12" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R32" gate="G$1" pin="2" />
                <wire x1="335.08" y1="112.00" x2="340.16" y2="112.00" width="0.1524" layer="91" />
                <label x="340.16" y="112.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R33" gate="G$1" pin="1" />
                <wire x1="324.92" y1="81.00" x2="307.14" y2="81.00" width="0.1524" layer="91" />
                <label x="307.14" y="81.00" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="AMP_L_GAIN" class="0">
              <segment>
                <pinref part="U5" gate="G$1" pin="GAIN_SLOT" />
                <wire x1="165.22" y1="203.20" x2="147.44" y2="203.20" width="0.1524" layer="91" />
                <label x="147.44" y="203.20" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R34" gate="G$1" pin="2" />
                <wire x1="67.08" y1="183.00" x2="72.16" y2="183.00" width="0.1524" layer="91" />
                <label x="72.16" y="183.00" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SAI1_BCLK_M0" class="0">
              <segment>
                <pinref part="U5" gate="G$1" pin="BCLK" />
                <wire x1="165.22" y1="208.28" x2="147.44" y2="208.28" width="0.1524" layer="91" />
                <label x="147.44" y="208.28" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SAI1_LRCK_M0" class="0">
              <segment>
                <pinref part="U5" gate="G$1" pin="LRCLK" />
                <wire x1="165.22" y1="200.66" x2="147.44" y2="200.66" width="0.1524" layer="91" />
                <label x="147.44" y="200.66" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SAI1_SDO0_M0" class="0">
              <segment>
                <pinref part="U5" gate="G$1" pin="DIN" />
                <wire x1="165.22" y1="205.74" x2="147.44" y2="205.74" width="0.1524" layer="91" />
                <label x="147.44" y="205.74" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SPK_L_P" class="0">
              <segment>
                <pinref part="U5" gate="G$1" pin="OUTP" />
                <wire x1="200.78" y1="205.74" x2="205.86" y2="205.74" width="0.1524" layer="91" />
                <label x="205.86" y="205.74" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J4" gate="G$1" pin="SPK_P" />
                <wire x1="309.14" y1="200.66" x2="291.36" y2="200.66" width="0.1524" layer="91" />
                <label x="291.36" y="200.66" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SPK_L_N" class="0">
              <segment>
                <pinref part="U5" gate="G$1" pin="OUTN" />
                <wire x1="200.78" y1="208.28" x2="205.86" y2="208.28" width="0.1524" layer="91" />
                <label x="205.86" y="208.28" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="J4" gate="G$1" pin="SPK_N" />
                <wire x1="354.86" y1="200.66" x2="359.94" y2="200.66" width="0.1524" layer="91" />
                <label x="359.94" y="200.66" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="AMP_L_SELECT_REF" class="0">
              <segment>
                <pinref part="U6" gate="G$1" pin="IN+" />
                <wire x1="97.14" y1="120.81" x2="79.36" y2="120.81" width="0.1524" layer="91" />
                <label x="79.36" y="120.81" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R35" gate="G$1" pin="2" />
                <wire x1="119.08" y1="83.00" x2="124.16" y2="83.00" width="0.1524" layer="91" />
                <label x="124.16" y="83.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R36" gate="G$1" pin="1" />
                <wire x1="178.92" y1="83.00" x2="161.14" y2="83.00" width="0.1524" layer="91" />
                <label x="161.14" y="83.00" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="AMP_L_ENABLE_GATE" class="0">
              <segment>
                <pinref part="U6" gate="G$1" pin="IN-" />
                <wire x1="97.14" y1="118.27" x2="79.36" y2="118.27" width="0.1524" layer="91" />
                <label x="79.36" y="118.27" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R29" gate="G$1" pin="2" />
                <wire x1="56.08" y1="139.00" x2="61.16" y2="139.00" width="0.1524" layer="91" />
                <label x="61.16" y="139.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R30" gate="G$1" pin="1" />
                <wire x1="45.92" y1="94.00" x2="28.14" y2="94.00" width="0.1524" layer="91" />
                <label x="28.14" y="94.00" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="AMP_L_SELECT_GATE" class="0">
              <segment>
                <pinref part="U6" gate="G$1" pin="OUT" />
                <wire x1="142.86" y1="117.00" x2="147.94" y2="117.00" width="0.1524" layer="91" />
                <label x="147.94" y="117.00" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="Q6" gate="G$1" pin="G" />
                <wire x1="229.14" y1="115.73" x2="211.36" y2="115.73" width="0.1524" layer="91" />
                <label x="211.36" y="115.73" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R31" gate="G$1" pin="2" />
                <wire x1="196.08" y1="144.00" x2="201.16" y2="144.00" width="0.1524" layer="91" />
                <label x="201.16" y="144.00" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="AMP_L_SD_SOURCE" class="0">
              <segment>
                <pinref part="Q6" gate="G$1" pin="D" />
                <wire x1="229.14" y1="118.27" x2="211.36" y2="118.27" width="0.1524" layer="91" />
                <label x="211.36" y="118.27" size="1.016" layer="95" />
              </segment>
              <segment>
                <pinref part="R32" gate="G$1" pin="1" />
                <wire x1="324.92" y1="112.00" x2="307.14" y2="112.00" width="0.1524" layer="91" />
                <label x="307.14" y="112.00" size="1.016" layer="95" />
              </segment>
            </net>
            <net name="SD_MODE_L" class="0">
              <segment>
                <pinref part="R29" gate="G$1" pin="1" />
                <wire x1="45.92" y1="139.00" x2="28.14" y2="139.00" width="0.1524" layer="91" />
                <label x="28.14" y="139.00" size="1.016" layer="95" />
              </segment>
            </net>
          </nets>
        </sheet>
      </sheets>
    </schematic>
  </drawing>
</eagle>
