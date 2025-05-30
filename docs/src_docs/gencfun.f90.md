# gencfun.f90

## Overview

  Generates the smooth characteristic function. This is the function which is
  0 within the muffin-tins and 1 in the intersitial region and is constructed
  from radial step function form-factors with $G<G_{\rm max}$. The form
  factors are given by
  $$ \tilde{\Theta}_i(G)=\begin{cases}
   \frac{4\pi R_i^3}{3 \Omega} & G=0 \\
   \frac{4\pi R_i^3}{\Omega}\frac{j_1(GR_i)}{GR_i} & 0<G\le G_{\rm max} \\
   0 & G>G_{\rm max}\end{cases}, $$
  where $R_i$ is the muffin-tin radius of the $i$th species and $\Omega$ is
  the unit cell volume. Therefore the characteristic function in $G$-space is
  $$ \tilde{\Theta}({\bf G})=\delta_{G,0}-\sum_{ij}\exp(-i{\bf G}\cdot
   {\bf r}_{ij})\tilde{\Theta}_i(G), $$
  where ${\bf r}_{ij}$ is the position of the $j$th atom of the $i$th species.

  Created January 2003 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE gencfun

## Important Variables/Constants

- `Complex (8), Allocatable :: zfft (:)` (No comment)
- `Integer :: is, ia, ig, ifg` (No comment)
- `Real (8) :: t1, t2` (No comment)
- `Real (8), Allocatable :: ffacg (:)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- constants
- modinput
- modmain

**Calls:**
- zfftifc
