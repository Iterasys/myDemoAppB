import pytest
from pages import main_page, product_page, cart_page


# inicializar as classes das páginas
@pytest.fixture()
def main(driver):
    return main_page.MainPage(driver)


@pytest.fixture()
def product(driver):
    return product_page.ProductPage(driver)


@pytest.fixture()
def cart(driver):
    return cart_page.CartPage(driver)


# os testes

# teste positivo do fluxo de comprar
def testar_comprar_mochila_vermelha(main, product, cart,
                                    quantidade=2,
                                    nome_produto_esperado='Sauce Lab Back Packs',
                                    preco_produto_esperado='$ 29.99',
                                    total_produto_esperado='$ 59.98'
                                    ):
    # tela inicial
    main.selecionar_primeiro_produto_()

    # tela de produto
    assert product.ler_nome_() == nome_produto_esperado
    assert product.ler_preco_() == preco_produto_esperado

    product.arrastar_para_cima_()
    product.como_(quantidade)  # adicionar 2 mochilas vermelhas no carrinho

    # tela de carrinho
    cart.ir_para_o_carrinho_de_compras()

    assert cart.ler_dados_do_carrinho() == [nome_produto_esperado, preco_produto_esperado, total_produto_esperado]
