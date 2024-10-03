# ppt2video
## A tool that converts a PowerPoint (PPT) to a video with voice narration (reading the notes from each slide)

This tool reads the note contents from each slide using Google TTS and converts the PPT to an MP4 video. 

### Installation

```
pip install ppt2video
```


### Usage

+ Step 1: Place your PPT file (or `.pptx`) into a specific folder (e.g., `data/ppt/your_ppt_name.pptx`).

+ Step 2: Open your PowerPoint software and save the slides as images (e.g., PNG) to a specific folder (usually, `data/ppt/your_ppt_name/`).

+ Step 3: Set up Google Cloud Authentication to access the note contents in your slides:

    - You need to set up authentication using your Google Cloud service account key. Follow these steps:
        * Go to the Google Cloud Console ([https://console.cloud.google.com/](https://console.cloud.google.com/)).
        * Create a new project (or use an existing project).
        * Enable the Text-to-Speech API for that project.
        * Create a Service Account and download the JSON key file.

+ Step 4: Run the code

```python
from ppt2video.tools import *

meta = Meta(
    ppt_file='your_ppt_slide.pptx',  # Name of your PPT file
    image_prefix='slide',  # The prefix for image files (varies depending on the PowerPoint language version)
    google_application_credentials='/config/google_cloud.json'  # Location and filename of your Google Cloud service account key
)

# Run the conversion
ppt_to_video(meta)
```

### Additional settings
You may adjust additional settings as follows:

```python
    # PPT settings
    ppt_file: str 
    ppt_path: str = 'data/ppt/'  # Directory for the PPT and image files
    image_prefix: str = 'slide'  # The prefix for image file names (used when saving slides as images)
    image_extension: str = 'PNG'  # The image file format (default is PNG)
    ppt_extension: str = '.pptx'  # The PowerPoint file extension

    # Google TTS settings
    voice_enabled: bool = True  # Enable or disable voice narration
    google_application_credentials: str = None  # Location of the Google API key (downloaded as JSON)
    voice_path: str = 'data/voice/'  # Directory to save the generated audio files
    max_size: int = 4500  # Maximum text size limit for a single Google TTS API request (default 5000)
    slide_break: float = 2  # Time delay (in seconds) between slides
    line_break: float = 0.7  # Time delay (in seconds) when there's a line break in the text (e.g., '\n')
    lang: str = 'E'  # Language setting: 'E' for English, 'K' for Korean 
    wave: bool = False  # Whether to use Wavenet voices (True or False)

    # MoviePy video settings
    fps: int = 24  # Frames per second for the video
```




