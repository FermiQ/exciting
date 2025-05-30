# genrhoir.f90

## Overview

  Generates the partial valence charge density from the eigenvectors at
  $k$-point {\tt ik}. In the muffin-tin region, the wavefunction is obtained
  in terms of its $(l,m)$-components from both the APW and local-orbital
  functions. Using a backward spherical harmonic transform (SHT), the
  wavefunction is converted to real-space and the density obtained from its
  modulus squared. This density is then transformed with a forward SHT and
  accumulated in the global variable {\tt rhomt}. A similar proccess is used
  for the intersitial density in which the wavefunction in real-space is
  obtained from a Fourier transform of the sum of APW functions. The
  interstitial density is added to the global array {\tt rhoir}. See routines
  {\tt wavefmt}, {\tt genshtmat} and {\tt seceqn}.

  Created April 2003 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE genrhoir

## Important Variables/Constants

- `Complex (8), Allocatable :: zfft (:, :)` (No comment)
- `Complex (8), Intent (In) :: evecfv (nmatmax, nstfv, nspnfv)` (No comment)
- `Complex (8), Intent (In) :: evecsv (nstsv, nstsv)` (No comment)
- `Integer :: ir, irc, itp, igk, ifg, i, j, n` (No comment)
- `Integer :: nsd, ispn, jspn, is, ia, ias, ist` (No comment)
- `Integer, Intent (In) :: ik` (No comment)
- `Real (8) :: magir_k (ngrtot, ndmag)` (No comment)
- `Real (8) :: rhoir_k (ngrtot)` (No comment)
- `Real (8) :: t1, t2, t3, t4` (No comment)
- `Real (8) :: ts0, ts1` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain

**Calls:**
- timesec
- zfftifc
