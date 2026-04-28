# Congruity Ride Gate Demo

This repository contains a public 3.0 Lite demonstration of a Congruity Gate applied to transport decisions.

The demo evaluates whether a proposed ride is economically and logistically coherent before execution.

It does not merely optimize an accepted action.  
It asks whether the action should exist in the first place.

## Core idea

A proposed transport action is evaluated through a simple proportionality score:

Congruity Score = Value / Systemic Cost

Where:

- Value = price or useful output
- Systemic Cost = energy cost + impact cost + structural cost

## Decision states

EXECUTE   = coherent action  
SIMPLIFY  = borderline action requiring correction  
REJECT    = incoherent action  

## Example

A ride with:

- 80 km from depot to pickup  
- 75 km of service  
- 75 km return  
- €120 price  
- €290 estimated systemic cost  

produces:

Congruity Score = 120 / 290 = 0.414  
Decision = REJECT  

The system may suggest:

- use a closer operator  
- increase the price  
- simplify the action  

## Why this matters

Most systems optimize actions after they are already accepted.

A Congruity Gate introduces an ex-ante admissibility layer:

detect → evaluate → decide → prevent or simplify

## Run locally

pip install -r requirements.txt  
uvicorn main:app --reload  

Then open:

http://127.0.0.1:8000/docs
