SELECT 
    pc.codigo as codigo, 
    pc.quantidade, 
    p.codigo as codigo_produto,
    p.descricao as descricao_produto, 
    pm.codigo as codigo_produto_mercado, 
    pm.descricao as descricao_produto_mercado, 
    pm.valor_unitario 
FROM 
    produtos_carrinho pc 
INNER JOIN 
    produtos_mercados pm ON pc.codigo_produto_mercado = pm.codigo 
INNER JOIN 
    produtos p ON pm.codigo_produto = p.codigo
ORDER by pc.codigo
