# Credit Risk

Of the 94,683 loans from the LendingClub data, 94,116 (99.4%) are low risk and 567 (0.6%) are high risk. As such, we have built a machine learning models to assess the credit risk. The following values were assigned to the loan status' provided in the dataset.
  * Low Risk (Current) = "0"
  * High Risk (Charged Off, In Grace Period, Late (16-30 days), Late (31-120 days) = "1"
Through the credit risk resample techniques, the following results were observed from the imbalanced classification report and balanced accuracy scores.
  * Random Oversample
    * Precision: From the samples classified as low risk, 100% were actually low risk. From the samples classified as high risk, 10% were actually high risk.
    * Recall: From all the actual low risk samples, 73% were classified as low risk. From all the actual high risk samples, 65% were classified as high risk.
    * Balanced Accuracy Score: For the imbalanced dataset, the average recall obtained on each class was 68.8%
  * SMOTE Oversample
    * Precision: From the samples classified as low risk, 100% were actually low risk. From the samples classified as high risk, 10% were actually high risk.
    * Recall: From all the actual low risk samples, 73% were classified as low risk. From all the actual high risk samples, 66% were classified as high risk.
    * Balanced Accuracy Score: For the imbalanced dataset, the average recall obtained on each class was 69.7%.
  * Undersample
    * Precision: From the samples classified as low risk, 99% were actually low risk. From the samples classified as high risk, 10% were actually high risk.
    * Recall: From all the actual low risk samples, 51% were classified as low risk. From all the actual high risk samples, 50% were classified as high risk.
    * Balanced Accuracy Score: For the imbalanced dataset, the average recall obtained on each class was 50.5%.
  * Combination sample
    * Precision: From the samples classified as low risk, 99% were actually low risk. From the samples classified as high risk, 10% were actually high risk.
    * Recall: From all the actual low risk samples, 66% were classified as low risk. From all the actual high risk samples, 73% were classified as high risk.
    * Balanced Accuracy Score: For the imbalanced dataset, the average recall obtained on each class was 69.8%.

In summary, we can conclude that the loans classified as low risk are actually low risk with a high degree of precision while the balanced accuracy score reflects lower average recall for low/high risk loans ranging from ~50%-70%. The average low risk loan is ~$17,000, and high risk loan is ~%16,000. To expand the sample size of the loans, we can incorporate data from other lending services companies. The hypothesis is that with higher loan amounts than what we are seeing in this dataset, there will be increased high risk loans, which will provide additional data points for the model to further assess credit risk.
