# eqpongrid.f90

## Overview

*No overview extracted.*

## Key Components

- SUBROUTINE eqpongrid

## Important Variables/Constants

- `character(30) :: fname` (No comment)
- `integer :: nkp, ibgw, nbgw` (No comment)
- `integer :: nv, ik, nk, ib, nb, iknr, is, iv, m, ix, iy, iz` (No comment)
- `integer(4)    :: recl` (No comment)
- `logical :: exist` (No comment)
- `real(8) :: eferqp, eferks` (No comment)
- `real(8) :: s(3), v1(3), dt, vk(3)` (No comment)
- `real(8), allocatable :: eval2(:,:), vvl(:,:), ongrid(:,:)` (No comment)
- `real(8), allocatable :: kvecs(:,:), eqp(:,:), eks(:,:)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- mod_wannier
- modinput
- modmain

**Calls:**
- findkpt
- r3mv
