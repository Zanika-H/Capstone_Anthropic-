# Dataset Notes

## 1. Dataset Provenance

### Dataset Name

Anthropic Economic Index

### Release

September 15, 2025 — Third Anthropic Economic Index Release

### Research Question

Do consumers and businesses use AI differently on the same tasks?

### Source URLs

**Anthropic report:**  
https://www.anthropic.com/research/anthropic-economic-index-september-2025-report

**Dataset repository:**  
https://huggingface.co/datasets/Anthropic/EconomicIndex/tree/main/release_2025_09_15/data

### Download Information

**Release/version:** September 15, 2025 — Third Anthropic Economic Index Release

**Data period:** August 4, 2025 through August 11, 2025

**Download date:** [09/07/2026]

**License:** CC-BY for the data; MIT for the accompanying code.

---

## 2. Documentation Notes

### Data Collection

The September 2025 AEI release contains Claude.ai usage data and first-party API (1P API) usage data.

The Claude.ai dataset contains usage metrics aggregated by geography and analysis dimensions (facets).

The 1P API dataset contains usage metrics based on a sample of first-party API traffic and uses privacy-preserving methods.

### Unit of Observation

For the Claude.ai data, each row represents one metric value for a specific geography and facet combination.

For the 1P API data, each row represents one metric value for a specific facet combination at the global level.

### Main Variables

Important variables include:

- `facet`
- `level`
- `variable`
- `cluster_name`
- `value`

The Claude.ai data also includes geographic information such as `geo_id` and `geography`.

### Collaboration / AI Use

The dataset includes collaboration patterns describing how humans and AI interact.

The documentation includes:

- `automation_pct`: percentage of classifiable collaboration that is automation-focused
- `augmentation_pct`: percentage of classifiable collaboration that is augmentation-focused

### Derived Metrics

The documentation states that some metrics are calculated during the enrichment process rather than being directly present in the raw data. These include indices, tiers, per-capita calculations, and automation/augmentation percentages.

### Data Files Relevant to My Research Question

Claude.ai:

`aei_raw_claude_ai_2025-08-04_to_2025-08-11.csv`

First-party API:

`aei_raw_1p_api_2025-08-04_to_2025-08-11.csv`

Both files are located in the `data/intermediate/` folder of the September 2025 release.

---

## 3. Verification Targets / Headline Numbers

The September 2025 Anthropic Economic Index report provides the following numbers that can be used as verification targets:

1. Claude.ai usage was dominated by computer and mathematical tasks, which accounted for approximately 36% of overall usage.

2. 1P API usage was approximately 77% automation-focused.

3. Claude.ai usage was approximately 50% automation-focused.

These numbers will be used to verify that the downloaded data and calculations are consistent with the published Anthropic Economic Index report.

---

## Label / Outcome Production

The AEI data contains measures describing how Claude is used in relation to human-AI collaboration.

For Claude.ai data, automation and augmentation percentages are derived during the enrichment process rather than being directly contained in the raw data.

Automation percentage represents the percentage of classifiable collaboration that is automation-focused.

Augmentation percentage represents the percentage of classifiable collaboration that is augmentation-focused.

The data also contains O*NET task classifications, which allow AI usage to be associated with specific occupational tasks.

---

## 4. Dataset Inventory

The inventory script (`src/inventory.py`) was used to examine the downloaded CSV files.

### Claimed vs. Actual Inventory

| File | Expected/Documented | Actual |
|---|---|---:|
| Claude.ai CSV | Downloaded from September 2025 release | 100,062 rows, 10 columns, 18.02 MB |
| 1P API CSV | Downloaded from September 2025 release | 33,794 rows, 10 columns, 6.70 MB |

### Missing Values

The 1P API file contains no missing values.

The Claude.ai file contains:

- 22 missing values in `geo_id` (0.02%)
- 450 missing values in `cluster_name` (0.45%)
- All other fields have no missing values.

The inventory was generated using `src/inventory.py`.

---

## Verification Results

### 1P API Automation

Anthropic reports that 1P API usage was approximately 77% automation-focused.

Using `src/verify_targets.py`, I calculated the automation percentage by adding the percentages for the `directive` and `feedback loop` collaboration patterns.

The calculated automation percentage was **77.37%**, which is consistent with Anthropic's published figure of approximately **77%**.

**Result: Match.**

### Claude.ai Automation

Anthropic reports that Claude.ai usage was approximately 50% automation-focused.

Using `src/verify_targets.py`, I examined the global Claude.ai collaboration percentages. The automation-focused categories are `directive` and `feedback loop`.

The calculated automation percentage was:

38.779816% + 10.318156% = **49.10%**

This is consistent with Anthropic's published figure of approximately **50%**.

**Result: Match.**

### Claude.ai Computer and Mathematical Tasks

Anthropic reports that approximately 36% of Claude.ai usage maps to Computer and Mathematical occupations.

Using the enriched Claude.ai dataset and the `soc_occupation` facet, the percentage for the `Computer and Mathematical` occupation group was **35.88%**.

This is consistent with Anthropic's published figure of approximately **36%**.

**Result: Match.**

---

## 5. Raw Data Examples

I inspected five raw rows from the Claude.ai dataset. The examples are from Andorra (`geo_id = AD`) for August 4–11, 2025.

1. A `collaboration_count` row with `cluster_name = not_classified` has a value of 25. This means 25 observations were classified as not_classified for this country and time period.

2. A `collaboration_pct` row with `cluster_name = not_classified` has a value of 62.5. This means the not_classified observations represented 62.5% of the collaboration observations.

3. A `collaboration_count` row with `cluster_name = task iteration` has a value of 15. This means 15 observations were classified as task iteration.

4. A `collaboration_pct` row with `cluster_name = task iteration` has a value of 37.5. This means task iteration represented 37.5% of the collaboration observations.

5. A `country` facet row with `variable = usage_count` has a value of 40. This represents the total usage count for this country and time period. The missing `cluster_name` is expected because this row is a total rather than a collaboration category.

These examples show that the dataset contains both count and percentage measurements and organizes metrics by facets such as collaboration and country. The count and percentage values are internally consistent because the collaboration counts sum to 40 and the corresponding percentages sum to 100%.

### Five Additional Raw Examples

I also inspected five additional raw rows from the Claude.ai dataset. These examples are from the United Arab Emirates (`geo_id = AE`) for August 4–11, 2025 and use the `request` facet.

6. A `request_count` row for "Debug and fix existing trading bot code and functionality" has a value of 19. This means there were 19 requests associated with this task.

7. A `request_pct` row for the same trading bot task has a value of 0.63102. This represents approximately 0.63% of requests in this group.

8. A `request_count` row for "Develop automated trading systems and technical analysis strategies" has a value of 32. This indicates that 32 requests were associated with this task.

9. A `request_pct` row for the automated trading systems task has a value of 1.06277. This represents approximately 1.06% of requests in this group.

10. A `request_count` row for "Draft new emails and messages from scratch for various purposes" has a value of 17. This shows that the dataset includes communication-related tasks as well as technical tasks.