# gencore.f90

## Overview

  Computes the core radial wavefunctions, eigenvalues and densities. The
  radial Dirac equation is solved in the spherical part of the effective
  potential to which the atomic potential has been appended for
  $r>R^{\rm MT}$. In the case of spin-polarised calculations, the effective
  magnetic field is ignored.

  Created April 2003 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE gencore

## Important Variables/Constants

- `Integer :: is, ia, ja, ias, jas, ist, ir` (No comment)
- `Logical :: done (natmmax)` (No comment)
- `Real (8) :: t1` (No comment)
- `Real (8) :: vr (spnrmax)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- constants
- mod_atoms
- mod_corestate
- mod_muffin_tin
- mod_potential_and_density
- mod_symmetry
- modinput

**Calls:**
- rdirac
