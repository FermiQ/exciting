# addrhocr.f90

## Overview

  Adds the core density to the muffin-tin and interstitial densities. A
  uniform background density is added in the interstitial region to take into
  account leakage of core charge from the muffin-tin spheres.

  Created April 2003 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE addrhocr

## Important Variables/Constants

- `Integer :: is, ia, ias, ir` (No comment)
- `Real (8) :: fr (nrmtmax), gr (nrmtmax), cf (3, nrmtmax)` (No comment)
- `Real (8) :: t1, sum1, sum2` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- constants
- modmain

**Calls:**
- fderiv
