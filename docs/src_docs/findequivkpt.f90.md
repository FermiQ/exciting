# findequivkpt.f90

## Overview

*No overview extracted.*

## Key Components

- SUBROUTINE findequivkpt

## Important Variables/Constants

- `integer :: iq, is, lspl, iv(3)` (No comment)
- `integer, intent( out) :: ik( kset%nkpt)` (No comment)
- `integer, intent( out) :: isym( kset%nkpt)` (No comment)
- `integer, intent( out) :: nk` (No comment)
- `real(8) :: s(3,3), v1(3), v2(3), t1` (No comment)
- `real(8), intent( in) :: vpl(3)` (No comment)
- `type( k_set), intent( in) :: kset` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- mod_kpointset
- modinput
- modmain

**Calls:**
- r3frac
- r3mtv
