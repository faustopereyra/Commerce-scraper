from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

#Get html document
with open("aliwan.html") as file:
    content = file.read()

#Parse HTML document
soup = BeautifulSoup(content, "html.parser")

colums = soup.find_all(name="tr")

final_dataframe = []

for colum in colums:
    rows = colum.find_all(name="span")
    final_colum = [row.getText() for row in rows]
    final_colum = [col for col in final_colum if col != "ComisiÃ³n"]
    final_dataframe.append(final_colum)


official_colums = final_dataframe.pop(0)
final_dataframe.pop(-1)

official_colums.pop(official_colums.index('Estado'))
official_colums.pop(official_colums.index('Verificado'))



df = pd.DataFrame(np.array(final_dataframe),columns=official_colums, dtype=object)

print(df)

df.to_csv("df.csv")
