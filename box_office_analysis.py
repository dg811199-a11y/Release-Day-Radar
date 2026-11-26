# Release Day Radar - correlation and charts (run in Colab or locally)
# Data: YouTube stats and sentiment from MySQL queries 2 and 4; opening weekend = first 3 days from
# release day, India net, Rs crore (Bollywood Hungama for Hindi films, Sacnilk all-language for others).
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr, spearmanr

df = pd.DataFrame({
    "movie": ["Chhaava", "Saiyaara", "Housefull 5", "Dhurandhar", "Kantara Chapter 1",
              "Coolie", "They Call Him OG", "Lokah Chapter 1"],
    "language": ["Hindi", "Hindi", "Hindi", "Hindi", "Kannada", "Tamil", "Telugu", "Malayalam"],
    "views": [81728339, 81394643, 33956584, 101967499, 23925371, 29543836, 18054008, 16311601],
    "engagement_rate": [1.6329, 1.0240, 1.8934, 0.9490, 3.4209, 2.9564, 4.2807, 1.2562],
    "positive_pct": [54, 69, 80, 50, 52, 43, 29, 54],
    "negative_pct": [27, 13, 10, 28, 27, 42, 44, 25],
    "opening_weekend_cr": [121.43, 84.50, 81.85, 106.50, 162.85, 158.35, 100.70, 14.30],
})

# 1. Correlations (n = 8, so treat as indicative only)
rows = []
for col in ["views", "engagement_rate", "positive_pct", "negative_pct"]:
    r, p = pearsonr(df[col], df["opening_weekend_cr"])
    s, sp = spearmanr(df[col], df["opening_weekend_cr"])
    rows.append([col, round(r, 2), round(p, 2), round(s, 2), round(sp, 2)])
corr = pd.DataFrame(rows, columns=["metric", "pearson_r", "pearson_p", "spearman_rho", "spearman_p"])
print(corr.to_string(index=False))
corr.to_csv("correlation_results.csv", index=False)

# 2. Scatter charts with finding-style titles
def scatter(x, xlabel, title, fname):
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(df[x], df["opening_weekend_cr"], s=60)
    for _, r in df.iterrows():
        ax.annotate(r["movie"], (r[x], r["opening_weekend_cr"]), fontsize=8,
                    xytext=(4, 4), textcoords="offset points")
    ax.set_xlabel(xlabel); ax.set_ylabel("Opening weekend, India net (Rs crore)")
    ax.set_title(title, fontsize=11, loc="left")
    fig.tight_layout(); fig.savefig(fname, dpi=150); plt.close(fig)

scatter("views", "YouTube trailer views (cumulative, 26 Nov 2026)",
        "Trailer views did not predict opening weekends (r = 0.08, n = 8)", "chart1_views_vs_opening.png")
scatter("engagement_rate", "Engagement rate (%)",
        "Engagement rate shows a weak, non-significant link to openings (r = 0.51, p = 0.20)",
        "chart2_engagement_vs_opening.png")

# 3. Min-max normalised comparison (one chart, films on the same scale)
cols = ["views", "engagement_rate", "positive_pct", "opening_weekend_cr"]
norm = (df[cols] - df[cols].min()) / (df[cols].max() - df[cols].min())
norm.index = df["movie"]
ax = norm.plot(kind="bar", figsize=(10, 5))
ax.set_ylabel("Min-max scaled value (0 to 1)"); ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.28), ncol=4)
ax.set_title("On one scale, no online signal lines up with opening weekends", loc="left", fontsize=11)
plt.xticks(rotation=30, ha="right"); plt.tight_layout()
plt.savefig("chart3_normalised.png", dpi=150); plt.close()
print("Charts saved")
