# readstate.f90

## Overview

  Reads in the charge density and other relevant variables from the file
  {\tt STATE.OUT}. Checks for version and parameter compatibility.

  Created May 2003 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE readstate

## Important Variables/Constants

- `Character(40) :: githash_` (No comment)
- `Complex (8), Allocatable :: veffig_ (:)` (No comment)
- `Complex (8), Allocatable :: vmatlu_ (:, :, :, :, :)` (No comment)
- `Integer :: idm, ngm, i1, i2, i3, j1, j2, j3` (No comment)
- `Integer :: iostat` (No comment)
- `Integer :: is, ia, ias, lmmax, lm, ir, jr` (No comment)
- `Integer :: natoms_, nrmt_ (maxspecies), nrmtmax_` (No comment)
- `Integer :: ngrid_ (3), ngrtot_, ngvec_, ndmag_` (No comment)
- `Integer :: nspinor_, ldapu_, lmmaxlu_` (No comment)
- `Integer :: version_ (3), nspecies_, lmmaxvr_` (No comment)
- `Integer, Allocatable :: mapir (:)` (No comment)
- `Logical :: spinpol_` (No comment)
- `Real (8) :: t1` (No comment)
- `Real (8), Allocatable :: bxcir_ (:, :)` (No comment)
- `Real (8), Allocatable :: bxcmt_ (:, :, :, :)` (No comment)
- `Real (8), Allocatable :: magir_ (:, :)` (No comment)
- `Real (8), Allocatable :: magmt_ (:, :, :, :)` (No comment)
- `Real (8), Allocatable :: rhoir_ (:)` (No comment)
- `Real (8), Allocatable :: rhomt_ (:, :, :)` (No comment)
- `Real (8), Allocatable :: spr_ (:, :)` (No comment)
- `Real (8), Allocatable :: vclir_ (:)` (No comment)
- `Real (8), Allocatable :: vclmt_ (:, :, :)` (No comment)
- `Real (8), Allocatable :: veffir_ (:)` (No comment)
- `Real (8), Allocatable :: veffmt_ (:, :, :)` (No comment)
- `Real (8), Allocatable :: vxcir_ (:)` (No comment)
- `Real (8), Allocatable :: vxcmt_ (:, :, :)` (No comment)
- `character(1024) :: message` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain
- modxs

**Calls:**
- rfinterp
- warning
