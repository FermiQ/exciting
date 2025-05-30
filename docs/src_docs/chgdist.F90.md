# chgdist.F90

## Overview

  Calculated the charge distance between two charge densities of the current
  and of the last iteration according to
  the expression
  $$
    \Delta Q = \int_{\Omega} {\rm d}^3 r [\rho^{(n)}({\bf r}) -
    \rho^{(n-1)}({\bf r})].
  $$
  Based on the routine {\tt charge}.

  Created 2010 (Sagmeister)
  Modified 2014 (DIN)
EOP
BOC

## Key Components

- SUBROUTINE chgdist

## Important Variables/Constants

- `Integer :: is, ia, ias, ir` (No comment)
- `real(8) :: cf (3, nrmtmax), sht00(lmmaxvr)` (No comment)
- `real(8) :: fr (nrmtmax), gr (nrmtmax), hr1(lmmaxvr), hr2(lmmaxvr)` (No comment)
- `real(8) :: sum, chgdstmt, chgdstir` (No comment)
- `real(8), intent(in) :: rhoirref(ngrtot)` (No comment)
- `real(8), intent(in) :: rhomtref(lmmaxvr,nrmtmax,natmtot)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- constants
- modmain

**Calls:**
- dgemv
- fderiv
