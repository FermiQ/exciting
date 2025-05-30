# checkmt.f90

## Overview

  Checks for overlapping muffin-tins. If any muffin-tins are found to
  intersect the program is terminated with error.

  Created May 2003 (JKD)
  Revised October 2014 (PAS)
EOP
BOC

## Key Components

- SUBROUTINE checkmt

## Important Variables/Constants

- `Integer :: i1, i2, i3` (No comment)
- `Integer :: ia, is, ja, js` (No comment)
- `Real (8) :: t1, t2` (No comment)
- `Real (8) :: v1(3), v2(3), v3(3)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain

**Calls:**
- *None identified.*
