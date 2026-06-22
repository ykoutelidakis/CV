<style>img {width: 250px;height: 150px;margin-right: 15px;float: left;}</style>

# Blockchain & DeFi

## Economic Protocol Design at RDX Works

While serving as Lead Economist at RDX Works (Radix layer-one protocol developer), I applied systems thinking and macroeconomic principles to design the economics of an algorithmic, partially-collateralized stablecoin protocol. This involved:

- Designing economic incentive structures and stability mechanisms for a decentralized stablecoin with focus on protocol-level risk controls
- Using macroeconomic frameworks (feedback loops, shock propagation, tail-risk management) to analyze nonlinear dynamics in liquidity management
- Applying network science principles to understand protocol-level contagion risks and cascade dynamics
- Designing market microstructure adapted to blockchain-native constraints (block times, MEV, atomic composability)

## Stablecoins: Taxonomy & Design

I studied a number of stablecoin projects both collateralised (fully or partially, on-chain and off-chain) and algorithmic (Constant Function Market Makers):

![](IMG/MCD.bmp)
<div>
    <p><b>Collateralized Stablecoins:</b> Multi-Collateral DAI, Terra-Luna, Frax, FEI, USDT, USDC</p>
    <p><b>Design dimensions:</b> Collateralization ratio, diversification, liquidation mechanics, governance incentives</p>
</div>

## Automated Market Makers & Market Microstructure

I analyzed AMM mechanisms and their market microstructure implications based on research including [Tarun Chitra's](https://web.stanford.edu/~boyd/papers/pdf/cfmm.pdf) and [Uniswap v.3](https://uniswap.org/whitepaper-v3.pdf) and [Curve](https://curve.fi/files/stableswap-paper.pdf) whitepapers:

![](IMG/CFMM.bmp)
<div> 
    <p><b>Core AMM Concepts:</b> Liquidity Pools, Impermanent Loss, Slippage, Miner Extractable Value (MEV), Protocol fees</p>
    <p><b>Price impact & execution:</b> Constant product formula, concentrated liquidity, bonding curves</p>
    <p><b>Risk factors:</b> Slippage, divergence loss, toxicity from informed flow, flash loan risks</p>
</div>

## Liquidity Demographics in Crypto

At S&P Global, I co-authored research on liquidity demographics within DeFi ecosystems, analyzing participant behavior and market microstructure in cryptocurrency trading. The research examined:

- Trading participation patterns across time zones and market regimes
- Liquidity concentration and market depth evolution
- Micro-structural drivers of price efficiency and volatility
- Insights for CFMM designs focused on reducing price impact and slippage

This work has informed thinking on liquidity-aware protocol design and the role of market microstructure in stable-asset protocols.