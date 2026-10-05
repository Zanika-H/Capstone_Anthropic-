# Cross-Release Harmonization

## Research Question

How did patterns of Claude.ai usage across occupations and tasks change across AEI releases from February 2025 to June 2026?


## Cross-Release Comparison

| Release | Main File | Task Information | Occupation Information | Main Usage Measure | Time Period | Platform | Comparable? |
|---|---|---|---|---|---|---|---|
| Feb 2025 | `onet_task_mappings.csv` | `task_name`, `pct` | Not directly included | `pct` | TBD | TBD | TBD |
| Mar 2025 | `task_pct_v1.csv` | `task_name`, `pct` | Not directly included | `pct` | TBD | TBD | TBD |
| Sep 2025 | `aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv` | `facet = onet_task`; `onet_task_pct` | `facet = soc_occupation`; `soc_pct` | `value` | Aug. 4–11, 2025 | Claude AI (Free and Pro) | TBD |
| Jan 2026 | `aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv` | `facet = onet_task`; `onet_task_pct` | No direct `soc_occupation` facet found | `value` | Nov. 13–20, 2025 | Claude AI (Free and Pro) | TBD |
| Mar 2026 | `aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv` | `facet = onet_task`; `onet_task_pct` | No direct `soc_occupation` facet found | `value` | Feb. 5–12, 2026 | Claude AI (Free, Pro, and Max) | TBD |
| Jun 2026 | `aei_claude_ai_2026-06-26.csv` | `category_name = onet`; `metric_id = pct` | `category_name = soc_occupation`; `metric_id = pct` | `value` | May 1–June 1, 2026 | Claude AI | TBD |


## Findings from Initial Inspection

### Task-Level Data

All six selected releases contain some form of task-level information.

The February and March 2025 releases use a simple two-column structure:

- `task_name`
- `pct`

The September 2025, January 2026, and March 2026 releases use the `onet_task` facet with `onet_task_count` and/or `onet_task_pct`.

The June 2026 release uses:

- `category_name = onet`
- `metric_id = pct`
- `node_name`
- `node_external_id`

The June 2026 data therefore uses a different file structure from the earlier releases.


### Task Overlap

The selected releases contain substantial overlap in O*NET task names, although the number of tasks available changes across releases.

The number of unique tasks found in each release was:

| Release | Unique Tasks |
|---|---:|
| Feb 2025 | 3,514 |
| Mar 2025 | 3,514 |
| Sep 2025 | 2,618 |
| Jan 2026 | 3,170 |
| Mar 2026 | 3,260 |

The number of shared task names between releases was:

| Release Pair | Shared Tasks |
|---|---:|
| Feb 2025 vs Mar 2025 | 3,514 |
| Feb 2025 vs Sep 2025 | 2,203 |
| Feb 2025 vs Jan 2026 | 2,522 |
| Feb 2025 vs Mar 2026 | 2,565 |
| Mar 2025 vs Sep 2025 | 2,203 |
| Mar 2025 vs Jan 2026 | 2,522 |
| Mar 2025 vs Mar 2026 | 2,565 |
| Sep 2025 vs Jan 2026 | 2,357 |
| Sep 2025 vs Mar 2026 | 2,366 |
| Jan 2026 vs Mar 2026 | 2,888 |

The February and March 2025 releases contain the same 3,514 unique task names.

Later releases contain different task sets, but there is still substantial overlap between releases. This suggests that longitudinal task-level analysis may be possible using tasks that appear in multiple releases.

However, having the same task name does not automatically mean that its percentage can be compared across releases. The definitions and denominators of the percentage variables still need to be verified.


### Occupation-Level Data

Occupation-level information is not directly present in the February or March 2025 files.

The September 2025 release contains a `soc_occupation` facet with a `soc_pct` variable.

The January and March 2026 files did not return any records with `facet = soc_occupation` during the initial inspection.

The June 2026 release contains a `soc_occupation` category with a `pct` metric and explicit occupation names and SOC identifiers.

Therefore, direct occupation-level comparisons appear to be available for fewer releases than task-level comparisons.


### Initial Harmonization Concern

Although multiple releases contain task-level percentages, the variable names and data structures changed across releases.

For example:

- February and March 2025 use `pct`.
- September 2025, January 2026, and March 2026 use `onet_task_pct` stored in the `value` column.
- June 2026 uses `metric_id = pct` with the measurement stored in the `value` column.

These percentage values should not automatically be treated as directly comparable until the definitions and denominators for each release have been checked.

The same issue applies to occupation-level data.


## Key Findings So Far

All six selected releases contain task-level information, but their structures changed over time.

There is substantial overlap in O*NET task names across the releases. February and March 2025 contain the same 3,514 unique task names, while later releases contain somewhat different sets of tasks.

The February and March 2025 files do not contain occupation information directly.

September 2025 and June 2026 contain direct occupation-level information. January and March 2026 contain task-level information but did not return direct `soc_occupation` records during the initial inspection.

Task-level comparisons therefore appear more feasible across the releases than occupation-level comparisons.

However, the percentage definitions and denominators still need to be verified before determining which values can be directly compared across releases.


## Harmonization Questions

The following questions still need to be answered before creating the final cross-release dataset:

- How is a task identified in each release?
- How is an occupation identified in each release?
- What does `pct`, `onet_task_pct`, `soc_pct`, or `value` represent?
- Are the percentages calculated using the same denominator?
- What does one row represent in each release?
- Are the O*NET task identifiers or task definitions consistent across releases?
- Are occupation identifiers consistent across releases?
- Did the Claude.ai platform population change between releases?
- Did the measurement methodology change?
- Which variables can be compared directly across releases?


## Harmonization Decisions

To be completed after checking the documentation and definitions of the task and occupation percentage measures for each release.

At this stage, no release has been marked as fully comparable because the percentage definitions and denominators have not yet been verified.
