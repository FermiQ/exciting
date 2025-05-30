# findband.f90

## Overview

  Finds the band energies for a given radial potential and angular momentum.
  This is done by first searching upwards in energy until the radial
  wavefunction at the muffin-tin radius is zero. This is the energy at the top
  of the band, denoted $E_{\rm t}$. A downward search is now performed from
  $E_{\rm t}$ until the slope of the radial wavefunction at the muffin-tin
  radius is zero. This energy, $E_{\rm b}$, is at the bottom of the band. The
  band energy is taken as $(E_{\rm t}+E_{\rm b})/2$. If either $E_{\rm t}$ or
  $E_{\rm b}$ cannot be found then the band energy is set to the input value.

  Created September 2004 (JKD)
EOP
BOC

## Key Components

- SUBROUTINE findband

## Important Variables/Constants

- `Character (*), Intent (In) :: findlinentype` (No comment)
- `Integer :: ie, nn` (No comment)
- `Integer, Intent(In)    :: k` (No comment)
- `Integer, Intent(In)    :: l` (No comment)
- `Integer, Intent(In)    :: nr` (No comment)
- `Integer, Parameter :: maxstp = 1000` (No comment)
- `Real (8) :: de, e, t0, t1, t00, t10, dl, dl0` (No comment)
- `Real (8) :: e1, e2, eidn, eiup` (No comment)
- `Real (8) :: p0 (nr), p1 (nr), q0 (nr), q1 (nr)` (No comment)
- `Real (8), Parameter :: ecutlow = - 100.d0` (No comment)
- `Real (8), Parameter :: edefault1 = 1.d0` (No comment)
- `Real (8), Parameter :: ediffusebands = efermibands + erangebands` (No comment)
- `Real (8), Parameter :: edncut = -10.d0` (No comment)
- `Real (8), Parameter :: efermibands = 0.5d0` (No comment)
- `Real (8), Parameter :: erange1 = 3.d0` (No comment)
- `Real (8), Parameter :: erangebands = 1.d0` (No comment)
- `Real (8), Parameter :: etoolow = - 1000.d0` (No comment)
- `Real (8), Parameter :: eupcut = 30.d0` (No comment)
- `Real(8), Intent(In)    :: de0` (No comment)
- `Real(8), Intent(In)    :: r (nr)` (No comment)
- `Real(8), Intent(In)    :: vr (nr)` (No comment)
- `Real(8), Intent(Inout) :: e0` (No comment)
- `character(10) :: fname` (No comment)
- `character(1024) :: message` (No comment)
- `logical, intent(out)   :: tfnd` (No comment)
- `real(8), intent(in)    :: etol` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modmain

**Calls:**
- rschroddme
- warning
