#%% 
from ppt2video.tools import *

# meta = Meta(
#     ppt_file='your_ppt_slide.pptx',  # Name of your PPT file
#     image_prefix='slide',  # The prefix for image files (varies depending on the PowerPoint language version)
#     google_application_credentials='/config/google_cloud.json',  # Location and filename of your Google Cloud service account key
#     fade_after_slide= [], 
#     lang = 'E',
#     convert_slides_upto_slide_no=0,
# )

# ppt_to_video(meta)

meta = Meta(
    ppt_file='',  # Name of your PPT file
    image_prefix='슬라이드',  # The prefix for image files (varies depending on the PowerPoint language version)
    google_application_credentials='../config/google_cloud.json',  # Location and filename of your Google Cloud service account key
    fade_after_slide= [], 
    lang='K',
    convert_slides_upto_slide_no=0,
)

ppt_to_video(meta)

