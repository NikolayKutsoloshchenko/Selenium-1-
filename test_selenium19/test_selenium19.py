import pytest
from Application import application

@pytest.fixture
def app(request):
    app = application()
    request.addfinalizer(app.driver.quit)
    return app

def test_adding_to_cart(app):
    app.add_3_ducks()
    assert app.items_in_bag >= 1

def test_removing_from_cart(app):
    app.add_3_ducks()
    app.delete_all_ducks()
    assert app.items_in_bag == 0