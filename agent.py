import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent

from config import get_llm

class PandasAgent:
    def __init__(self, file_path):
        self.df = self.load_dataframe(file_path)
        self.agent = self.create_agent()
    def load_dataframe(self,file_path):
        if file_path.endswith(".csv"):
            return pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            return pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format")
    def create_agent(self):
        llm = get_llm()
        return create_pandas_dataframe_agent(llm=llm,
        df=self.df,
        verbose=False,
        allow_dangerous_code=True
        )       
    def ask(self, question):
        response = self.agent.invoke(question)
        return response["output"]             