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

### 10/19 - 10/25
-Compared April and May 2026 Claude.ai task usage using compare_april_may.py.

--Matched 2,300 O*NET task IDs.

--272 tasks increased, 87 decreased, and 1,941 showed no recorded change.

--Largest increase: +0.26 percentage points.

--Largest decrease: −0.08 percentage points.

-Analyzed the magnitude of April–May changes using analyze_task_changes.py.

--Average absolute change: 0.0029 percentage points.

--Only 23 tasks changed by at least 0.05 percentage points.

--Generated figures/april_may_change_distribution.png.

-Checked global task data for the September 2025, January 2026, and March 2026 AEI releases using check_global_releases.py.

--Found 2,618, 3,170, and 3,260 global task records, respectively.

--Confirmed no missing percentage values.

-Compared task usage across August 2025, November 2025, and February 2026 using compare_earlier_releases.py.

--Matched 2,284 tasks across all three collection periods.

--Identified the largest increases in educational support and customer assistance tasks.

--Identified the largest decreases in programming and technical troubleshooting tasks.

--Saved outputs/earlier_release_task_comparison.csv.

-Analyzed the magnitude of earlier-release changes using analyze_earlier_changes.py.

-Excluded the none category, leaving 2,283 classified tasks.

--August 2025 to February 2026 average absolute change: 0.0182 percentage points.

--152 tasks changed by at least 0.05 percentage points.

--Generated figures/aug_to_feb_change_distribution.png.

-Checked task overlap across all five collection periods using check_longitudinal_overlap.py.

--Found 876 tasks shared across August 2025, November 2025, February 2026, April 2026, and May 2026.

--Saved outputs/five_period_shared_tasks.csv.
      ## Findings 
-Most matched tasks showed relatively small changes in reported usage percentages.

-Some educational support and customer assistance tasks increased, while several programming-related tasks decreased between August 2025 and February 2026.

-Results are descriptive and do not establish statistical significance or causation.

-Differences in sampling, classification, product coverage, percentage definitions, and rounding may affect comparisons between releases.

## Proposed Research Hypothesis

Research Question: How did patterns of Claude.ai usage across occupations and tasks change across AEI releases from February 2025 to June 2026?

Null Hypothesis (H₀): There is no systematic change in the distribution of Claude.ai task usage percentages across the AEI collection periods.

Alternative Hypothesis (H₁): There is a systematic change in the distribution of Claude.ai task usage percentages across the AEI collection periods.

## Next Steps

-Create src/build_longitudinal_dataset.py.

-Combine the 876 shared tasks into a five-period dataset.

-Verify metric definitions and task comparability before interpreting longitudinal trends.

-Explore visualizations of task usage changes across the five periods.


11/2 - 11/9
-Built a five-period longitudinal dataset comparing Claude.ai O*NET task usage across August 2025, November 2025, February 2026, April 2026, and May 2026.

-Matched 876 task descriptions across the five periods and excluded three ambiguous descriptions associated with multiple task IDs.

-Created the final dataset containing 873 matched tasks, with no duplicate task names or missing values.

-Developed Python scripts to check data quality and compare percentage distributions across releases.

-Examined task rankings, reported percentages, and zero values to identify potential differences between releases.

# Key Findings
-Earlier releases showed programming and software-related tasks among the highest reported usage percentages.

-April and May 2026 showed information searching, reference searches, and product recommendations among the highest reported tasks.

-April contained 348 reported zero values, while May contained 334. These may partly result from the lower decimal precision in the newer release.

-Some tasks showed substantial percentage differences between February and April 2026.

-These differences are preliminary and cannot yet be interpreted as confirmed changes in user behavior because the releases may use different measurement methods.

## Next Steps
-Review the AEI documentation to compare metric definitions, denominators, task classification methods, and product coverage across releases.

-Determine whether the five periods can be analyzed together or should be separated into comparable groups.

-Create visualizations showing task usage patterns and rankings over time.

-Investigate occupation-level data to address the occupation component of the research question.

-Incorporate the February 2025 release if its data can be harmonized with the later releases.

-Select and conduct appropriate statistical tests after confirming measurement comparability.

-ocument limitations and begin drafting the results and methodology sections.
>>>>>>> 64caae2 (Build five-period longitudinal dataset and validate task data)
