from EmotionDetection.emotion_detection import emotion_detector 
import unittest

class TestEmotionDetector(unittest.TestCase): 
  def test_sentiment_analyzer(self):
    result_1 = emotion_detector('I love working with Python') 
    self.assertEqual(['dominant_emotion'], 'joy')
    
    result_2 = emotion_detector('I hate working with Python') 
    self.assertEqual(['dominant_emotion'], 'joy')
     
    result_3 = emotion_detector('I am neutral on Python') 
    self.assertEqual(['dominant_emotion'], 'joy')

if __name__ == '__main__':
    unittest.main()
