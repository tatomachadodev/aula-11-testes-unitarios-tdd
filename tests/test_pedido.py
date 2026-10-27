import pytest

from src.pedido import calcular_taxa_entrega, calcular_total


def test_calcula_total_de_varios_itens():
    # Arrange
    itens = [
        {"preco": 20, "quantidade": 2},
        {"preco": 10, "quantidade": 1},
    ]

    # Act
    total = calcular_total(itens)

    # Assert
    assert total == 50


def test_retorna_zero_quando_lista_esta_vazia():
    # Arrange
    itens = []

    # Act
    total = calcular_total(itens)

    # Assert
    assert total == 0


def test_rejeita_item_com_preco_zero():
    itens = [{"preco": 0, "quantidade": 1}]

    with pytest.raises(ValueError, match="preco"):
        calcular_total(itens)


def test_rejeita_item_com_quantidade_zero():
    itens = [{"preco": 20, "quantidade": 0}]

    with pytest.raises(ValueError, match="quantidade"):
        calcular_total(itens)


def test_cobra_taxa_de_cinco_reais_ate_tres_km():
    assert calcular_taxa_entrega(2, 50) == 5


def test_acrescenta_dois_reais_por_km_excedente():
    assert calcular_taxa_entrega(4, 50) == 7


def test_dar_frete_gratis_para_pedido_a_partir_de_cem_reais():
    assert calcular_taxa_entrega(5, 100) == 0


def test_rejeita_distancia_negativa():
    with pytest.raises(ValueError, match="distancia"):
        calcular_taxa_entrega(-1, 50)
