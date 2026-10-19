# Cross-Release Harmonization

## Research Question

How did patterns of Claude.ai usage across occupations and tasks change across AEI releases from February 2025 to June 2026?

## Cross-Release Comparison

| Release | Main File | Task Information | Occupation Information | Usage Measure | Time Period | Comparable? |
|---|---|---|---|---|---|---|
| Feb 2025 | `onet_task_mappings.csv` | `task_name`, `pct` | Not directly included | `pct` | TBD | TBD |
| Mar 2025 | `task_pct_v2.csv` | `task_name`, `pct` | Not directly included | `pct` | TBD | TBD |
| Sep 2025 | `aei_enriched_claude_ai_2025-08-04_to_2025-08-11.csv` | `facet = onet_task` | `facet = soc_occupation` | `onet_task_pct`, `soc_pct` in `value` | Aug. 4–11, 2025 | TBD |
| Jan 2026 | `aei_raw_claude_ai_2025-11-13_to_2025-11-20.csv` | `facet = onet_task` | No direct `soc_occupation` facet found | `onet_task_pct` in `value` | Nov. 13–20, 2025 | TBD |
| Mar 2026 | `aei_raw_claude_ai_2026-02-05_to_2026-02-12.csv` | `facet = onet_task` | No direct `soc_occupation` facet found | `onet_task_pct` in `value` | Feb. 5–12, 2026 | TBD |
| Jun 2026 | `aei_claude_ai_2026-06-26.csv` | `category_name = onet` | `category_name = soc_occupation` | `metric_id = pct`, stored in `value` | May 1–June 1, 2026 | TBD |

## Findings from Initial Inspection

### Task-Level Data

All six selected releases contain task-level information, but their file structures differ.

- February and March 2025 use `task_name` and `pct`.
- September 2025, January 2026, and March 2026 use `facet = onet_task` and `variable = onet_task_pct`.
- June 2026 uses `category_name = onet`, `metric_id = pct`, `node_name`, and `node_external_id`.

### February and March 2025 File Comparison

Compared February's `onet_task_mappings.csv` with March's `task_pct_v1.csv`.

Results:
- Both contain 3,514 rows.
- Both contain identical data (`a.equals(b) = True`).
- Both have percentages totaling approximately 100%.

Next, compared March's `task_pct_v1.csv` and `task_pct_v2.csv`.

Results:
- V1 contains 3,514 rows.
- V2 contains 3,365 rows.
- Both use `task_name` and `pct`.
- The files are not identical.
- Both have percentages totaling approximately 100%.

The March 2025 README identifies `task_pct_v2.csv` as the current version and defines `pct` as the percentage of task prevalence in the dataset.

**Decision:** Use `task_pct_v2.csv` as the provisional main March 2025 file.

However, we still need to verify whether February and March V2 use the same measurement methodology before interpreting differences as changes over time.

### Task Overlap

Created `src/check_task_overlap.py` to compare unique O*NET task
names across AEI releases.

Updated the script to use `task_pct_v2.csv` for March 2025,
as identified in the March release documentation.

The number of unique tasks found in each release was:

| Release | Unique Tasks |
|---|---:|
| Feb 2025 | 3,514 |
| Mar 2025 V2 | 3,365 |
| Sep 2025 | 2,618 |
| Jan 2026 | 3,170 |
| Mar 2026 | 3,260 |

The number of shared task names between releases was:

| Release Pair | Shared Tasks |
|---|---:|
| Feb 2025 vs Mar 2025 V2 | 2,781 |
| Feb 2025 vs Sep 2025 | 2,203 |
| Feb 2025 vs Jan 2026 | 2,522 |
| Feb 2025 vs Mar 2026 | 2,565 |
| Mar 2025 V2 vs Sep 2025 | 2,166 |
| Mar 2025 V2 vs Jan 2026 | 2,465 |
| Mar 2025 V2 vs Mar 2026 | 2,487 |
| Sep 2025 vs Jan 2026 | 2,357 |
| Sep 2025 vs Mar 2026 | 2,366 |
| Jan 2026 vs Mar 2026 | 2,888 |

### Task Overlap Findings

- February and March 2025 V2 share 2,781 task names.
- March V2 contains 3,365 unique tasks, compared with
  3,514 in February.
- Later releases also share many task names.
- This suggests that task-level comparisons may be possible
  using tasks that appear across releases.
- June 2026 has not yet been included in the overlap analysis.

However, shared task names do not automatically mean that
their usage percentages are directly comparable.

The percentage definitions, denominators, and methodology
still need to be verified.

### Occupation-Level Data

- February and March 2025: No direct occupation records in the selected task files.
- September 2025: Contains `soc_occupation` and `soc_pct`.
- January and March 2026: No direct `soc_occupation` records found during initial inspection.
- June 2026: Contains `soc_occupation`, occupation names, and SOC identifiers.

Occupation-level comparison may therefore be more limited than task-level comparison.

### Percentage Definitions

The March 2025 README defines `pct` as the percentage of task prevalence in the dataset.

For the later releases, the task usage percentages are stored differently:

- September 2025: `onet_task_pct`
- January 2026: `onet_task_pct`
- March 2026: `onet_task_pct`
- June 2026: `metric_id = pct`

Although these variables appear to measure task usage, we still need to verify their definitions, denominators, geographic scope, and methodology before comparing them directly.

## Key Findings So Far

1. All six selected releases contain task-level information, but their structures differ.
2. February 2025 and March 2025 V1 contain identical task measurements.
3. March 2025 V2 contains different task measurements and is identified as the current version in the March README.
4. Many task names overlap across releases.
5. Occupation-level information is not directly available in every selected file.
6. The percentage measures still need to be checked before analyzing changes over time.

## Harmonization Questions

- What does each task percentage represent?
- Are percentages calculated using the same denominator?
- Did the measurement methodology change between releases?
- Are task names and identifiers consistent?
- Did the platform population or geographic scope change?
- Can occupation-level information be derived consistently across releases?
- Which releases can be compared directly?

## Harmonization Decisions

**Decision 1: March 2025 file selection**

Use `task_pct_v2.csv` provisionally because the March README identifies it as the current version.

**Decision 2: Task comparison**

Use shared O*NET tasks as potential matches across releases, but verify that their definitions and percentages are comparable.

**Decision 3: Comparability**

Keep all releases marked `TBD` until the measurement definitions and methodologies have been verified.

## Next Steps

1. Update `check_task_overlap.py` to use March 2025 V2 instead of V1.
2. Recalculate task overlap using the updated March file.
3. Check the documentation for the percentage variables across the remaining releases.
4. Determine which releases can be compared fairly.
5. Create a harmonized dataset for the final analysis.

### June 2026 Task Overlap

Extended `src/check_task_overlap.py` to include the June 2026
release.

The June dataset uses `node_name` for task descriptions and
`node_external_id` for O*NET identifiers.

Initially, the script found zero shared tasks between June
and the earlier releases.

After standardizing task names to lowercase and removing
extra spaces, the following overlap was found:

| Release Pair | Shared Tasks |
|---|---:|
| Feb 2025 vs Jun 2026 | 1,336 |
| Mar 2025 V2 vs Jun 2026 | 1,253 |
| Sep 2025 vs Jun 2026 | 1,119 |
| Jan 2026 vs Jun 2026 | 1,249 |
| Mar 2026 vs Jun 2026 | 1,292 |

### Findings

- June 2026 contains 3,846 unique O*NET entry names.
- Task-name capitalization differed between June and earlier releases.
- Standardizing capitalization revealed substantial overlap.
- June contains some broader O*NET work activities in addition
  to specific task descriptions.
- Further filtering may be necessary to ensure that equivalent
  O*NET categories are compared.

These results show that matching across all six releases
is possible, but do not yet establish that usage percentages
are directly comparable.

### June 2026 O*NET Identifier Inspection

Examined the `node_name` and `node_external_id` columns
for June 2026 O*NET percentage records.

Results:
- 3,846 unique O*NET names.
- 3,878 unique O*NET identifiers.
- Identifiers include numeric values and structured codes.

Finding:
June 2026 appears to contain different types of O*NET
entries, including task descriptions and broader work
activities.

The number of unique identifiers is greater than the
number of unique names, suggesting that some names may
be associated with multiple identifiers.

Next step:
Examine the identifier formats and determine whether
June needs to be filtered to specific O*NET task records
before comparing it with earlier releases.

### June 2026 Identifier Types

Examined the O*NET identifiers in the June 2026 release.

Results:
- Numeric identifiers: 2,861
- Structured identifiers beginning with `4.`: 1,017
- Other identifiers: 0

The June dataset contains multiple types of O*NET
identifiers.

Numeric identifiers appear to represent specific task
statements, while structured identifiers appear to
represent broader or detailed work activities.

This suggests that June's O*NET category may include
more than one type of occupational information.

Before comparing June with earlier releases, the
appropriate O*NET categories need to be identified.

### June 2026 Numeric-ID Task Comparison

Compared March 2025 V2 with June 2026 using only
June records with numeric O*NET identifiers.

Results:
- March 2025 V2: 3,365 unique tasks.
- June 2026 numeric-ID records: 2,858 unique task names.
- Shared task names: 1,253.

The previous comparison using all June O*NET records
also found 1,253 shared task names.

Finding:
Restricting June to numeric identifiers did not change
the number of shared task names with March 2025.

This suggests that the matched tasks are represented
among June's numeric-ID records.

Next:
Verify the meaning of June's identifier types before
deciding which records belong in the final analysis.

### September 2025 Percentage Definition

Reviewed the September 2025 `data_documentation.md`.

The documentation defines:

- `onet_task_count`: Number of conversations using a specific O*NET task.
- `onet_task_pct`: Percentage of geographic total using this task.
- `soc_pct`: Percentage of classified O*NET tasks associated
  with an SOC major occupation group.

Each row represents one metric for a specific geography
and analysis category.

Finding:
September 2025 provides a clear definition of task
usage percentages.

However, March 2025 defines `pct` as the percentage
of task prevalence in the dataset.

The two measures may be related, but their denominators
have not been confirmed to be equivalent.

Decision:
Keep comparability between March and September as TBD.

Next:
Check whether January 2026 uses the same percentage
definition as September 2025.

### January 2026 Percentage Definition

Reviewed the January 2026 `data_documentation.md`.

The documentation defines:

- `onet_task_count`: Number of conversations using a specific O*NET task.
- `onet_task_pct`: Percentage of geographic total using this task.
- `onet_task_pct_index`: Task specialization index relative to a geographic baseline.

Finding:
January 2026 uses the same documented definition of
`onet_task_pct` as September 2025.

Both releases measure task usage as a percentage of
the geographic total.

January 2026 includes global, country, and country-state
geographic levels.

Decision:
The task percentage definitions match between September
2025 and January 2026.

However, full comparability still requires checking
methodology, geographic filtering, and task classifications.

Next:
Review March 2026 documentation to verify whether its
`onet_task_pct` definition is consistent.