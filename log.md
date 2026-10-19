# Week 09/14-09/21
-Refined Question to "How does AI usage vary across occupations, and which occupations show the highest penetration in the Anthropic Economic Index?"

-Loaded and explored the AEI dataset; confirmed the available variables and identified that soc_pct is the correct metric for occupation-level AI usage.

-Generated three core visualizations and interpreted each graphs:

Top 20 Occupations by AI Penetration

Distribution of AI Penetration Across Occupations

Average AI Penetration by Occupation Group

-Added bottom 20 occupations to show exactly which job categories have minimal AI exposure.

## Next Step: Download a different release and check if results are consistent. 

# Week 09/21 - 09/28

- Had difficulty finding another comparable enriched dataset to compare against the September release. 

-Decided to reconsider my research question in a way that it fits longitudinal analysis across different releases.

-New proposed question: How did patterns of Claude.ai usage across occupations and tasks change across AEI releases from February 2025 to June 2026?

# 09/28 - 10/5

- Continued looking at the different AEI releases for my updated research question.
- Compared how task and occupation information is stored across the releases.
- Created a harmonization table to keep track of the differences between releases.
- Checked how many task names overlap between releases and found that many of the same tasks appear across multiple releases.
- Found that task-level data is available more consistently than occupation-level data.
## Next step: check what the percentage variables mean in each release to see if they can actually be compared.


### 10/05–10/19

- Compared February and March 2025 task datasets. Found that February and March V1 contain identical data, while March V2 differs.
- Selected March 2025 V2 as the provisional dataset based on the release documentation.
- Created and updated `check_task_overlap.py` to compare shared O*NET task names across AEI releases.
- Calculated task overlap across releases and standardized task names to identify matches with June 2026.
- Reviewed AEI documentation for September 2025, January 2026, March 2026, and June 2026 to understand task usage percentage definitions.
- Found that September 2025, January 2026, and March 2026 use the same documented percentage definition, while June 2026 uses a similar definition.
- Identified differences in dataset structures, Claude product coverage, and O*NET task classifications that may affect comparisons.
- Investigated June 2026's O*NET hierarchy and determined that `hierarchy_level = 0` represents individual tasks.
- Found that the June 2026 release contains separate April and May observations.
- Filtered June data to global O*NET task-level records and found 2,410 task IDs in April and 2,713 in May.
- Compared April and May task IDs and found that 2,300 appeared in both months.
- Checked occupation-level data availability and found that occupation records are not consistently available across all releases.
- Identified shared task IDs as a starting point for comparing task usage percentages.

### Next Steps

- Check for duplicate task IDs and missing percentage values.
- Compare actual task usage percentages between April and May 2026.
- Continue verifying comparability across releases, including differences in measurement methods and task classifications.
- Investigate occupation-level comparisons where data is available.
- Prepare a cleaned, harmonized dataset for the final analysis.
