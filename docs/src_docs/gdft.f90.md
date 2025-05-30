# gdft.f90

## Overview

*No overview extracted.*

## Key Components

- SUBROUTINE gdft

## Important Variables/Constants

- `Complex (8), Allocatable :: apwalm (:, :, :, :)` (No comment)
- `Complex (8), Allocatable :: evecfv (:, :)` (No comment)
- `Complex (8), Allocatable :: evecsv (:, :)` (No comment)
- `Complex (8), Allocatable :: wfir (:, :, :)` (No comment)
- `Complex (8), Allocatable :: wfmt (:, :, :, :, :)` (No comment)
- `Integer :: ir, irc, itp` (No comment)
- `Integer :: ist, jst, is, ia, ias` (No comment)
- `Integer, Intent (In) :: ik` (No comment)
- `Real (8) :: fr (nrcmtmax), gr (nrcmtmax), cf (3, nrcmtmax)` (No comment)
- `Real (8) :: rflm (lmmaxvr), rftp (lmmaxvr)` (No comment)
- `Real (8) :: sum, t1, t2` (No comment)
- `Real (8), Allocatable :: rfir (:)` (No comment)
- `Real (8), Allocatable :: rfmt (:, :, :)` (No comment)
- `Real (8), Intent (Out) :: delta (nstsv, nstsv)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- constants
- modinput
- modmain

**Calls:**
- dgemv
- fderiv
- genwfsv
- getevecfv
- getevecsv
- match
