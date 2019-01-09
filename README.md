# hack-a-thing-1-hqbot
hack-a-thing-1-hqbot created by GitHub Classroom

I built an OCR HQ Trivia Bot that parses a screenshot of of the HQ Trivia app, converts the image to a binary file, and google searches for the most related result. Initially, I am searching for the number of results that occur when you search based on the question statement and each answer individually. However, I also added googling for the question and then searching the returned results text description for occurrences of each answer. The returned results are then parsed, tabulated, and presented to the user in the terminal.

Additionally, I created an applescript that takes a screenshot of the screen, saves it under a particular filename, and opens up the terminal.

I had never used the google OCR tool before or tried to use google through their API, and was curious how accurate their image recognition was and how fast the results would return. I had discussed doing an OCR project for our CS98 project, so this was an apt hack-a-thing to get familiar with google's service.

The most difficult part of the problem was returning results quickly. Considering that HQ Trivia only gives you 10 seconds to answer a question, the image -> binary -> OCR recognition computation -> google search -> result tabulation must all occur as fast as possible. This made it difficult to use certain google advanced search features since it would slow down the response time. The most time intensive part was the image recognition, so I tried downgrading the image quality to make it a smaller file to upload and read for Google Cloud Services.

I would have additionally liked to add a feature that could pick the answer on the phone screen but was not able to figure out how to use a ios driver library.
