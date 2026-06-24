# Systems Thinking & Network Science

A through-line across my work — from peer-reviewed research on interbank contagion to DeFi protocol design and the Nvidia GNN project — is a **systems-thinking and network-science lens**: modelling financial and economic systems as interconnected networks where structure, feedback and non-linear contagion drive outcomes, as opposed to linear regressions. That is the only way to accurately capture empirically observed behaviours.
Whether it's climate (absorbing state of ruin), credit risk (again the default grade is an absorbing state), the ensemble vs. time series dichotomy of LGD-PD relationship, the non-linearity assumption for impacts at the heart of all stress-testing exercises (a 5% GDP drop will **not** cause 5x as many losses as a 1% recession) or the eye-watering Gini coefficients of most blockchain wallet distributions the one common thread is **non-linear impacts**. This has informed my interest in non-linear, structural models, where SME expertise and intuition can be deployed to assist with modeling and explainability, rather than defaulting to reduced form, black-box approaches.

## From Econometrics to Modern ML

Much of modern AI/ML generalises the econometrics and credit-risk methods I have built and deployed in production for nearly two decades. Data science was not a common term when I started working in 2005 - it was just called statistics. The mapping below summarises how core techniques on my CV relate to their machine-learning counterparts:

| Established Method | Machine-Learning Generalisation |
|--------------------|---------------------------------|
| PD model (logistic regression) | Binary classification (cross-entropy loss) |
| LGD fractional regression | Regression with bounded / distributional targets |
| Vector Autoregression (VAR) | Sequence models (RNNs, attention) |
| Kalman filter | Optimal Bayesian state estimation for linear-Gaussian systems |
| Network science (interbank contagion) | Graph Neural Networks (learnable neighbour aggregation) |
| Agent-based modelling | Multi-agent / reinforcement-learning systems |
| Monte Carlo simulation | Importance sampling, variational inference |

The transition from classical econometrics to modern ML is largely a move from specifying relationships by hand to **learning them from data** — automatic feature engineering and model structure in place of explicit functional forms. In the end, we still need to embed these forms in the model somehow - whether they emerge through parameter fitting during training, as a result of the interactions of agents in a network ABM or we code them in manually. 

## Key Methods in Context

- **Agent-Based Models (ABM):** Rather than a single aggregate equation, many heterogeneous agents follow behavioural rules and macro behaviour (liquidity, price dynamics, cascades) emerges from their interactions — well suited to non-linear, out-of-equilibrium systemic-risk questions.
- **Loss Distribution Approach (LDA):** Frequency compounded with severity (e.g. Poisson–lognormal) yields an aggregate-loss distribution via Monte Carlo, closely related to generative modelling of loss trajectories.
- **Transition Matrices & Markov Chains:** The Point-in-Time versus Through-the-Cycle distinction reflects state-dependent dynamics; in a GNN, transition behaviour can be conditioned on the wider network state rather than on the issuer's rating alone.
- **Copulas & Dependence:** Separating marginals from dependence structure parallels how a GNN learns joint dependence through message passing, with the learned weights encoding how shocks propagate across the system.

---

Across these methods the common thread is a **network-science and systems-thinking lens** — now expressed through Graph Neural Networks and agent-based models — applied to long-standing problems in credit risk and macro-financial stability.
