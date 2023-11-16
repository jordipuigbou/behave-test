from behave import *
from requests import request
import json
from os.path import join


@step('I send a "{method}" request to "{url}"')
def send_method_request(context, method, url):
    context.response = request(method, url)


@step('the response status code should be "{status_code:d}"')
def check_status_code(context, status_code):
    assert context.response.status_code == status_code, f"Expected status code {status_code} but got {context.response.status_code}"


@step('the response JSON body should contain "{elements:d}" elements')
def check_json_body(context, elements):
    assert len(context.response.json()) == int(
        elements), f"Expected {elements} elements but got {len(context.response.json())}"


@step('I send a "{method}" request to "{url}" with a JSON body')
def set_method_request_with_json_body(context, method, url):
    context.response = request(method, url, json=json.loads(context.text))


@step('I get the id of the first element and store in context')
def get_id(context):
    context.id = context.response.json()[0]['_id']['$oid']


@step('I send a "{method}" request to "{url}" with the id stored in context')
def set_method_request_with_id(context, method, url):
    context.response = request(method, join(url, context.id))

@step('I send a "{method}" request to "{url}" with a JSON body and the id stored in context')
def set_method_request_with_json_body_and_context_id(context, method, url):
    context.response = request(method, join(url, context.id), json=json.loads(context.text))

@step('the response JSON body should contain "{value}"')
def check_json_body_with_string(context, value):
    assert value in context.response.text, f"Expected {value} but got {context.response.text}"
