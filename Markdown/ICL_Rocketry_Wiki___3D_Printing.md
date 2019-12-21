::: {#page}
::: {#main .aui-page-panel}
::: {#main-header}
::: {#breadcrumb-section}
1.  [ICL Rocketry Wiki](index.html)
2.  [ICL Rocketry Wiki Home](ICL-Rocketry-Wiki-Home_142270843.html)
3.  [Manufacturing](Manufacturing_142271214.html)
:::

[ ICL Rocketry Wiki : 3D Printing ]{#title-text} {#title-heading .pagetitle}
================================================
:::

::: {#content .view}
::: {.page-metadata}
Created by [ Kacker, Shreeyam]{.author}, last modified by [ Fonseca,
Francisco]{.editor} on Nov 19, 2019
:::

::: {#main-content .wiki-content .group}
### **Overall workflow** {#id-3DPrinting-Overallworkflow}

In a perfect world, any part would be easily 3D printed as a prototype,
and would not require any changes when designed for other manufacturing.
Unfortunately due to the way that a 3D printer is just a hot glue gun on
a CNC gantry, this is not quite possible, and some things need to be
kept in min mind when designing something for 3D printing. Truly, 3D
printing should almost always be the **last option you consider. **3D
prints are often **heavier, bulkier, and not as strong** as conventional
manufacturing methods. Consider laser cutting, or turning and milling if
you have access and don\'t need complex features.

The overall workflow consists of:

1.  **Generating a CAD model** in your software of choice (Fusion 360
    for ICLR), with some key things kept in mind in the design section.
2.  **Exporting an STL** from CAD software. The STL file is a
    discretisation of the CAD models into many faces and polygons.
3.  **Slice the STL** to produce a gcode file. This file produces raw,
    very basic instructions for how the 3D printer should move the
    gantry, acceleration, and extrude filament. Currently the most
    feature-packed free and open source slicer software is **Cura** from
    Ultimaker.

### **Structure of a print** {#id-3DPrinting-Structureofaprint}

A 3D printed part is made of **walls, infill, top/bottom layers, and
support structure** generally.

### **Material properties** {#id-3DPrinting-Materialproperties}

The standard settings in Cura make the strength of your part far from
isotropic. Generally, the z axis (the direction of the layers) is the
weakest, as each layer presents a thin section that is almost
universally a weakness and reduces strength in that direction.

Standard infill is also stacked in the z axis, giving additional
compressive strength there. Change the infill pattern to cubic or gyroid
to get near-isotropic material properties.

### **Tolerancing:** {#id-3DPrinting-Tolerancing:}

Make sure to allow for tolerances in parts before printing them. In
general most 3D printing is +-0.2mm on a calibrated printer. (Some
cheaper printers may require calibration of steps/mm with a test cube
before they can be used to print parts where dimensioning is critical -
Eg. Creality Ender 3).

### Supports: {#id-3DPrinting-Supports:}

3D printed materials often require support material to be able to print
- eg. for overhangs, etc\... These will be added by the slicer program
automatically where you need them if you tell it to. If you can design
your part to minimize the supports required (ideally eliminate them) you
will end up with a better print as supports can be annoying to remove,
waste filament and ruin the finish of the part at the locations they are
needed. Most printers can safely do overhangs of 45 degrees or less
without support, more than this and the print may fail without supports.

### **Design for 3D printing** {#id-3DPrinting-Designfor3Dprinting}

**A useful external resource for material properties of common
filaments: <https://www.simplify3d.com/support/materials-guide/properties-table/>**

::: {.table-wrap}
<table style="width:100%;">
<colgroup>
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>Material</th>
<th><p>Young's Modulus [GPa]</p>
<p>(Material, not part)</p></th>
<th>Flexural Modulus [GPa]</th>
<th>Yield/Ultimate Strength [MPa]</th>
<th>Glass Transition [<span style="color: rgb(51,51,51);">°</span>C]</th>
<th>Print Temperature (nozzle/bed) [<span style="color: rgb(51,51,51);">°</span>C]</th>
<th>Z Strength Reduction [-]</th>
<th>Common Usage</th>
<th>Notes</th>
<th>Cool fax</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PLA</td>
<td>3.5</td>
<td><br />
</td>
<td>40 (Yield), 65 (Ultimate)</td>
<td>60</td>
<td>200/50</td>
<td>0.8</td>
<td>Everything that doesn't need to be printed with another filament. Be wary of UV degredation if used outside for a long time.</td>
<td>Most widely used and cheaply and readily available. Easy to print. If you can make your part in PLA it's probably the easiest option.</td>
<td>Made from plants and not dinosaur extract. Easy to print, cheap, <strong>low amount of warping</strong> makes it easy to print stuff fairly dimensionally accurately. Will degrade if exposed to UV for too long</td>
</tr>
<tr class="even">
<td>ABS</td>
<td>2 ish</td>
<td><br />
</td>
<td>30 (Yield), 40 (Ultimate)</td>
<td>140</td>
<td>240/110 (On PEI Sheet)</td>
<td>0.8</td>
<td>Car bumpers, often preferred to PLA for structural parts for better strength between layers, better UV resistance and better temperature resistance.</td>
<td><strong>Needs a print enclosure, all-metal hot-end if going near to 240C (may be able to get away with lower print-temp and other hot-end but please don't).</strong> Very commonly used good option for many prints. If part will be used outside for a long time and is structural then black filament is preferred as it will resist UV degradation better.</td>
<td>Expect more <strong>warping of parts</strong> than for PLA. For larger parts expect more warping - be generous with tolerances. Without a PEI sheet to print on then build plate adhesion is problematic.</td>
</tr>
<tr class="odd">
<td>PETG</td>
<td>2.2</td>
<td><br />
</td>
<td>45 (Yield), 53 (Ultimate)</td>
<td>90</td>
<td>240/70</td>
<td>0.95</td>
<td>Plastic bottles</td>
<td><strong>Needs all metal hot-end</strong></td>
<td>Looks dope</td>
</tr>
<tr class="even">
<td>Nylon</td>
<td>2.7</td>
<td><br />
</td>
<td>40-85 (Ultimate)</td>
<td>41</td>
<td>255/110 (Glass &amp; Glue build plate)</td>
<td>0.9</td>
<td>Low friction. impact. Printed gears, etc... Moderate structural parts (Not as strong as polycarbonate, can even be weaker than PLA dependent on the exact filament, print, etc...)</td>
<td><strong>Needs a print enclosure, a dry box, and an all metal hot end. Do NOT print this on a normal printer. The PTFE heatbread will decompose into neurotoxin. Cannot be printed if waterlogged due to absorbing water vapour from air. Dry out the filament in the oven before use. For large prints keeping the filament dry during the print may also be necessary.</strong></td>
<td>People once thought making clothes out of non-biodegradable material was cool. Elevated temperature means warping likely. Try garolite (Or G10 FR4) build plate if adhesion is problematic</td>
</tr>
<tr class="odd">
<td>Flex (TPU)</td>
<td>0.1-1</td>
<td><br />
</td>
<td>26-43 (Ultimate)</td>
<td>-20</td>
<td>220/30</td>
<td>0.95</td>
<td>idk bendy things?</td>
<td><strong>Can't print this fast. 30mm/s MAX.</strong></td>
<td><br />
</td>
</tr>
<tr class="even">
<td>Polycarbonate</td>
<td>2.3 (Check this)</td>
<td>2.47</td>
<td>72 (Ultimate)</td>
<td>150</td>
<td>260-310/80-120</td>
<td>?</td>
<td>Structural parts, parts requiring good temperature resistance (Up to 135C)</td>
<td><strong>Very strong, but hard to print. Bed adhesion tricky. Garolite (Or G10 FR4) build plate allegedly can work good. PEI build plate apparently also is workable. Sucks up moisture rapidly so to print anything super large you will need to dry the filament whilst printing (and also before in the oven) - if you do not do this then part strength will be significantly weaker and stringing or other artefacts may occur.</strong></td>
<td>Expect <strong>some warping</strong> of parts as it's hard to avoid</td>
</tr>
<tr class="odd">
<td>Onyx (Optionally with carbon fibre reinforcement)</td>
<td>1.4 (Without CF)</td>
<td>2.9 (Without CF)</td>
<td>36MPa (Ultimate) (Without CF)</td>
<td><br />
</td>
<td>?</td>
<td>?</td>
<td>Structural parts, high strength/quality required.</td>
<td>Department can print this material on their fancy printer (Markforged). But it's quite an <strong>expensive filament</strong>, if you add <strong>carbon reinforcement</strong> then prints can easily get up to <strong>£100s for materials alone. </strong>Hackspace also can print this.</td>
<td>Super fancy, looks great and is very stiff and strong. However be wary of the cost of printing with it. Strength added by carbon fibre reinforcement (if used) hard to predict.</td>
</tr>
</tbody>
</table>
:::

The finest feature that can be printed well is equal to the nozzle size.
**Universally almost every 3D printer has a nozzle size of 0.4mm**, so
keep thin walls and features (\<3 mm) to **multiples of the nozzle
size.** Everything larger has a varying amount of infill that can be
accommodated easily.

### **Finishing / Sanding** {#id-3DPrinting-Finishing/Sanding}

When sanding, remember the following:

1.  Always ensure that the surface to be sanded is at least damp
    1.  Inhalation of fine metal / plastic particles is a health hazard
        1.  We are not responsible for any long-term health issues you
            may face due to your own idiocy
2.  As such, make sure to use waterproof files / pads
3.  For a smooth finish, ensure that sanding is done in all directions,
    rather than along two (or even one) directions alone.
    1.  If pads / papers are being used, sanding in circles will give a
        good finish
4.  When sanding, to save time, increase the grit by 2x (where possible)
    every time you finish sanding the material

**Traps for young players:**

-   If you are setting a print, stay with it for about 20 minutes to
    make sure it starts correctly. A print is most likely to fail at the
    very start.
-   When setting a print please remember that the bed and the nozzle
    heat up before the print. This causes the filament in the nozzle to
    drizzle. Close to the end of the heating period, take a piece of
    paper or some clippers and grab this filament and pull it out of the
    nozzle (keeping in mind that the nozzle is VERY HOT).
-   Do not make the mistake of assuming that the bed of the printer you
    are using is calibrated. Always check if the printer you are using
    has auto bed levelling and if it does not this can easily be done
    with a piece of paper. There are many youtube videos showing how you
    can do this for every different printer.
:::
:::
:::

::: {#footer role="contentinfo"}
::: {.section .footer-body}
Document generated by Confluence on Dec 21, 2019 10:27

::: {#footer-logo}
[Atlassian](http://www.atlassian.com/)
:::
:::
:::
:::
