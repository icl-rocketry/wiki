::: {#page}
::: {#main .aui-page-panel}
::: {#main-header}
::: {#breadcrumb-section}
1.  [ICL Rocketry Wiki](index.html)
2.  [ICL Rocketry Wiki Home](ICL-Rocketry-Wiki-Home_142270843.html)
3.  [Electronics & Payload Team](142271011.html)
4.  [Test Logs](Test-Logs_149336890.html)
:::

[ ICL Rocketry Wiki : RFM96 Range Test 2019-11-23 ]{#title-text} {#title-heading .pagetitle}
================================================================
:::

::: {#content .view}
::: {.page-metadata}
Created by [ Kacker, Shreeyam]{.author}, last modified by [ Bella,
Daniele V]{.editor} on Dec 07, 2019
:::

::: {#main-content .wiki-content .group}
::: {.contentLayout2}
::: {.columnLayout .single layout="single"}
::: {.cell .normal type="normal"}
::: {.innerCell}
General Information {#RFM96RangeTest2019-11-23-GeneralInformation}
-------------------

### Team Members Present {#RFM96RangeTest2019-11-23-TeamMembersPresent}

-   Shreeyam Kacker
-   Luis Marques
-   Daniele Bella

Travelled distance: 1000m

Link budget (Rx sensitivity): -148 dBm

Initial RSSI: -24 dBm

Tx power: 20 dBm (0.1 W)

\

\
:::
:::
:::

::: {.columnLayout .single layout="single"}
::: {.cell .normal type="normal"}
::: {.innerCell}
Method {#RFM96RangeTest2019-11-23-Method}
------

It was a cloudy and somewhat miserable looking afternoon, as the members
entered the Wormwood Scrubs park. The transmitter was given to Shreeyam
and Luis, whilst Daniele used his laptop to monitor the receiver. After
a brief test to make sure everything was still working, and to find the
RSSI at zero distance, the transmitter and receiver were turned on, and
the two groups walked away from each other in opposite directions.

Daniele was simultaneously holding a netbook, an umbrella, and a jumbled
mess of wires that was the packet receiver, so he stopped at a nearby
bench soon after. That bench had coordinates 51.52025N, 0.24689W.

Meanwhile, Shreeyam and Luis kept on walking, until they reached the end
of the park at coordinates 51.522640, -0.232961. Afterwards, they
switched off the transmitter and walked back to meet Daniele at the
bench.
:::
:::
:::

::: {.columnLayout .two-left-sidebar layout="two-left-sidebar"}
::: {.cell .aside type="aside"}
::: {.innerCell}
Results {#RFM96RangeTest2019-11-23-Results}
-------

The final positions, by complete and utter coincidence, happen to be
exactly 1000m apart.

For the analysis, the distance for each packet was calculated by
assuming that both groups walked at the same speed.

This lead to the graph found to the right.

The curve of best fit for the lower flat section has the equation:

\$RSSI=-(\\log\_{10}(1.306\\times10\^7 d + 1.601\\times10\^{10}))\^2\$

\

where \$d\$ is the distance.
:::
:::

::: {.cell .normal type="normal"}
::: {.innerCell}
[![](attachments/142272831/142274262.png){.confluence-embedded-image
width="600"}]{.confluence-embedded-file-wrapper
.confluence-embedded-manual-size}

\
:::
:::
:::

::: {.columnLayout .two-right-sidebar layout="two-right-sidebar"}
::: {.cell .normal type="normal"}
::: {.innerCell}
Analysis and Discussion {#RFM96RangeTest2019-11-23-AnalysisandDiscussion}
-----------------------

The table to the right shows some values of the RSSI obtained using the
curve of best fit. The values that are obtained are more optimistic than
my study plan.

Doubling the distance should lead to half of the transmission power.
Thus, it should lead to a difference of \$20\\log\_{10}(\\frac{1}{2}) =
3\$ dBm. However, in our case, doubling the distance  leads to about a
3.5 dB drop. This is quite optimistic.

The prediction also puts the max range of the antenna at over 60 km.
This is probably wrong.

This is likely due to the data having a bizarre distribution, as seen in
the graph.

The \"kink\" is likely due to the transmitter and receiver both moving
away from each other at the start of the experiment. This was corrected
using the code by setting doubling the speed before the kink, but it
didn\'t help much.

The \"kink\" also led to the curve of best fit being found only for the
latter half of the experiment.

The noise in the data is partly due to the fact that the members were
holding the antennas in their hands, trying to keep it upwards. This
lead to inconsistency in how the antenna was held, and in its height
above the ground.

### Lessons Learnt {#RFM96RangeTest2019-11-23-LessonsLearnt}

-   Orientation of the antennas should be accurately controlled
-   Receiver should stay stationary
-   Transmitter and altimeter height should not vary significantly
:::
:::

::: {.cell .aside type="aside"}
::: {.innerCell}
::: {.table-wrap}
  Distance (km)   Best Fit Predicted RSSI (dBm)
  --------------- -------------------------------
  0.5             -107.2
  1.0             -109.48
  1.5             -111.3
  2.0             -112.9
  2.5             -114.2
  3.0             -115.4
  60.0            -141.7
:::
:::
:::
:::

::: {.columnLayout .single layout="single"}
::: {.cell .normal type="normal"}
::: {.innerCell}
Raw data and Code {#RFM96RangeTest2019-11-23-RawdataandCode}
-----------------

### Raw data {#RFM96RangeTest2019-11-23-Rawdata}

[rawRadioData.txt](attachments/142272831/142274263.txt) was directly
obtained from the serial monitor.

[uncorruptedRadioData.txt](attachments/142272831/142274264.txt) contains
the raw data edited to remove corrupted data packets and startup
sequence of ESP32. The latter was perhaps not necessary due to how the
code was written, but was done as a precaution.

### Code {#RFM96RangeTest2019-11-23-Code}

#### ESP32 code used {#RFM96RangeTest2019-11-23-ESP32codeused}

[LoRaSenderMod.ino](attachments/142272831/142274268.ino) and
[LoRaReceiverBasic.ino](attachments/142272831/142274267.ino) were run on
the transmitter and receiver respectively during the test.

#### Data analysis {#RFM96RangeTest2019-11-23-Dataanalysis}

[radioAnalysis.py](attachments/142272831/142274265.py) was written in
Python to import the raw data, remove extraneous sections, find the line
of best fit, and plot the graph. It uses Python 3.8.0, numpy 1.17.4, and
matplotlib 3.1.1.
:::
:::
:::
:::
:::

::: {.pageSection .group}
::: {.pageSectionHeader}
Attachments: {#attachments .pageSectionTitle}
------------
:::

::: {.greybox align="left"}
![](images/icons/bullet_blue.gif){width="8" height="8"}
[Final.svg](attachments/142272831/142274261.svg) (image/svg+xml)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[Final.png](attachments/142272831/142274262.png) (image/png)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[rawRadioData.txt](attachments/142272831/142274263.txt) (text/plain)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[uncorruptedRadioData.txt](attachments/142272831/142274264.txt)
(text/plain)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[radioAnalysis.py](attachments/142272831/142274265.py)
(application/octet-stream)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[LoRaReceiverMod.ino](attachments/142272831/142274266.ino)
(application/octet-stream)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[LoRaReceiverBasic.ino](attachments/142272831/142274267.ino)
(application/octet-stream)\
![](images/icons/bullet_blue.gif){width="8" height="8"}
[LoRaSenderMod.ino](attachments/142272831/142274268.ino)
(application/octet-stream)\
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
