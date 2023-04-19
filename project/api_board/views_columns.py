from flask import Flask, render_template, request, redirect, url_for, jsonify, json, Request
from api_board import api_board_bp
from util.util import json_response
from util import queries


@api_board_bp.route("/boards/<int:board_id>/columns/", methods=["GET"])
@json_response
def get_columns_for_board(board_id: int):
    """
    All columns that belongs to a board
    :param board_id: id of the parent board
    """
    return queries.get_table_by_element_order_by_element(
        "columns",
        "board_id",
        board_id,
        "column_order"
    )


@api_board_bp.route("/boards/columns/", methods=["POST"])
@json_response
def create_column():
    data = request.get_json()
    board_id = request.get_json()["board_id"]
    title = request.get_json()["title"]
    column_order = len(queries.get_everything_by_id('columns', 'board_id', board_id)) + 1
    queries.add_column(board_id, title, column_order)
    return data, 201

@api_board_bp.route("/boards/columns/<int:column_id>", methods=["DELETE"])
@json_response
def delete_column(column_id: int):

    return queries.delete_column(column_id)


<<<<<<< HEAD
@api_board_bp.route("/boards/columns/<int:column_id>/updata", methods=["POST"])
@json_response
def updata_column(column_id):
    column_title = request.get_json()["title"]
    queries.updata_title('columns',column_id,column_title)
    return {"title": column_title, "http_code": 201}
=======
@api_board_bp.route("/boards/columns/", methods=["PUT"])
@json_response
def updata_column():
    column_title = request.json["title"]
    column_id = request.json["id"]
    queries.updata_column(column_id,column_title)
    return {"title": column_title, "http_code": 201}
>>>>>>> development
