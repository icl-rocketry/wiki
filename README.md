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

*CSS:*

There is a  `styles` folder which contains the css, and therefore the look and feel of the website. It is likely that we have worked on the css file, and therefore you should have kept the original. Either be careful about this when loading in the wiki, or simple remove these particular changes from github.

At the moment, there are no css changes, and as such it doesn't matter.

*Two column layout:*

A simple trick to aid navigating the wiki is to have two columns. Confluence's exported `index.html` contains links to each of the wiki articles in a nice tree structure. unfortunately, this is hard-coded. Therefore we use this simple trick:

A) rename `index.html` to `index_menu.html`

B) create a new `index.html` file (the code can be copied over from `template_index_two_cols.html`). This file sets up the two columns.

C) We need to change each html file, since they all have a nav bar at the top and the link points to `index.html`. It should point to `index_menu.html`, and so we use a simple bash/perl script to change all the files at once. I've only tested this on a mac. Navigate to the root directory of the wiki, and run this command:

`perl -pi -w -e 's/index.html/index_menu.html/g;' *.html`

D) In `index_menu.html`, we need all the links to open in the right frame. To do this, we change the default link load position of the links by adding

`<base target="content">`

within the `<head></head>` tags.

Note, unfortunately frames are no longer supported by HTML5, and I really shouldn't be doing this at all. Until I find another way though...

9) Push the changes to the github repo, and the new website should work.



How does this work?

Confluence effectively exports a website. all the images and text are already included in the folder. Therefore when github is asked to render the webiste, it simply finds the `index.html` file in the folder and renders it on your browser. As you click links, it is just navigating your github repo.
