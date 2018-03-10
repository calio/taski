import pytest
from app.arguments import parse, str2unicode


def test_str2unicoce():
    s = str2unicode("Hello")
    assert s == "Hello"


def test_parse_rank_project():
    cmd = ["rank", "-p", "my-project"]
    args = parse(cmd=cmd)
    assert args.project == "my-project"


def test_parse_plan():
    cmd = ["plan", "-l" "100", "-n", "10"]
    args = parse(cmd=cmd)
    assert args.limit == 100
    assert args.daily_goal == 10
