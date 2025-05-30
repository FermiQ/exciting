# findsymcrys.f90

## Overview

  Finds the complete set of symmetries which leave the crystal structure
  (including the magnetic fields) invariant. A crystal symmetry is of the
  form $\{\alpha_S|\alpha_R|{\bf t}\}$, where ${\bf t}$ is a translation
  vector, $\alpha_R$ is a spatial rotation operation and $\alpha_S$ is a
  global spin rotation. Note that the order of operations is important and
  defined to be from right to left, i.e. translation followed by spatial
  rotation followed by spin rotation. In the case of spin-orbit coupling
  $\alpha_S=\alpha_R$. In order to determine the translation vectors, the
  entire atomic basis is shifted so that the first atom in the smallest set of
  atoms of the same species is at the origin. Then all displacement vectors
  between atoms in this set are checked as possible symmetry translations. If
  the global variable {\tt tshift} is set to {\tt .false.} then the shift is
  not performed. See L. M. Sandratskii and P. G. Guletskii, {\it J. Phys. F:
  Met. Phys.} {\bf 16}, L43 (1986) and the routine {\tt findsym}.

  Created April 2007 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE findsymcrys

## Important Variables/Constants

- `Integer :: ia, ja, is, js, i, n` (No comment)
- `Integer :: isym, nsym, iv (3)` (No comment)
- `Integer :: lspl (48), lspn (48)` (No comment)
- `Integer, Allocatable :: iea (:, :, :)` (No comment)
- `Real (8) :: v (3), t1` (No comment)
- `Real (8), Allocatable :: vtl (:, :)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain
- modxs

**Calls:**
- findsym
- r3frac
- r3mv
