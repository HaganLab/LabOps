---
title: "Publishing"
author: "Amnah Siddiqa"
date: "2026-07-03"
---



## Lab Policy: Sharing Data and Code at Publication

Per the [Hagan Lab Manual](https://github.com/HaganLab), we are committed to open, reproducible science and to meeting the data-sharing requirements of journals and funders, including the **NIH Data Management and Sharing (DMS) Policy**. A few things to plan for from the start of a project, not just at submission time:

* **Discuss the data-sharing plan with the PI early.** Don't wait until a manuscript is in review to figure out where data and code will live.
* **Deposit data in an established, discipline-appropriate public repository** where possible (e.g., [GEO](https://www.ncbi.nlm.nih.gov/geo/), [SRA](https://www.ncbi.nlm.nih.gov/sra), [ImmPort](https://www.immport.org/), or others listed below) rather than only as a journal supplement.
* **Make analysis code available**, typically via the lab's GitHub, at the time of publication.
* If your project involves **human-subjects data**, any shared data must be appropriately de-identified and shared only in accordance with our IRB protocol and participant consent — check with the PI before sharing anything derived from PHI.
* Keep data and metadata organized and documented (see [Acquiring and Sharing Data](Acquiring_and_sharing_data.html)) throughout the project so that deposition at the end is straightforward rather than a scramble.

## Findable and Accessible: Where to publish?

* As a supplement: simple but not not standardized and easy to overlook, lose, and mishandle  
https://www.the-scientist.com/news-opinion/the-push-to-replace-journal-supplements-with-repositories--66296

* As a separate product:  
Increases accessibility and reproducibility, promotes detailed descriptions as well as credit  
  A DOI-issuing repository is better than URL for permanency  
  A registry of repositories: https://www.re3data.org/  
  Examples:  
    * Mendeley: centralized data repository, minimal description, not standardized  
    * Dryad: centralized data repository with peer review  
    * ResearchGate: social media for scientists  
    * Data-in-Brief: thorough and standardized description of data and methods  
    * MethodX: the nitty-gritty of the methods (computational and experimental)  
    * Github: for code mostly
    * Zenodo: for development and review as well as publication, integrates with github

## Running the nf-core RNA-seq Pipeline

Several lab projects use the [nf-core/rnaseq](https://nf-co.re/rnaseq) Nextflow pipeline for standardized, containerized, and reproducible RNA-seq analysis (see [Containerizing](Containerizing.html) for background on why these pipelines run in containers on the HPC cluster).

* [nf-core/rnaseq usage docs](https://nf-co.re/rnaseq/1.4.2/docs/usage)
* [Streamlined RNA-seq analysis using Nextflow (NYU Gencore)](https://gencore.bio.nyu.edu/streamlined-rna-seq-analysis-using-nextflow/)
