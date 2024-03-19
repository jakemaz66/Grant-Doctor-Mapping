import fasttext
import numpy as np
import pandas as pd
import jarowinkler
from sentence_transformers import SentenceTransformer

class NameDistance():

    def __init__(self, ft_model_path: str = 'data/cc.en.50.bin'):
        #Loading fasttext model
        self.ft_model = fasttext.load_model('data/cc.en.50.bin')

    def combine_prediction_data(self, grants, npi) -> pd.DataFrame:
        grants = grants.iloc[0:100].add_prefix('grant_')
        npi = npi.iloc[0:100].add_prefix('npi_')

        grants['merge_val'] = 1
        npi['merge_val'] = 1

        return grants.merge(npi, how='outer', on='merge_val')

    def training_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        This function takes in the comined npi and grants dataframe and adds features for entity resolution like jarowinkler distances

        Args:
        df -> the combined npi and grants data frames

        Returns:
        A dataframe with distance features
        """
        #Grants data has
        #last_name, forename, city, state, country
        #NPI Data has
        #last_name, firstname, city, state, country
        #Prefix of grant_ or npi_

        data_cols = df.columns

        #Getting Features
        df['jw_dist_last_name'] = df.apply(lambda row: jarowinkler.jaro_similarity(row['grant_last_name'], row['npi_last_name']), axis=1)

        df['jw_dist_forename'] = df.apply(lambda row: jarowinkler.jaro_similarity(row['grant_forename'], row['npi_forename']), axis=1)

        df['match_city'] = df.apply(lambda row: row['grant_city'] == row['npi_city'], axis=1)
        df['match_state'] = df.apply(lambda row: row['grant_state'] == row['npi_state'], axis=1)

        df['npi_last_name'].fillna('', inplace=True)
        df['npi_forename'].fillna('', inplace=True)
        df['grant_last_name'].fillna('', inplace=True)
        df['grant_forename'].fillna('', inplace=True)


        #Getting fast text sentence vectors
        for dataset in ['grant', 'npi']:
            for col in ['last_name', 'forename']:
                df[f'vec_{dataset}_{col}'] = df[f'{dataset}_{col}'].apply(
                    lambda x: self.ft_model.get_sentence_vector(x))

        #Calculating fasttext semantic differences
        df['ft_dist_last_name'] = df.apply(
            lambda row: np.linalg.norm(row['vec_grant_last_name'] - 
                                       row['vec_npi_last_name']), axis=1)
        
         
        #model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        #for dataset in ['grant', 'npi']:
        #    for col in ['last_name', 'forename']:
        #        txts = df[col].to_list()
        #        df[f'{col}_vec']= model.embed(txts)
        
        #Calculating huggingFace semantic differences
        #df['hf_dist_last_name'] = df.apply(
        #    lambda row: np.linalg.norm(row['grant_last_name_vec'] - 
        #                               row['npi_last_name_vec']), axis=1)
        
        #Returning Datafrane with only features
        return df.drop(columns=data_cols).drop(columns=[
            v for v in df.columns if 'vec_' in v])
    
    #Pass the output of this into a new classifier model from reusable classifier, train the classifier

    if __name__ == '__main__':
        pass





    