import requests
import unittest


class TestTableStructureRecognition(unittest.TestCase):
    def test_1(self):
        payload = {'image_path': 'img/TestCase1_Tencent.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['26'], 2)

    def test_2(self):
        payload = {'image_path': 'img/TestCase2_Tesla.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['16'], 1)

    def test_3(self):
        payload = {'image_path': 'img/TestCase3_NVIDIA.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['8'], 3)


if __name__ == '__main__':
    unittest.main()
