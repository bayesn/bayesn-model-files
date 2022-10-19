# bayesn-model-files
A place for files specifying trained BayeSN models

Maintained by: Stephen Thorp (@stevet40), Kaisey S. Mandel (@CambridgeAstroStat), and Gautham Narayan (@gnarayan)

This repository will be periodically updated as new versions of BayeSN are published. The model files provided herein will be compatible with the [SNANA](https://github.com/RickKessler/SNANA/) implementation of BayeSN, and the [public BayeSN code](https://github.com/bayesn/bayesn-public).

## Repository Contents
Each subdirectory of the repository will have a name like `BAYESN.XYZ`, where `XYZ` is the shorthand name for a version of the model. The different models currently provided are [listed below](#provided-models). Each directory will contain the following standard set of files:
 * `BAYESN.INFO`: DOCANA format file containing some information about the model version.
 * `BAYESN.YAML`: YAML format file containing all parameters required to specify the model.
 * `bayesn.params`: SNANA params file containing a few default parameter ranges for simulation.

There will also be a set of text files specifying the model parameters. These contain the same information as `BAYESN.YAML`, and are provided for compatibility with the BayeSN Python implementation. They are:
 * `l_knots.txt`: A list of rest frame wavelength knot locations, in Angstroms.
 * `tau_knots.txt`: A list of rest frame phase knot locations, in days.
 * `W0.txt`: The _W<sub>0</sub>_ matrix describing the zeroth order warping of the Hsiao template which gives the mean intrinsic SED. This has a column for every phase knot, and a row for every wavelength knot (plus one extra row at the top and bottom).
 * `W1.txt`: The _W<sub>1</sub>_ matrix describing the first functional principal component. This is the same shape as `W0.txt`, with the rows/columns having the same meaning.
 * `L_Sigma_epsilon.txt`: The Cholesky factor of the residual covariance matrix.
 * `M0_sigma0_RV_tauA.txt`: Other global model parameters (intrinsic: _M<sub>0</sub>_, _σ<sub>0</sub>_; dust: _R<sub>V</sub>_, _τ<sub>A</sub>_).
 * `theta1_range.txt`: The minimum and maximum _θ<sub>1</sub>_ values from the training set.

## Provided Models

Details of currently provided models are given in the table below.

Model | Wavelength Range (Å) | Phase Range (days) | Description | Model Reference | Training Set Reference
--- | --- | --- | --- | --- | ---
`M20` | [3000, 18500] | [-10, 40] | Mandel+22 BayeSN model. Covers rest wavelength range of 3000-18500Å (_BVriYJH_). No treatment of host mass effects. Global _R<sub>V</sub>_ assumed. Trained on low-_z_ Avelino+19 compilation of CfA, CSP and others. | [Mandel et al. (2022)](https://ui.adsabs.harvard.edu/abs/2022MNRAS.510.3939M/abstract) | [Avelino et al. (2019)](https://ui.adsabs.harvard.edu/abs/2019ApJ...887..106A/abstract), and references therein
`T21` | [3500, 9500] | [-10, 40] | Thorp+21 BayeSN _No-Split_ model. Covers rest wavelength range of 3500-9500Å (_griz_). No treatment of host mass effects. Global _R<sub>V</sub>_ assumed. Trained on Foundation DR1 (Foley+18, Jones+19). | [Thorp et al. (2021)](https://ui.adsabs.harvard.edu/abs/2021MNRAS.508.4310T/abstract) | [Foley et al. (2018)](https://ui.adsabs.harvard.edu/abs/2018MNRAS.475..193F/abstract); [Jones et al. (2019)](https://ui.adsabs.harvard.edu/abs/2019ApJ...881...19J/abstract); [GitHub](https://github.com/djones1040/Foundation_DR1)
`W22` | [3000, 18500] | [-10, 40] | Ward+22 BayeSN model. Covers rest wavelength range of 3000-18500Å (_BgVrizYJH_). No treatment of host mass effects. Global _R<sub>V</sub>_ assumed. Trained on combination of Foundation DR1 (Foley+18, Jones+19) and Avelino+19 compilation. | [Ward et al. (2022)](https://ui.adsabs.harvard.edu/abs/2022arXiv220910558W/abstract) | [Avelino et al. (2019)](https://ui.adsabs.harvard.edu/abs/2019ApJ...887..106A/abstract), and references therein; [Foley et al. (2018)](https://ui.adsabs.harvard.edu/abs/2018MNRAS.475..193F/abstract); [Jones et al. (2019)](https://ui.adsabs.harvard.edu/abs/2019ApJ...881...19J/abstract)
