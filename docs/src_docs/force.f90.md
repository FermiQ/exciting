# force.f90

## Overview

  Computes the various contributions to the atomic forces. In principle, the
  force acting on a nucleus is simply the gradient at that site of the
  classical electrostatic potential from the other nuclei and the electronic
  density. This is a result of the Hellmann-Feynman theorem. However because
  the basis set is dependent on the nuclear coordinates and is not complete,
  the Hellman-Feynman force is inacurate and corrections to it are required.
  The first is the core correction which arises because the core wavefunctions
  were determined by neglecting the non-spherical parts of the effective
  potential $v_s$. Explicitly this is given by
  $$ {\bf F}_{\rm core}^{\alpha}=\int_{\rm MT_{\alpha}} v_{\rm s}({\bf r})
   \nabla\rho_{\rm core}^{\alpha}({\bf r})\,d{\bf r} $$
  for atom $\alpha$. The second, which is the incomplete basis set (IBS)
  correction, is due to the position dependence of the APW functions, and is
  derived by considering the change in total energy if the eigenvector
  coefficients were fixed and the APW functions themselves were changed. This
  would result in changes to the first-variational Hamiltonian and overlap
  matrices given by
  \begin{align*}
   \delta H_{\bf G,G'}^{\alpha}&=i({\bf G-G'})
   \left(H^{\alpha}_{\bf G+k,G'+k}-\frac{1}{2}({\bf G+k})\cdot({\bf G'+k})
   \tilde{\Theta}_{\alpha}({\bf G-G'})e^{-i({\bf G-G'})\cdot{\bf r}_{\alpha}}
   \right)\\
   \delta O_{\bf G,G'}^{\alpha}&=i({\bf G-G'})\left(O^{\alpha}_{\bf G+k,G'+k}
   -\tilde{\Theta}_{\alpha}({\bf G-G'})e^{-i({\bf G-G'})\cdot{\bf r}_{\alpha}}
   \right)
  \end{align*}
  where both ${\bf G}$ and ${\bf G'}$ run over the APW indices;
  $\tilde{\Theta}_{\alpha}$ is the form factor of the smooth step function for
  muffin-tin $\alpha$; and $H^{\alpha}$ and $O^{\alpha}$ are the muffin-tin
  Hamiltonian and overlap matrices, respectively. The APW-local-orbital part
  is given by
  \begin{align*}
   \delta H_{\bf G,G'}^{\alpha}&=i({\bf G+k})H^{\alpha}_{\bf G+k,G'+k}\\
   \delta O_{\bf G,G'}^{\alpha}&=i({\bf G+k})O^{\alpha}_{\bf G+k,G'+k}
  \end{align*}
  where ${\bf G}$ runs over the APW indices and ${\bf G'}$ runs over the
  local-orbital indices. There is no contribution from the
  local-orbital-local-orbital part of the matrices. We can now write the IBS
  correction in terms of the basis of first-variational states as
  \begin{align*}
   {\bf F}_{ij}^{\alpha{\bf k}}=\sum_{\bf G,G'}
   b^{i{\bf k}*}_{\bf G}b^{j{\bf k}}_{\bf G'}\left(
   \delta H_{\bf G,G'}^{\alpha}-\epsilon_j\delta O_{\bf G,G'}^{\alpha}\right),
  \end{align*}
  where $b^{i{\bf k}}$ is the first-variational eigenvector.
  Finally, the ${\bf F}_{ij}^{\alpha{\bf k}}$ matrix elements can be
  multiplied by the second-variational coefficients, and contracted over all
  indices to obtain the IBS force:
  \begin{align*}
   {\bf F}_{\rm IBS}^{\alpha}=\sum_{\bf k}w_{\bf k}\sum_{l\sigma}n_{l{\bf k}}
   \sum_{ij}c_{\sigma i}^{l{\bf k}*}c_{\sigma j}^{l{\bf k}}
   {\bf F}_{ij}^{\alpha{\bf k}}
   +\int_{\rm MT_{\alpha}}v_{\rm s}({\bf r})\nabla\left[\rho({\bf r})
   -\rho^{\alpha}_{\rm core}({\bf r})\right]\,d{\bf r},
  \end{align*}
  where $c^{l{\bf k}}$ are the second-variational coefficients, $w_{\bf k}$
  are the $k$-point weights, $n_{l{\bf k}}$ are the occupancies, and
  $v_{\rm s}$ is the Kohn-Sham effective potential. See routines {\tt hmlaa},
  {\tt olpaa}, {\tt hmlalo}, {\tt olpalo}, {\tt energy}, {\tt seceqn} and
  {\tt gencfun}.

  Created January 2004 (JKD)
  Fixed problem with second-variational forces, May 2008 (JKD)
  k-point parallelisation of IBS forces, October 2013 (Andris)
EOP
BOC

## Key Components

- SUBROUTINE force

## Important Variables/Constants

- `Integer :: ik, is, ia, ias, nr, i` (No comment)
- `Real (8) :: rfmtinp` (No comment)
- `Real (8) :: sum, t1` (No comment)
- `Real (8) :: ts0, ts1` (No comment)
- `Real (8), Allocatable :: ffacg (:, :)` (No comment)
- `Real (8), Allocatable :: forcesum(:,:)` (No comment)
- `Real (8), Allocatable :: grfmt (:, :, :)` (No comment)
- `Real (8), Allocatable :: rfmt (:, :)` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- modinput
- modmain
- modmpi

**Calls:**
- DFT_D2_force
- MPI_ALLREDUCE
- TS_vdW_force
- forcek
- genffacg
- gradrfmt
- olprad
- symvect
- timesec
