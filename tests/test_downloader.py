# tests/test_downloader.py

import os
import tempfile

import pytest

from sigmoidalvision.assets import download_media_asset, MediaAsset


@pytest.fixture
def temp_dir():
    with tempfile.TemporaryDirectory() as temp_dir:
        original_dir = os.getcwd()
        os.chdir(temp_dir)
        yield temp_dir
        os.chdir(original_dir)


def test_download_media_asset(temp_dir):
    # Test downloading a valid media asset
    filename = download_media_asset(MediaAsset.AIRPORT)
    assert filename == MediaAsset.AIRPORT.value
    assert os.path.exists(os.path.join(temp_dir, filename))

    # Test downloading an invalid media asset
    try:
        download_media_asset("invalid_asset.mp4")
        assert False, "Expected ValueError for invalid media asset"
    except ValueError:
        pass
