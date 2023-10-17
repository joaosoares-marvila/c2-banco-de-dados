SELECT 
    pm.codigo,
    pm.descricao,
    pm.valor_unitario,
    pm.codigo_produto,
    p.descricao AS descricao_produto,
    m.nome AS mercado
FROM produtos_mercados pm
INNER JOIN produtos p
    ON pm.codigo_produto = p.codigo
INNER JOIN mercados m
    ON pm.codigo_mercado = m.codigo
ORDER BY pm.descricao;