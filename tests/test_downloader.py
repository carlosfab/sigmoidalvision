# tests/test_downloader.py

import os
from sigmoidalvision.assets.downloader import download_media_asset
from sigmoidalvision.assets.catalog import MediaAsset


def test_download_media_asset():
    # Test downloading a valid media asset
    filename = download_media_asset(MediaAsset.AIRPORT)
    assert filename == MediaAsset.AIRPORT.value
    assert os.path.exists(filename)

    # Test downloading an invalid media asset
    try:
        download_media_asset("invalid_asset.mp4")
        assert False, "Expected ValueError for invalid media asset"
    except ValueError:
        pass
