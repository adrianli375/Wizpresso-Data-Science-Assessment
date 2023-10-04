import requests
import unittest


class TestTableStructureRecognition(unittest.TestCase):
    def test_01(self):
        payload = {'image_path': 'img/TestCase01_Tencent.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['26'], 2)

    def test_02(self):
        payload = {'image_path': 'img/TestCase02_Tesla.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['16'], 1)

    def test_03(self):
        payload = {'image_path': 'img/TestCase03_NVIDIA.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['8'], 3)

    def test_04(self):
        payload = {'image_path': 'img/TestCase04_Prudential.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['3'], 1)

    def test_05(self):
        payload = {'image_path': 'img/TestCase05_Wharf.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['11'], 4)

    def test_06(self):
        payload = {'image_path': 'img/TestCase06_PCCW.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['16'], 0)

    def test_07(self):
        payload = {'image_path': 'img/TestCase07_HKEX3322.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['7'], 2)

    def test_08(self):
        payload = {'image_path': 'img/TestCase08_HKEX1405.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['18'], 2)

    def test_09(self):
        payload = {'image_path': 'img/TestCase09_HKEX1955.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['15'], 4)

    def test_10(self):
        payload = {'image_path': 'img/TestCase10_HKEX251.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['11'], 5)

    def test_11(self):
        payload = {'image_path': 'img/TestCase11_HKEX1396.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['30'], 5)

    def test_12(self):
        payload = {'image_path': 'img/TestCase12_HKEX1753.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['6'], 1)

    def test_13(self):
        payload = {'image_path': 'img/TestCase13_HKEX1231.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['6'], 3)

    def test_14(self):
        payload = {'image_path': 'img/TestCase14_HKEX1820.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['14'], 5)

    def test_15(self):
        payload = {'image_path': 'img/TestCase15_HKEX1782.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['15'], 4)

    def test_16(self):
        payload = {'image_path': 'img/TestCase16_HKEX1775.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['0'], 2)

    def test_17(self):
        payload = {'image_path': 'img/TestCase17_HKEX69.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['19'], 2)

    def test_18(self):
        payload = {'image_path': 'img/TestCase18_HKEX1848.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['12'], 3)

    def test_19(self):
        payload = {'image_path': 'img/TestCase19_HKEX270.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['1'], 4)

    def test_20(self):
        payload = {'image_path': 'img/TestCase20_HKEX320.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['24'], 5)

    def test_21(self):
        payload = {'image_path': 'img/TestCase21_HKEX1119.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['3'], 2)

    def test_22(self):
        payload = {'image_path': 'img/TestCase22_HKEX694.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['10'], 5)

    def test_23(self):
        payload = {'image_path': 'img/TestCase23_HKEX607.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['7'], 1)

    def test_24(self):
        payload = {'image_path': 'img/TestCase24_HKEX144.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['6'], 2)

    def test_25(self):
        payload = {'image_path': 'img/TestCase25_HKEX6823.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['15'], 1)

    def test_26(self):
        payload = {'image_path': 'img/TestCase26_HKEX518.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['18'], 4)

    def test_27(self):
        payload = {'image_path': 'img/TestCase27_HKEX2177.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['9'], 1)

    def test_28(self):
        payload = {'image_path': 'img/TestCase28_HKEX2878.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['7'], 5)

    def test_29(self):
        payload = {'image_path': 'img/TestCase29_HKEX1593.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['1'], 1)

    def test_30(self):
        payload = {'image_path': 'img/TestCase30_HKEX1580.jpg'}
        response = requests.post('http://127.0.0.1:8815/process-table-structure', json=payload).json()
        self.assertEqual(response['labels']['15'], 1)


if __name__ == '__main__':
    unittest.main()

