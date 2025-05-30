# energynn.f90

## Overview

*No overview extracted.*

## Key Components

- SUBROUTINE energynn

## Important Variables/Constants

- `Complex (8), Allocatable :: zrhoir (:)` (No comment)
- `Complex (8), Allocatable :: zrhomt (:, :, :)` (No comment)
- `Complex (8), Allocatable :: zvclir (:)` (No comment)
- `Complex (8), Allocatable :: zvclmt (:, :, :)` (No comment)
- `Integer :: is, ia, ias, lmax` (No comment)
- `Real (8) :: vn, t1` (No comment)
- `Real (8), Allocatable :: jlgr (:, :, :)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain

**Calls:**
- genjlgpr
- potnucl
- zpotcoul
