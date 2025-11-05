# HND Digital Technologies for England (Cyber Security)
## Module 4: Programming Assignment - Task 1

>This repository holds my __"North Sussex Judo"__ programming project.
> Directions to set up and run the program are shown at the top.
>__Fictional Entities__
> AQ Digital Solutions and North Sussex Judo refer to the
> HND Vocational Scenario and are used for Assessment purposes.
> Any similarity to existing organisations is unintended, and should
> be considered in the spirit and context in which this project exists.

Jump to the **[North Sussex Judo Report](#Introducing-North-Sussex-Judo)**

### **Repository Information:** spatial-doodle

The latest version of this document and program is always available at:
`https://github.com/arumbold/spatial-doodle`

Details about what information is contained, and where to find it are here:
**[Repository Structure](docs/repository_structure.md)**

## License & Authorship Statement
Python Source Code, documents, branding & imagery in this repository
are published under the MIT Licence and are my own work.
See the [LICENCE](LICENCE) file for details.

## Installation Requirements

### Mandatory Technologies

**Python 3** (Tested with 3.8.10 and 3.12.10)

### Recommended Additions

**pip** (for add-on compatibility)
**git** (to obtain and update the latest code)
```
git clone https://github.com/arumbold/spatial-doodle.git
cd spatial-doodle
pip install -r requirements.txt

```

## Usage

To run the Graphical Application

> python src/main.py


To generate the monthly Training Fee Report
> python src/main.py report

Other Commands available can be run in the same way
> python  src/main.py *[command]*


```
Commands available:

   report       : Create the Athlete Training Fee Report
   diagnostic   : Checks the core program functions with known data
   help         : Show usage information
```

# Introducing North Sussex Judo

This project forms part of the __HND Digital Technologies For England (Cyber Security)__ programme.
It demonstrates the full project lifecycle from getting a design brief right through to the creation of a fully-featured UI driven application.

In industry, the requirements and information gathering would likely be considered a part of the development process, which is one area where making use of Agile Development would be at a clear advantage as compared to a more pre-structured, waterfall design. For this project, the requirements are already known and clear.

I will be implementing a hybrid approach - using Agile Principles and structured algorithm creation to create a feature-based development pipeline that makes use of Test Driven Development. Tests will be identified during the Algorithm process.

## Algorithm design

The choice and construction of the algorithms required for this project are intrinsincally linked to the features defined in the assessment brief.

The requirement "North Sussex Judo requires a program to capture the following information"(Assignment Brief, 2025, paraphrased) gives us a list of program inputs for our athlete.

We will use this list to begin defining the scope of our algorithm

### (START)

**[INPUT_data](docs/ATHLETE_data.md)**

This input data is our entry point into an algorithm that will transform this data and "output the following information"(Assignment Brief, 2025):

### [BEGIN PROCESS]

**[U](docs/INPUT_validation.md)**
**[INPUT_validation](docs/INPUT_validation.md)**
**[OUTPUT_validation](docs/OUTPUT_validation.md)**

### [END PROCESS]

**[OUTPUT_data](docs/OUTPUT_data.md)**


### (STOP)
This combination of input and output gives us the bounds for our program execution. We now have **(START)**, and **(END)**.


Supplemental data for **Process**
It's almost time to map the steps required to generate this, after defining some additional criteria:
> Ability to register additional athletes


Additional output specifics:



(flowcharts, pseudocode, explanation)

## Steps from algorithm to code
(process and justification of chosen language)

## Development process
(including challenges faced and how they were addressed)

## Debugging process and IDE features used
(breakpoints, step-through, error logs, monitoring)

## Coding standards applied and their importance

## Enhancements and optimisation of the algorithm

## Evaluation of algorithm vs final program, role of IDE, and coding standards

## Harvard-style in-text citations and full bibliography
