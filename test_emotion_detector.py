from EmotionDetection.emotion_detection import emotion_detector 
import unittest

class TestEmotionDetector(unittest.TestCase): 
  def test_sentiment_analyzer(self):
    result_1 = emotion_detector('I love working with Python') 
    self.assertEqual(result_1['label'], 'SENT_POSITIVE') 
    
    result_2 = emotion_detector('I hate working with Python') 
    self.assertEqual(result_2['label'], 'SENT_NEGATIVE') 
     
    result_3 = emotion_detector('I am neutral on Python') 
    self.assertEqual(result_3['label'], 'SENT_NEUTRAL')

unittest.main()
