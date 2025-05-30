# effmass.f90

## Overview

*No overview extracted.*

## Key Components

- SUBROUTINE effmass

## Important Variables/Constants

- `Complex (8), Allocatable :: evecfv (:, :, :)` (No comment)
- `Complex (8), Allocatable :: evecsv (:, :)` (No comment)
- `Integer :: i, j, k, l, m, n` (No comment)
- `Integer :: i1, i2, i3, j1, j2, j3` (No comment)
- `Integer :: ik, ik0, ist, info` (No comment)
- `Integer, Allocatable :: ipiv (:)` (No comment)
- `Integer, Parameter :: lwork = 10` (No comment)
- `Real (8) :: d (3, 3), em (3, 3)` (No comment)
- `Real (8) :: v1 (3), v2 (3)` (No comment)
- `Real (8) :: w (3), work (lwork)` (No comment)
- `Real (8), Allocatable :: a (:, :)` (No comment)
- `Real (8), Allocatable :: b (:, :, :, :)` (No comment)
- `Real (8), Allocatable :: c (:, :, :)` (No comment)
- `Real (8), Allocatable :: evalfv (:, :)` (No comment)
- `Type (xmlf_t), Save :: xf` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- Fox_wxml
- modinput
- modmain

**Calls:**
- MTInitAll
- MTNullify
- dgesv
- dsyev
- genapwfr
- genlofr
- genmeffig
- hmlint
- init0
- init1
- linengy
- mt_hscf
- olprad
- r3minv
- r3mv
- readstate
- seceqn
- xml_AddAttribute
- xml_AddCharacters
- xml_Close
- xml_EndElement
- xml_NewElement
- xml_OpenFile
