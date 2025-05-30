# genapwfr.f90

## Overview

  Generates the APW radial functions. This is done by integrating the scalar
  relativistic Schr\"{o}dinger equation (or its energy deriatives) at the
  current linearisation energies using the spherical part of the effective
  potential. The number of radial functions at each $l$-value is given by the
  variable {\tt apword} (at the muffin-tin boundary, the APW functions have
  continuous derivatives up to order ${\tt apword}-1$). Within each $l$, these
  functions are orthonormalised with the Gram-Schmidt method. The radial
  Hamiltonian is applied to the orthonormalised functions and the results are
  stored in the global array {\tt apwfr}.

  Created March 2003 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE genapwfr

## Important Variables/Constants

- `Integer :: is, ia, ias, nr, ir` (No comment)
- `Integer :: nn, l, io1, io2` (No comment)
- `Real (8) :: hp0 (nrmtmax)` (No comment)
- `Real (8) :: q0 (nrmtmax, apwordmax), q1 (nrmtmax, apwordmax)` (No comment)
- `Real (8) :: t1` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain

**Calls:**
- fderiv
- rschroddme
