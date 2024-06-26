# SigmoidalVision

SigmoidalVision is a Python package for computer vision and machine learning tasks. It is currently under development and aims to provide a set of tools and utilities for working with image and video data.

## Features

- Download media assets from a catalog
- Verify the integrity of downloaded files using MD5 hash

## Installation

SigmoidalVision can now be installed directly from PyPI with the following command:

```bash
pip install sigmoidalvision
```

## Usage

Here's an example of how to download a media asset using SigmoidalVision:

```python
from sigmoidalvision.assets import download_media_asset, MediaAsset
download_media_asset(MediaAsset.AIRPORT)
# File santos_dumont_airport.mp4 downloaded successfully.
```

Please note that SigmoidalVision is still under development, and features may be added or changed in future releases.