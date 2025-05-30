# genrhomt.f90

## Overview

  Generates the muffin tin part of the charge density from the density matrix.

  Created May 2014 (Andris)
  Revised Aug 2020 (Ronaldo)
EOP
BOC

## Key Components

- SUBROUTINE genrhomt

## Important Variables/Constants

- `Real (8) :: t1, t2` (No comment)
- `Real (8) :: ts0, ts1` (No comment)
- `integer :: i, n` (No comment)
- `integer :: ilo1,ilo2,maxnlo,maxaa,wfsize` (No comment)
- `integer :: is, ia, ias` (No comment)
- `integer :: l3,lm3,m3,io1,io2,if1,if3,l1,m1,lm1,lm2,if3old,if1old` (No comment)
- `integer, pointer :: losize(:)` (No comment)
- `real(8) :: alpha,a` (No comment)
- `real(8), allocatable :: factors(:),rho(:,:,:),factorsnew(:,:),frnew(:,:)` (No comment)
- `real(8), intent(out) :: densitymt(lmmaxvr,nrmtmax,natmtot)` (No comment)
- `type(apw_lo_basis_type), intent(in) :: basis1, basis2` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain
- modmpi

**Calls:**
- timesec
