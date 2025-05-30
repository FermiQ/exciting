# occupy.f90

## Overview

  Finds the Fermi energy and sets the occupation numbers for the
  second-variational states using the routine {\tt fermi}.

  Created February 2004 (JKD)
  Modifiactions for tetrahedron method, November 2007 (RGA alias
    Ricardo Gomez-Abal)
  Modifications for tetrahedron method, 2007-2010 (Sagmeister)
  Modifications for tetrahedron method, 2011 (DIN)
  Simplicistic method for systems with gap added, 2013 (STK)
EOP
BOC

## Key Components

- SUBROUTINE occupy

## Important Variables/Constants

- `character(1024) :: message` (No comment)
- `integer :: ik, ist, it, nvm` (No comment)
- `integer, parameter :: maxit = 1000` (No comment)
- `logical :: lspin` (No comment)
- `real(8) :: dfde(nstsv,nkpt)` (No comment)
- `real(8) :: e0, e1, chg, x, t1` (No comment)
- `real(8) :: egap` (No comment)
- `real(8) :: sdelta, stheta` (No comment)
- `real(8), parameter :: de0=1.d0` (No comment)
- `type( k_set) :: kset` (No comment)
- `type( t_set) :: tetra` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- mod_kpointset
- mod_opt_tetra
- modinput
- modmain

**Calls:**
- delete_k_vectors
- fermi_exciting
- generate_k_vectors
- opt_tetra_destroy
- opt_tetra_efermi
- opt_tetra_init
- opt_tetra_wgt_delta
- tetiw
- warning
