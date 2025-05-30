# borncharges.f90

## Overview

*No overview extracted.*

## Key Components

- SUBROUTINE borncharges
- SUBROUTINE get
- SUBROUTINE put

## Important Variables/Constants

- `character(*), intent( in) :: mode` (No comment)
- `character(256) :: fname, buf` (No comment)
- `integer :: ia, is, ias, ip, vi(3), un` (No comment)
- `integer :: un, i, l, ias` (No comment)
- `integer :: un` (No comment)
- `logical :: exist` (No comment)
- `logical, intent( in)      :: sumrule` (No comment)
- `real(8) :: vr(3)` (No comment)
- `real(8), intent( in)      :: pol(3,2,3,natmtot), disp` (No comment)
- `real(8), intent( in) :: z(3,3,0:natmtot)` (No comment)
- `real(8), intent( inout)   :: zstar(3,3,0:natmtot)` (No comment)
- `real(8), intent( out) :: z(3,3,0:natmtot)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- m_getunit
- mod_atoms
- mod_lattice
- mod_misc
- modinput
- modmpi

**Calls:**
- barrier
- get
- getunit
- put
- r3mv
- r3ws
- terminate
