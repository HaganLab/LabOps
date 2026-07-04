---
title: "Organizing Projects"
author: "Amnah Siddiqa"
date: "2026-07-03"
---


## FAIR Principles

Good project organization is what makes your work **F**indable, **A**ccessible, **I**nteroperable, and **R**eusable (FAIR) — both for collaborators now and for your future self returning to a project months later. Two conventions from the [Hagan Lab Manual](https://github.com/HaganLab) that apply to every project, computational or otherwise:

* Use dates in **`YYYY-MM-DD`** format in file and folder names so they sort chronologically, along with a project identifier and version information where relevant.
* Keep raw data separate from processed data and scripts, and never overwrite raw data — treat it as read-only (see [Acquiring and Sharing Data](Acquiring_and_sharing_data.html)).

**Rules of thumb for [a project-oriented workflow](https://rstats.wtf/project-oriented-workflow.html):**

* Set up your project folder as a formal R project in RStudio, or the equivalent in other IDEs
  * In Rstudio: set 'save workspace on exit' to 'never' (Preferences -> General)
* Use standardized naming and structure following [community conventions](https://community.rstudio.com/t/best-practice-for-good-documented-reproducible-analysis/1995/)
* Keep raw data separate from scripts and output (more details in [Acquiring and Sharing Data](Acquiring_and_sharing_data.html)
* Treat input data as read-only and output as disposable. [Script everything](https://kbroman.org/steps2rr/pages/scripts.html), and [save scripts, not workspaces](https://rstats.wtf/save-source.html)  
* Include a “dumbed-down” [README file](https://data.research.cornell.edu/content/readme) as a walk-through (maybe a flow chart; maybe md file)  
* Include a license file as needed; CC-0 and CC-BY are [commonly used](https://blog.datadryad.org/2017/09/11/some-dos-and-donts-for-cc0/)  
* If your project involves working on several file systems, it's a good idea to duplicate whole project folders, not bits and pieces of data/code.  
  * You can sync your local copy with Box/Dropbox for extra backup and version control (note: box doesn't work with RStudio projects).
  * Options for synchronizing your local and remote copies: Globus, FileZila

  
  
  
  
