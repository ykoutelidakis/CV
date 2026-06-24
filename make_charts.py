"""
Regenerate the illustrative charts used across the CV pages with a consistent,
high-contrast, high-DPI theme. Output filenames match the existing IMG/ assets so
the Markdown `![](IMG/...)` references continue to resolve.

These are schematic/illustrative figures (not real client data); they exist to
convey the shape of each method. Run automatically in CI before the book build.
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import gridspec

np.random.seed(7)

IMG = os.path.join(os.path.dirname(__file__), "IMG")
os.makedirs(IMG, exist_ok=True)

# --- consistent theme: bold, readable at small (250px) display sizes ---
NAVY   = "#16324f"
BLUE   = "#1f6fb2"
TEAL   = "#0e8f9c"
RED    = "#d7301f"
GREEN  = "#1a9850"
PURPLE = "#6a51a3"
FILL   = "#bcd4ea"
GRID   = "#c9c9c9"

plt.rcParams.update({
    "figure.dpi": 150,
    "savefig.dpi": 150,
    "savefig.bbox": "tight",
    "font.size": 13,
    "axes.titlesize": 15,
    "axes.titleweight": "bold",
    "axes.labelsize": 13,
    "axes.edgecolor": "#444444",
    "axes.linewidth": 1.1,
    "axes.grid": True,
    "grid.color": GRID,
    "grid.linewidth": 0.8,
    "grid.alpha": 0.5,
    "lines.linewidth": 2.6,
    "legend.fontsize": 11,
    "legend.frameon": True,
})


def save(fig, name):
    fig.savefig(os.path.join(IMG, name), facecolor="white")
    plt.close(fig)
    print("wrote", name)


# 1. CDS spread (Macro) ------------------------------------------------------
def cds():
    yrs = np.arange(2005, 2010.9, 0.25)
    spread = np.array([10,10,11,11,12,12,13,14,15,20,30,50,70,60,50,40,
                       35,30,25,20,15,15,14,14])[:len(yrs)]
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(yrs, spread, color=NAVY, marker="o", markersize=5,
            markerfacecolor=BLUE, markeredgecolor=NAVY)
    ax.set_title("CDS Spread 2005-2010 (Quarterly)")
    ax.set_xlabel("Year"); ax.set_ylabel("CDS Spread (basis points)")
    save(fig, "CDS.jpg")


# 2. Nowcast vs actual GDP (Macro) ------------------------------------------
def nowcast():
    yrs = np.arange(2005, 2010.9, 0.25)
    actual = np.array([3.5,3.8,4.0,4.2,4.4,4.5,4.3,4.1,3.6,2.8,1.5,0.5,
                       -0.5,-1.5,-2.5,-3.0,-2.5,-1.5,0.5,1.5,2.0,2.5,3.0,3.0])[:len(yrs)]
    nowc = actual + np.array([0,-0.05,-0.25,0.25,-0.1,0.1,0,-0.2,0.3,0.2,0,-0.2,
                              -0.1,0.3,0,-0.05,0,0,0.45,0,0.1,0.2,-0.3,0])[:len(yrs)]
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(yrs, actual, color=NAVY, marker="o", markersize=4, label="Actual GDP YoY Growth")
    ax.plot(yrs, nowc, color=RED, ls="--", lw=2.2, label="NowCast GDP YoY Growth")
    ax.axhline(0, color="#888", lw=1)
    ax.set_title("GDP Nowcast vs Actual (YoY %)")
    ax.set_xlabel("Year"); ax.set_ylabel("GDP YoY Growth (%)")
    ax.legend()
    save(fig, "NowCast.png")


# 3. OBR output-gap impulse response (Macro) --------------------------------
def obr2():
    t = np.arange(0, 20)
    resp = -1.0 * np.exp(-0.22 * t)
    fig, ax = plt.subplots(figsize=(8, 4.4))
    ax.axhline(0, color="#666", ls="--", lw=1.5)
    ax.plot(t, resp, color=NAVY, marker="o", markersize=5, markerfacecolor=BLUE,
            label="Output Gap Response")
    ax.set_title("Output Gap Impulse Response")
    ax.set_xlabel("Time Periods"); ax.set_ylabel("Output Gap")
    ax.legend()
    save(fig, "OBR2.jpg")


# 4. ECL loss distribution (Credit/Climate) ---------------------------------
def ecl():
    s = np.random.lognormal(mean=0.7, sigma=0.55, size=40000)
    fig, ax = plt.subplots(figsize=(8, 4.4))
    ax.hist(s, bins=120, range=(0, 12), density=True, color=FILL,
            edgecolor="none", label="Frequency of Losses")
    xs = np.linspace(0, 12, 400)
    from math import pi
    pdf = (1/(xs*0.55*np.sqrt(2*pi)+1e-9))*np.exp(-(np.log(xs+1e-9)-0.7)**2/(2*0.55**2))
    ax.plot(xs, pdf, color=NAVY, lw=2.6, label="Fitted PDF")
    for val, col, lab in [(2.09, TEAL, "Expected Loss (EL) = 2.09"),
                          (3.20, PURPLE, "Unexpected Loss (UL) = 3.20"),
                          (4.21, NAVY, "95% VaR = 4.21"),
                          (5.24, RED, "Expected Shortfall (ES) = 5.24"),
                          (4.88, GREEN, "Median Shortfall (MS) = 4.88")]:
        ax.axvline(val, color=col, ls="--", lw=2)
        ax.plot([], [], color=col, ls="--", label=lab)
    ax.set_title("ECL = PD x LGD x EAD")
    ax.set_xlabel("Potential Loss"); ax.set_ylabel("Frequency")
    ax.legend(fontsize=9)
    save(fig, "ECL.png")


# 5. TTC vs PiT PD (Credit) -------------------------------------------------
def pit_ttc():
    t = np.linspace(0, 32, 500)
    pit = 0.05 + 0.02*np.sin(0.6*t) + 0.012*np.sin(1.4*t+0.5)
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.axhline(0.05, color=NAVY, ls="--", lw=2.4, label="TTC PD")
    ax.plot(t, pit, color=RED, lw=2.6, label="Irregular PiT PD")
    ax.set_ylim(0, 0.10)
    ax.set_title("TTC PD vs Irregular PiT PD Over Time")
    ax.set_xlabel("Time"); ax.set_ylabel("Probability of Default")
    ax.legend()
    save(fig, "PIT_TTC.png")


# 6. GDP fan chart (Credit) -------------------------------------------------
def ar_mc():
    yrs = np.arange(2020, 2051)
    centre = 100 * (1.025) ** (yrs - 2020)
    h = (yrs - 2020)
    fig, ax = plt.subplots(figsize=(8, 4.4))
    for k, alpha, col in [(0.06, 0.30, FILL), (0.035, 0.55, BLUE)]:
        band = centre * k * np.sqrt(h)
        ax.fill_between(yrs, centre - band, centre + band, color=col, alpha=alpha)
    ax.plot(yrs, centre, color=NAVY, lw=2.6, label="GDP Forecast (central)")
    ax.fill_between([], [], color=FILL, alpha=0.6, label="80% Confidence Interval")
    ax.fill_between([], [], color=BLUE, alpha=0.6, label="60% Confidence Interval")
    ax.set_title("GDP Forecast 2020-2050 with Uncertainty (Fan Chart)")
    ax.set_xlabel("Year"); ax.set_ylabel("GDP")
    ax.legend()
    save(fig, "AR_MC.jpg")


# 7. Merton Z-factor shift (Climate) ----------------------------------------
def merton():
    x = np.linspace(40, 170, 400)
    def npdf(x, mu, sd): return np.exp(-(x-mu)**2/(2*sd**2))/(sd*np.sqrt(2*np.pi))
    fig, ax = plt.subplots(figsize=(8, 4.0))
    ax.plot(x, npdf(x, 105, 20), color=BLUE, lw=2.6, label="Original (Z = 0)")
    ax.plot(x, npdf(x, 135, 20), color=RED, lw=2.6, label="Shifted (Z = 1.5)")
    ax.fill_between(x, npdf(x, 105, 20), color=BLUE, alpha=0.12)
    ax.fill_between(x, npdf(x, 135, 20), color=RED, alpha=0.12)
    ax.set_title("Effect of Z-factor on Asset Value Distribution (Merton)")
    ax.set_xlabel("Asset Value"); ax.set_ylabel("Density")
    ax.legend()
    save(fig, "Merton.png")


# 8. LDA mixture (Climate) --------------------------------------------------
def lda():
    a = np.random.normal(500, 300, 9000).clip(0)
    b = np.random.normal(5200, 1400, 7000).clip(0)
    agg = np.concatenate([a, b])
    fig, ax = plt.subplots(figsize=(8, 4.4))
    ax.hist(agg, bins=70, range=(0, 12000), color=FILL, edgecolor=NAVY,
            linewidth=0.4, label="Aggregated Loss Distribution")
    ax.axvline(np.percentile(agg, 95), color=RED, ls="--", lw=2.2, label="VaR (95%)")
    ax.axvline(agg.mean(), color=GREEN, ls="--", lw=2.2, label="Mean Loss")
    ax.set_title("Loss Distribution Approach (LDA)")
    ax.set_xlabel("Loss"); ax.set_ylabel("Frequency")
    ax.legend()
    save(fig, "LDA.png")


# 9. Copula joint + marginals (Climate) -------------------------------------
def copula():
    n = 1400
    x = np.random.normal(0, 1, n)
    y = 0.0 * x + np.random.normal(0, 1, n)
    fig = plt.figure(figsize=(6.4, 6.4))
    gs = gridspec.GridSpec(4, 4, hspace=0.05, wspace=0.05)
    axm = fig.add_subplot(gs[1:4, 0:3])
    axt = fig.add_subplot(gs[0, 0:3], sharex=axm)
    axr = fig.add_subplot(gs[1:4, 3], sharey=axm)
    axm.scatter(x, y, s=12, color=BLUE, alpha=0.5, edgecolors="none")
    axm.set_xlabel("X"); axm.set_ylabel("Y")
    axt.hist(x, bins=28, color=TEAL, edgecolor="white", linewidth=0.4)
    axr.hist(y, bins=28, orientation="horizontal", color=TEAL,
             edgecolor="white", linewidth=0.4)
    for a in (axt, axr):
        a.axis("off")
    axt.set_title("t-Copula: joint dependence with marginals", fontsize=13)
    save(fig, "Copula.png")


# 10. Empirical vs fitted return distribution (Climate) ---------------------
def var_chart():
    r = np.random.normal(0, 1, 30000)
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.hist(r, bins=80, density=True, color=FILL, edgecolor="none",
            label="Empirical Distribution")
    xs = np.linspace(-4, 4, 400)
    ax.plot(xs, np.exp(-xs**2/2)/np.sqrt(2*np.pi), color=NAVY, lw=2.6,
            label="Fitted Normal Distribution")
    for val, col, lab in [(-1.64, BLUE, "VaR 5%"),
                          (-2.06, PURPLE, "Expected Shortfall"),
                          (-3.0, RED, "Maximum Shortfall")]:
        ax.axvline(val, color=col, ls="--", lw=2, label=lab)
    ax.set_title("Empirical vs Fitted Return Distribution (VaR, ES, MS)")
    ax.set_xlabel("Returns"); ax.set_ylabel("Density")
    ax.legend(fontsize=9)
    save(fig, "VAR.jpeg")


# 11. Sectoral decarbonisation pathway (Climate) ----------------------------
def sda():
    yrs = np.arange(2020, 2040)
    pathway = 100 * (1 - 0.034) ** (yrs - 2020)
    rng = np.random.default_rng(3)
    company = pathway + rng.normal(0, 4, len(yrs)) + np.linspace(8, -4, len(yrs))
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(yrs, pathway, color=TEAL, lw=2.6, label="Sectoral Decarbonisation Pathway")
    ax.plot(yrs, company, color=NAVY, marker="o", markersize=4, label="Company's Emissions")
    ax.fill_between(yrs, pathway, company, where=(company >= pathway),
                    color=RED, alpha=0.30, label="Above SDA Pathway")
    ax.fill_between(yrs, pathway, company, where=(company < pathway),
                    color=GREEN, alpha=0.30, label="Below SDA Pathway")
    ax.set_title("Emission Profile under Sectoral Decarbonisation Approach")
    ax.set_xlabel("Year"); ax.set_ylabel("Emissions (MtCO2e)")
    ax.legend(fontsize=9)
    save(fig, "SDA.jpeg")


if __name__ == "__main__":
    cds(); nowcast(); obr2(); ecl(); pit_ttc(); ar_mc()
    merton(); lda(); copula(); var_chart(); sda()
    print("All charts regenerated.")
