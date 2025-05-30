# bandstr.f90

## Overview

  Produces a band structure along the path in reciprocal-space which connects
  the vertices in the array {\tt vvlp1d}. The band structure is obtained from
  the second-variational eigenvalues and is written to the file {\tt BAND.OUT}
  with the Fermi energy set to zero. If required, band structures are plotted
  to files {\tt BAND\_Sss\_Aaaaa.OUT} for atom {\tt aaaa} of species {\tt ss},
  which include the band characters for each $l$ component of that atom in
  columns 4 onwards. Column 3 contains the sum over $l$ of the characters.
  Vertex location lines are written to {\tt BANDLINES.OUT}.

  Created June 2003 (JKD)
  Modified June 2012 (DIN)
  Modified March 2014 (UW)
  Modified June 2018 (SeTi)
EOP
BOC

## Key Components

- SUBROUTINE bandstr

## Important Variables/Constants

- `Character (128) :: buffer` (No comment)
- `Character (256) :: fname` (No comment)
- `Complex (8), Allocatable :: apwalm (:, :, :, :, :)` (No comment)
- `Complex (8), Allocatable :: dmat (:, :, :, :, :)` (No comment)
- `Complex (8), Allocatable :: evecfv (:, :, :)` (No comment)
- `Complex (8), Allocatable :: evecsv (:, :)` (No comment)
- `Integer :: ik, ispn, is, ia, ias, iv, ist` (No comment)
- `Integer :: lmax, lmmax, l, m, lm` (No comment)
- `Real (4), Allocatable :: bc (:, :, :, :)` (No comment)
- `Real (8) :: emin, emax, sum` (No comment)
- `Real (8), Allocatable :: evalfv (:, :)` (No comment)
- `Type (xmlf_t), Save :: xf` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- FoX_wxml
- m_write_hdf5
- modinput
- modmain
- modmpi

**Calls:**
- MPI_barrier
- MTInitAll
- MTNullify
- genapwfr
- gendmat
- genlofr
- genmeffig
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
- terminate
- write_bandstr_hdf5
- xml_AddAttribute
- xml_AddCharacters
- xml_AddXMLPI
- xml_NewElement
- xml_OpenFile
- xml_close
- xml_endElement
