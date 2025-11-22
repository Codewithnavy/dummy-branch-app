from flask import Blueprint, jsonify
from sqlalchemy import text
from app.db import SessionContext

bp = Blueprint("health", __name__)

@bp.route("/health", methods=["GET"])
def health():
    try:
        with SessionContext() as session:
            session.execute(text("SELECT 1"))
        return jsonify({"status": "ok", "database": "connected"})
    except Exception as e:
        return jsonify({
            "status": "error",
            "database": "disconnected",
            "details": str(e)
        }), 503
