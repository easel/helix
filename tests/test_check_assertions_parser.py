"""Regression tests for check_assertions.parse_assertions edge cases."""
import sys
from pathlib import Path

# Allow running from repo root without install
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts" / "demos"))

from check_assertions import parse_assertions  # noqa: E402
import tempfile, textwrap


def _parse(text: str) -> dict:
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yml", delete=False) as f:
        f.write(textwrap.dedent(text))
        tmp = Path(f.name)
    try:
        return parse_assertions(tmp)
    finally:
        tmp.unlink()


def test_list_item_with_colon_in_value():
    """A list item whose value contains a colon must not be misclassified as a dict entry."""
    result = _parse("""
        slug: demo
        expect:
          - kind: shell
            contains_all:
              - "bun:test"
              - "plain"
    """)
    assert result["expect"][0]["contains_all"] == ["bun:test", "plain"], result


def test_list_item_without_colon_still_works():
    result = _parse("""
        slug: demo
        expect:
          - kind: shell
            contains_all:
              - "bun test"
    """)
    assert result["expect"][0]["contains_all"] == ["bun test"], result


def test_dict_subkey_still_works():
    result = _parse("""
        slug: demo
        expect:
          - kind: tool_call
            args_contain:
              file_path: "docs/helix/01-frame/prd.md"
    """)
    assert result["expect"][0]["args_contain"]["file_path"] == "docs/helix/01-frame/prd.md", result


if __name__ == "__main__":
    test_list_item_with_colon_in_value()
    test_list_item_without_colon_still_works()
    test_dict_subkey_still_works()
    print("all tests passed")
