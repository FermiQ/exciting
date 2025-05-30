# findkpt.f90

## Overview

*No overview extracted.*

## Key Components

- SUBROUTINE findkpt

## Important Variables/Constants

- `Integer :: lspl, iv (3)` (No comment)
- `Integer, Intent (Out) :: ik` (No comment)
- `Integer, Intent (Out) :: isym` (No comment)
- `Real (8) :: s (3, 3), v1 (3), v2 (3), t1` (No comment)
- `Real (8), Intent (In) :: vpl (3)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- mod_kpoint
- mod_symmetry
- modinput

**Calls:**
- r3frac
- r3mtv
