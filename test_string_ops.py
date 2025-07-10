import unittest

def reverse_sentence(s):
    return s[::-1]

def reverse_each_word(s):
    return ' '.join(word[::-1] for word in s.split())

def get_first_letter(s):
    return ' '.join(word[:1] for word in s.split())

def remove_first_letter(s):
    return ' '.join(word[1:] for word in s.split())

def get_last_letter(s):
    return ' '.join(word[-1:] for word in s.split())

def remove_last_letter(s):
    return ' '.join(word[:-1] for word in s.split())

class TestStringManipulations(unittest.TestCase):
    def setUp(self):
        self.input = "Hello World"

    def test_reverse_sentence(self):
        self.assertEqual(reverse_senten_
