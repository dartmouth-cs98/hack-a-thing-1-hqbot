#!/usr/bin/env python

import io
import os
import urllib.request
from unidecode import unidecode

from googleapiclient.discovery import build

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

raw = []
choices = []

def google_results_count(query):
    # service = build("customsearch", "v1",
    #                 developerKey="AIzaSyBIVobUohwFaqcHmHNjzzvYGIdYcpx2dzY")
    service = build("customsearch", "v1",
                    developerKey="AIzaSyA0shB46vFldA67M78IUj7lPqFOpXowoWs")

    result = service.cse().list(
            q=query,
            cx='017735030349167315482:c7kz5dj36s4'
        ).execute()

    # return result["searchInformation"]["totalResults"]
    print(result)
    return result["items"]

"""Detects text in the file."""
client = vision.ImageAnnotatorClient()

with io.open("/Users/azharhussain/Desktop/question.png", 'rb') as image_file:
	content = image_file.read()

	image = types.Image(content=content)

	response = client.text_detection(image=image)
	texts = response.text_annotations

	for text in texts:
		des = text.description
		raw.append(des)

	spliced = raw[0].split("?")
	query = spliced[0].replace("\n", " ")
	san = unidecode(spliced[1])
	answers = san.split("\n")
	answers = list(filter(None, answers))
	print(san)
	print(answers)
