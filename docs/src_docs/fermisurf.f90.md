# fermisurf.f90

## Overview

*No overview extracted.*

## Key Components

- SUBROUTINE fermisurf

## Important Variables/Constants

- `complex(8), allocatable :: evecfv(:,:,:)` (No comment)
- `complex(8), allocatable :: evecsv(:,:)` (No comment)
- `integer :: fnum,fnum0,fnum1` (No comment)
- `integer :: ik,ist,ist0,ist1` (No comment)
- `integer :: lst,nst,i,i1,i2,i3,j1,j2,j3` (No comment)
- `real(8) :: vc(3,4)` (No comment)
- `real(8), allocatable :: evalfv(:,:)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modmain
- modmpi

**Calls:**
- MTInitAll
- MTNullify
- genapwfr
- genlofr
- genmeffig
- hmlint
- init0
- init1
- linengy
- mpi_allgatherv_ifc
- mt_hscf
- olprad
- readfermi
- readstate
- seceqn
