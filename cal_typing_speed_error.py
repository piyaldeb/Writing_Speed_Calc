import tkinter
from time import *
import random as ran


def error(input, test):
    error1 = 0
    try:
        for i in range(len(test)):
            if (test[i] != input[i]):
                error1 = error1 + 1
    except:
        error1 = error1 + 1

    return error1


def speed(s, e, input):
    delay = (e - s)/60
    tans = round(delay, 2)
    speed = len(input) / tans
    return round(speed)


test = [
    "Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are designed to think and act like humans. These machines can perform tasks that typically require human-like intelligence, such as speech recognition, decision making, and language translation. AI is an interdisciplinary field that combines computer science, mathematics, psychology, and engineering. The development of AI technology has been revolutionizing various industries, including healthcare, finance, and education, among others. With AI, organizations can automate processes, improve efficiency, and enhance customer experience.",
    "There are various types of AI, including narrow or weak AI, general or strong AI, and super AI. Narrow AI is designed to perform specific tasks, such as image recognition or speech recognition. In contrast, general AI has the ability to perform any intellectual task that a human being can perform. Super AI refers to AI that surpasses human intelligence in multiple domains. This type of AI is still theoretical and has not been achieved yet.",
    "AI has numerous applications in various industries. In healthcare, AI is used to improve medical diagnoses and treatment planning. In finance, AI is used to detect fraud and manage investments. In education, AI is used to personalize learning experiences and provide real-time feedback to students. AI is also used in the criminal justice system to analyze data and assist in investigations. Additionally, AI is being used to improve urban planning and transportation systems, reduce energy consumption, and enhance weather forecasting accuracy.",
    "As AI continues to advance, there are growing concerns about its ethical implications. For example, there is a fear that AI will lead to job loss, as machines will be able to perform tasks that were previously done by humans. Additionally, AI raises questions about privacy, as machines have access to vast amounts of personal data. There are also concerns about AI being used for malicious purposes, such as cyber attacks or biased decision making. To address these ethical concerns, organizations must consider the impact of AI on society and establish ethical principles to guide its development and use.",
    "The future of AI is uncertain, but it is clear that the technology will continue to evolve and impact various industries. It is likely that AI will become more integrated into our daily lives, making tasks easier and more efficient. AI may also play a role in solving complex global problems, such as climate change and disease outbreaks. However, it is also important to consider the potential consequences of AI, such as job loss and privacy violations. To ensure that AI develops in a responsible and ethical manner, it is crucial to continue the conversation about its impact on society.",
    "In conclusion, Artificial Intelligence is a rapidly growing field that has the potential to revolutionize various industries. While AI has numerous benefits, there are also ethical concerns that must be addressed. As AI continues to advance, it is important to consider its impact on society and establish ethical principles to guide its development and use. The future of AI is uncertain, but it is clear that it will play a significant role in shaping our world."]
test1 = ran.choice(test)
print("write down the bellow paragraph")
print(test1)
print()
print()
print()
t1 = time()
input = input("Enter: ")
t2 = time()
print("Error:  ", error(input, test1))
print("Speed  ", speed(t1, t2, input) , "wpm")
