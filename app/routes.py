from flask import Blueprint, request, jsonify
from .quotes import QUOTES
from .utils import get_random_quote, last_quote_cache

quote_bp = Blueprint('quote', __name__)

@quote_bp.route("/quote", methods=["GET"])
def get_quote():
    category = request.args.get("category", "general").lower()
    
    if category not in QUOTES:
        return jsonify({"error": "Invalid category"}), 400

    quote = get_random_quote(category, last_quote_cache)
    return jsonify({
        "quote": quote,
        "category": category
    })
