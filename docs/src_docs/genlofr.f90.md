# genlofr.f90

## Overview

  Generates the local-orbital radial functions. This is done by integrating
  the scalar relativistic Schr\"{o}dinger equation (or its energy deriatives)
  at the current linearisation energies using the spherical part of the
  effective potential. For each local-orbital, a linear combination of
  {\tt lorbord} radial functions is constructed such that its radial
  derivatives up to order ${\tt lorbord}-1$ are zero at the muffin-tin radius.
  This function is normalised and the radial Hamiltonian applied to it. The
  results are stored in the global array {\tt lofr}.

  Created March 2003 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE genlofr

## Important Variables/Constants

- `Integer :: ilo, io1, io2` (No comment)
- `Integer :: is, ia, ias, nr, ir` (No comment)
- `Integer :: j, l, nn, info, np` (No comment)
- `Integer, Allocatable :: ipiv (:)` (No comment)
- `Real (8) :: hp0 (nrmtmax)` (No comment)
- `Real (8) :: p0 (nrmtmax, maxlorbord), p1 (nrmtmax,maxlorbord)` (No comment)
- `Real (8) :: p0s (nrmtmax), p1s (nrmtmax) ,q0s (nrmtmax), q1s (nrmtmax)` (No comment)
- `Real (8) :: polynom` (No comment)
- `Real (8) :: q0 (nrmtmax, maxlorbord), q1 (nrmtmax, maxlorbord)` (No comment)
- `Real (8) :: t1` (No comment)
- `Real (8), Allocatable :: a (:, :), b (:), c (:)` (No comment)
- `Real (8), Allocatable :: xa (:), ya (:)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain

**Calls:**
- dgesv
- fderiv
- rdirac
- rschroddme
