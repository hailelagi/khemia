# khemia

Source for research into the electro-chemical performance of maize straw in solid oxide direct carbon fuel cell. 

## Introduction
A fuel cell can be defined as a device that produces electrical power directly from a fuel via an electrochemical process. They have some similarities with the more common [galvanic cell](https://en.wikipedia.org/wiki/Galvanic_cell) where they spontaneously produces a voltage due to the migration of free protons(hydrogen electrons freed due to oxidation) but reactants are stored outside the cell and are typically designed in a "stack" series due to the low volatage output.

This model(s) attempts to aid in experimentally determining the feasibility of a carbon-based fuel in a solid oxide direct carbon fuel cell(SOFC). The major reasons for the development of a computational model are -
- Isolating interesting variables
- Cost of fabrication and material costs
- Speed of experimental iteration

> "The worst manifestations of exhaustion were successfully cured by a long period of rest but it was immediately apparent to me that I had lost once and for all my former capacity for carrying out experimental work until physically tired"
> Friedrich Ostwald

SOFCs are an interesting choice, because the raw material(s) required as a fuel are inexpensive, abundant and most importantly sustainable. The by-product of this process is harmless - water.

However, this particular fuel cell is plagued with a fundamental question. *Slow reaction rates. (ie. Activation energy required for oxidation and reduction)* Solid oxide direct carbon fuel cells require rediculous amounts thermal energy - north of 600 degrees celcius and peaking in the 1000 range. This occurs because the useful "fuel" is actually Impure Hydrogen that is released during combustion. Not withstanding they have an wide range of applicability from vehicle battries(kw) to power stations(mw). However, the ceramic material which could withstand such high temperatures are expensive to manufacture and often fragile. At larger scales this could prove problematic, however it has _little to no moving parts_ and makes no noise!

## How to Figure out Efficiency? How good is this cell anyway?
_brace yourself :) sketchy math ahead!_

There are several energy sources at play here, electrical energy which is easy enough to compute
`Power = V x I` and 
`Energy = V x I x t`

What about the chemical energy though? We're mostly concerned with `Gibbs free energy`. Put simply and at the risk of sounding non-techinical, how much heat (at constant pressure) can make a reaction occur?
`ΔG = ΔH − TΔS`

we might need the Nernst equation here too! why? well if temperature at both anode and cathode is taken into account(it's an exothermic reaction) what about pressure and concentration? which are likely to vary?
# TODO: add latex formatting for the Nernst equation


