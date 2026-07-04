---
title: "Git and GitHub"
---



## Lab Policy: Why We Use Git

Per the [Hagan Lab Manual](https://github.com/HaganLab), analysis code should be version-controlled and uploaded to the lab's GitHub repositories — this is part of maintaining reproducible, well-documented records that anyone in the lab (including your future self) can pick up. Documented analysis pipelines and coding conventions are maintained under [github.com/HaganLab](https://github.com/HaganLab) and the HaganLab HPC folder; if you're using an AI coding assistant to help write analysis code, the same expectations apply — see [Using AI Tools](Using_AI_Tools.html).

## Set up Git and GitHub

There are plenty of resources out there to help you configure Git and GitHub in more depth — the steps below are just enough to get you started.

### For Mac
Use this command to download git 👉 `brew install git`

Then verify it installed correctly: `git --version`

### For Linux (Ubuntu)
Use this command to download git 👉 `sudo apt-get install git`

## Create an account on GitHub and create a new repo

https://github.com/

- Create a new repo by clicking "New repository"

![Creating a new repository on GitHub](https://github.com/amnahsiddiqa/Docker_Singularity_HPC_Stuffs/assets/28387956/bacf34a6-81be-4285-8dff-327bb431d509)

## Clone Repo

```
mkdir projectname

git clone <repo-url>
```
## Configure Git

```
git config --global user.name "amnahsiddiqa"
git config --global user.email "amnahsiddiqa@gmail.com"

# confirm your config
git config -l
```

## Make changes to remote

Remember the order: add, commit, pull, push :)

```
# Stage all changes in the current directory
git add .

# Stage a specific file, e.g., filename.tsv
git add filename.tsv

# Commit your changes with a meaningful message
git commit -m "Add analysis for Figure 1"

# Fetch and integrate changes from the remote repository
git pull

# Push your committed changes to the remote repository
git push

```

See more beginner's tips [here](https://render.com/blog/git-organized-a-better-git-flow)

## How do I go back from my current state to a snapshot made on a certain commit?
There are two types of commands, and you should choose carefully between them based on their purpose: `git reset` and `git revert`.

- `git reset` is a rewind call: it moves your branch's history back to a specific commit, and everything after that point is gone from the branch's timeline.

- `git revert`, on the other hand, undoes the changes made in a given commit by creating a new commit that is the reverse (reciprocal) of it — nothing is removed from history.

```
(base) ➜  test_demo2 git:(main) ✗ git reset 3bbe6d4 --hard
# output: HEAD is now at 3bbe6d4 Initial commit
(base) ➜  test_demo2 git:(main) ✗ git reset --soft "HEAD@{1}"
(base) ➜  test_demo2 git:(main) ✗ git commit -m "Revert to 3bbe6d4"

```

## Issues and commits for better collaboration

- Reference an issue's number in a commit message (e.g. `Fixes #12`) to automatically close it when the commit is merged.
- Use issues to ask for help or to track work that needs doing.

## Terminology

**Commit SHA (Secure Hash Algorithm) key** — commonly referred to as a "commit hash" or "commit SHA-1," this is a unique identifier for a specific commit in a version control system such as Git. It's a cryptographic hash value generated from the commit's contents and metadata, and it's used to uniquely identify and reference a particular state or snapshot of a repository at a specific point in time.
