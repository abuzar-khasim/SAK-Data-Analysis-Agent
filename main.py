from agent import PandasAgent
File_Path = input("Enter CSV or Excel file path: ")

agent =PandasAgent(File_Path)
print("Pandas Agent Started !")
print("Type 'exit' to quit.\n")

while True:
    question=input("YOU :")

    if question.lower() == {"exit","quit"}:
        break
    try:
        answer = agent.ask(question)

        print("AGENT :",answer)
        print("-"*50) 
    except Exception as e:
        print("Error:",e)
            
