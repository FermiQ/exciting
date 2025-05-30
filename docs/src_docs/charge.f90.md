# charge.f90

## Overview

  Computes the muffin-tin, interstitial and total charges by integrating the
  density.

  Created April 2003 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE charge

## Important Variables/Constants

- `Integer :: is, ia, ias, ir` (No comment)
- `Real (8) :: fr (nrmtmax), gr (nrmtmax), cf (3, nrmtmax)` (No comment)
- `Real (8) :: sum, t1` (No comment)
- `character(1024) :: message` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- constants
- modinput
- modmain

**Calls:**
- fderiv
- warning
