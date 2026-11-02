"""
MCP Server for Salivary Alpha-Amylase (sAA) & Autonomic Sympathetic Reactivity.
Exposes JSON-RPC endpoints for assessing sAA surge kinetics and sympathetic stress resilience.
"""

import json
import sys
from client import SalivaryAlphaAmylaseClient

client = SalivaryAlphaAmylaseClient()


def handle_request(request: dict) -> dict:
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {})

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "evaluate_acute_sympathetic_reactivity",
                        "description": "Evaluates salivary alpha-amylase (sAA) noradrenergic response to acute challenge, computing AUC, clearance slope, and Sympathetic Stress Resilience Index.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "baseline_saa_u_ml": {"type": "number", "description": "Resting baseline sAA activity in U/mL"},
                                "peak_saa_u_ml": {"type": "number", "description": "Peak sAA activity reached during/immediately after challenge in U/mL"},
                                "post30_saa_u_ml": {"type": "number", "description": "sAA activity at 30 minutes post-challenge in U/mL"},
                                "sampling_times_min": {
                                    "type": "array",
                                    "items": {"type": "number"},
                                    "description": "Optional list of sampling timestamps in minutes (e.g. [0, 15, 30, 60])"
                                },
                                "saa_values_u_ml": {
                                    "type": "array",
                                    "items": {"type": "number"},
                                    "description": "Optional corresponding sAA readings in U/mL"
                                }
                            },
                            "required": ["baseline_saa_u_ml", "peak_saa_u_ml", "post30_saa_u_ml"]
                        }
                    }
                ]
            }
        }

    elif method == "tools/call":
        tool_name = params.get("name")
        args = params.get("arguments", {})

        if tool_name == "evaluate_acute_sympathetic_reactivity":
            res = client.evaluate_acute_sympathetic_reactivity(
                baseline_saa_u_ml=args.get("baseline_saa_u_ml", 45.0),
                peak_saa_u_ml=args.get("peak_saa_u_ml", 110.0),
                post30_saa_u_ml=args.get("post30_saa_u_ml", 55.0),
                sampling_times_min=args.get("sampling_times_min"),
                saa_values_u_ml=args.get("saa_values_u_ml")
            )
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}
            }

        else:
            return {
                "jsonrpc": "2.0",
                "id": req_id,
                "error": {"code": -32601, "message": f"Method {tool_name} not found"}
            }

    return {
        "jsonrpc": "2.0",
        "id": req_id,
        "error": {"code": -32600, "message": "Invalid Request"}
    }


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            resp = handle_request(req)
            sys.stdout.write(json.dumps(resp) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
