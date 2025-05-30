# gendmatmt.f90

## Overview

  Constructs a contribution to the density matrix  due to the $\mathbf{k}$-point ik.

  Created May 2014 (Andris)
  Revised Aug 2020 (Ronaldo)
EOP
BOC

## Key Components

- SUBROUTINE gendmatmt

## Important Variables/Constants

- `Complex (8), Allocatable :: apwalm (:, :, :, :, :),apwi(:,:)` (No comment)
- `Complex (8), Allocatable :: dm2(:,:)` (No comment)
- `Complex (8), Intent (In) :: evecfv (nmatmax, nstfv, nspnfv)` (No comment)
- `Complex (8), Intent (In) :: evecsv (nstsv, nstsv)` (No comment)
- `Complex (8), pointer :: wf1(:,:), wf2prime(:,:), wfalpha(:,:),wfbeta(:,:)` (No comment)
- `Integer :: i, n, maxaa, maxnlo, wfsize` (No comment)
- `Integer :: ispn, is, ia, ias` (No comment)
- `Integer :: l, m, lm, io` (No comment)
- `Integer, Intent (In) :: ik` (No comment)
- `Real (8) :: t1, t2` (No comment)
- `Real (8) :: ts0, ts1` (No comment)
- `integer , pointer :: losize(:)` (No comment)
- `integer :: l3,lm3,if3,ngp,l1,lm1,j1,j3` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- constants
- modinput
- modmain
- modmpi

**Calls:**
- match
- timesec
- zgemm
