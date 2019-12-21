::: {#page}
::: {#main .aui-page-panel}
::: {#main-header}
::: {#breadcrumb-section}
1.  [ICL Rocketry Wiki](index.html)
2.  [ICL Rocketry Wiki Home](ICL-Rocketry-Wiki-Home_142270843.html)
3.  [Airframe & Recovery](142271815.html)
:::

[ ICL Rocketry Wiki : CO2 Raptor ]{#title-text} {#title-heading .pagetitle}
===============================================
:::

::: {#content .view}
::: {.page-metadata}
Created by [ Harayama, Sena]{.author}, last modified on Nov 30, 2019
:::

::: {#main-content .wiki-content .group}
Log of the works around the COTS CO2 ejection system Peregrine Raptor.

Context:

-   Recovery team started looking into CO2 ejection system in the
    2018-2019 year, initially due to concerns around acquiring and
    storing explosives (detailed more in LINK TO THE DOCUMENT THAT [Gir,
    Tanvi](https://wiki.imperial.ac.uk/display/~trg18){.confluence-userlink
    .user-mention}  WILL CREATE ABOUT EXPLOSIVES AT ICLR) in the UK. 
-   A CO2 system refers to an ejection device that uses CO2 to
    pressurize the inside of the rocket and split it for the ejection of
    the parachute(s).
-   Beginning of 2019-2020 year, the airframe and recovery team worked
    extensively on the CO2 system, designing the November Rocket aka
    Pierce Brosnen as a test rocket dedicated to recovery systems, and
    investigating the possibility of making our own custom CO2 system
    (both purely mechanical and combined explosive/CO2 systems).
-   Meanwhile, the team decided to invest on a COTS system, as a backup
    and reference.
-   Only supplier for COTS systems selling to the UK is FruityChutes,
    based in the US. Among their inventory, three items were shortlisted
    as candidates:\
    Put links
-   <https://12f23cf9-3149-6c03-4d40-a5bf89d0c9f7.filesusr.com/ugd/b73de9_c96c3a3b75104cc1a593dd3d4c328036.pdf>
-   [[![](rest/documentConversion/latest/conversion/thumbnail/142273682/1){height="250"}](/download/attachments/142273169/peregrineraptor_userguide.pdf?version=1&modificationDate=1575142674000&api=v2){.confluence-embedded-file}]{.confluence-embedded-file-wrapper}

\

### Log of 27/11/2019 {#CO2Raptor-Logof27/11/2019}

\
New urgent problem:

-   The adapters might not fit (Thread size was advised from aero
    technician Mark as being a 1/2 inch BSP, however considering the
    product comes from the USA there is a high chance that they actually
    are UNF threads).
-   The adapters come with a lip (see pic for reference). This may add a
    few extra millimeters to the position of the canister into the
    Raptor, which means that the canister may not be in the reach of the
    piercing needle anymore. 

Looking less than a week before the scheduled launch, the team decided
to urgently work towards an alternative system. Urgent design bureau was
set on the day, and an alternative solution prototype was tested on the
day in Prince\'s Gardens at around 1:00 am (lol)

Solution: Do not rely on threads, instead clamp the canister tightly
against the Raptor, and rely on the tight fit and O-rings to create a
seal.\
[Author: Dev\
Working members: [Agrawal,
Devansh](https://wiki.imperial.ac.uk/display/~dra16){.confluence-userlink
.user-mention .current-user-mention}, [Anyamele,
Nnaemeka](https://wiki.imperial.ac.uk/display/~nfa18){.confluence-userlink
.user-mention} [Gir,
Tanvi](https://wiki.imperial.ac.uk/display/~trg18){.confluence-userlink
.user-mention} [Harayama,
Sena](https://wiki.imperial.ac.uk/display/~sh5915){.confluence-userlink
.user-mention} ]{style="letter-spacing: 0.0px;"}

Log:

Decided to use laser cut plywood centering rings held by M6
steel ![(question)](images/icons/emoticons/help_16.svg){.emoticon
.emoticon-question} rods into the bulkhead. To avoid the CO2 canister to
move axially in the Raptor (3/8 inch diameter for canister vs 1/2 inch
diameter for the Raptor), small ring shaped inserts were laser cut to be
put between the canister and the CO2, just so to minimize axial
movement.

Difficulties: (many)

-   Requires flipping the CO2 system compared to the original plan (the
    centering rings and housing assembly need to not interfere with the
    pressurisation and even less with the shock chord and parchute)
-   Hole in the original bulkhead was sized for the chamfered bit of the
    Raptor so now needs to be enlarged)
-   Needs new holes for the threaded rods, original bulkhead already
    epoxied on so limited accessibility to do any further modifications.
-   Nut and eyebolt already expoxied onto the original bulkhead may
    interfere with placing additional bulkheads.

Other notes:

-   Sleeve on the igniters are there for the charge through the wires to
    reach the igniter head. Probably could get around with taping.
    Sleeve needs to be cut to be flush with the hole in the Black powder
    housing.
-   Igniter needs to be secured on the black powder housing by putting
    5min epoxy onto the bottom of the sleeve. This time used Wood glue,
    worked perfectly fine.
-   Needs some cleaning equipment, especially if we want to do multiple
    tests, so need to bring water and stuff to the launch site.
-   Needs gloves!

Outcome:

-   Worked very fine\
    Link to the video: [Anyamele,
    Nnaemeka](https://wiki.imperial.ac.uk/display/~nfa18){.confluence-userlink
    .user-mention}
-   Pictures:\
    I\'ll put em here later

\

### Log 30/11/2019 {#CO2Raptor-Log30/11/2019}

\

Ground test in rocket

Some issue:

-   First test: Unsuccessful (nothing happened when the button was
    pressed, tried twice and nothing happened)
    -   Reasons:
        -   The ematch did not go: At the base of the ignitor, the wires
            are exposed as they are not fully covered by the electrical
            insulation. Because of that, they were touching which was
            shorting the ignition circuit
-   Second test: Successful with some minor issues (the explosion did go
    off but the nosecone did not pop off the rocket. Also there was
    clearly some gas coming out the bottom, suggesting there are some
    leaks)
    -   Reasons:
        -   The canister did not get fully pierced: The clamping
            assembly was a bit loose, hence there was some leaks between
            the O-ring and the canister. Also the canister was not
            centered and got pierced off centered.
        -   The friction fit between the nosecone and the rocket was
            probably too tight 
        -   Gas was leaking from the ematch hole, as well as directly
            from the canister but the wrong way (due to first problem).
            Some black powder may have been leaking from the pyrohouse
            through the ematch hole.
-   Third test: Successful (nose cone and drogue did come off, nose only
    flew about a meter, so we may want more gas, the canister hole was
    centered, could be larger but no fix for that)
    -   Notes:
        -   Ematch hole was now plugged in using white tack 
        -   Nuts were tightened carefully, and we thoroughly checked
            that the canister was centered. We added a thin strip of
            masking tape around the canister threads to help with the
            centering but not sure how much that actually helped
        -   Used some electrical tape to make sure the ematch wires were
            not shorting
        -   Used wood glue to seal the ematch hole.
        -   At launch, use the 20 grams CO2 canister. Urgently cut some
            longer rods to accommodate for those.

### Assembly procedure {#CO2Raptor-Assemblyprocedure}

1.  Put shock chord into the black shockchord loop
2.  Prepare the pyrohousing (put the ematch through, taking care the
    wires are not shorting, put the sleeve or electrical tape, put some
    wood glue at the bottom of the sleeve or tape, put and make sure the
    hole is sealed)
3.  Black powder: measure, pour, masking tape (or red sticker it)
4.  Red cap + spring + piston assembly
5.  Red cap in to the Raptor
6.  Use the magic stick to pass the ematch through the hole
7.  Assemble the canister housing and tighten the nuts, making sure that
    the canister is centered
8.  Blue tack in ematch hole from the top (pressurized side)
9.  Wire ematch onto the avionics bay
10. Good to go
:::

::: {.pageSection .group}
::: {.pageSectionHeader}
Attachments: {#attachments .pageSectionTitle}
------------
:::

::: {.greybox align="left"}
![](images/icons/bullet_blue.gif){width="8" height="8"}
[peregrineraptor\_userguide.pdf](attachments/142273169/142273682.pdf)
(application/pdf)\
:::
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
