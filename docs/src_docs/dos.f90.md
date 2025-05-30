# dos.f90

## Overview

  Produces a total and partial density of states (DOS) for plotting. The total
  DOS is written to the file {\tt TDOS.OUT} while the partial DOS is written
  to the file {\tt PDOS\_Sss\_Aaaaa.OUT} for atom {\tt aaaa} of species
  {\tt ss}. In the case of the partial DOS, each symmetrised
  $(l,m)$-projection is written consecutively and separated by blank lines.
  If the global variable {\tt lmirep} is {\tt .true.}, then the density matrix
  from which the $(l,m)$-projections are obtained is first rotated into a
  irreducible representation basis, i.e. one that block diagonalises all the
  site symmetry matrices in the $Y_{lm}$ basis. Eigenvalues of a quasi-random
  matrix in the $Y_{lm}$ basis which has been symmetrised with the site
  symmetries are written to {\tt ELMIREP.OUT}. This allows for identification
  of the irreducible representations of the site symmetries, for example $e_g$
  or $t_{2g}$, by the degeneracies of the eigenvalues. In the plot, spin-up is
  made positive and spin-down negative. See the routines {\tt gendmat} and
  {\tt brzint}.

  Created January 2004 (JKD)
  Added more efficient trilinear integration and tetrahedron integration, August 2020 (SeTi)
EOP
BOC

## Key Components

- SUBROUTINE dos

## Important Variables/Constants

- `Character (256) :: fname` (No comment)
- `Character (512) :: buffer` (No comment)
- `Character(256) :: string` (No comment)
- `Complex (8), Allocatable :: a (:, :)` (No comment)
- `Complex (8), Allocatable :: apwalm (:, :, :, :, :)` (No comment)
- `Complex (8), Allocatable :: dmat (:, :, :, :, :)` (No comment)
- `Complex (8), Allocatable :: evecfv (:, :, :)` (No comment)
- `Complex (8), Allocatable :: evecsv (:, :)` (No comment)
- `Complex (8), Allocatable :: sdmat (:, :, :, :)` (No comment)
- `Complex (8), Allocatable :: ulm (:, :, :)` (No comment)
- `Integer :: Ndosspn, spinor_factor` (No comment)
- `Integer :: idosspn` (No comment)
- `Integer :: ik, nsk (3), ist, iw, jst, n, i` (No comment)
- `Integer :: ispn, jspn, is, ia, ias` (No comment)
- `Integer :: lmax, lmmax, l, m, lm` (No comment)
- `Integer :: ntrans, mtrans` (No comment)
- `Integer, dimension(2) :: sign_factor = (/1.d0, -1.d0/)` (No comment)
- `Logical :: lonly` (No comment)
- `Logical :: tsqaz` (No comment)
- `Real (4), Allocatable :: bc (:, :, :, :, :)` (No comment)
- `Real (8) :: dw, th, t1` (No comment)
- `Real (8) :: v1 (3), v2 (3), v3 (3)` (No comment)
- `Real (8), Allocatable :: dosg(:,:), dosgl(:,:,:)` (No comment)
- `Real (8), Allocatable :: e (:, :, :)` (No comment)
- `Real (8), Allocatable :: edif(:,:,:), ej(:,:), fj(:,:)` (No comment)
- `Real (8), Allocatable :: elm (:, :)` (No comment)
- `Real (8), Allocatable :: f (:, :)` (No comment)
- `Real (8), Allocatable :: g(:,:), gp(:)` (No comment)
- `Real (8), Allocatable :: jdos (:, :, :), jdosocc (:, :, :)` (No comment)
- `Real (8), Allocatable :: w (:)` (No comment)
- `Real (8), Allocatable :: wgt (:, :, :)` (No comment)
- `Type (xmlf_t), Save :: xf` (No comment)
- `type( k_set) :: kset` (No comment)
- `type( t_set) :: tset` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- FoX_wxml
- mod_eigenvalue_occupancy
- mod_kpointset
- mod_lattice
- mod_opt_tetra
- modinput
- modmain
- modmpi

**Calls:**
- axangsu2
- brzint
- brzint_new
- delete_k_vectors
- fsmooth
- genapwfr
- gendmat
- generate_k_vectors
- genlofr
- gensdmat
- getevalsv
- getevecfv
- getevecsv
- getoccsv
- init0
- init1
- linengy
- match
- opt_tetra_destroy
- opt_tetra_init
- opt_tetra_int_deltadiff
- opt_tetra_wgt_delta
- r3cross
- readfermi
- readstate
- xml_AddAttribute
- xml_AddCharacters
- xml_NewElement
- xml_OpenFile
- xml_close
- xml_endElement
- z2mm
- z2mmct
- zgemm
