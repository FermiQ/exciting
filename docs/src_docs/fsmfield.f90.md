# fsmfield.f90

## Overview

  Updates the effective magnetic field, ${\bf B}_{\rm FSM}$, required for
  fixing the spin moment to a given value, $\boldsymbol{\mu}_{\rm FSM}$. This
  is done by adding a vector to the field which is proportional to the
  difference between the moment calculated in the $i$th self-consistent loop
  and the required moment:
  $$ {\bf B}_{\rm FSM}^{i+1}={\bf B}_{\rm FSM}^i+\lambda\left(
   \boldsymbol{\mu}^i-\boldsymbol{\mu}_{\rm FSM}\right), $$
  where $\lambda$ is a scaling factor.

  Created March 2005 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE fsmfield

## Important Variables/Constants

- `Integer :: is, ia, ias, ir, idm` (No comment)
- `Real (8) :: v (3), t1` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain

**Calls:**
- *None identified.*
