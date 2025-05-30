# atom.f90

## Overview

  Solves the Dirac-Kohn-Sham equations for an atom using the
  exchange-correlation functional {\tt xctype} and returns the self-consistent
  radial wavefunctions, eigenvalues, charge densities and potentials. The
  variable {\tt np} defines the order of polynomial used for performing
  numerical integration. Requires the exchange-correlation interface routine
  {\tt xcifc}.

  Created September 2002 (JKD)
  Fixed s.c. convergence problem, October 2003 (JKD)
  Added support for GGA functionals, June 2006 (JKD)
  Almost entirely rewritten 2013 (Andris)
EOP
BOC

## Key Components

- SUBROUTINE atom

## Important Variables/Constants

- `Integer :: ir, ist, iscl` (No comment)
- `Integer, Intent (In) :: k (nst)` (No comment)
- `Integer, Intent (In) :: l (nst)` (No comment)
- `Integer, Intent (In) :: n (nst)` (No comment)
- `Integer, Intent (In) :: nr,mtnr` (No comment)
- `Integer, Intent (In) :: nst` (No comment)
- `Integer, Intent (In) :: xcgrad` (No comment)
- `Integer, Intent (In) :: xctype(3)` (No comment)
- `Integer, Parameter :: maxscl = 500` (No comment)
- `Logical, Intent (In) :: dirac_eq` (No comment)
- `Logical, Intent (In) :: ptnucl` (No comment)
- `Real (8) :: sum, dv, dvp, ze, beta, t1` (No comment)
- `Real (8), Allocatable :: dwf1(:),dwf2(:),dwf3(:),dwf4(:)` (No comment)
- `Real (8), Allocatable :: grho (:), g2rho (:), g3rho (:)` (No comment)
- `Real (8), Intent (In) :: r (nr)` (No comment)
- `Real (8), Intent (In) :: zn` (No comment)
- `Real (8), Intent (Inout) :: occ (nst)` (No comment)
- `Real (8), Intent (Out) :: eval (nst)` (No comment)
- `Real (8), Intent (Out) :: rho (nr)` (No comment)
- `Real (8), Intent (Out) :: rwf (nr, 2, nst)` (No comment)
- `Real (8), Intent (Out) :: vr (nr)` (No comment)
- `Real (8), Parameter :: alpha = 1.d0 / 137.03599911d0` (No comment)
- `Real (8), Parameter :: eps = 1.d-8` (No comment)
- `Real (8), Parameter :: fourpi = 12.566370614359172954d0` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modxcifc

**Calls:**
- fderiv
- potnucl
- rdirac
- warning
- xcifc
