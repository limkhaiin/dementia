# Multimodal Classification of Dementia: Audio, Text and Timestamps
Dementia is a progressive neurological disorder that profoundly affects the daily lives of older adults, impairing abilities from verbal communication to cognitive function. Early diagnosis is essential for enhancing both lifespan and quality of life for affected individuals. Despite its importance, diagnosing dementia is complex and often necessitates a multi-modal approach incorporating diverse clinical data types. In this study, we apply transfer learning techniques to Wav2vec and Word2vec algorithms and train models using three distinct data types: audio recordings, text transcripts, and timestamps. We experiment with four conditions: original datasets versus datasets purged of short sentences, each with and without data augmentation. Our results indicate that data augmentation generally enhances model performance, underscoring the importance of data volume for achieving high accuracy. Additionally, models trained on text data frequently excel and can further improve the performance of other modalities when combined. In conclusion, the selection and integration of data modalities are crucial factors influencing the effectiveness of dementia diagnostic models.



## Pre-trained models
Wav2vec (Baevski et al., 2020) is a self-supervised convolutional architecture that transforms audio waveforms into representative embeddings. Initially trained on unlabeled audio data, these embeddings are then processed through a transformer for a masked task. In this task, half of the audio embeddings are masked and predicted by the remaining unmasked portions. Wav2vec is particularly useful in speech recognition tasks due to its adaptability to various audio recordings and its  inherently robust performance.

Word2vec (Mikolov et al., 2013) is a feed-forward neural network designed to produce vector representations of words. It uses surrounding words as input to generate these vectors, capturing semantic relationships between the words. The resulting vectors effectively position semantically similar words closer in the vector space.

## Model architecture
Audio data are passed through the pre-trained Wav2vec model for feature extraction and the resulting embeddings is passed to a dense layer (sigmoid activation) for binary classification. 
Text data, after its word embeddings are extracted based on words, and timestamps are processed through an LSTM model and a dense layer  (sigmoid activation).

## Data Augmentation
We applied a data augmentation techinique of synonym replacement, when a synonym in a sentence was found, the duplicate sentence was created with the word replaced by the synonynm. Each word was replaced by its synonym only once (n=1). 

## Datasets
The training and validation data utilized in this project were sourced from the English/Pitt dataset within the Dementia Databank (https://dementia.talkbank.org). This dataset contains timestamps of words and are useful in our project. 
3,873 are dementia-related and 5,574 are control points.

## 4 conditions
We created four conditions to compare the performance after data augmentation.

Original Condition: The original dataset with 9,447 datapoints, including 3,873 dementia and 5,574 control datapoints.

Shorts-Removed Condition: Excluded sentences shorter than two words, resulting in 4,318 control and 3,368 dementia datapoints.

Original-Augmented Condition: Augmented from the dataset in Original Condition, leading to 31,273 control and 22,664 dementia datapoints.

Shorts-Augmented Condition: Augmented from the dataaset in Short-Removed Condition, yielding 28,964 control and 22,039 dementia datapoints.

For all conditions, the datasets were divided into training and test sets using a 4:1 ratio. Furthermore, the training datasets were also split into training and validation sets with a 4:1 ratio, facilitating 5-fold cross-validation for hyperparameter optimization.

## Results

The text modality constantly showed the best performance, where in augemented condition and with its combined models, the AUROC scores can reach 90%.
The audio modality showed suboptimal performace, achieving only 60% auroc scores even after data augmentation. Removing short sentences didn't affect the performance significantly. 
