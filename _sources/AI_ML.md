<style>img {width: 250px;height: 150px;margin-right: 15px;float: left;}</style>

# AI & Machine Learning

## Graph Neural Networks for Financial Markets

At S&P Global, I co-led an inter-disciplinary project with Nvidia to apply Graph Neural Networks (GNNs) and Agent-Based Models (ABMs) to financial market analysis. This work was showcased at Nvidia's flagship 2025 GTC (GPU Technology Conference) in San Jose, California.

### What are Graph Neural Networks?

GNNs are the learnable generalization of network science, where node representations are updated by aggregating information from neighboring nodes. In each layer, each node gathers ("aggregates") messages from its neighbors and updates itself with learnable weights. The key insight is that the structure itself becomes part of the model — graph topology encodes relationships that traditional ML approaches would require as explicit feature engineering.

**Key math:** Message passing and GCN layers aggregate neighbor features:

```
h_v^(k) = UPDATE(h_v^(k-1), AGG_{u ∈ N(v)} MSG(h_u^(k-1)))
```

After k layers, each node's representation encodes its k-hop neighborhood.

### Application to Bond Markets

We applied GNNs to model the US corporate bond market by representing:

- **Nodes:** Individual bond issuers (corporations)
- **Edges:** Financial relationships (subsidiary relations, supply chain links, competitive dynamics, common investors)
- **Features:** Issuer characteristics (credit ratings, financial metrics, market positioning)
- **Target:** Credit risk metrics (default probability, spread predictions, systemic importance)

The GNN learns to predict bond-level credit risk by combining:
1. **Node features:** Issuer fundamentals
2. **Neighborhood structure:** How an issuer connects to systemically important peers
3. **Contagion dynamics:** How shocks propagate through financial networks

### Why GNNs for Finance?

Traditional credit models use issuer-level features (EBITDA/leverage, profitability, industry). They miss **contagion** — that a seemingly healthy company can face credit stress if its major customers, suppliers, or lenders experience distress.

GNNs automatically learn to propagate information across the network, capturing:
- Direct exposure: a company's direct borrowing relationships
- Indirect exposure: contagion through shared suppliers, customers, or markets
- Systemic importance: how central a company is to the broader financial network

This bridges **network science** (the field you published on) with **deep learning** (the modern AI toolkit).

### Modeling Approach

We implemented an Agent-Based Model where:
1. Each bond issuer is an agent with a state (credit quality, leverage, market dynamics)
2. Agents interact through financial networks (credit links, supply chains, market competition)
3. Shocks propagate through the network (e.g., one issuer's distress increases financing costs for peers)
4. The ABM emerges macro-level behaviors (credit contagion cascades, portfolio losses)
5. GNNs learn the relationship between network structure and credit outcomes

This combines:
- **Econometrics:** Time-series credit dynamics, scenario analysis
- **Network Science:** Graph structure, centrality, contagion paths
- **Deep Learning:** Learnable message passing, non-linear representations

## AI and Machine Learning Foundations

### Relationship to Your Existing Work

The through-line to articulate: most "AI/ML" techniques are generalizations of the econometrics and credit risk tools you've deployed for two decades:

| Your Tool | ML Generalization |
|-----------|-------------------|
| PD Model (logistic regression) | Binary Classification (cross-entropy loss) |
| LGD Fractional Regression | Regression with distributional targets |
| VAR time series | RNN/Attention (sequence modeling) |
| Kalman filter | Optimal Bayesian state estimation for linear-Gaussian systems |
| Network science (your publications) | Graph Neural Networks (learnable neighbor aggregation) |
| Agent-based modeling | Multi-agent reinforcement learning |
| Monte Carlo simulation | Importance sampling, variational inference |

The shift from traditional econometrics to modern ML is largely one of **learning the relationships** (automatic feature engineering and model structure) instead of specifying them by hand.

### Key Concepts Referenced in Your CV

**Agent-Based Models (ABM):** Instead of one equation for the whole market, simulate many heterogeneous agents following behavioral rules and let macro behavior (liquidity, price dynamics, cascades) emerge from interactions. Non-linear, out-of-equilibrium, good for studying systemic risk.

**Loss Distribution Approach (LDA):** Compound (Poisson × severity) to get aggregate loss distribution. This is Monte Carlo sampling — you can view it as generative modeling of loss trajectories.

**Transition Matrices & Markov Chains:** PiT vs. TTC distinction is about state-dependent dynamics. With GNNs, the transition probabilities can depend on the broader network state, not just the current issuer rating.

**Copulas & Dependence:** Separate marginals from dependence structure. A GNN effectively learns the joint dependence by message passing — the learned weights encode how shocks propagate across dimensions.

---

**Interview angle:** When probed on AI/ML, anchor to the table above. You're not learning ML from zero — you're relabeling and extending a production toolkit you've shipped for two decades. The GNN application is simply network science (which you've published on) made learnable and applied to credit risk (your domain).
