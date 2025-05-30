# linengy.f90

## Overview

  Calculates the new linearisation energies for both the APW and local-orbital
  radial functions. See the routine {\tt findband}.

  Created May 2003 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE linengy

## Important Variables/Constants

- `Integer :: is, ia, ja, ias, jas` (No comment)
- `Integer :: l, ilo, io1, io2` (No comment)
- `Logical :: done (natmmax)` (No comment)
- `Real (8) :: vr (nrmtmax)` (No comment)
- `character(1024) :: message` (No comment)
- `character(256) :: linenetype, fname` (No comment)
- `integer :: nr, nn` (No comment)
- `logical :: tfnd` (No comment)
- `real(8) :: t0, t1, e, dl` (No comment)
- `real(8), allocatable :: p0 (:), p1 (:), q0 (:), q1 (:)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain
- scl_xml_out_Module

**Calls:**
- findband
- rschroddme
- warning
