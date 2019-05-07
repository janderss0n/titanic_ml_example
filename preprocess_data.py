import numpy as np
import pandas as pd


def filter_columns(df, columns_to_keep):
    return df.loc[:, columns_to_keep]


def replace_null_with_1_else_0(df, column_name):
    df.loc[df[column_name].notnull(), column_name] = 1
    df.loc[df[column_name].isnull(), column_name] = 0
    return df


def replace_nan_age_with_median(df, age_column_name, median_age):
    df.loc[df[age_column_name].isnull(), age_column_name] = median_age
    return df


def create_dummies_columns(df, column_name, prefix=None, columns_to_create=None):
    col_from_dummies = pd.get_dummies(df[column_name], prefix=prefix)

    if columns_to_create:
        col_keep = set(columns_to_create).intersection(set(col_from_dummies.columns))
        col_missing = set(columns_to_create) - col_keep
        df_missing_col = pd.DataFrame(0, index=np.arange(df.shape[0]), columns=list(col_missing)+list(col_keep))

    return pd.concat([df, df_missing_col], axis=1)


def preprocess_data(df, interesting_columns, median_age):
    new_df = filter_columns(df, interesting_columns)
    new_df = replace_null_with_1_else_0(new_df, 'Cabin')
    new_df = replace_nan_age_with_median(new_df, 'Age', median_age)
    new_df = create_dummies_columns(new_df, 'Embarked', prefix='Embarked',
         columns_to_create=['Embarked_C', 'Embarked_Q', 'Embarked_S'])
    return create_dummies_columns(new_df, 'Sex', columns_to_create=['female', 'male'])


if __name__=='__main__':
    data = pd.read_csv('titanic_data/train.csv')
    interesting_columns = ['Pclass', 'Sex', 'Age', 'Cabin', 'Embarked']
    median_age = 28
    data_for_model = preprocces_data(data, interesting_columns, median_age)
    print(data_for_model.head())
