Feature: Check product crud backend endpoint
    As an API consumer
    I want to check product crud backend endpoint methods

  @health
  Scenario: Check service health
     When I send a "GET" request to "http://backend:8888/health"
     Then the response status code should be "200"

  @products
  Scenario: Check products list is empty
     When I send a "GET" request to "http://backend:8888/products"
     Then the response status code should be "200"
      And the response JSON body should contain "0" elements

  @products
  Scenario Outline: Insert "<Title>" product and check there are "<Elements>" in the list
     When I send a "POST" request to "http://backend:8888/products" with a JSON body
        """
            {
                "Date": "<Date>",
                "CopyRight": <CopyRight>,
                "Title": "<Title>",
                "Picture": "<Picture>"
            }
        """
      And the response status code should be "200"
     Then I send a "GET" request to "http://backend:8888/products"
      And the response status code should be "200"
      And the response JSON body should contain "<Elements>" elements

    Examples:
          | Date       | CopyRight | Title     | Picture                                                                                                              | Elements |
          | 2023-01-03 | 2020      | iPhone X  | https://www.apple.com/newsroom/images/products/iphone/standard/Apple_announce-iphone12pro_10132020_big.jpg.large.jpg | 1        |
          | 2023-01-04 | 2022      | iPhone 12 | https://www.apple.com/newsroom/images/products/iphone/standard/Apple_announce-iphone12pro_10132020_big.jpg.large.jpg | 2        |

  @products
  Scenario: Delete one product and check there is one element in the list
    Given I send a "GET" request to "http://backend:8888/products"
      And I get the id of the first element and store in context
     When I send a "DELETE" request to "http://backend:8888/products" with the id stored in context
      And the response status code should be "200"
     Then I send a "GET" request to "http://backend:8888/products"
      And the response status code should be "200"
      And the response JSON body should contain "1" elements

  @products
  Scenario: Update one product and verify fields have been updated
    Given I send a "GET" request to "http://backend:8888/products"
      And I get the id of the first element and store in context
     When I send a "PUT" request to "http://backend:8888/products" with a JSON body and the id stored in context
        """
            {
                "Date": "2024-01-01",
                "CopyRight": 2030,
                "Title": "Iphone 20",
                "Picture": "https://www.apple.com/newsroom/images/products/iphone/standard/Apple_announce-iphone12pro_10132020_big.jpg.large.jpg"
            }
        """
      And the response status code should be "200"
     Then I send a "GET" request to "http://backend:8888/products"
      And the response status code should be "200"
      And the response JSON body should contain "2024-01-01"
      And the response JSON body should contain "2030"
      And the response JSON body should contain "Iphone 20"
      And the response JSON body should contain "https://www.apple.com/newsroom/images/products/iphone/standard/Apple_announce-iphone12pro_10132020_big.jpg.large.jpg"

  @products
  Scenario: When try to update a wrong product id, the response status code should be 500
     When I send a "PUT" request to "http://backend:8888/products/fake_id" with a JSON body
        """
            {
                "Date": "2024-01-01",
                "CopyRight": 2030,
                "Title": "Iphone 20",
                "Picture": "https://www.apple.com/newsroom/images/products/iphone/standard/Apple_announce-iphone12pro_10132020_big.jpg.large.jpg"
            }
        """
      And the response status code should be "500"
      And the response JSON body should contain "product not updated"