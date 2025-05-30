# asserts.F90

## Overview

*No overview extracted.*

## Key Components

- MODULE Procedure
- MODULE asserts
- SUBROUTINE assert_true
- SUBROUTINE terminate

## Important Variables/Constants

- `Integer, Parameter :: error_code_logical = -101` (No comment)
- `integer :: ierr` (No comment)
- `logical, intent(in) :: logical_condition` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- iso_fortran_env
- mpi
- trace

**Calls:**
- MPI_ABORT
- terminate
- trace_back
