# allatoms.f90

## Overview

  Solves the Kohn-Sham-Dirac equations for each atom type in the solid and
  finds the self-consistent radial wavefunctions, eigenvalues, charge
  densities and potentials. The atomic densities can then be used to
  initialise the crystal densities, and the atomic self-consistent potentials
  can be appended to the muffin-tin potentials to solve for the core states.
  Note that, irrespective of the value of {\tt xctype}, exchange-correlation
  functional type 3 is used. See also {\tt atoms}, {\tt rhoinit},
  {\tt gencore} and {\tt modxcifc}.

  Created September 2002 (JKD)
  Modified for GGA, June 2007 (JKD)
  Modified for DFT-1/2, 2015 (Ronaldo)
EOP
BOC

## Key Components

- SUBROUTINE allatoms

## Important Variables/Constants

- `Character (256) :: fname` (No comment)
- `Integer :: fnum_ = 333` (Comment:  file where Vs (see DFT-1/2 details) is written)
- `Integer :: is, i, ir, n, nshell` (No comment)
- `Integer :: xctypearray(3)` (No comment)
- `Integer, Allocatable :: shell(:)` (No comment)
- `Integer, Parameter :: xcgrad_ = 0` (No comment)
- `Integer, Parameter :: xctype_ = 3` (No comment)
- `Logical :: dirac_eq` (No comment)
- `Real (8) :: ampl, cut, cutfunction, aux` (No comment)
- `Real (8), Allocatable :: ionization(:)` (No comment)
- `Real (8), Allocatable :: newspocc(:)` (No comment)
- `Real (8), Allocatable :: rhoslave(:)` (No comment)
- `Real (8), Allocatable :: rwf (:, :, :)` (No comment)
- `Type (xmlf_t), Save :: xf` (No comment)
- `character(100)::buffer` (No comment)
- `integer :: verbosity` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- FoX_wxml
- modinput
- modmain
- modmpi

**Calls:**
- atom
- finitMPI
- vhalfinit
- xml_AddAttribute
- xml_EndElement
- xml_NewElement
- xml_OpenFile
- xml_close
