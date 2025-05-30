# autoradmt.f90

## Overview

  Automatically determines the muffin-tin radii from the formula
  $$ R_i\propto 1+\zeta|Z_i|^{1/3}, $$
  where $Z_i$ is the atomic number of the $i$th species, $\zeta$ is a
  user-supplied constant ($\sim 0.625$). The parameter $\zeta$ is stored in
  {\tt rmtapm(1)} and the value which governs the distance between the
  muffin-tins is stored in {\tt rmtapm(2)}. When {\tt rmtapm(2)} $=1$, the
  closest muffin-tins will touch.

  Created March 2005 (JKD)
  Changed the formula, September 2006 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE autoradmt

## Important Variables/Constants

- `Integer :: is, js, ia, ja, i1, i2, i3` (No comment)
- `Real (8) :: r3dist` (No comment)
- `Real (8) :: s, v1 (3), v2 (3), t1, t2, t3` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain

**Calls:**
- *None identified.*
