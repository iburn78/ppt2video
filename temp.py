#%% 
from ppt2video.tools import *

# meta = Meta(
#     ppt_file='your_ppt_slide.pptx',  # Name of your PPT file
#     image_prefix='slide',  # The prefix for image files (varies depending on the PowerPoint language version)
#     google_application_credentials='/config/google_cloud.json'  # Location and filename of your Google Cloud service account key
# )

image_prefix = '슬라이드'
gca ='../config/google_cloud.json'

ppt_file='삼성전자_2024_2Q_K_2024-10-03_shorts01.pptx'
lang = 'K'
meta = Meta(ppt_file=ppt_file, image_prefix=image_prefix, lang=lang, google_application_credentials=gca)

ppt_to_video(meta)
# n = ppt_to_text(meta)
# print(ppt_tts(meta, n))

ppt_file='yourfile_2024_2Q_E_2024-09-30.pptx'
lang = 'E'
meta = Meta(ppt_file=ppt_file, image_prefix=image_prefix, lang=lang, google_application_credentials=gca)

# ppt_to_video(meta)
# n = ppt_to_text(meta)
# print(ppt_tts(meta, n))
