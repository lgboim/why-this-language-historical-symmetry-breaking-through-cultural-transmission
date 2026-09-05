# Why This Language? Version 2 Revision Notes

**Ariel Elboim**  
Independent Researcher, Israel  
Corresponding author: lgboim@gmail.com  
Version 2.0, September 5, 2026  
Previous version: [Version 1.0, September 4, 2026](https://doi.org/10.5281/zenodo.22305643)

## Purpose and scope

These notes accompany Version 2 of *Why This Language? Historical Symmetry Breaking through Cultural Transmission* and its Supplementary Material. Code and data checks identified an error in the adjusted Rand index, a mismatch between a registered subgroup and its analysis, an incorrectly implemented model condition, and reporting inconsistencies. This revision corrects those issues and narrows the affected interpretations. The original version remains available in the archive linked above.

The neural corrections use saved experimental runs; no neural network was retrained. The reconstruction model's persistence condition was implemented again after its operational definition was documented, and its negative result is reported. Full corrected results, cohorts, uncertainty intervals and decision rules appear in Supplementary Tables S1–S4. Test identifiers below refer to those tables.

## 1. Corrected partition-similarity metric

The earlier adjusted Rand index implementation assigned zero to identical partitions when all objects formed separate classes. Such partitions must score one. A shared corrected implementation now supplies the affected analyses. The correction has substantial effects in the second architecture, where languages are close to injective.

| Second-architecture result | Version 1 | Version 2 |
|---|---|---|
| A1: partition inheritance, rewritten record versus no record | Supported in two of four channel families | Supported in all four: differences +0.165, +0.685, +0.398 and +0.442 |
| A3: sibling coordination, same versus different records | −0.010 [−0.116, +0.071] | +0.290 [+0.058, +0.516], 12/20 positive; still inconclusive under the seed rule |
| A4: coordination, immature versus mature anchors | +0.152 [+0.027, +0.286]; criterion met | −0.198 [−0.477, +0.089]; criterion not met; no directional decrease established either |
| Partition-inheritance analogue, capacity 40 with random selection | +0.091 [+0.010, +0.207] | +0.461 [+0.311, +0.597], 19/20 positive |

The last comparison remains descriptive, without a registered verdict. It measures partition inheritance, not language structure. Other affected lineage contrasts are reported in Table S4. The later form-level A3′ and A4′ analyses remain distinct from these partition-level tests.

In the main learner, the K13a capacity-40 difference changes from +0.640 to +0.643; its verdict is unchanged. The descriptive K13b capacity-40 hard-selection contrast changes from +0.055 to +0.065 and remains inconclusive under its seed rule.

## 2. Registered subgroups and decision rules

K12 registered a comparison conditional on zero versus at least two taught neighbours. Version 1 instead reported the subgroup with three or more as the registered test. The corrected, registered subgroup gives +0.038 [+0.009, +0.068] in confirmation and +0.064 [+0.033, +0.094] in replication. It meets the equivalence criterion once, and fails replication. The three-or-more subgroup remains reported as an additional analysis. No exact three-anchor threshold is inferred.

The K12 rule requires both an absolute mean difference below 0.05 and a confidence interval inside ±0.08. K14 instead uses point-estimate bands. K17a's asymmetric rule is now described as a criterion for no material weakening, rather than proof of equality or symmetric equivalence. K11 supports a positive aggregate slope; monotonicity at every step in every experimental cell was not established. The larger-world experiment M1 supports the predicted direction but falls below its registered magnitude of 0.15.

## 3. Independent units and figure corrections

The seed is the independent unit for uncertainty. K8 fidelity differences are averaged across matched conditions within each seed before resampling: +0.052 [+0.040, +0.064] in confirmation and +0.053 [+0.044, +0.061] in replication, positive in 20/20 seeds in each cohort. This replaces pooling dependent seed-by-condition observations. The separate K8 structure result does not establish equivalence.

Affected figure means and error bars now use per-seed summaries. Figure 2c identifies the one stratum with 29 eligible seeds; the others have 30. Figure 2b's chance reference is calculated on the same untaught-source cases as its comparison bar, changing the reference from 0.186 to 0.180. The corresponding confirmation and replication analyses remain within their stated mean bands.

Figure 4d changes from 77%/25% to 79%/26% over 65 seeds. Two discovery seeds had been compared with a parent's 12,000-step language rather than the 2,000-step language used in the experiment. Correcting this endpoint changes the means; using seeds rather than siblings as independent observations changes the standard errors. The related parent comparisons in Figures 1 and 3 were also regenerated.

Figure 4a now states its own population and statistic: all 64 objects at the final generation, rewrite minus accumulate +0.074, positive in 24/30 seeds. The separate −0.095 statistic concerns training objects averaged across inherited generations and is labelled with that scope.

## 4. Reconstruction model: negative persistence result

The earlier T4 implementation sampled an unrelated shallow partition in every generation of the accumulating-record arm. It therefore did not test the registered frozen early partition. In the corrected experiment, that arm repeatedly samples anchors from the founder's fixed early partition.

At generation 5, similarity to the founder is 0.198 under rewriting and 0.306 under the frozen early record. The paired difference is −0.109 [−0.175, −0.048], with rewriting higher in only 5/20 seeds. This fails to reproduce the neural persistence pattern. The model-support claim is withdrawn, and the negative result is retained in the Supplement. The neural K18 result remains separate. No numerical T4 decision threshold was registered, and the endpoint contrast is reported descriptively.

The T2 argument that joining an anchored class costs less than the edge penalty was also incorrect. It is replaced by a measured move-cost analysis that includes collision, class-count and edge terms. The original T1–T3 simulation values were not independently rerun as part of this correction; this limitation is disclosed.

## 5. Other numerical and interpretive corrections

The second architecture's 40-seed A4′ strength difference is −0.064 [−0.112, −0.016], with levels 0.374 versus 0.439, replacing −0.117 [−0.181, −0.053]. Its failure verdict is unchanged. The K17b summary distinguishes the original 15-seed analysis, whose interval crosses zero, from the pooled and replication analyses. Neither confirmation cohort meets its seed-fraction criterion.

Descriptions of comparable structure and communicative value are narrowed to the measured comparisons. Similar item-level accuracy does not demonstrate functional equivalence of complete alternative languages. The class-matched versus other-form comparison is identified as conditional, and distractor geometry is not treated as controlling the number of viable partitions.

K18 was added to the registration while the replication was running, before inspection according to the registration record. The available repository history cannot independently certify the timing of every threshold. Reproduction instructions distinguish the corrected model from its superseded implementation and disclose that arbitrary fresh-seed replication has not been verified end-to-end.

## Reading this revision

The revised article and Supplementary Material provide the current results and interpretations; this document explains their changes relative to Version 1. The [original code and results archive](https://doi.org/10.5281/zenodo.22305564) identifies the earlier release. These notes do not claim a new literature or originality review. The article's disclosure of generative-AI assistance is retained.
