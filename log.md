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


## 10/05-10/19

-Reviewed the AEI data documentation for September 2025, January 2026, March 2026, and June 2026.

-Checked how task usage percentages are defined across the different releases.

-Found that September 2025, January 2026, and March 2026 use the same documented percentage definition. June 2026 uses a similar definition.

-Found some differences between releases, including changes in dataset structure, available Claude products, and task categories.

-Learned that June 2026 includes both April and May data, so these months need to be analyzed separately.

-Filtered June's dataset to look only at global O*NET tasks.

-Found 2,410 task IDs in April and 2,713 in May.

-Compared task IDs between the two months and found that 2,300 appeared in both.

-Decided to use matching task IDs to compare April and May task percentages.

## Next steps

-Check for duplicate task IDs and missing percentage values.

-Compare task usage percentages between April and May.

-Continue checking which tasks and occupations can be compared across releases.

-Prepare a cleaned dataset for the analysis.




