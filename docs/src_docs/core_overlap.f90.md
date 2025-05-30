# core_overlap.f90

## Overview

Calculates the overlap between a selected group of core states and the
valence and conduction states. While we assume that the overlap between
these states vanishes, there is finite overlap since the two groups of
states are obtained from different Hamiltonians. The overlap
$\int dr^3 \psi^*_{\mu}(\mathbf{r})\psi_{i\mathbf{k}}(\mathbf{r})$ between
a core state $\psi_{\mu \mathbf{k}}$ and valence/conduction state
$\psi_{i\mathbf{k}}$ and energy differences $\Delta \epsilon=\epsilon_{i
\mathbf{k}}-\epsilon_{\mu}$ are stored either in xml or hdf5 file.
  Created December 2020 (Christian Vorwerk) based on bandstr.f90
EOP
BOC

## Key Components

- SUBROUTINE core_overlap

## Important Variables/Constants

- `Character (128) :: buffer` (No comment)
- `Complex (8), Allocatable :: apwalmt (:, :, :, :)` (No comment)
- `Complex (8), Allocatable :: evecfv (:, :)` (No comment)
- `Complex (8), Allocatable :: evecsv (:, :)` (No comment)
- `Complex (8), Allocatable :: overlap(:,:,:)` (No comment)
- `Complex (8), Allocatable :: wfmt(:,:,:)` (No comment)
- `Integer :: ik, is, ia, ias, ist1, ist2, irc, ir` (No comment)
- `Integer :: lm1, lm2` (No comment)
- `Integer :: lxas` (No comment)
- `Real (8), Allocatable :: evalfv (:,:)` (No comment)
- `Real(8) :: t1, t2` (No comment)
- `Real(8), Allocatable     :: de(:,:,:)` (No comment)
- `Real(8), Allocatable :: cf(:,:)` (No comment)
- `Real(8), Allocatable :: fr0(:), fr1(:), fr2(:), gr(:)` (No comment)
- `Type (xmlf_t), Save :: xf` (No comment)
- `character(*), parameter :: thisname="writeoverlap"` (No comment)
- `character(256) :: cik` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- FoX_wxml
- constants
- mod_APW_LO
- mod_Gkvector
- mod_atoms
- mod_eigensystem
- mod_eigenvalue_occupancy
- mod_hdf5
- mod_kpoint
- mod_muffin_tin
- mod_spin
- modinput
- modmpi
- modxas
- mpi

**Calls:**
- MTInitAll
- MTNullify
- coreinit
- fderiv
- genapwfr
- genlofr
- genmeffig
- hdf5_create_group
- hdf5_write
- hmlint
- init0
- init1
- linengy
- match
- mpi_allgatherv_ifc
- mt_hscf
- olprad
- readfermi
- readstate
- seceqn
- wavefmt
- xml_AddAttribute
- xml_AddXMLPI
- xml_NewElement
- xml_OpenFile
- xml_close
- xml_endElement
