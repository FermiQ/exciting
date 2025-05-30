# findprim.f90

## Overview

  This routine finds the smallest primitive cell which produces the same
  crystal structure as the conventional cell. This is done by searching
  through all the vectors which connect atomic positions and finding those
  which leave the crystal structure invariant. Of these, the three shortest
  which produce a non-zero unit cell volume are chosen.

  Created April 2007 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE findprim

## Important Variables/Constants

- `Integer :: i, j, n, na` (No comment)
- `Integer :: i1, i2, i3, iv (3)` (No comment)
- `Integer :: is, js, ia, ja, ka` (No comment)
- `Real (8) :: apl (3, maxatoms)` (No comment)
- `Real (8) :: r3taxi` (No comment)
- `Real (8) :: t1, t2` (No comment)
- `Real (8) :: v1 (3), v2 (3), v3 (3)` (No comment)
- `Real (8), Allocatable :: distance (:)` (No comment)
- `Real (8), Allocatable :: vp (:, :)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain

**Calls:**
- r3cross
- r3frac
- r3minv
- r3mv
