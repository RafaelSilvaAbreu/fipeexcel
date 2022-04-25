# fipeexcel
Projeto desenvolvido no SENAI BETIM, inspirado na ideia do aluno Bruno José
<h1> FIPEXCEL </h1>
Uma concessionário de veículos realiza consultas online a tabela FIPE(tabela de valores de automóveis) mensalmente. O tempo gasto nessas consultas é em média <b>2 horas</b> diárias, pois são consiltados cerca de 400 veículos. Visando solucianar esse problema criamos um sistema que consulta os dados online e os armazena em uma planilha excel. Utilizando o sistema o <b>tempo gasto na consulta cai para média 5 minutos</b>.




# Requisitos Funcionais do Sistema

RF-001: O sistema deve permitir a busca de informação dos veículos a partir de um código e ano de fabricação.  

RF-002: O sistema deve gravar os dados retornados pela consulta em um arquivo Excel, os dados são armazenados sâo: Código do veículo, Marca, Modelo, Ano, Preço, Tipo de combustível, Mês de Referência da Consulta.



# Requisitos não Funcionais

RFN: 001 - sistema deve salvar o arquivo em XLSX versão 2007 ou superior.

RFN: 002 - Sistema deve ter acesso a internet.

RFN: 003 - O usuário deve ter instalado em seu computador o Python na verção 3.7 ou superior.



#Regras de Negócio

Regra de Negócio: 001 - Consulta a tabela FIPE. A consulta a tabela FIPE deve ser feita pelo código oficial do veículo, todo veículo possui um código, gerenciado pela organização que cuida da FIPE. Requisito Funcional - 001

# <h1>Diagrama de Classe</h1>
![Diagrama](https://user-images.githubusercontent.com/96276519/165191126-bda117f9-bad2-490f-a220-7a4c6bfcbbe7.png)


https://parallelum.com.br/fipe/api/v2/cars/brands
