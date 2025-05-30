# elfplot.f90

## Overview

  Outputs the electron localisation function (ELF) for 1D, 2D or 3D plotting.
  The spin-averaged ELF is given by
  $$ f_{\rm ELF}({\bf r})=\frac{1}{1+[D({\bf r})/D^0({\bf r})]^2}, $$
  where
  $$ D({\bf r})=\frac{1}{2}\left(\tau({\bf r})-\frac{1}{4}
   \frac{[\nabla n({\bf r})]^2}{n({\bf r})}\right) $$
  and
  $$ \tau({\bf r})=\sum_{i=1}^N \left|\nabla\Psi_i({\bf r})
   \right|^2 $$
  is the spin-averaged kinetic energy density from the spinor wavefunctions.
  The function $D^0$ is the kinetic energy density for the homogeneous
  electron gas evaluated for $n({\bf r})$:
  $$ D^0({\bf r})=\frac{3}{5}(6\pi^2)^{2/3}\left(\frac{n({\bf r})}{2}
   \right)^{5/3}. $$
  The ELF is useful for the topological classification of bonding. See for
  example T. Burnus, M. A. L. Marques and E. K. U. Gross [Phys. Rev. A 71,
  10501 (2005)].

  Created September 2003 (JKD)
  Fixed bug found by F. Wagner (JKD)
EOP
BOC

## Key Components

- SUBROUTINE elfplot

## Important Variables/Constants

- `Character(256) :: string` (No comment)
- `Complex (8), Allocatable :: evecfv (:, :)` (No comment)
- `Complex (8), Allocatable :: evecsv (:, :)` (No comment)
- `Complex (8), Allocatable :: zfft1 (:), zfft2 (:)` (No comment)
- `Integer :: ik, is, ia, ias` (No comment)
- `Integer :: ir, i, itp, ig, ifg` (No comment)
- `Real (8) :: t1, t2` (No comment)
- `Real (8), Allocatable :: elfir (:)` (No comment)
- `Real (8), Allocatable :: elfmt (:, :, :)` (No comment)
- `Real (8), Allocatable :: grfir (:)` (No comment)
- `Real (8), Allocatable :: grfmt (:, :, :)` (No comment)
- `Real (8), Allocatable :: gwf2ir (:)` (No comment)
- `Real (8), Allocatable :: gwf2mt (:, :, :)` (No comment)
- `Real (8), Allocatable :: rftp1 (:), rftp2 (:), rftp3 (:)` (No comment)
- `type(plotlabels),pointer ::labels` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- constants
- modinput
- modmain
- modmpi
- modplotlabels

**Calls:**
- destroy_plotlablels
- dgemv
- genapwfr
- gencore
- genlofr
- getevecfv
- getevecsv
- getoccsv
- gradrfmt
- gwf2cr
- gwf2val
- init0
- init1
- linengy
- plot1d
- plot2d
- plot3d
- readfermi
- readstate
- set_plotlabel_axis
- symrf
- zfftifc
