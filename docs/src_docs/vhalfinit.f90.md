# vhalfinit.f90

## Overview

  Initialises the crystal charge density. Inside the muffin-tins it is set to
  the spherical atomic density. In the interstitial region it is taken to be
  constant such that the total charge is correct. Requires that the atomic
  densities have already been calculated.

  Created January 2015 (Ronaldo R Pela)
EOP
BOC

## Key Components

- SUBROUTINE vhalfinit

## Important Variables/Constants

- `Complex (8), Allocatable :: zfft (:)` (No comment)
- `Complex (8), Allocatable :: zfmt (:, :),z2fmt (:,:)` (No comment)
- `Integer :: is, ia, ias, ig, ifg` (No comment)
- `Integer :: lmax, lmmax, l, m, lm, ir, irc` (No comment)
- `Integer, Parameter :: n = 4` (No comment)
- `Real (8) :: fr (spnrmax), gr (spnrmax), cf (3, spnrmax)` (No comment)
- `Real (8) :: rhoder,rhoder2, tp(2),r` (No comment)
- `Real (8) :: ta,tb, tc,td` (No comment)
- `Real (8) :: x, t1, t2, jlgr01, jlgr(0:1)` (No comment)
- `Real (8), Allocatable :: auxgrid(:),auxrho(:),a(:),c(:),b(:)` (No comment)
- `Real (8), Allocatable :: ffacg (:)` (No comment)
- `Real (8), Allocatable :: jj(:,:)` (No comment)
- `Real (8), Allocatable :: rhomodel(:,:)` (No comment)
- `Real (8), Allocatable :: th (:, :)` (No comment)
- `complex(8),allocatable :: swc2(:,:,:),swctmp(:,:,:)` (Comment: ,pwswc(:,:))
- `integer :: auxgridsize,mtgridsize,lastpoint` (No comment)
- `integer :: nsw,isw,jsw,info` (Comment:  number of spherical waves)
- `integer, parameter :: PointsPerPeriod=20` (No comment)
- `integer:: boundhi,boundlo,middle` (No comment)
- `integer:: whichthread,nthreads` (No comment)
- `real(8) :: aa,bb,ans,rmt3` (No comment)
- `real(8) :: maxswg,swg,rhotest` (No comment)
- `real(8), parameter :: sixth=1d0/6d0` (No comment)
- `real(8), parameter :: third=1d0/3d0` (No comment)
- `real(8), parameter :: threshold=1d-12` (No comment)
- `real(8),allocatable :: swc(:),swoverlap(:,:),sine(:),cosine(:),swgr(:),pwswc(:,:),swoverlap2(:,:,:),pwswc2(:)` (No comment)
- `real(8):: jthr,cs,sn,xi` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- constants
- modinput
- modmain
- omp_lib

**Calls:**
- dgemv
- dpotrf
- dpotri
- dpotrs
- fderiv
- rfmtctof
- sbessel
- timesec
- zfftifc
- ztorflm
