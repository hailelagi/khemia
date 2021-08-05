# khemia

Source for research into the electro-chemical performance of maize straw (_mia zea_) in a molten hydroxide direct carbon
fuel cell. A simple model of a fuel cell is developed using [cantera's surface chemistry](https://cantera.org/)

> "The worst manifestations of exhaustion were successfully cured by a long period of rest but it was immediately
> apparent to me that I had lost once and for all my former capacity for carrying out experimental work until physically
> tired"
> 
> Friedrich Ostwald

## Installation and Dependencies
- Install [conda](https://docs.conda.io/en/latest/) or skip if you have Anaconda
- In the conda shell, enter `conda create --name modcfc --channel cantera/label/dev cantera numpy scipy matplotlib`
  to set up an environment with required packages
- activate the environment with `conda activate modcfc`

## Getting started
- Simulated model entry point is `model/modcfc.py`
- `plots` contains graphs of experimental data