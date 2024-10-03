from setuptools import setup, find_packages

setup(
    name='ppt2video',  # Name of the package
    version='0.1.0',  # Version number
    packages=find_packages(),  # Automatically finds all packages in the directory
    install_requires=[         # List dependencies here
        'python-pptx',
        'moviepy',
        'google-cloud-texttospeech'
    ],
    entry_points={             # If your package has entry points (CLI tools)
    },
    author='IssueTracker',        
    author_email='issuetree.tracker@gmail.com',  
    description='A tool that converts a PowerPoint (PPT) to a video with voice narration (reading the notes from each slide)',
    long_description=open('README.md').read(),  # Detailed description (usually from README)
    long_description_content_type='text/markdown',  # Format of README
    url='https://github.com/iburn78/ppt2video',  # URL for your package (GitHub link, etc.)
    classifiers=[              # Optional metadata classifiers
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',   # Python version requirement
)
