---
title: "Acquiring and Sharing Data"
---



## Lab Policy: Where Data Lives

Per the [Hagan Lab Manual](https://github.com/HaganLab), these rules apply to all lab data, regardless of project:

* **Approved storage**: CCHMC **OneDrive** for documents and working files, and the **BMI HPC cluster** for large datasets and analyses (see [Working with the HPC](Working_with_hpc.html)). Analysis code belongs in the lab's **GitHub** repositories under version control.
* **Never store the only copy of anything locally.** Data must never exist only on a personal device, a personal cloud account, or a single local drive — institutional storage is backed up automatically, and you're responsible for making sure your work actually lands there.
* **PHI / sensitive human-subjects data** must be stored *only* in CCHMC-approved secure locations in accordance with HIPAA and our IRB protocol. It must never be placed on personal accounts, unsecured drives, or **external AI tools** (see [Using AI Tools](Using_AI_Tools.html) for what "external" means here).
* **Naming and organization**: use clear, consistent, descriptive file names and folder structure — e.g., dates in `YYYY-MM-DD` format, project identifiers, and version information.
* **Raw vs. processed**: keep raw data separate from processed data and never overwrite the raw data. Document the provenance of derived files (code + inputs) so any result can be traced back to the raw data that produced it.
* Use **Git** for version control of code — see [Git and GitHub](git_and_github.html).

The rest of this page covers the mechanics of moving and linking larger data objects once you know where they're supposed to live.

## Goals

* Keep shared data (including processed data and results) in a stable shared location
* Link to data instead of copying/moving data
* Incorporate data linking in your script  
* Treat processed data and results as "raw" data objects for sharing purposes
* Describe data: origin, what's been done with it, what the columns/rows mean, etc.
* Keep data files together with their metadata and any processing scripts when applicable, either physically or with a reliable link between them.

A good way to interact with data objects is in a manner similar to working with git for developing code: "pushing" and "pulling" data objects to and from remote repositories from within your working directory, scripting everything, instead of copying data manually into the project folder. This not only makes work easier, but also helps maintain data provenance and promotes transparency and reproducibility. GitHub repositories, however, are (currently) limited in size and are therefore not optimal for sharing large data objects and research projects. Instead we can use services such as Synapse and RStudio Connect and tools such as [Globus CLI](https://docs.globus.org) and the R [`pins` package](http://pins.rstudio.com). In addition to providing a way to incorporate data transfer in the script, these tools also manage the caching and check for updates before re-downloading data. The caching ensures that we still have the latest version available in our system in the case that the original becomes unavailable for whatever reason.

Sharing data between "native" projects on the same file system can be done using the R package `pins`. Sharing data among file systems can be done either directly with Globus or via servers such as Synapse and RStudio Connect, using either their own clients or `pins`.

To read more about data provenance and management:  
https://old.dataone.org/sites/all/documents/DataONE_BP_Primer_020212.pdf  
https://www.w3.org/2005/Incubator/prov/wiki/What_Is_Provenance  
https://docs.synapse.org/articles/provenance.html  

An example for a resource sharing plan to include in NIH grants: https://github.com/lab-carpentry/blueprint-resourcesharing/blob/master/examples/NIH-example.md
