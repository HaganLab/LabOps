---
title: "Containerizing"
---



## Why Containers?

Containers package up code together with all of its dependencies (specific versions of tools, libraries, and OS-level packages) so that an analysis runs the same way regardless of which machine — your laptop, a labmate's laptop, or the HPC cluster — it runs on. This is central to reproducibility: a pipeline that only works because of something you happened to install on your own machine two years ago isn't something anyone else (including future you) can rerun.

## Docker vs. Singularity/Apptainer

* **Docker** is the most common tool for *building* and running containers locally, and most published container images are distributed as Docker images. However, Docker requires a background daemon running with elevated privileges, which shared, multi-user HPC systems generally don't allow for security reasons.
* **Singularity** (now also distributed as **Apptainer**) is the container runtime used on the CCHMC HPC cluster instead. It can pull and run existing Docker images without needing root access, which is why you'll see it referenced in the [Working with the HPC](Working_with_hpc.html) page (`module load singularity/3.7.0`).

In practice, for most lab work you won't need to build your own containers — you'll pull existing, well-maintained images (e.g., from [nf-core](https://nf-co.re/) pipelines, which auto-pull the containers they need, or from [Bioconda](https://bioconda.github.io/)/[Biocontainers](https://biocontainers.pro/)) rather than writing your own `Dockerfile`.

## Using a Container on the HPC


``` bash
# Load the module
module load singularity/3.7.0

# Pull a container image (example)
singularity pull docker://some-org/some-tool:latest

# Run a command inside the container
singularity exec some-tool_latest.sif some-command --args
```

nf-core pipelines handle this pulling and execution automatically when you point Nextflow at the `singularity` profile — you generally don't need to do this manually unless you're troubleshooting or running a tool outside of an existing pipeline.

## Running the nf-core RNA-seq Pipeline

Several lab projects use the [nf-core/rnaseq](https://nf-co.re/rnaseq) Nextflow pipeline for standardized, containerized, and reproducible RNA-seq analysis, using the container mechanics above.

* [nf-core/rnaseq usage docs](https://nf-co.re/rnaseq/1.4.2/docs/usage)
* [Streamlined RNA-seq analysis using Nextflow (NYU Gencore)](https://gencore.bio.nyu.edu/streamlined-rna-seq-analysis-using-nextflow/)

### In Progress

* Building custom images with a `Dockerfile` for lab-specific tools
* Converting a Docker image to a Singularity `.sif` file for the HPC
