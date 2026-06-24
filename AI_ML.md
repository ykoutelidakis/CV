<style>img {width: 250px;height: 150px;margin-right: 15px;float: left;}</style>

# AI & Machine Learning

## Graph Neural Networks for Financial Markets

At S&P Global, I contributed to an inter-disciplinary project with Nvidia to apply Graph Neural Networks (GNNs) and Agent-Based Models (ABMs) to financial market analysis, under the supervision of S&P Global's CTO and led by the company's Chief Innovation Officer. There I assisted in the decomposition and analysis of the underpinning variables to help formulate the nodes and edges of the graph and helped with setting reasonable "bands" of tolerance for the data.  This work was showcased at Nvidia's flagship 2025 GTC (GPU Technology Conference) in San Jose, California — [**watch the session on demand**](https://www.nvidia.com/en-us/on-demand/session/gtc25-s74726/).

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

For how these methods connect to my broader work on networks and the mapping from classical econometrics to modern ML, see [Systems Thinking & Network Science](Systems.md).
