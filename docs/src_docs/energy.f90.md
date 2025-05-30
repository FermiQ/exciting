# energy.f90

## Overview

  The {\tt energy} subroutine computes the total energy and its individual contributions.
  The total energy is composed of kinetic, Coulomb, and exchange-correlation energy,
  %
  \begin{equation}
   E_{\rm tot}\,=\,T_{\rm s}\,+\,E_{C}\,+\,E_{\rm xc}.
  \end{equation}
  %
  The kinetic energy of the non-interacting system is given by
  %
  \begin{equation}
   T_{\rm s} = \sum_i n_i\epsilon_i \, - \, V_{\rm eff},
  \label{kinetic}
  \end{equation}
  %
  where $n_i$ are the occupancies and $\epsilon_i$ are the eigenvalues of both the core and
  valence states. The effective potential energy, $V_{\rm eff}$, can be expressed as
  %
  \begin{eqnarray}
   V_{\rm eff}\,&=&\,\int\rho({\bf r}) \, v_{\rm C}({\bf r}) \, d{\bf r} + \int\rho({\bf r}) \, v_{\rm xc}({\bf r})\,d{\bf r} \nonumber \\
                &+&\int {\bf m}({\bf r})\cdot\left[{\bf B}_{\rm xc}({\bf r})+{\bf B}_{\rm ext}({\bf r})\right]\,d{\bf r}.
  \label{Eeff}
  \end{eqnarray}
  %
  The first and second term of Eq.~(\ref{Eeff}) are the Coulomb potential energy, $V_{C}$, and
  exchange-correlation potential energy, $V_{\rm xc}$, respectively. ${\bf m}({\bf r})$ is the
  magnetization density, and ${\bf B}_{\rm xc}$ and ${\bf B}_{\rm ext}$ are the
  exchange-correlation effective magnetic and the external magnetic fields, respectively.

  The Coulomb energy consists of the Hartree energy, $E_{\rm H}$, the electron-nuclear energy, $
  E_{\rm en}$, and the nuclear-nuclear energy, $E_{\rm nn}$,
  %
  \begin{eqnarray}
   E_{\rm C}\,&=&\,E_{\rm H}\,+\,E_{\rm en}\,+\,E_{\rm nn} \nonumber \\
              &=&\,(\underbrace{E_{\rm H}\,+\,\frac{1}{2}E_{\rm en}})\,+\,(\underbrace{\frac{1}{2}E_{\rm en}\,+\,E_{\rm nn}}) \nonumber \\
              &=&\, \hspace{8mm} \frac{1}{2}V_{\rm C} \hspace{9.5mm} + \hspace{9mm} E_{\rm Madelung}.
  \label{Eq4}
  \end{eqnarray}
  %
  The Madelung energy is given by
  %
  \begin{eqnarray}
  E_{\rm Madelung}=\frac{1}{2}\sum_{\alpha}z_{\alpha}R_{\alpha},
  \end{eqnarray}
  where for each atom $\alpha$ with nuclear charge $z_{\alpha}$
  %
  \begin{eqnarray}
   R_{\alpha}=\lim_{r\rightarrow 0}\left(v^{\rm C}_{\alpha,00}(r)Y_{00} +\frac{z_{\alpha}}{r}\right)
  \end{eqnarray}
  %
  with $v^{\rm C}_{\alpha,00}$ being the $l=0$ component of the spherical harmonic expansion of
  $v_{\rm C}$ in the muffin-tin region. Using Eq.~(\ref{Eq4}), the electron-nuclear and Hartree
  energies can be expressed as
  %
  \begin{eqnarray}
   E_{\rm en}=2\left(E_{\rm Madelung}-E_{\rm nn}\right)
  \end{eqnarray}
  %
  and
  %
  \begin{eqnarray}
   E_{\rm H}=\frac{1}{2}(V_{\rm C}-E_{\rm en}).
  \end{eqnarray}
  %
  $E_{\rm xc}$ is obtained either by integrating the exchange-correlation energy density,
  %
  \begin{eqnarray}
   E_{\rm xc}\,=\, \int \rho({\bf r})\,\epsilon_{\rm xc}({\bf r})\,d{\bf r},
  \end{eqnarray}
  %
  or in the case of exact exchange, the explicit calculation of the Fock exchange integral.

  The energy from the external magnetic fields in the muffin-tins, {\tt bfcmt}, is always
  removed from the total since these fields are non-physical: their field lines do not close.
  The energy of the physical external field, {\tt bfieldc}, is also not included in the total
  because this field, like those in the muffin-tins, is used for breaking spin symmetry and
  taken to be infinitesimal. If this field is intended to be finite, then the associated energy,
  {\tt engybext}, should be added to the total by hand.
  See {\tt potxc}, {\tt exxengy} and related subroutines.

  Created Jun 2013
EOP
BOC

## Key Components

- SUBROUTINE energy

## Important Variables/Constants

- `Complex (8), Allocatable :: evecsv (:, :), c (:, :)` (No comment)
- `Integer :: is, ia, ias, ik, ist, idm, jdm, ir, lm` (No comment)
- `Real (8) :: v2(50)` (No comment)
- `Real (8) :: vn` (No comment)
- `Real (8), Parameter :: alpha = 1.d0 / 137.03599911d0` (No comment)
- `Real (8), Parameter :: ga4 = ge * alpha / 4.d0` (No comment)
- `Real (8), Parameter :: ge = 2.0023193043718d0` (No comment)

## Usage Examples

*TODO: Add usage examples if applicable.*

## Dependencies and Interactions

**Uses:**
- mod_hybrids
- modinput
- modmain

**Calls:**
- DFT_D2_energy
- TS_vdW_energy
- energykncr
- getevecsv
- potnucl
- zgemm
