# -*- coding: utf-8 -*-
"""chi-square-final

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KiI6EH-_LsVxpPS7nyH5kX31-m85Saci
"""

!pip install scipy

import numpy as np
from scipy.stats import chisquare

"""**Criterion**"""

# Example observed data where Llama-2 has a strong preference in the "Argument from Similarity" scheme
observed_criterion = np.array([18,8,12])  # Llama-2, Mistral, GPT-Neo

# Ensure expected frequencies sum to the same total as observed frequencies
total_votes = observed_criterion.sum()
expected_criterion = np.array([total_votes/3] * 3)

# Perform Chi-Square goodness-of-fit test
chi2_stat, p_val = chisquare(f_obs=observed_criterion, f_exp=expected_criterion)

# Print the results
print(f"Scheme: citerion")
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"p-value: {p_val}")
print(f"Observed: {observed_criterion}")
print(f"Expected Frequencies: {expected_criterion}\n")


# Determine if there's a significant difference
if p_val < 0.05:
    print("There is a significant difference in model performance for the Criterion scheme.")
    # Correctly analyze which model performed better based on the observed frequencies.
    best_model_index = np.argmax(observed_criterion)  # Change this to observed_criterion
    print(f"The model with the highest preference is at index {best_model_index}.")
else:
    print("No significant difference found in Criterion.")

"""**Similarity**"""

# Example observed data where Llama-2 has a strong preference in the "Argument from Similarity" scheme
observed_criterion = np.array([20,9,9])  # Llama-2, Mistral, GPT-Neo

# Ensure expected frequencies sum to the same total as observed frequencies
total_votes = observed_criterion.sum()
expected_criterion = np.array([total_votes/3] * 3)

# Perform Chi-Square goodness-of-fit test
chi2_stat, p_val = chisquare(f_obs=observed_criterion, f_exp=expected_criterion)

# Print the results
print(f"Scheme: citerion")
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"p-value: {p_val}")
print(f"Observed: {observed_criterion}")
print(f"Expected Frequencies: {expected_criterion}\n")


# Determine if there's a significant difference
if p_val < 0.05:
    print("There is a significant difference in model performance for the similarity scheme.")
    # Correctly analyze which model performed better based on the observed frequencies.
    best_model_index = np.argmax(observed_criterion)  # Change this to observed_criterion
    print(f"The model with the highest preference is at index {best_model_index}.")
else:
    print("No significant difference found in similarity.")

"""**Authority**"""

# Example observed data where Llama-2 has a strong preference in the "Argument from Similarity" scheme
observed_criterion = np.array([16,14,8])  # Llama-2, Mistral, GPT-Neo

# Ensure expected frequencies sum to the same total as observed frequencies
total_votes = observed_criterion.sum()
expected_criterion = np.array([total_votes/3] * 3)

# Perform Chi-Square goodness-of-fit test
chi2_stat, p_val = chisquare(f_obs=observed_criterion, f_exp=expected_criterion)

# Print the results
print(f"Scheme: citerion")
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"p-value: {p_val}")
print(f"Observed: {observed_criterion}")
print(f"Expected Frequencies: {expected_criterion}\n")


# Determine if there's a significant difference
if p_val < 0.05:
    print("There is a significant difference in model performance for the authority scheme.")
    # Correctly analyze which model performed better based on the observed frequencies.
    best_model_index = np.argmax(observed_criterion)  # Change this to observed_criterion
    print(f"The model with the highest preference is at index {best_model_index}.")
else:
    print("No significant difference found in authority.")

"""**Example**"""

# Example observed data where Llama-2 has a strong preference in the "Argument from Similarity" scheme
observed_criterion = np.array([13,14,11])  # Llama-2, Mistral, GPT-Neo

# Ensure expected frequencies sum to the same total as observed frequencies
total_votes = observed_criterion.sum()
expected_criterion = np.array([total_votes/3] * 3)

# Perform Chi-Square goodness-of-fit test
chi2_stat, p_val = chisquare(f_obs=observed_criterion, f_exp=expected_criterion)

# Print the results
print(f"Scheme: citerion")
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"p-value: {p_val}")
print(f"Observed: {observed_criterion}")
print(f"Expected Frequencies: {expected_criterion}\n")


# Determine if there's a significant difference
if p_val < 0.05:
    print("There is a significant difference in model performance for the example scheme.")
    # Correctly analyze which model performed better based on the observed frequencies.
    best_model_index = np.argmax(observed_criterion)  # Change this to observed_criterion
    print(f"The model with the highest preference is at index {best_model_index}.")
else:
    print("No significant difference found in example.")

"""**Goal**"""

# Example observed data where Llama-2 has a strong preference in the "Argument from Similarity" scheme
observed_criterion = np.array([13,16,9])  # Llama-2, Mistral, GPT-Neo

# Ensure expected frequencies sum to the same total as observed frequencies
total_votes = observed_criterion.sum()
expected_criterion = np.array([total_votes/3] * 3)

# Perform Chi-Square goodness-of-fit test
chi2_stat, p_val = chisquare(f_obs=observed_criterion, f_exp=expected_criterion)

# Print the results
print(f"Scheme: citerion")
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"p-value: {p_val}")
print(f"Observed: {observed_criterion}")
print(f"Expected Frequencies: {expected_criterion}\n")


# Determine if there's a significant difference
if p_val < 0.05:
    print("There is a significant difference in model performance for the goal scheme.")
    # Correctly analyze which model performed better based on the observed frequencies.
    best_model_index = np.argmax(observed_criterion)  # Change this to observed_criterion
    print(f"The model with the highest preference is at index {best_model_index}.")
else:
    print("No significant difference found in goal.")

"""**Consequence**"""

# Example observed data where Llama-2 has a strong preference in the "Argument from Similarity" scheme
observed_criterion = np.array([17,12,9])  # Llama-2, Mistral, GPT-Neo

# Ensure expected frequencies sum to the same total as observed frequencies
total_votes = observed_criterion.sum()
expected_criterion = np.array([total_votes/3] * 3)

# Perform Chi-Square goodness-of-fit test
chi2_stat, p_val = chisquare(f_obs=observed_criterion, f_exp=expected_criterion)

# Print the results
print(f"Scheme: citerion")
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"p-value: {p_val}")
print(f"Observed: {observed_criterion}")
print(f"Expected Frequencies: {expected_criterion}\n")


# Determine if there's a significant difference
if p_val < 0.05:
    print("There is a significant difference in model performance for the consequence scheme.")
    # Correctly analyze which model performed better based on the observed frequencies.
    best_model_index = np.argmax(observed_criterion)  # Change this to observed_criterion
    print(f"The model with the highest preference is at index {best_model_index}.")
else:
    print("No significant difference found in consequence.")

"""**Commitment**"""

# Example observed data where Llama-2 has a strong preference in the "Argument from Similarity" scheme
observed_criterion = np.array([20,7,11])  # Llama-2, Mistral, GPT-Neo

# Ensure expected frequencies sum to the same total as observed frequencies
total_votes = observed_criterion.sum()
expected_criterion = np.array([total_votes/3] * 3)

# Perform Chi-Square goodness-of-fit test
chi2_stat, p_val = chisquare(f_obs=observed_criterion, f_exp=expected_criterion)

# Print the results
print(f"Scheme: citerion")
print(f"Chi-Square Statistic: {chi2_stat}")
print(f"p-value: {p_val}")
print(f"Observed: {observed_criterion}")
print(f"Expected Frequencies: {expected_criterion}\n")


# Determine if there's a significant difference
if p_val < 0.05:
    print("There is a significant difference in model performance for the commitment scheme.")
    # Correctly analyze which model performed better based on the observed frequencies.
    best_model_index = np.argmax(observed_criterion)  # Change this to observed_criterion
    print(f"The model with the highest preference is at index {best_model_index}.")
else:
    print("No significant difference found in commitment.")