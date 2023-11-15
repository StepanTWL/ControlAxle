from unittest import TestCase, main

from main import FindAxle


class control_axle_test(TestCase):
	def test_0001(self):  # single
		data = f"SYS1(1:100µs; 0:1100µs; 1:1600µs); SYS2(1:500µs; 0:1500µs; 1:1600µs)"
		count_axle = 1
		count_sys1 = 1
		count_sys2 = 1
		find_axle = FindAxle()
		find_axle.work_find_axle(data)
		self.assertEqual(find_axle.get_count_axle(), count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys2)
		find_axle.reset()
		find_axle.work_find_axle(data.replace('SYS1', 'SYS3').replace('SYS2', 'SYS1').replace('SYS3', 'SYS2'))
		self.assertEqual(find_axle.get_count_axle(), -count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys2)
		self.assertEqual(find_axle.get_count_sys2(), count_sys1)

	def test_0002(self):  # 380+620+400 single
		data = f"SYS1(1:120µs; 0:1120µs; 1:1600µs); SYS2(1:500µs; 0:1520µs; 1:1600µs)"
		count_axle = 0
		count_sys1 = 1
		count_sys2 = 1
		find_axle = FindAxle()
		find_axle.work_find_axle(data)
		self.assertEqual(find_axle.get_count_axle(), count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys2)
		find_axle.reset()
		find_axle.work_find_axle(data.replace('SYS1', 'SYS3').replace('SYS2', 'SYS1').replace('SYS3', 'SYS2'))
		self.assertEqual(find_axle.get_count_axle(), -count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys2)
		self.assertEqual(find_axle.get_count_sys2(), count_sys1)

	def test_0003(self):  # 420+580+420 single
		data = f"SYS1(1:100µs; 0:1100µs; 1:1600µs); SYS2(1:520µs; 0:1520µs; 1:1600µs)"
		count_axle = 0
		count_sys1 = 1
		count_sys2 = 1
		find_axle = FindAxle()
		find_axle.work_find_axle(data)
		self.assertEqual(find_axle.get_count_axle(), count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys2)
		find_axle.reset()
		find_axle.work_find_axle(data.replace('SYS1', 'SYS3').replace('SYS2', 'SYS1').replace('SYS3', 'SYS2'))
		self.assertEqual(find_axle.get_count_axle(), -count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys2)
		self.assertEqual(find_axle.get_count_sys2(), count_sys1)

	def test_0004(self):  # 400+620+380 single
		data = f"SYS1(1:100µs; 0:1120µs; 1:1600µs); SYS2(1:500µs; 0:1500µs; 1:1600µs)"
		count_axle = 0
		count_sys1 = 1
		count_sys2 = 1
		find_axle = FindAxle()
		find_axle.work_find_axle(data)
		self.assertEqual(find_axle.get_count_axle(), count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys2)
		find_axle.reset()
		find_axle.work_find_axle(data.replace('SYS1', 'SYS3').replace('SYS2', 'SYS1').replace('SYS3', 'SYS2'))
		self.assertEqual(find_axle.get_count_axle(), -count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys2)
		self.assertEqual(find_axle.get_count_sys2(), count_sys1)

	def test_0005(self): # 380+600+400 single
		data = f"SYS1(1:120µs; 0:1100µs; 1:1600µs); SYS2(1:500µs; 0:1500µs; 1:1600µs)"
		count_axle = 0
		count_sys1 = 0
		count_sys2 = 1
		find_axle = FindAxle()
		find_axle.work_find_axle(data)
		self.assertEqual(find_axle.get_count_axle(), count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys2)
		find_axle.reset()
		find_axle.work_find_axle(data.replace('SYS1', 'SYS3').replace('SYS2', 'SYS1').replace('SYS3', 'SYS2'))
		self.assertEqual(find_axle.get_count_axle(), -count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys2)
		self.assertEqual(find_axle.get_count_sys2(), count_sys1)

	def test_0006(self): # 400+600+380 single
		data = f"SYS1(1:100µs; 0:1100µs; 1:1600µs); SYS2(1:500µs; 0:1480µs; 1:1600µs)"
		count_axle = 0
		count_sys1 = 1
		count_sys2 = 0
		find_axle = FindAxle()
		find_axle.work_find_axle(data)
		self.assertEqual(find_axle.get_count_axle(), count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys2)
		find_axle.reset()
		find_axle.work_find_axle(data.replace('SYS1', 'SYS3').replace('SYS2', 'SYS1').replace('SYS3', 'SYS2'))
		self.assertEqual(find_axle.get_count_axle(), -count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys2)
		self.assertEqual(find_axle.get_count_sys2(), count_sys1)

	def test_0007(self): # 400+580+400 single
		data = f"SYS1(1:100µs; 0:1100µs; 1:1600µs); SYS2(1:520µs; 0:1520µs; 1:1600µs)"
		count_axle = 0
		count_sys1 = 1
		count_sys2 = 1
		find_axle = FindAxle()
		find_axle.work_find_axle(data)
		self.assertEqual(find_axle.get_count_axle(), count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys2)
		find_axle.reset()
		find_axle.work_find_axle(data.replace('SYS1', 'SYS3').replace('SYS2', 'SYS1').replace('SYS3', 'SYS2'))
		self.assertEqual(find_axle.get_count_axle(), -count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys2)
		self.assertEqual(find_axle.get_count_sys2(), count_sys1)

	def test_0008(self): # 400+600+400 single
		data = f"SYS1(1:100µs; 0:1100µs; 1:1600µs); SYS2(1:500µs; 0:1500µs; 1:1600µs)"
		count_axle = 1
		count_sys1 = 1
		count_sys2 = 1
		find_axle = FindAxle()
		find_axle.work_find_axle(data)
		self.assertEqual(find_axle.get_count_axle(), count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys2)
		find_axle.reset()
		find_axle.work_find_axle(data.replace('SYS1', 'SYS3').replace('SYS2', 'SYS1').replace('SYS3', 'SYS2'))
		self.assertEqual(find_axle.get_count_axle(), -count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys2)
		self.assertEqual(find_axle.get_count_sys2(), count_sys1)

	def test_0009(self): # dual
		data = f"SYS1(1:100µs; 0:1100µs; 1:1200µs; 0:2200µs; 1:2700µs); SYS2(1:500µs; 0:2600µs; 1:2700µs)"
		count_axle = 1
		count_sys1 = 2
		count_sys2 = 1
		find_axle = FindAxle()
		find_axle.work_find_axle(data)
		self.assertEqual(find_axle.get_count_axle(), count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys2)
		find_axle.reset()
		find_axle.work_find_axle(data.replace('SYS1', 'SYS3').replace('SYS2', 'SYS1').replace('SYS3', 'SYS2'))
		self.assertEqual(find_axle.get_count_axle(), -count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys2)
		self.assertEqual(find_axle.get_count_sys2(), count_sys1)

	def test_0010(self): # dual
		data = f"SYS1(1:100µs; 0:1100µs; 1:1200µs; 0:2200µs; 1:2700µs); SYS2(1:500µs; 0:2500µs; 1:2700µs)"
		count_axle = 0
		count_sys1 = 2
		count_sys2 = 1
		find_axle = FindAxle()
		find_axle.work_find_axle(data)
		self.assertEqual(find_axle.get_count_axle(), count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys2)
		find_axle.reset()
		find_axle.work_find_axle(data.replace('SYS1', 'SYS3').replace('SYS2', 'SYS1').replace('SYS3', 'SYS2'))
		self.assertEqual(find_axle.get_count_axle(), -count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys2)
		self.assertEqual(find_axle.get_count_sys2(), count_sys1)

	def test_0011(self): # dual
		data = f"SYS1(1:100µs; 0:1100µs; 1:1200µs; 0:2200µs; 1:2700µs); SYS2(1:500µs; 0:1600µs; 1:2700µs)"
		count_axle = 0
		count_sys1 = 2
		count_sys2 = 1
		find_axle = FindAxle()
		find_axle.work_find_axle(data)
		self.assertEqual(find_axle.get_count_axle(), count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys2)
		find_axle.reset()
		find_axle.work_find_axle(data.replace('SYS1', 'SYS3').replace('SYS2', 'SYS1').replace('SYS3', 'SYS2'))
		self.assertEqual(find_axle.get_count_axle(), -count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys2)
		self.assertEqual(find_axle.get_count_sys2(), count_sys1)

	def test_0012(self): # dual
		data = f"SYS1(1:100µs; 0:1100µs; 1:1600µs; 0:2600µs; 1:3100µs); SYS2(1:500µs; 0:3000µs; 1:3100µs)"
		count_axle = 1
		count_sys1 = 2
		count_sys2 = 1
		find_axle = FindAxle()
		find_axle.work_find_axle(data)
		self.assertEqual(find_axle.get_count_axle(), count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys2)
		find_axle.reset()
		find_axle.work_find_axle(data.replace('SYS1', 'SYS3').replace('SYS2', 'SYS1').replace('SYS3', 'SYS2'))
		self.assertEqual(find_axle.get_count_axle(), -count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys2)
		self.assertEqual(find_axle.get_count_sys2(), count_sys1)

	def test_0013(self): # dual
		data = f"SYS1(1:100µs; 0:1100µs; 1:1600µs; 0:2600µs; 1:3100µs); SYS2(1:500µs; 0:1500µs; 1:3100µs)"
		count_axle = 1
		count_sys1 = 2
		count_sys2 = 1
		find_axle = FindAxle()
		find_axle.work_find_axle(data)
		self.assertEqual(find_axle.get_count_axle(), count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys2)
		find_axle.reset()
		find_axle.work_find_axle(data.replace('SYS1', 'SYS3').replace('SYS2', 'SYS1').replace('SYS3', 'SYS2'))
		self.assertEqual(find_axle.get_count_axle(), -count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys2)
		self.assertEqual(find_axle.get_count_sys2(), count_sys1)

	def test_0014(self): # two part
		data = f"SYS1(1:1000µs; 0:1600µs); SYS2(1:1400µs; 0:1600µs)"
		data_1 = f"SYS1(0:400µs; 1:1600µs); SYS2(0:800µs; 1:1600µs)"
		count_axle = 0
		count_sys1 = 0
		count_sys2 = 0
		count_axle_1 = 1
		count_sys1_1 = 1
		count_sys2_1 = 1
		find_axle = FindAxle()
		find_axle.work_find_axle(data)
		self.assertEqual(find_axle.get_count_axle(), count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys2)
		find_axle.work_find_axle(data_1)
		self.assertEqual(find_axle.get_count_axle(), count_axle_1)
		self.assertEqual(find_axle.get_count_sys1(), count_sys1_1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys2_1)
		find_axle.reset()
		find_axle.work_find_axle(data.replace('SYS1', 'SYS3').replace('SYS2', 'SYS1').replace('SYS3', 'SYS2'))
		self.assertEqual(find_axle.get_count_axle(), count_axle)
		self.assertEqual(find_axle.get_count_sys1(), count_sys2)
		self.assertEqual(find_axle.get_count_sys2(), count_sys1)
		find_axle.work_find_axle(data_1.replace('SYS1', 'SYS3').replace('SYS2', 'SYS1').replace('SYS3', 'SYS2'))
		self.assertEqual(find_axle.get_count_axle(), -count_axle_1)
		self.assertEqual(find_axle.get_count_sys1(), count_sys2_1)
		self.assertEqual(find_axle.get_count_sys2(), count_sys1_1)



	"""
	def test_0010(self):  #
		tmp = f"SYS1(1:100µs; 0:1100µs; 1:1300µs; 0:2300µs; 1:2600µs; 0:3600µs; 1:4100µs); SYS2(1:500µs; 0:4000µs; 1:4100µs)"
		find_axle = FindAxle()
		find_axle.work_find_axle(tmp)
		self.assertEqual(find_axle.get_count_axle(), 1)
		self.assertEqual(find_axle.get_count_sys1(), 3)
		self.assertEqual(find_axle.get_count_sys2(), 1)

	def test_0011(self):  #
		tmp = f"SYS2(1:100µs; 0:1100µs; 1:1300µs; 0:2300µs; 1:2600µs; 0:3600µs; 1:4100µs); SYS1(1:500µs; 0:4000µs; 1:4100µs)"
		find_axle = FindAxle()
		find_axle.work_find_axle(tmp)
		self.assertEqual(find_axle.get_count_axle(), -1)
		self.assertEqual(find_axle.get_count_sys1(), 1)
		self.assertEqual(find_axle.get_count_sys2(), 3)

	def test_0012(self):  #
		tmp = f"SYS1(1:100µs; 0:1100µs; 1:1300µs; 0:2300µs; 1:2600µs; 0:3600µs; 1:4100µs); SYS2(1:500µs; 0:3200µs; 1:4100µs)"
		find_axle = FindAxle()
		find_axle.work_find_axle(tmp)
		self.assertEqual(find_axle.get_count_axle(), 0)
		self.assertEqual(find_axle.get_count_sys1(), 3)
		self.assertEqual(find_axle.get_count_sys2(), 1)

	def test_0013(self):  #
		tmp = f"SYS2(1:100µs; 0:1100µs; 1:1300µs; 0:2300µs; 1:2600µs; 0:3600µs; 1:4100µs); SYS1(1:500µs; 0:3200µs; 1:4100µs)"
		find_axle = FindAxle()
		find_axle.work_find_axle(tmp)
		self.assertEqual(find_axle.get_count_axle(), 0)
		self.assertEqual(find_axle.get_count_sys1(), 1)
		self.assertEqual(find_axle.get_count_sys2(), 3)
	"""

if __name__ == '__main__':
	main()
