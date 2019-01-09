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


winningScore = 0
winningAnswer = ""


answerOne = 0
answerTwo = 0
answerThree = 0

resultsList = google_results_count(query + " (\"" + answers[0] + "\"|\"" + answers[2] + "\"|\"" + answers[4] + "\")")

for item in resultsList:
	answerOne += item["htmlSnippet"].count(answers[0])
	answerTwo += item["htmlSnippet"].count(answers[2])
	answerThree += item["htmlSnippet"].count(answers[4])
	print(answers[0] + " SCORE: " + str(answerOne))
	print(answers[2] + " SCORE: " + str(answerTwo))
	print(answers[4] + " SCORE: " + str(answerThree))

	if answerOne > winningScore:
		winningScore = answerOne
		winningAnswer = "1"

	if answerTwo > winningScore:
		winningScore = answerTwo
		winningAnswer = "2"

	if answerThree > winningScore:
		winningScore = answerThree
		winningAnswer = "3"

	print("PICK THIS: " + winningAnswer)

if (answerOne + answerTwo + answerThree) < 10:
	print("confidence low, starting deep search")

	for item in resultsList:

		try:
			res = urllib.request.urlopen(item["link"])
			for line in res:
				output = line.decode('utf-8')
			# html = res.read()
				answerOne += output.count(answers[0])
				answerTwo += output.count(answers[1])
				answerThree += output.count(answers[2])
				print(answers[0] + " SCORE: " + str(answerOne))
				print(answers[1] + " SCORE: " + str(answerTwo))
				print(answers[2] + " SCORE: " + str(answerThree))
				if answerOne > winningScore:
					winningScore = answerOne
					winningAnswer = "1"

				if answerTwo > winningScore:
					winningScore = answerTwo
					winningAnswer = "2"

				if answerThree > winningScore:
					winningScore = answerThree
					winningAnswer = "3"

				print("PICK THIS: " + winningAnswer)
		except:
			pass
