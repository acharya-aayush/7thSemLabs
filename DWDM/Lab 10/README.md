# Lab 10: Apply Agglomerative Hierarchical Clustering Filter of WEKA

## Objective
Apply the Agglomerative Hierarchical Clustering filter in Weka to a suitable dataset and analyze the resulting clusters.

## Theory
Hierarchical clustering constructs a hierarchy of clusters either by merging small clusters into larger ones or by dividing large clusters into smaller ones. In the agglomerative approach, each instance begins as its own cluster, and similar clusters are merged until the desired number of clusters or stopping criterion is reached. The result is often displayed as a dendrogram that shows the order and distance at which clusters were combined.

Agglomerative clustering can use different distance measures such as Euclidean or Manhattan distance. Linkage criteria determine how cluster distance is computed: single linkage uses the nearest neighbor, complete linkage uses the farthest points, average linkage uses the average distance, and Ward's method minimizes within-cluster variance.

## Dataset: Weekly Office Activity
This dataset describes weekly office activity for a set of employees.

Attributes:
- `Work_Hours`: total hours worked in a week
- `Meetings`: number of meetings attended
- `Emails_Sent`: count of emails sent
- `Coffee_Cups`: number of coffee cups consumed
- `Focus_Score`: subjective focus rating out of 100

This dataset is a normal office activity dataset and does not match the earlier football-related or churn-related topics.

## How to use in Weka
1. Open Weka.
2. Click `Explorer`.
3. In the `Preprocess` tab, click `Open file...`.
4. Load `Lab 10/weekly_activity.arff`.
5. Confirm the data loaded and all numeric attributes appear.

## Apply Agglomerative Hierarchical Clustering
1. Click the `Cluster` tab.
2. Click `Choose` and select `HierarchicalClusterer`.
3. Click the `HierarchicalClusterer` text box to open the parameter editor.
4. Set `numClusters` to `3` (or leave default if you want Weka to choose).
5. Set `linkType` to `SINGLE`, `COMPLETE`, `AVERAGE`, or `WARD`.
6. Set `distanceFunction` to `EuclideanDistance`.
7. Enable `printNewick` if available to see hierarchy output.
8. Click `OK`.
9. Click `Start`.

## Visualize the tree
1. After clustering completes, right-click `HierarchicalClusterer` in the result list.
2. Select `Visualize tree`.
3. View the dendrogram to understand the cluster hierarchy and merge distances.

## Discussion
Agglomerative hierarchical clustering groups similar weekly activity profiles step by step. The dendrogram shows how individual weeks merge into clusters based on work hours, meetings, emails, coffee consumption, and focus score. The chosen linkage method affects the merge order and cluster shape. For example, single linkage may group points based on one pair of close samples, while complete linkage uses the farthest pair.

This procedure is useful when you want to explore the data structure without predefining exact cluster boundaries. Clusters can reveal patterns like high-workload weeks, low-activity weeks, and moderate weeks with balanced focus.

## Conclusion
This lab demonstrates Weka's HierarchicalClusterer for agglomerative clustering. The exercise shows how a dendrogram helps interpret cluster relationships and hierarchy. Agglomerative clustering is especially valuable when the dataset structure matters and when you want to compare different linkage methods and cluster distances.

## Notes
- If you use the CSV file, choose `Yes` when Weka asks whether the first row contains headers.
- Numeric attributes are best for HierarchicalClusterer, so this dataset uses office activity measurements.
