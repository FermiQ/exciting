# genexpiqr.f90

## Overview

*No overview extracted.*

## Key Components

- SUBROUTINE genexpiqr

## Important Variables/Constants

- `Complex (8), Allocatable :: apwalm1 (:, :, :, :)` (No comment)
- `Complex (8), Allocatable :: apwalm2 (:, :, :, :)` (No comment)
- `Complex (8), Allocatable :: em (:, :)` (No comment)
- `Complex (8), Allocatable :: evecfv1 (:, :)` (No comment)
- `Complex (8), Allocatable :: evecfv2 (:, :)` (No comment)
- `Complex (8), Allocatable :: evecsv1 (:, :)` (No comment)
- `Complex (8), Allocatable :: evecsv2 (:, :)` (No comment)
- `Complex (8), Allocatable :: sfacgkq (:, :)` (No comment)
- `Complex (8), Allocatable :: wfir (:)` (No comment)
- `Complex (8), Allocatable :: wfmt1 (:, :)` (No comment)
- `Complex (8), Allocatable :: wfmt2 (:, :, :)` (No comment)
- `Complex (8), Allocatable :: wfmt3 (:, :)` (No comment)
- `Complex (8), Allocatable :: zfir1 (:)` (No comment)
- `Complex (8), Allocatable :: zfir2 (:)` (No comment)
- `Complex (8), Intent (Out) :: emat (nstsv, nstsv)` (No comment)
- `Integer :: i, j, k, l, ispn` (No comment)
- `Integer :: is, ia, i1, i2, i3, iv (3)` (No comment)
- `Integer :: l1, l2, l3, m1, m2, m3` (No comment)
- `Integer :: lm1, lm2, lm3, ist, jst` (No comment)
- `Integer :: ngkq, igk, ifg, ir, irc` (No comment)
- `Integer, Allocatable :: igkqig (:)` (No comment)
- `Integer, Intent (In) :: ik` (No comment)
- `Real (8) :: gaunt` (No comment)
- `Real (8) :: v1 (3), v2 (3), v3 (3)` (No comment)
- `Real (8) :: vecqc (3), qc, tp (2)` (No comment)
- `Real (8) :: vkql (3), vkqc (3), x, t1` (No comment)
- `Real (8), Allocatable :: gkqc (:)` (No comment)
- `Real (8), Allocatable :: gnt (:, :, :)` (No comment)
- `Real (8), Allocatable :: jlqr (:, :)` (No comment)
- `Real (8), Allocatable :: tpgkqc (:, :)` (No comment)
- `Real (8), Allocatable :: vgkqc (:, :)` (No comment)
- `Real (8), Allocatable :: vgkql (:, :)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- constants
- modinput
- modmain

**Calls:**
- gengpvec
- gensfacgp
- genylm
- getevecfv
- getevecsv
- match
- r3frac
- r3mv
- sbessel
- sphcrd
- wavefmt
- zfftifc
