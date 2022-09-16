""" TODO create a test case to test the following functions,

generate_url_for_question
 - check that the expected URL is returned for an example question. 

extract_answer_from_response
 - one test should create some example dictionaries that match the expected response from the API,
 and check that the correct answer is extracted and returned.
 - another test should create example dictionaries with a different structure to the one returned from the API, 
 and check that the function returns None. 

 TODO to think about - what else could you test about this program? 
 What types of expected and unexpected behavior might happen? You may be able to write tests for some 
 of your ideas now. We'll talk about ways to test other aspects of this program in class.

"""
import functions_magic
from unittest import TestCase


class TestMagic8Ball(TestCase):
    def test_generate_url_for_question(self):
        actual_url = functions_magic.generate_url_for_question(
            "Did the cat drag it in?"
        )
        expected_url = f"https://8ball.delegator.com/magic/JSON/Did the cat drag it in?"
        self.assertEqual(expected_url, actual_url)

    def test_extract_valid_answer_response(self):
        sample = {
            "magic": {
                "question": "Do I have toothpaste on my sweater?",
                "answer": "Signs point to yes",
                "type": "Affirmative",
            }
        }
        expected_answer = "Signs point to yes"
        actual_answer = functions_magic.extract_answer_from_response(sample)
        self.assertEqual(actual_answer, expected_answer)
