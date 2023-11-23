from endpoints.products import Products
from pytest import raises
def test_get_products():
    products = Products()
    response = products.get()
    assert response == ([], 200)

def test_delete_products_missing_id():
    products = Products()
    with raises(TypeError) as excinfo:
        products.delete()
    assert "missing 1 required positional argument" in str(excinfo.value)

def test_post_products_missing_id():
    products = Products()
    response = products.post()
    assert response == ({'status': 'error parsing json'}, 500)

def test_put_products_missing_json():
    products = Products()
    response = products.put()
    assert response == ({'status': 'product not updated because id is not provided'}, 500)