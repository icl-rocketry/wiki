# wiki
Hosts the wiki publicly.


# how to get it to this stage:

1) Go to the wiki (https://wiki.imperial.ac.uk/display/IRW/ICL+Rocketry+Wiki+Home)

2) Go to `Space Tools` (bottom left corner)

3) Click on `Content Tools`

4) Click on `Export`

5) Click on `HTML`, and export using the normal export option. (I haven't tried to export using the custom export yet)

6) Allow the link to be generated, and then download the zip folder.

7) Clone the ICLR wiki github repo to a folder on your computer.

8) Uncompress the downloaded zip folder and drag all its contents into the github repo. Replace all the files that were already there.

There is a  `styles` folder which contains the css, and therefore the look and feel of the website. It is likely that we have worked on the css file, and therefore you should have kept the original. Either be careful about this when loading in the wiki, or simple remove these particular changes from github.

At the moment, there are no css changes, and as such it doesn't matter.

9) Push the changes to the github repo, and the new website should work.


How does this work?

Confluence effectively exports a website. all the images and text are already included in the folder. Therefore when github is asked to render the webiste, it simply finds the `index.html` file in the folder and renders it on your browser. As you click links, it is just navigating your github repo.
