# plot1d.f90

## Overview

  Produces a 1D plot of the real functions contained in arrays {\tt rfmt} and
  {\tt rfir} along the lines connecting the vertices in the global array
  {\tt vvlp1d}. See routine {\tt rfarray}.

  Created June 2003 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE plot1d

## Important Variables/Constants

- `Character (128) :: buffer, buffer1` (No comment)
- `Integer :: i, ip, iv` (No comment)
- `Integer, Intent (In) :: ld` (No comment)
- `Integer, Intent (In) :: lmax` (No comment)
- `Integer, Intent (In) :: nf` (No comment)
- `Real (8) :: fmin, fmax, t1` (No comment)
- `Real (8), Allocatable :: fp (:, :)` (No comment)
- `Real (8), Intent (In) :: rfir (ngrtot, nf)` (No comment)
- `Real (8), Intent (In) :: rfmt (ld, nrmtmax, natmtot, nf)` (No comment)
- `Type (plot1d_type) :: plotdef` (No comment)
- `Type (xmlf_t), Save :: xf` (No comment)
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
- connect
- rfarray
- xml_AddAttribute
- xml_AddCharacters
- xml_NewElement
- xml_OpenFile
- xml_close
- xml_endElement
