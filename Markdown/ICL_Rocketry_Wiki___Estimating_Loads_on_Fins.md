::: {#page}
::: {#main .aui-page-panel}
::: {#main-header}
::: {#breadcrumb-section}
1.  [ICL Rocketry Wiki](index.html)
2.  [ICL Rocketry Wiki Home](ICL-Rocketry-Wiki-Home_142270843.html)
3.  [Airframe & Recovery](142271815.html)
:::

[ ICL Rocketry Wiki : Estimating Loads on Fins ]{#title-text} {#title-heading .pagetitle}
=============================================================
:::

::: {#content .view}
::: {.page-metadata}
Created by [ Agrawal, Devansh]{.author}, last modified on Dec 20, 2019
:::

::: {#main-content .wiki-content .group}
To be able to select fins and size them for our rocket, here I present a
small guide to estimating the forces on the fins. 

\

A simplified analysis of the forces on the fins can be performed by
imagining they are a flat plate at a small angle of attack, cantilevered
at the rocket tube. The fins therefore produce some lift, and this can
be modelled using plate bending theory, or even more simply a flat plate
assumption. 

\

Which forces do fins feel? {#EstimatingLoadsonFins-Whichforcesdofinsfeel?}
--------------------------

A lift force, and a drag force. But the drag force on a  thin plate at a
small angle of attack is quite small, and the fins need to be designed
to take on the root bending moment.

We will calculate this load using a few different methods: A point load
assumption and a cantilevered beam model. In the future, we may try to
solve this using plate bending theory, or FEA.

\

[![](attachments/142274830/142274835.png){.confluence-embedded-image
height="400"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}

### Model 1: Point loads {#EstimatingLoadsonFins-Model1:Pointloads}

We can use a very simple approximation to find the order of magnitude of
the root bending moment. We assume that this is a flat plate, with some
small angle of attack α, and that it feels a single concentrated force
at the centre of fin. 

\

#### **Derivation** {#EstimatingLoadsonFins-Derivation}

[The total area of the fin is
simply]{style="color: rgb(34,34,34);letter-spacing: 0.0px;"}

[![](attachments/142274830/142274838.png){.confluence-embedded-image
.confluence-thumbnail width="150"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}

[A flat plate has a lift curve slope of 2π, and so we can make a simple
approximation of the lift in terms of the angle of attack (in
radians):]{.mwe-math-element
style="color: rgb(34,34,34);text-decoration: none;"}

[[![](attachments/142274830/142274842.png){.confluence-embedded-image
.confluence-thumbnail width="80"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}]{.mwe-math-element
style="color: rgb(34,34,34);text-decoration: none;"}

Therefore, the total wing produces a lift of magnitude, 

[![](attachments/142274830/142274843.png){.confluence-embedded-image
.confluence-thumbnail width="300"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}

(with α defined in radians)

To find the moment arm, we will need to find the mean aerodynamic chord,
and then find the y location of that chord. 

[For a single fin (with geometry defined above), the mean aerodynamic
chord is defined as,]{style="color: rgb(34,34,34);"}

[![](attachments/142274830/142274837.png){.confluence-embedded-image
width="150"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}

[Next, we need to find the  chord as a function of the y
coordinate: ]{.mwe-math-element
style="color: rgb(34,34,34);text-decoration: none;"}

[![](attachments/142274830/142274839.png){.confluence-embedded-image
.confluence-thumbnail width="180"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}

[therefore, the MAC of this fin is given by:]{.mwe-math-element
style="color: rgb(34,34,34);text-decoration: none;"}

[[![](attachments/142274830/142274841.png){.confluence-embedded-image
.confluence-thumbnail width="200"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}\
]{.mwe-math-element style="color: rgb(34,34,34);text-decoration: none;"}

[Now we can solve for the y location of the MAC, using the previous
equation. ]{.mwe-math-element
style="color: rgb(34,34,34);text-decoration: none;"}

[[![](attachments/142274830/142274844.png){.confluence-embedded-image
.confluence-thumbnail width="150"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}]{.mwe-math-element
style="color: rgb(34,34,34);text-decoration: none;"}

\

[Therefore the total root bending moment is given by ]{.mwe-math-element
style="color: rgb(34,34,34);text-decoration: none;"}

[[![](attachments/142274830/142274845.png){.confluence-embedded-image
width="350"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}]{.mwe-math-element
style="color: rgb(34,34,34);text-decoration: none;"}

[If you want to include the effect of compressibility, you have to
include a Prandtl Glauert correction, that is only accurate upto
Ma\<\~0.7)]{.mwe-math-element
style="color: rgb(34,34,34);text-decoration: none;"}

[[![](attachments/142274830/142274846.png){.confluence-embedded-image
width="400"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}\
]{.mwe-math-element style="color: rgb(34,34,34);text-decoration: none;"}

[Note: The classic fuselage correction on lift (1+(total wing
span/fuselage diameter)\^2) factor may not be relevant to
our ]{style="letter-spacing: 0.0px;"}problem. Using approximate numbers
from Sporadic impulse, that factor evaluates to 10. The correction was
designed for medium-high aspect ratio aircrafts, not our very low aspect
ratio fins. 

Therefore, we see that the root bending moment is proportional to

1.  dynamic pressure
2.  angle of attack
3.  the span, *squared*
4.  and (cr + 2ct)
5.  compressibility factor

Therefore, the fins root bending moment is primarily sized by the maxQ
condition, but you need to be generous with the angles of attack in case
the rocket is hit by a gust at this condition! (See below for gust
correction)

#### Sample Calculation (for a rocket similar to Sporadic Impulse) {#EstimatingLoadsonFins-SampleCalculation(forarocketsimilartoSporadicImpulse)}

Suppose our rocket has the following parameters:

1.  Geometry:
    1.  Root Chord: 12 in = 0.3 m
    2.  Tip Chord: 6 in = 0.15 m
    3.  Semi-span: 6 in = 0.15 m
2.  Flight Conditions:
    1.  rho=1.225 kg/m3
    2.  max V = 255 m/s
    3.  Ma = 0.77 (slightly outside the PG correction region, but we
        will use it for now)

Using

 [[![](attachments/142274830/142274846.png){.confluence-embedded-image
width="400"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}]{.mwe-math-element
style="color: rgb(34,34,34);text-decoration: none;"}

[We get a bending moment of ]{.mwe-math-element
style="color: rgb(34,34,34);text-decoration: none;"}

[M =      882.5 α    if α was in radians, or ]{.mwe-math-element
style="color: rgb(34,34,34);text-decoration: none;"}

[M = 50,561.6 α    if α is in degrees]{.mwe-math-element
style="color: rgb(34,34,34);text-decoration: none;"}

[which means that (note this isn\'t an accurate
table)]{.mwe-math-element
style="color: rgb(34,34,34);text-decoration: none;"}

::: {.table-wrap}
  -----------------------------------------------------------------------
              alpha (deg)                           Bending moment (kN m)
  ----------------------- -----------------------------------------------
                      0.1                                            5.06

                      0.5                                            25.3

                      1.0                                            50.6

                      5.0                                           252.8
  -----------------------------------------------------------------------
:::

\

These are definitely not insignificant, but luckily, if our static
margin is large enough, our angles of attack should be very small for
most of our journey. 

In fact we can see what this is like, on a representative openRocket
Simulation (Sporadic Impulse, 5 Dec 2019)

[![](attachments/142274830/142274854.png){.confluence-embedded-image
height="250"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}

\

[![](attachments/142274830/142274847.png){.confluence-embedded-image
height="250"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}[![](attachments/142274830/142274849.png){.confluence-embedded-image
height="250"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}[![](attachments/142274830/142274855.png){.confluence-embedded-image
height="250"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}

Notice that after the launch rod clearance, the angle of attack is
always less than 5 deg, and gets to be less than 0.5 from about 3
seconds into flight.

Some more useful plots are:

[![](attachments/142274830/142274850.png){.confluence-embedded-image
height="250"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}[![](attachments/142274830/142274856.png){.confluence-embedded-image
height="250"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}[![](attachments/142274830/142274857.png){.confluence-embedded-image
height="250"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}

\

Using the last plot where we club together the effect of , we can say
that (alpha (rad) \* V\^2/sqrt(1-Ma\^2)) will stay below 160 rad
m\^2/s\^2 for this rocket. 

Therefore if we still assume rho=1.225 kg/m3 throughout, we can get the
following estimate on the total bending moment of the rocket:

\

::: {.table-wrap}
  Condition       Bending Moment (N m)(THIS IS WRONG SEE BELOW)
  --------------- -----------------------------------------------
  Bounding Case   1.385 
:::

\

Which is really small! Note, this simulation was done with wind speeds
of about 2 m/s, but really should be done with wind speeds on order of
30 m/s for worst case analysis

\

**However this isn\'t what sizes the fins!! You have to worry about
gusts!**

\

To deal with gusts, we need an estimate on what the gust can look like.
There is a very good explanation of this (and currently being
implemented in full in rocketPy) from
AspireSpace: <http://www.aspirespace.org.uk/downloads/Rocket%20vehicle%20loads%20and%20airframe%20design.pdf>

\

For fins, the most important point is that the gust can be modelled as a
9m/s step increase in horizontal speed. That implies that there is
suddenly an increase in alpha. Let\'s estimate this increase in alpha.

As an approximation, we can assume the rocket is going straight up (as
we say earlier the \$\\alpha\$ goes to 0 very quickly) and is flying at
a speed V. Then it sees a 9 m/s wind gust, and therefore the alpha is 

[![](attachments/142274830/149336726.png){.confluence-embedded-image
.confluence-thumbnail width="120"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}

\

::: {.table-wrap}
    V (m/s)   alpha (deg)
  --------- -------------
        30           16.7
         50          10.2
        100           5.1
        250           2.1
:::

Which ends up changing the graphs to look like these:

[![](attachments/142274830/149336731.png){.confluence-embedded-image
height="250"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}[![](attachments/142274830/149336728.png){.confluence-embedded-image
height="250"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}[![](attachments/142274830/149336729.png){.confluence-embedded-image
height="250"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}[![](attachments/142274830/149336730.png){.confluence-embedded-image
height="250"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}

Which is definitely far greater than anything we\'ve designed for at the
moment! 

**And the most important graph:**

[![](attachments/142274830/149336732.png){.confluence-embedded-image
.confluence-content-image-border width="368"
height="250"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}

\

So overall, it seems we need to design our fins to sustain about 35 Nm
of root bending moment. 

**This is equivalent to placing about 24 kg of load at the tip of any
single fin!**

\

\

\

Method 2: 

\

\

\

\

\

\
:::

::: {.pageSection .group}
::: {.pageSectionHeader}
Attachments: {#attachments .pageSectionTitle}
------------
:::

::: {.greybox align="left"}
![](images/icons/bullet_blue.gif){width="8" height="8"}
[fin\_forces.eps](attachments/142274830/142274833.eps)
(application/postscript)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[fin\_forces.svg](attachments/142274830/142274834.svg) (image/svg+xml)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[fin\_forces.png](attachments/142274830/142274836.png) (image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[fin\_forces.png](attachments/142274830/142274835.png) (image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[image2019-12-7\_0-36-14.png](attachments/142274830/142274837.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[image2019-12-7\_0-37-31.png](attachments/142274830/142274838.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[image2019-12-7\_0-39-26.png](attachments/142274830/142274839.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[image2019-12-7\_0-42-24.png](attachments/142274830/142274840.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[image2019-12-7\_0-42-46.png](attachments/142274830/142274841.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[image2019-12-7\_0-44-20.png](attachments/142274830/142274842.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[image2019-12-7\_0-49-15.png](attachments/142274830/142274843.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[image2019-12-7\_0-56-27.png](attachments/142274830/142274844.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[image2019-12-7\_1-3-32.png](attachments/142274830/142274845.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[image2019-12-7\_1-12-34.png](attachments/142274830/142274846.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-07 at 01.24.46.png](attachments/142274830/142274847.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-07 at 01.25.27.png](attachments/142274830/142274848.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-07 at 01.26.36.png](attachments/142274830/142274849.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-07 at 01.29.37.png](attachments/142274830/142274850.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-07 at 01.30.51.png](attachments/142274830/142274851.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-07 at 01.39.53.png](attachments/142274830/142274852.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-07 at 01.41.28.png](attachments/142274830/142274853.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-07 at 01.44.02.png](attachments/142274830/142274854.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-07 at 01.45.06.png](attachments/142274830/142274855.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-07 at 01.46.03.png](attachments/142274830/142274856.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-07 at 01.50.02.png](attachments/142274830/142274857.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[image2019-12-20\_15-23-39.png](attachments/142274830/149336726.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-20 at 15.31.19.png](attachments/142274830/149336727.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-20 at 15.32.00.png](attachments/142274830/149336728.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-20 at 15.32.25.png](attachments/142274830/149336729.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-20 at 15.34.01.png](attachments/142274830/149336730.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-20 at 15.45.12.png](attachments/142274830/149336731.png)
(image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"} [Screenshot
2019-12-20 at 15.45.33.png](attachments/142274830/149336732.png)
(image/png)\
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
