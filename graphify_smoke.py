"""Smoke-test module for Graphify's hosted push-to-index pipeline.

Pushing this file exercises the full loop end to end: GitHub webhook ->
control-plane acceptance -> launcher reconcile tick -> index task -> graph
update. The function below exists only so the new graph node is trivial to find.
"""


def graphify_smoke_marker() -> str:
    """Return a stable marker string to locate this node in the updated graph."""
    return "graphify-push-to-index-ok"
