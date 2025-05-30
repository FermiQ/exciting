# gendmat.f90

## Overview

*No overview extracted.*

## Key Components

- SUBROUTINE gendmat

## Important Variables/Constants

- `Complex (8), Allocatable :: wfmt1 (:, :, :, :)` (No comment)
- `Complex (8), Allocatable :: wfmt2 (:, :, :)` (No comment)
- `Complex (8), Intent (In) :: evecfv (nmatmax, nstfv, nspnfv)` (No comment)
- `Complex (8), Intent (In) :: evecsv (nstsv, nstsv)` (No comment)
- `Integer :: i, j, n, ist, irc` (No comment)
- `Integer :: ispn, jspn, lmmax` (No comment)
- `Integer :: l, m1, m2, lm1, lm2` (No comment)
- `Integer, Intent (In) :: ia` (No comment)
- `Integer, Intent (In) :: is` (No comment)
- `Integer, Intent (In) :: ld` (No comment)
- `Integer, Intent (In) :: lmax` (No comment)
- `Integer, Intent (In) :: lmin` (No comment)
- `Integer, Intent (In) :: ngp (nspnfv)` (No comment)
- `Logical, Allocatable :: done (:, :)` (No comment)
- `Logical, Intent (In) :: tlmdg` (No comment)
- `Logical, Intent (In) :: tspndg` (No comment)
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
- zaxpy
