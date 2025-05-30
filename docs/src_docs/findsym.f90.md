# findsym.f90

## Overview

  Finds the symmetries which rotate one set of atomic positions into another.
  Both sets of positions differ only by a translation vector and have the same
  muffin-tin magnetic fields (stored in the global array {\tt bfcmt}). Any
  symmetry element consists of a spatial rotation of the atomic position
  vectors followed by a global magnetic rotation: $\{\alpha_S|\alpha_R\}$. In
  the case of spin-orbit coupling $\alpha_S=\alpha_R$. The symmetries are
  returned as indices of elements in the Bravais lattice point group. An
  index to equivalent atoms is stored in the array {\tt iea}.

  Created April 2007 (JKD)
  Fixed use of proper rotations for spin, February 2008 (L. Nordstrom)
EOP
BOC

## Key Components

- SUBROUTINE findsym

## Important Variables/Constants

- `Integer :: is, ia, ja, iv (3), md` (No comment)
- `Integer :: isym, jsym, jsym0, jsym1` (No comment)
- `Integer :: jea (natmmax, nspecies)` (No comment)
- `Integer, Intent (Out) :: iea (natmmax, nspecies, 48)` (No comment)
- `Integer, Intent (Out) :: lspl (48)` (No comment)
- `Integer, Intent (Out) :: lspn (48)` (No comment)
- `Integer, Intent (Out) :: nsym` (No comment)
- `Real (8) :: apl3 (3, natmmax)` (No comment)
- `Real (8) :: r3taxi` (No comment)
- `Real (8) :: sl (3, 3), v (3), t1` (No comment)
- `Real (8), Intent (In) :: apl1 (3, maxatoms, maxspecies)` (No comment)
- `Real (8), Intent (In) :: apl2 (3, maxatoms, maxspecies)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain

**Calls:**
- r3frac
- r3mv
