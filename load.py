import os
import subprocess
import requests
from dotenv import load_dotenv
from google.cloud import storage
from io import BytesIO
from PIL import Image, ExifTags
# from PIL.ExifTags import TAGS

load_dotenv()


def load_image(blob_name):
    """Loads an image and its metadata from the bucket."""
    # Initialize a client
    storage_client = storage.Client(project=os.environ.get("USER"))
    # os.environ.get("GOOGLE_CLOUD_STORAGE_BUCKET"
    # Get the bucket
    bucket = storage_client.bucket(os.environ.get("GOOGLE_CLOUD_STORAGE_BUCKET"))

    # Create a blob object from the blob name
    blob = bucket.blob(blob_name)

    # Download the blob's content as a byte stream
    byte_stream = BytesIO(blob.download_as_bytes())

    # Load the image using PIL
    image = f"https://storage.googleapis.com/{os.environ.get('GOOGLE_CLOUD_STORAGE_BUCKET')}/{blob_name}"
    # Fetch the image
    response = requests.get(image)
    exeProcess = "hachoir-metadata"
    process = subprocess.Popen([exeProcess,response.content],
                                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                            universal_newlines=True)
    infoDict = {}
    for tag in process.stdout:
            line = tag.strip().split(':')
            infoDict[line[0].strip()] = line[-1].strip()

    for k,v in infoDict.items():
        return(k,':', v)

    # Get metadata
    # metadata = {
    #     "name": blob.name,
    #     "content_type": blob.content_type,
    #     "size": blob.size,
    #     "updated": blob.updated,
    #     "generation": blob.generation,
    #     "metageneration": blob.metageneration,
    # }

    # return  metadata

def meat(data):
    

    # open the image
    image = f"https://storage.googleapis.com/{os.environ.get('GOOGLE_CLOUD_STORAGE_BUCKET')}/{data}"
    # Fetch the image
    response = requests.get(image)

    # Check if the request was successful
    if response.status_code == 200:
        # Open the image
        image = Image.open(BytesIO(response.content))

        # Extract EXIF data
        exif_data = image._getexif()
        
        # If there is no EXIF data, print a message
        if not exif_data:
            return("No EXIF metadata found")
        else:
            # Convert EXIF data to human-readable form
            exif = {ExifTags.TAGS[k]: v for k, v in exif_data.items() if k in ExifTags.TAGS}
            tag = []
            value = []
            # Print the metadata
            for tag, value in exif.items():
                data = [f"{tag}: {value}"]
            return data
    else:
        return (f"Failed to retrieve image. Status code: {response.status_code}")


# data= load_image("kanye")
# print(data)
data = meat("mifi")
print(data)



