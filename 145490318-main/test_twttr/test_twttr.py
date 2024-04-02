import twttr
from twttr import shorten
import pytest

def main():
    test_prog()


def test_prog():
    assert shorten("akshat") == "ksht"
    assert shorten ("hello") == "hll"
    assert shorten("Akshat") == "ksht"

if __name__=="__main__":
    main()
