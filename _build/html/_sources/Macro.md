# Macroeconomics

Over the years I have produced econometric models (in EViews, Matlab, R, Excel, Python, VBA) for various business needs as well as written reports (regular or ad-hoc) on a number of macro-themes (EM, DM, China, markets, financial contagion), including producing a number of publications in peer reviewed academic journals.

## Market-implied PD
<style>img {width: 250px;height: 150px;margin-right: 15px;float: left;}</style>

While at Fathom Consulting, I built a model to extract market-implied conditional Sovereign PD from CDS spreads, based on Bank of England research and the CDS valuation paper of [O'Kane & Turnbull 2003](https://quantlabs.net/academy/download/free_quant_instituitional_books_/%5BLehman%20Brothers%5D%20Valuation%20of%20Credit%20Default%20Swaps.pdf)

![](IMG/CDS.jpg)
<div>
    <p>Extract the CDS  implied PD using a hazard rate approach.</p>
    <p>Apply a bivariate copula to the marginal PD distributions of each sovereign and extract the joint distribution.</p>
    <p>Estimate the conditional PD of one sovereign defaulting, as the ratio of the joint over the marginal.</p>
</div>



## Nowcasting GDP
<style>img {width: 250px;height: 150px;margin-right: 15px;float: left;}</style>

While at Fathom Consulting, I replicated the ECB published [Nowcasting methodology](https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1275.pdf?145bf6e35251eedc79d9b1b6ff325e7a) of Reichlin & Giannone, using Kalman filtering, VAR and bridging with factors.

![](IMG/NowCast.png)
<div>
    <p>This involves Kalman-filtering the various, high-frequency, inputs.</p>
    <p>Then we proceed to extract a set of common factors which are then bridged into the appropriate (lower) frequency.</p> 
    <p>Gaps are filled to deal with rugged-edges due to asynchronous publication schedules.Finally the factors are used in a VAR to estimate GDP.</p>
</div>

## OBR macro model

At NatWest Group (then RBS) I worked on macro-economic scenario design and expansion, building a  scenario expansion engine based on the [OBR's](https://obr.uk/) own [econometric model](https://obr.uk/docs/dlm_uploads/Working-paper-No4-A-small-model-of-the-UK-economy.pdf).

The OBR Small model is based around four core behavioural equations:

<style>img {width: 250px;height: 175px;margin-right: 15px;float: left;}</style>
![](IMG/OBR.png)
<div>
    <p>1. IS relation</p>
    <p>2. Philips Curve</p>
    <p>3. Uncovered Interest Parity (UIP)</p>
    <p>4. Central Bank Reaction function (Taylor rule)</p>
</div>

With a number of extensions for:

<style>img {width: 250px;height: 150px;margin-right: 15px;float: left;}</style>
![](IMG/OBR2.jpg)
<div>
    <p>5. Credit Spreads (I implemented that using a simplified Nelson-Siegel approach)</p>
    <p>6. Unconventional Monetary Policy (QE)</p>
    <p>7. Public Finances (Debt Sustainability Analysis equations)</p>
</div>

 









