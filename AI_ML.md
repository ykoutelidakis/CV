<style>img {width: 250px;height: 150px;margin-right: 15px;float: left;}</style>

# AI & Machine Learning

## Graph Neural Networks for Financial Markets

At S&P Global, I co-led an inter-disciplinary project with Nvidia to apply Graph Neural Networks (GNNs) and Agent-Based Models (ABMs) to financial market analysis. This work was showcased at Nvidia's flagship 2025 GTC (GPU Technology Conference) in San Jose, California — [**watch the session on demand**](https://www.nvidia.com/en-us/on-demand/session/gtc25-s74726/).

### What are Graph Neural Networks?

GNNs are the learnable generalization of network science, where node representations are updated by aggregating information from neighboring nodes. In each layer, each node gathers ("aggregates") messages from its neighbors and updates itself with learnable weights. The key insight is that the structure itself becomes part of the model — graph topology encodes relationships that traditional ML approaches would require as explicit feature engineering.

**Key math.** A generic message-passing layer updates each node $v$ by aggregating transformed messages from its neighbours $\mathcal{N}(v)$:

$$
h_v^{(k)} = \mathrm{UPDATE}\!\left(h_v^{(k-1)},\ \underset{u \in \mathcal{N}(v)}{\mathrm{AGG}}\ \mathrm{MSG}\!\left(h_u^{(k-1)}\right)\right)
$$

The Graph Convolutional Network (GCN) is the canonical instance, with symmetric-normalised neighbour aggregation:

$$
H^{(l+1)} = \sigma\!\left(\tilde{D}^{-\tfrac{1}{2}}\,\tilde{A}\,\tilde{D}^{-\tfrac{1}{2}}\,H^{(l)}\,W^{(l)}\right),
\qquad \tilde{A} = A + I
$$

After $k$ layers, each node's representation encodes its $k$-hop neighbourhood.

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

This bridges **network science** — the subject of my peer-reviewed publications on interbank contagion — with **deep learning**, the modern AI toolkit.

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

## Foundations: From Econometrics to Modern ML

Much of modern AI/ML generalises the econometrics and credit-risk methods I have built and deployed in production for nearly two decades. The mapping below summarises how core techniques on this CV relate to their machine-learning counterparts:

| Established Method | Machine-Learning Generalisation |
|--------------------|---------------------------------|
| PD model (logistic regression) | Binary classification (cross-entropy loss) |
| LGD fractional regression | Regression with bounded / distributional targets |
| Vector Autoregression (VAR) | Sequence models (RNNs, attention) |
| Kalman filter | Optimal Bayesian state estimation for linear-Gaussian systems |
| Network science (interbank contagion) | Graph Neural Networks (learnable neighbour aggregation) |
| Agent-based modelling | Multi-agent / reinforcement-learning systems |
| Monte Carlo simulation | Importance sampling, variational inference |

The transition from classical econometrics to modern ML is largely a move from specifying relationships by hand to **learning them from data** — automatic feature engineering and model structure in place of explicit functional forms.

### Key Methods in Context

- **Agent-Based Models (ABM):** Rather than a single aggregate equation, many heterogeneous agents follow behavioural rules and macro behaviour (liquidity, price dynamics, cascades) emerges from their interactions — well suited to non-linear, out-of-equilibrium systemic-risk questions.
- **Loss Distribution Approach (LDA):** Frequency compounded with severity (e.g. Poisson–lognormal) yields an aggregate-loss distribution via Monte Carlo, closely related to generative modelling of loss trajectories.
- **Transition Matrices & Markov Chains:** The Point-in-Time versus Through-the-Cycle distinction reflects state-dependent dynamics; in a GNN, transition behaviour can be conditioned on the wider network state rather than on the issuer's rating alone.
- **Copulas & Dependence:** Separating marginals from dependence structure parallels how a GNN learns joint dependence through message passing, with the learned weights encoding how shocks propagate across the system.

---

Across these methods the common thread is a **network-science and systems-thinking lens** — now expressed through Graph Neural Networks and agent-based models — applied to long-standing problems in credit risk and macro-financial stability.
