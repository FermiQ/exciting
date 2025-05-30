# plot2d.f90

## Overview

  Produces a 2D plot of the real functions contained in arrays {\tt rfmt} and
  {\tt rfir} on the parallelogram defined by the corner vertices in the global
  array {\tt vclp2d}. See routine {\tt rfarray}.

  Created June 2003 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE plot2d

## Important Variables/Constants

- `Character (128) :: buffer, buffer1` (No comment)
- `Integer :: i, ip, ip1, ip2` (No comment)
- `Integer, Intent (In) :: ld` (No comment)
- `Integer, Intent (In) :: lmax` (No comment)
- `Integer, Intent (In) :: nf` (No comment)
- `Real (8) :: d1, d2, d12, t1, t2, t3, t4` (No comment)
- `Real (8) :: vl1 (3), vl2 (3), vc1 (3), vc2 (3),delta(3)` (No comment)
- `Real (8), Allocatable :: fp (:, :)` (No comment)
- `Real (8), Allocatable :: vpl (:, :)` (No comment)
- `Real (8), Intent (In) :: rfir (ngrtot, nf)` (No comment)
- `Real (8), Intent (In) :: rfmt (ld, nrmtmax, natmtot, nf)` (No comment)
- `Type (plot2d_type) :: plotdef` (No comment)
- `Type (xmlf_t), Save :: xf` (No comment)
- `character (20) :: buffer20` (No comment)
- `type(plotlabels), Intent (In) :: labels` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- FoX_wxml
- mod_Gvector
- mod_atoms
- mod_muffin_tin
- mod_plotting
- modinput
- modmpi
- modplotlabels

**Calls:**
- rfarray
- xml_AddAttribute
- xml_AddCharacters
- xml_Close
- xml_NewElement
- xml_OpenFile
- xml_endElement
