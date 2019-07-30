import logging
import ffmpy3
import os

import azure.functions as func

os.popen('chmod u+x /home/site/wwwroot/BlobTrigger/ffmpeg').read()

def main(myblob: func.InputStream,
    context: func.Context):
    logging.info(f"Python blob trigger function processed blob \n"
                 f"Name: {myblob.name}\n"
                 f"Blob Size: {myblob.length} bytes")
    
    file = open("input.mp4", "wb")
    file.write(myblob.read())
    file.close()
    ff = ffmpy3.FFmpeg(
     executable=context.function_directory + '/ffmpeg',
     inputs={'input.mp4': None},
     outputs={'output_%d.png': '-y -vf fps=1'}
    )
    ff.run()