# Workout diary / Workout tracker / WOLog (Work Out Log)

## Problem definition
I want to track my workout progress.

## Requirements
* An initial program is okay, but the programming should be adjustable
  in the long run. A program is a curated set of exercises tailored for a
  specific goal, targeting the large muscle groups across the whole body.
* Workout sessions should be saved, so that they can be recalled later.
* The application should suggest next workout, based on previous workout log.
* The application should show compare an entry to the previous entry with the
  same exercises, and display the change in % (number of sets/reps/weight).
* The application should show progress compared to last max test results.
* The progress should be linked to an overarching goal (increase max weight?).
* The source code should be well-written and the application fully documented.
* The application should have more than 90 % test coverage.

## Tools, targets, backup plan
I'm writing this application for my own use, as I find it a little tedious to
calculate and write down each workout the night before. I will still do this,
I just want something to display automatically what my next workout is going to
be, and remind me of my goals.

If at all, the application will be published as part of my own blog. 

The application will be written in Python, using the Flask and pytest frameworks.
Source code will be kept in a git resository, with backups to github or gitlab.

## Structure - breakdown
* Track workouts
** Define who we are tracking _for_.
*** We track for a person.
**** A person has a name, an age and a weight.
**** A person has a given max for any given exercise.

** Define a workout program
*** Starts with a warmup routine
**** Warmup routines consist of one or more exercises of type warmup or mobility.

*** Proceeds with sets of main exercises
**** Exercises have names.
**** Exercises have types: strength, stretching, warmup, mobility.
**** Exercises have target muscle(s).
**** Exercises have antagonist muscle(s).
**** Exercises have max load

*** Ends with a stretching routine.
**** Stretching exercises have protagonist and antagonist muscles as well.

## Sequences of events
1. Get next workout
  1. Get previous workout
  1. Add expected progress
  1. Adjust weight after progress addition to match available weights
     - Barbell style: Increment by 2.5 kg
     - Dumbbell style: Increment by 1 kg for 1-10 kg range, 2 kg for > 10.
  1. 

