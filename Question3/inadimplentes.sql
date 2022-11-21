WITH inadimplentes AS (
SELECT * FROM pessoas
JOIN contratos ON pessoas.CONTRATO_ID = contratos.id
JOIN pagamentos ON pessoas.ID = pagamentos.PESSOA_ID)
SELECT nome, STRFTIME('%d', dt_pagamento) as DIA_MES,valor_parcela from inadimplentes
WHERE inadimplente = 'S';
