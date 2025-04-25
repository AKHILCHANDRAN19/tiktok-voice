# setup.py

import setuptools
import os

# Function to read the README file.
def read_readme(fname):
    """Reads the README file."""
    try:
        with open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8') as f:
            return f.read()
    except IOError:
        return "" # Return empty string if README is not found

setuptools.setup(
    name="tiktok-voice-unofficial", # Choose a name (added -unofficial)
    version="0.1.0", # Initial version
    author="oscie57 (Original Author)",
    author_email="author@example.com", # Placeholder email
    description="An unofficial Python wrapper for the TikTok Text-to-Speech API.",
    long_description=read_readme("README.md"), # Read long description from README.md
    long_description_content_type="text/markdown", # Specify README format
    url="https://github.com/oscie57/tiktok-voice", # Project homepage
    project_urls={ # Optional: Add more URLs
        "Bug Tracker": "https://github.com/oscie57/tiktok-voice/issues",
        # "Source": "https://github.com/your-username/tiktok-voice/", # Add your fork URL if applicable
    },
    # Automatically find the package directory (tiktok_voice)
    packages=setuptools.find_packages(where='.'),
    # Or explicitly: packages=['tiktok_voice'],
    classifiers=[ # Standard classifiers
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: Other/Proprietary License", # Reflects lack of clear open source license
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.6", # Minimum Python version
    install_requires=[ # List runtime dependencies
        "requests>=2.20.0",
        "pydub>=0.25.0",
    ],
    # If your package included data files:
    # include_package_data=True,
    # package_data={
    #     'your_package_name': ['data/*.dat'],
    # },
)

# --- End of setup.py ---
