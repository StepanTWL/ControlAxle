from unittest import TestCase, main

from main import FindAxle


class control_axle_test(TestCase):
	def test_0001(self):  #
		tmp = f"SYS1(1:660µs; 0:2780µs; 1:4000µs); SYS2(1:1480µs; 0:3400µs; 1:4000µs)"
		find_axle = FindAxle()
		find_axle.work_find_axle(tmp)
		self.assertEqual(find_axle.get_count_axle(), 1)
		self.assertEqual(find_axle.get_count_sys1(), 1)
		self.assertEqual(find_axle.get_count_sys2(), 1)

	def test_0002(self):  #
		tmp = f"SYS1(1:4100µs; 0:6400µs; 1:7700µs; 0:9900µs; 1:12100µs; 0:13600µs; 1:20000µs); SYS2(1:5100µs; 0:14400µs; 1:20000µs)"
		find_axle = FindAxle()
		find_axle.work_find_axle(tmp)
		self.assertEqual(find_axle.get_count_axle(), 1)
		self.assertEqual(find_axle.get_count_sys1(), 3)
		self.assertEqual(find_axle.get_count_sys2(), 1)

	def test_0003(self):  #
		tmp = f"SYS1(1:4100µs; 0:6400µs; 1:7700µs; 0:9900µs; 1:12100µs; 0:13600µs; 1:20000µs); SYS2(1:5100µs; 0:13000µs; 1:20000µs)"
		find_axle = FindAxle()
		find_axle.work_find_axle(tmp)
		self.assertEqual(find_axle.get_count_axle(), 0)
		self.assertEqual(find_axle.get_count_sys1(), 3)
		self.assertEqual(find_axle.get_count_sys2(), 1)

	def test_0004(self):  #
		tmp = f"SYS1(1:4100µs; 0:6400µs; 1:7900µs; 0:9500µs; 1:10600µs; 0:11900µs; 1:12800µs; 0:15000µs; 1:20000µs); SYS2(1:5200µs; 0:14000µs; 1:20000µs)"
		find_axle = FindAxle()
		find_axle.work_find_axle(tmp)
		self.assertEqual(find_axle.get_count_axle(), 1)
		self.assertEqual(find_axle.get_count_sys1(), 1)
		self.assertEqual(find_axle.get_count_sys2(), 1)


if __name__ == '__main__':
	main()
