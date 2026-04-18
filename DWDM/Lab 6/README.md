# Lab 6: Illustrate Multilayer Perceptron in Weka

## New Topic: Barcelona Match Outcome Prediction using MLP
This dataset is designed specifically for Weka and MLP. It predicts whether Barcelona will win a match based on match conditions and team form.

### Dataset description
- `opponent_strength`: {low, medium, high}
- `venue`: {home, away}
- `recent_form`: {poor, average, good}
- `star_player_available`: {yes, no}
- `shots_on_target`: numeric count of shots on goal
- `possession`: numeric percentage of ball possession
- `result`: {win, lose} (class label)

## How to use Weka for this dataset
1. Open Weka.
2. In the Weka GUI Chooser, click `Explorer`.
3. In the `Preprocess` tab, click `Open file...`.
4. Load `Lab 6/barca_mlp_matchdata.arff`.

## Set class attribute
1. After loading, check the attribute list on the left.
2. If the class is not already selected, click `Classify` tab.
3. Click the `Classify` panel's `More options...` and confirm `test options` if needed.
4. Make sure the `Class` field is set to `result`.

## Select Multilayer Perceptron
1. Click the `Classify` tab.
2. Click the `Choose` button.
3. Select `functions` > `MultilayerPerceptron`.
4. Click the text box to the right of `Choose` to open the `GenericObjectEditor`.
5. Set `GUI` to `True`.

## Important MLP parameters
- `learningRate`: controls weight updates. Use `0.3`.
- `momentum`: use `0.2`.
- `trainingTime`: set `500`.
- `hiddenLayers`: set to `a` (automatic) or `5` for a single hidden layer.
- `validationSetSize`: leave `0` for cross-validation.

## Evaluation settings
1. In `Test options`, choose `Cross-validation`.
2. Set `Folds` to `4`.

## Run the model
1. Click `Start`.
2. Review the output text area for:
   - Accuracy
   - Confusion matrix
   - Kappa statistic
   - Error rates

## Visualize the network
1. Click the MLP text box again.
2. Ensure `GUI` is `True`.
3. Click `Start` again.
4. A network window should open showing hidden layers and connections.

## Notes
- Use the ARFF file to avoid import issues.
- If you use the CSV file, choose `Yes` when Weka asks about headers.
- This dataset is created solely for MLP demonstration in Weka, not for churn prediction.
