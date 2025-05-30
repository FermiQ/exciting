# gendmat_nospin.f90

## Overview

*No overview extracted.*

## Key Components

- SUBROUTINE gendmat_nospin

## Important Variables/Constants

- `Complex (8), Allocatable :: wfmt2 (:, :, :)` (No comment)
- `Complex (8), Intent (In) :: apwalm( ngkmax, apwordmax, lmmaxapw, natmtot, nspnfv)` (No comment)
- `Complex (8), Intent (In) :: evecfv( nmatmax, fst:lst, nspnfv)` (No comment)
- `Complex (8), Intent (Out) :: dmat( ld, ld, fst:lst)` (No comment)
- `Integer :: i, j, n, ist, irc` (No comment)
- `Integer :: l, m1, m2, lm1, lm2` (No comment)
- `Integer :: lmmax` (No comment)
- `Integer, Intent (In) :: ia` (No comment)
- `Integer, Intent (In) :: is` (No comment)
- `Integer, Intent (In) :: ld` (No comment)
- `Integer, Intent (In) :: lmax` (No comment)
- `Integer, Intent (In) :: lmin, fst, lst` (No comment)
- `Integer, Intent (In) :: ngp` (No comment)
- `Real (8) :: fr1 (nrcmtmax), fr2 (nrcmtmax)` (No comment)
- `Real (8) :: gr (nrcmtmax), cf (3, nrcmtmax)` (No comment)
- `Real (8) :: t1, t2` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain

**Calls:**
- fderiv
- wavefmt
