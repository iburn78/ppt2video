from ppt2video.tools import *

meta = Meta(
    ppt_file='your_ppt_slide.pptx',  # Name of your PPT file
    image_prefix='slide',  # The prefix for image files (varies depending on the PowerPoint language version)
    google_application_credentials='/config/google_cloud.json'  # Location and filename of your Google Cloud service account key
)

# Run the conversion
ppt_to_video(meta)
