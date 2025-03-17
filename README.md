# Magnetic Tweezers Data Analysis

## Caleb Maddry

## Description
This repository contains my data analysis code for my magnetic tweezers. I have force calibration scripts, data, and data analysis notebooks in here. This NOT a comprehensive repository and is often used as a quick way to generate graphs and figures to look at data. 

At some point I will formalize the code, but for now it is a bit messy. I'm the only person that uses it currently.

## Code
Here is the code structure of this repository:

``` shell
.
├── Data
├── Scripts
└── dataAnalysisScripts
```
### [Data](Data)
This contains most of the good data that I have been looking at. The structure is pretty simple and is basically split up into when I took the data. 

``` shell
.
├── 2024
│   ├── December
│   │   └── 19
│   └── October
│       └── 6
└── 2025
    ├── January
    │   └── 7
    └── March
        └── 1
```
The subfolders then have names associated to the assay conditions (whether or not BSA was used, what kind of beads were used, etc.). I will be adding some textfiles in each directory to explain what the conditions were more thoroughly. The text files containing the actual data are then in teh subfolders. 

### [Scripts](Scripts )
This folder contains some older test scripts and data analysis scripts. I also worked on building a more robust Python package in here. That code is [here]("Scripts/Caleb/AutoScriptTestModular.ipynb"). I then later moved it to the next [section](/dataAnalysisScripts/calibration) in a more robust package and analysis workflow. I mainly just keep this folder around so that I can look at old data and use parts of the code in here for reference. 


### [Data Analysis Scripts](dataAnalysisScripts)
This is the main way that I look at data. I created the [calibration](dataAnalysisScripts/calibration) Python package. This is then used in the analysis notebooks which are just named of what data folder they are looking at. This package isn't the most robust (limited edge case testing), but I will hopefully be changing this in the future. Now that I have good data, it should be a lot easier to do this. 

 
