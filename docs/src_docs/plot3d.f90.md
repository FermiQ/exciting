# plot3d.f90

## Overview

  Produces a 3D plot of the real functions contained in arrays {\tt rfmt} and
  {\tt rfir} in the parallelepiped defined by the corner vertices in the
  global array {\tt vclp3d}. See routine {\tt rfarray}.

  Created June 2003 (JKD)
  Modified, October 2008 (F. Bultmark, F. Cricchio, L. Nordstrom)
  Modified, February 2011 (DIN)
  Fixed a bug in gengrid, February 2014 (DIN)
EOP
BOC

## Key Components

- SUBROUTINE gengrid
- SUBROUTINE plot3d

## Important Variables/Constants

- `Character (20) :: buffer20` (No comment)
- `Character (512) :: buffer` (No comment)
- `Integer :: i1, i2, i3, ip, jp` (No comment)
- `Integer :: isym, lspl` (No comment)
- `Integer :: np, ip1, ip2, ip3, i, ifunction, ip` (No comment)
- `Integer,  Allocatable :: ipmap (:,:,:)` (No comment)
- `Integer, Intent (In)  :: ngridp(3)` (No comment)
- `Integer, Intent (In) :: ld` (No comment)
- `Integer, Intent (In) :: lmax` (No comment)
- `Integer, Intent (In) :: nf` (No comment)
- `Integer, Intent (Out) :: ipmap(0:ngridp(1), 0:ngridp(2), 0:ngridp(3))` (No comment)
- `Integer, Intent (Out) :: npt` (No comment)
- `Real (8) :: boxl(3,4)` (No comment)
- `Real (8) :: tmpv(3)` (No comment)
- `Real (8) :: v1(3), v2(3), v3(3), t1, t2, t3` (No comment)
- `Real (8), Allocatable :: fp (:, :)` (No comment)
- `Real (8), Allocatable :: vpl (:,:)` (No comment)
- `Real (8), Intent (In) :: rfir (ngrtot, nf)` (No comment)
- `Real (8), Intent (In) :: rfmt (ld, nrmtmax, natmtot, nf)` (No comment)
- `Real (8), Intent (Out) :: vpl(3,(ngridp(1)+1)*(ngridp(2)+1)*(ngridp(3)+1))` (No comment)
- `Real(8) :: r1(3), r2(3), r3(3), vpl_(3)` (No comment)
- `Real(8) :: s(3,3), t1` (No comment)
- `Type (plot3d_type), Intent (In) :: plotdef` (No comment)
- `Type (xmlf_t), Save :: xf` (No comment)
- `integer :: iv(3)` (No comment)
- `real(8), intent(in) :: b(3,4)` (No comment)
- `type(plotlabels), Intent (In) :: plotlabels3d` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- FoX_wxml
- mod_Gvector
- mod_atoms
- mod_muffin_tin
- modinput
- modmain
- modmpi
- modplotlabels

**Calls:**
- DGEMV
- gengrid
- r3frac
- r3mv
- rfarray
- xml_AddAttribute
- xml_AddCharacters
- xml_Close
- xml_NewElement
- xml_OpenFile
- xml_endElement
