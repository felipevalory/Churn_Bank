import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder


def clean_data(df):
    df1 = df.copy()
    df1 = df1.dropna()
    if 'CustomerId' in list(df1.columns):
        df1 = df1.drop_duplicates(subset=['CustomerId'], keep='first')
    # Encode 'Gender' column using LabelEncoder (Female: 0, Male: 1)
    label_encoder = LabelEncoder()
    df1['Gender'] = label_encoder.fit_transform(df1['Gender'])

    # Transforming 'Geography' column into (France=1, Germany=2, Spain=3)
    df1['Geography'] = df1['Geography'].replace({'France': 1, 'Germany': 2,
                                                 'Spain': 3})
    return df1


# Graphic style config
sns.set(style="whitegrid")


# Age distribution graphic
def age_distribution(df1):
    plt.figure(figsize=(10, 6))
    sns.histplot(df1['Age'], bins=30, kde=True, color='blue')
    plt.title('Age Distribution', fontsize=16)
    plt.xlabel('Age', fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    plt.show()
    return


# Chunr per Country graphic
def churn_per_country(df1):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Geography', hue='Exited', data=df1, palette='Set2')
    plt.title('Churn per Country', fontsize=16)
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.legend(title='Churn', labels=['No', 'Yes'])
    plt.show()

    return


# Churn per gender graphic
def churn_per_gender(df1):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Gender', hue='Exited', data=df1, palette='Set2')
    plt.title('Churn per Gender', fontsize=16)
    plt.xlabel('Gender', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.legend(title='Churn', labels=['No', 'Yes'])
    plt.show()

    return


# Churn per tenure graphic
def churn_per_tenure(df1):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='Tenure', hue='Exited', data=df1, palette='Set2',
                  stat='percent')
    plt.title('Churn per Tenure', fontsize=16)
    plt.xlabel('Tenure', fontsize=12)
    plt.ylabel('Percent', fontsize=12)
    plt.legend(title='Churn', labels=['No', 'Yes'])
    plt.show()

    return


# Churn per tenure graphic
def churn_per_creditscore(df1):
    plt.figure(figsize=(10, 6))
    sns.histplot(x='CreditScore', hue='Exited', data=df1, palette='Set2',
                 kde=True, stat='percent', multiple='stack')
    plt.title('Churn per Credit Score', fontsize=16)
    plt.xlabel('Credit Score', fontsize=12)
    plt.ylabel('Percent', fontsize=12)
    plt.legend(title='Churn', labels=['No', 'Yes'])
    plt.show()

    return


# Churn per Balance
def churn_per_balance(df1):
    plt.figure(figsize=(10, 6))
    sns.histplot(x='Balance', hue='Exited', data=df1, palette='Set2',
                 kde=True, stat='percent', multiple='stack')
    plt.title('Churn per Balance', fontsize=16)
    plt.xlabel('Balance', fontsize=12)
    plt.ylabel('Percent', fontsize=12)
    plt.legend(title='Churn', labels=['No', 'Yes'])
    plt.show()

    return


# Churn per NumOfProducts
def churn_per_products(df1):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='NumOfProducts', hue='Exited', data=df1, palette='Set2',
                  stat='percent')
    plt.title('Churn per Number of Products', fontsize=16)
    plt.xlabel('NumOfProducts', fontsize=12)
    plt.ylabel('Percent', fontsize=12)
    plt.legend(title='Churn', labels=['No', 'Yes'])
    plt.show()

    return


# Churn per HasCrCard
def churn_per_hasCrCard(df1):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='HasCrCard', hue='Exited', data=df1, palette='Set2',
                  stat='percent')
    plt.title('Churn per Has Credit Card', fontsize=16)
    plt.xlabel('Has Cradit Card', fontsize=12)
    plt.ylabel('Percent', fontsize=12)
    plt.legend(title='Churn', labels=['No', 'Yes'])
    plt.show()

    return


# Churn per IsActiveMember
def churn_per_activeMember(df1):
    plt.figure(figsize=(10, 6))
    sns.countplot(x='IsActiveMember', hue='Exited', data=df1, palette='Set2',
                  stat='percent')
    plt.title('Churn per Is Active Member', fontsize=16)
    plt.xlabel('Is Active Member', fontsize=12)
    plt.ylabel('Percent', fontsize=12)
    plt.legend(title='Churn', labels=['No', 'Yes'])
    plt.show()

    return


# Churn per EstimatedSalary
def churn_per_estimatedSalary(df1):
    plt.figure(figsize=(10, 6))
    sns.histplot(x='EstimatedSalary', hue='Exited', data=df1, palette='Set2',
                 kde=True, stat='percent', multiple='stack')
    plt.title('Churn per EstimatedSalary', fontsize=16)
    plt.xlabel('Estimated Salary', fontsize=12)
    plt.ylabel('Percent', fontsize=12)
    plt.legend(title='Churn', labels=['No', 'Yes'])
    plt.show()

    return


def correlation(df1):
    # Removing unnecessary columns
    df_corr = df1.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

    # Calculate a correlation matrix
    corr_matrix = df_corr.corr()

    # Ploting a correlation heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Matrix', fontsize=16)
    plt.show()

    return
