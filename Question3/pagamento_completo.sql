WITH pagamento_completo AS (
SELECT * FROM pessoas
JOIN contratos ON pessoas.CONTRATO_ID = contratos.id
JOIN pagamentos ON pessoas.ID = pagamentos.PESSOA_ID)
SELECT nome,(valor_parcela*parcelas) AS VALOR_TOTAL from pagamento_completo
WHERE dt_completo IS NOT NULL;
