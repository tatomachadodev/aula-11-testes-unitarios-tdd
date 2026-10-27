# Registro do ciclo de TDD

## Comportamento escolhido

Cobrar taxa de entrega para uma distância de até 3 km.

## Red

**Teste criado:** `test_cobra_taxa_de_cinco_reais_ate_tres_km`

**Motivo da falha:** A função `calcular_taxa_entrega` ainda não existia.

## Green

**Implementação realizada:** Foi criada a função com a regra de cobrar R$ 5 até 3 km.

## Refactor

**Melhoria realizada:** Foram adicionadas as outras regras na mesma função e uma validação para distância negativa.

**Resultado final:** Todos os testes passaram, incluindo os quatro testes novos e os quatro testes que já existiam.
