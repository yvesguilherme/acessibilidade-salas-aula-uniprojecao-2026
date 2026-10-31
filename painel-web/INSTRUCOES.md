# Painel web de acessibilidade

## Executar localmente

No terminal, a partir da pasta painel-web:

    python3 servidor_local.py

Abra http://127.0.0.1:8765. Para encerrar, pressione Ctrl+C.

O painel usa apenas recursos nativos do navegador e da biblioteca padrão do Python. Não precisa instalar pacotes.

## Publicar em hospedagem estática

Publique os arquivos index.html e dados.json desta pasta em uma hospedagem estática. O arquivo servidor_local.py serve apenas para a prévia local e não é necessário na hospedagem.

dados.json contém somente contagens agregadas. Não publique o CSV original junto com o site: ele contém linhas individuais e carimbos de data/hora.

## Atualizar os números

Ao receber uma nova coleta, recalcule as contagens antes de substituir dados.json. Preserve apenas dados agregados e confira se os denominadores de cada pergunta correspondem às respostas válidas.

Para atualizar `respostas_por_periodo`, agrupe dias consecutivos até cada período conter pelo menos cinco respostas. Use rótulos relativos (por exemplo, “Dia 1” ou “Dias 2–3”) e não publique carimbos de data/hora. O gráfico de linha calcula o total acumulado a partir dessas contagens.
