# findsymlat.f90

## Overview

  Finds the point group symmetries which leave the Bravais lattice invariant.
  Let $A$ be the matrix consisting of the lattice vectors in columns, then
  $$ g=A^{\rm T}A $$
  is the metric tensor. Any $3\times 3$ matrix $S$ with elements $-1$, 0 or 1
  is a point group symmetry of the lattice if $\det(S)$ is $-1$ or 1, and
  $$ S^{\rm T}gS=g. $$
  The first matrix in the set returned is the identity.

  Created January 2003 (JKD)
  Removed arguments and simplified, April 2007 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE findsymlat

## Important Variables/Constants

- `Integer :: i, j, md, sym (3, 3)` (No comment)
- `Integer :: i11, i12, i13, i21, i22, i23, i31, i32, i33` (No comment)
- `Integer :: i3mdet` (No comment)
- `Real (8) :: c (3, 3), v (3), t1` (No comment)
- `Real (8) :: r3taxi` (No comment)
- `Real (8) :: s (3, 3), g (3, 3), sgs (3, 3)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain

**Calls:**
- i3minv
- r3mm
- r3mtm
- r3mtv
