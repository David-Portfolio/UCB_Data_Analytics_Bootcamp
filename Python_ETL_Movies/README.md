# Movies-ETL

  The scope of this project is to provide the hackathon with movie data for analysis. The goal is to predict which upcoming low budget movies being released will become popular. This will enable cost savings from buying the movie streaming rights before their popularity increases the streaming costs. A critical step to developing the predictive algorithm is the ETL process. Using a Python script for the data sources available to us (Wikipedia data, Kaggle metadata, MovieLens rating data), we have extracted, transformed, and loaded the datasets into a SQL database (movies and ratings tables) for the hackathon participants to access. Insights and trends derived are dependent on the quality of the data sources and constrained by the limitations. We assume that these data sources/sets provide the best indicators to make predictions through data analysis. That being said, the following should be noted:
  
  * Since Wikipedia is an open collaboration online encyclopedia, we will assume the community has validated the information for accuracy.
  * The Wikipedia data is for the year range 1990 to 2018.
  * Other variables such as employment rates and inflation that would have impacted budget, revenue, etc are not available. Through data analysis, this can be factored     however it would require additional datasets so we will assume that we are comparing "apples-to-apples" and the conditions are normalized.
  * The data sources have been transformed as part of the ETL process. This was done while reviewing the data in aggregate (it would be more too consuming
    inspect every single line item). Validations/data cleaning best practices were performed where necessary for accuracy, consistency and automation of the data for       the hackathon. Some examples include:
      * Comparing Wikipedia and Kaggle data to determine which to keep/drop.
      * Duplicates such as imdb id's were dropped.
      * Wikipedia data columns with >=90% null values dropped.
      * Missing data filled in for completeness (i.e. budget, revenue, rating with '0').
      * Column names changed and merged for consolidation.
      * Formatting/form of data types.
