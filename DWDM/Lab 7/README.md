# Lab 7: Frequent Pattern Mining Using Apriori and FPGrowth

## Objective
To mine frequent itemsets in Weka using Apriori and FPGrowth with minimum support 0.3.
To extract strong association rules from Barcelona match-day fan purchases at minimum confidence 0.85.

## Theory
Association rule mining discovers useful relationships in transaction-style data. A rule has the form X → Y, where X and Y are itemsets. Support measures how often the combined itemset appears in the dataset, while confidence measures how often the rule is correct when X occurs. Lift compares the observed co-occurrence of X and Y to what would be expected if they were independent.

Apriori finds frequent itemsets by generating and pruning candidates in a level-wise manner. It uses the anti-monotonicity property: if an itemset is not frequent, none of its supersets can be frequent. FPGrowth is a faster alternative that compresses the data into an FP-tree and mines frequent patterns directly without generating candidate sets.

## New Topic: Barcelona Match-Day Fan Purchases
This dataset models purchases made by Barcelona fans around a match. It is specially created for frequent pattern mining in Weka, not for a standard grocery basket example.

### Dataset description
- `Beer`: whether the fan bought beer
- `Popcorn`: whether the fan bought popcorn
- `Soda`: whether the fan bought a soda
- `SnackBox`: whether the fan bought a snack box
- `Jersey`: whether the fan bought a Barcelona jersey
- `Scarf`: whether the fan bought a Barcelona scarf
- `Flag`: whether the fan bought a flag
- `Camera`: whether the fan used a camera

All values are boolean (`t` or `f`). No class label is required because the goal is to mine item associations.

## What to do now
1. Open Weka.
2. Click `Explorer`.
3. In `Preprocess`, click `Open file...`.
4. Load `Lab 7/barca_matchday_association.arff`.
5. Confirm the dataset loaded and the attributes appear on the left.

### Apriori in Weka
1. Click the `Associate` tab.
2. Click `Choose` and select `Apriori`.
3. Click the text box next to `Choose` to open the `GenericObjectEditor`.
4. Change `lowerBoundMinSupport` to `0.3`.
5. Change `minMetric` to `0.85`.
6. Leave the rest of the settings as default.
7. Click `OK`.
8. Click `Start`.
9. Read the output to find frequent itemsets and strong association rules.

### FPGrowth in Weka
1. Click `Choose` again and select `FPGrowth`.
2. Click the `FPGrowth` text box to open the editor.
3. Set `lowerBoundMinSupport` to `0.3`.
4. Set `minMetric` to `0.85`.
5. Click `OK`.
6. Click `Start`.
7. Compare the frequent itemsets and rules with Apriori.

## Discussion
Using the Barcelona match-day dataset, both Apriori and FPGrowth should find frequent fan purchase patterns that meet support 0.3 and confidence 0.85. The results can reveal common combinations such as fans who buy a jersey also often buy a scarf, or fans who buy beer are likely to purchase popcorn. FPGrowth should be faster because it uses the FP-tree structure and avoids generating many candidates, while Apriori uses candidate generation and iterative pruning.

## Conclusion
This lab demonstrates that Weka can mine strong association rules from a custom dataset using Apriori and FPGrowth. With the same thresholds, both algorithms should discover similar patterns, but FPGrowth is usually more efficient. The exercise reinforces the importance of support and confidence values in selecting meaningful rules, while showing how association mining works on fan purchase behavior rather than a classic grocery example.

## Notes
- `support 0.3` means an itemset must appear in at least 30% of transactions.
- `confidence 0.85` means a rule should be correct at least 85% of the time when its antecedent is present.
- If you open the CSV file instead, choose `Yes` when Weka asks if the first row contains headers.
