#lib para pegar dados da internet
from pydoc import doc
import requests
import json
#biblioteca Excel - pip install xlsxwriter
import xlsxwriter

headers_info = {'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'}
dados = requests.get(url='https://parallelum.com.br/fipe/api/v2/motorcycles/brands', headers=headers_info )

lista_resposta = json.loads(dados.content)

#criar documento excelxl
documento_excel = xlsxwriter.Workbook('fipe.xlsx')
planilha_excel = documento_excel.add_worksheet('Marcas')
linha = 1

planilha_excel.write(0, 0, "MARCA")
planilha_excel.write(0,1, "CÒDIGO")

for marca in lista_resposta:

    planilha_excel.write(linha, 0, marca.get('name'))
    planilha_excel.write(linha,1, marca.get('code'))
    linha += 1


planilha_excel_motos = documento_excel.add_worksheet('Motos')

dados_modelo = requests.get(
    url="https://parallelum.com.br/fipe/api/v2/motorcycles/brands/101/models", 
    headers=headers_info)

lista_modelo = json.loads(dados_modelo.content)
linha = 1

for modelo in lista_modelo:
    planilha_excel_motos.write(linha, 0, modelo.get('name') )
    planilha_excel_motos.write(linha, 1, modelo.get('code'))
    linha +=1


planilha_excel_fipe_yamaha = documento_excel.add_worksheet('Fipe - Yamaha')
linha = 0
for modelo in lista_modelo:
    for ano in range(2022, 2023, 1):
        api = f"http://parallelum.com.br/fipe/api/v2/motorcycles/brands/101/models/{modelo.get('code')}/years/{ano}-1"
       # api = "http://parallelum.com.br/fipe/api/v2/motorcycles/brands/101/models/4571/years/2009-1"
        print(api)

        dados = requests.get(url=api, headers= headers_info)
        print(dados)
        
        if dados.status_code == 200:
            moto = json.loads(dados.content)
            planilha_excel_fipe_yamaha.write(linha, 0, moto.get('model') )
            planilha_excel_fipe_yamaha.write(linha, 1, moto.get('price') )
            planilha_excel_fipe_yamaha.write(linha, 2, moto.get('modelYear') )
            planilha_excel_fipe_yamaha.write(linha, 3, moto.get('fuel') )      
            linha += 1
        

documento_excel.close()  