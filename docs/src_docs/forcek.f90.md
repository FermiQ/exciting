# forcek.f90

## Overview

  Computes the {\bf k}-dependent contribution to the incomplete basis set
  (IBS) force. See the calling routine {\tt force} for a full description.

  Created June 2006 (JKD)
  Updated for spin-spiral case, May 2007 (Francesco Cricchio and JKD)
EOP
BOC

## Key Components

- SUBROUTINE forcek

## Important Variables/Constants

- `Complex (8), Allocatable :: apwalm (:, :, :, :)` (No comment)
- `Complex (8), Allocatable :: apwi(:,:),zm(:,:),apwi2(:,:)` (No comment)
- `Complex (8), Allocatable :: dlhij(:,:)` (No comment)
- `Complex (8), Allocatable :: dloij(:,:)` (No comment)
- `Complex (8), Allocatable :: evecfv (:, :, :),evecfv2(:,:,:)` (No comment)
- `Complex (8), Allocatable :: evecsv (:, :)` (No comment)
- `Complex (8), Allocatable :: ffv (:, :)` (No comment)
- `Complex (8), Allocatable :: y (:)` (No comment)
- `Integer :: i, j, k, l, iv (3), ig` (No comment)
- `Integer :: is, ia, ias, ist, jst` (No comment)
- `Integer :: np, ispn, jspn` (No comment)
- `Integer, Allocatable :: ijgij(:,:)` (No comment)
- `Integer, Intent (In) :: ik` (No comment)
- `Real (8) :: sum, t1, ta,tb` (No comment)
- `Real (8), Allocatable :: dpij(:,:)` (No comment)
- `Real (8), Allocatable :: evalfv (:, :)` (No comment)
- `Real (8), Intent (In) :: ffacg (ngvec, nspecies)` (No comment)
- `Type (evsystem) :: system` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- constants
- mod_eigensystem
- modfvsystem
- modinput
- modmain

**Calls:**
- deletesystem
- getevalfv
- getevecfv
- getevecsv
- getoccsv
- match
- newsystem
- zgemm
- zgemv
