# bayesn-model-files
A place for files specifying trained BayeSN models

Maintained by: Stephen Thorp (@stevet40), Kaisey S. Mandel (@CambridgeAstroStat), and Gautham Narayan (@gnarayan)

This repository will be periodically updated as new versions of BayeSN are published. The model files provided herein will be compatible with the to-be-released BayeSN code. Once a public BayeSN code is available, we will link it here!

## Provided Models

Details of currently provided models are given in the table below.

Model | Wavelength Range (Å) | Phase Range (days) | Description | Model Reference | Training Set Reference
--- | --- | --- | --- | --- | --- | ---
`M20` | [3000, 18500] | [-10, 40] | Mandel+20 BayeSN model. Covers rest wavelength range of 3000-18500Å (_BVriYJH_). No treatment of host mass effects. Global _R<sub>V</sub>_ assumed. Trained on low-_z_ Avelino et al. (2019) compilation of CfA, CSP and others. | Mandel et al. (2020; [arXiv:2008.07538](https://arxiv.org/abs/2008.07538)) | Avelino et al. (2019; [arXiv:1902.03261](https://arxiv.org/abs/1902.03261), [ADS](https://ui.adsabs.harvard.edu/abs/2019ApJ...887..106A/abstract)), and references therein


## The Files Which Specify a BayeSN Model

Generically, a BayeSN model is specified by six `.txt` files which specify the various population level model parameters. The relevant files are:
 * `l_knots.txt`: A list of rest frame wavelength knot locations, in Angstroms.
 * `tau_knots.txt`: A list of rest frame phase knot locations, in days.
 * `W0.txt`: The _W<sub>0</sub>_ matrix describing the zeroth order warping of the Hsiao template which gives the mean intrinsic SED. This has a column for every phase knot, and a row for every wavelength know (plus one extra row at the top and bottom).
 * `W1.txt`: The _W<sub>1</sub>_ matrix describing the first functional principal component. This is the same shape as `W0.txt`, with the rows/columns having the same meaning.
 * `L_Sigma_epsilon.txt`: The Cholesky factor of the residual covariance matrix.
 * `M0_sigma0_RV_tauA.txt`: Other global model parameters (intrinsic: _M<sub>0</sub>_, _σ<sub>0</sub>_; dust: _R<sub>V</sub>_, _τ<sub>A</sub>_).
