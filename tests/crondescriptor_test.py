# -*- coding: utf-8 -*-
"""Tests for crondescriptor."""

import unittest

from crondescriptor.crondescriptor import CronDescriptor
from crondescriptor.crondescriptor import Options


class CodeTest(unittest.TestCase):

    def testCron(self):
        descriptor = CronDescriptor()
        self.assertEqual("每分钟", descriptor.getDescription("* * * * *"))
        self.assertEqual("每分钟", descriptor.getDescription("*/1 * * * *"))
        self.assertEqual("每分钟", descriptor.getDescription("0 0/1 * * * ?"))
        self.assertEqual("每小时", descriptor.getDescription("0 0 * * * ?"))
        self.assertEqual("每小时", descriptor.getDescription("0 0 0/1 * * ?"))
        self.assertEqual("在 23:00, 星期一 到 星期五", descriptor.getDescription("0 23 ? * MON-FRI"))
        self.assertEqual("每秒", descriptor.getDescription("* * * * * *"))
        self.assertEqual("每 45 秒", descriptor.getDescription("*/45 * * * * *"))
        self.assertEqual("每 05 分钟", descriptor.getDescription("*/5 * * * *"))
        self.assertEqual("每 10 分钟", descriptor.getDescription("0 0/10 * * * ?"))
        self.assertEqual("每 05 分钟", descriptor.getDescription("0 */5 * * * *"))
        self.assertEqual("在 11:30, 星期一 到 星期五", descriptor.getDescription("30 11 * * 1-5"))
        self.assertEqual("在 11:30", descriptor.getDescription("30 11 * * *"))
        self.assertEqual("在 11:00 和 11:10 之间的每分钟", descriptor.getDescription("0-10 11 * * *"))
        self.assertEqual("每分钟, 仅在 三月", descriptor.getDescription("* * * 3 *"))
        self.assertEqual("每分钟, 仅在 三月 和 六月", descriptor.getDescription("* * * 3,6 *"))
        self.assertEqual("在 14:30 和 16:30", descriptor.getDescription("30 14,16 * * *"))
        self.assertEqual("在 06:30, 14:30 和 16:30", descriptor.getDescription("30 6,14,16 * * *"))
        self.assertEqual("在 09:46, 仅在 星期一", descriptor.getDescription("46 9 * * 1"))
        self.assertEqual("在 12:23, 每月的 15 号", descriptor.getDescription("23 12 15 * *"))
        self.assertEqual("在 12:23, 仅在 一月", descriptor.getDescription("23 12 * JAN *"))
        self.assertEqual("在 12:23, 仅在 一月", descriptor.getDescription("23 12 ? JAN *"))
        self.assertEqual("在 12:23, 一月 到 二月", descriptor.getDescription("23 12 * JAN-FEB *"))
        self.assertEqual("在 12:23, 一月 到 三月", descriptor.getDescription("23 12 * JAN-MAR *"))
        self.assertEqual("在 12:23, 仅在 星期日", descriptor.getDescription("23 12 * * SUN"))
        self.assertEqual("每 05 分钟, 在 15:00, 星期一 到 星期五", descriptor.getDescription("*/5 15 * * MON-FRI"))
        self.assertEqual("每分钟, 在 第三个星期一 每月", descriptor.getDescription("* * * * MON#3"))
        self.assertEqual("每分钟, 每月的最后一个 星期四 ", descriptor.getDescription("* * * * 4L"))
        self.assertEqual("每 05 分钟, 每月的最后一天, 仅在 一月", descriptor.getDescription("*/5 * L JAN *"))
        self.assertEqual("每分钟, 每月的最后一个平日", descriptor.getDescription("* * LW * *"))
        self.assertEqual("每分钟, 每月的最后一个平日", descriptor.getDescription("* * WL * *"))
        self.assertEqual("每分钟, 每月的 第一个平日 ", descriptor.getDescription("* * 1W * *"))
        self.assertEqual("每分钟, 每月的 第一个平日 ", descriptor.getDescription("* * W1 * *"))
        self.assertEqual("每分钟, 每月的 最接近 5 号的平日 ", descriptor.getDescription("* * 5W * *"))
        self.assertEqual("每分钟, 每月的 最接近 5 号的平日 ", descriptor.getDescription("* * W5 * *"))
        self.assertEqual("在 14:02:30", descriptor.getDescription("30 02 14 * * *"))
        self.assertEqual("在每分钟的 05 到 10 秒", descriptor.getDescription("5-10 * * * * *"))
        self.assertEqual("在每分钟的 05 到 10 秒, 在每小时的 30 到 35 分钟, 在 10:00 和 12:59 之间", descriptor.getDescription("5-10 30-35 10-12 * * *"))
        self.assertEqual("在每分钟的 30 秒, 每 05 分钟", descriptor.getDescription("30 */5 * * * *"))
        self.assertEqual("在每小时的 30 分, 在 10:00 和 13:59 之间, 仅在 星期三 和 星期五", descriptor.getDescription("0 30 10-13 ? * WED,FRI"))
        self.assertEqual("在每分钟的 10 秒, 每 05 分钟", descriptor.getDescription("10 0/5 * * * ?"))
        self.assertEqual("每 03 分钟, 在每小时的 02 到 59 分钟, 在 01:00, 09:00, 和 22:00, 在每月的 11 和 26 号之间, 一月 到 六月", descriptor.getDescription("2-59/3 1,9,22 11-26 1-6 ?"))
        self.assertEqual("在 06:00", descriptor.getDescription("0 0 6 1/1 * ?"))
        self.assertEqual("在每小时的 05 分", descriptor.getDescription("0 5 0/1 * * ?"))
        self.assertEqual("每秒, 仅在 2013", descriptor.getDescription("* * * * * * 2013"))
        self.assertEqual("每分钟, 仅在 2013 和 2014", descriptor.getDescription("* * * * * 2013,2014"))
        self.assertEqual("在 12:23, 一月 到 二月, 2013 到 2014", descriptor.getDescription("23 12 * JAN-FEB * 2013-2014"))
        self.assertEqual("在 12:23, 一月 到 三月, 2013 到 2015", descriptor.getDescription("23 12 * JAN-MAR * 2013-2015"))
        self.assertEqual("每 30 分钟, 在 08:00 和 09:59 之间, 每月的 5 和 20 号", descriptor.getDescription("0 0/30 8-9 5,20 * ?"))
        self.assertEqual("在 12:23, 在 第二个星期日 每月", descriptor.getDescription("23 12 * * SUN#2"))
        
        options = Options()
        options.dayOfWeekStartIndexZero = False
        self.assertEqual("在 12:23, 在 第二个星期日 每月", descriptor.getDescription("23 12 * * 1#2", options))
        self.assertEqual("在每小时的 25 分, 每 13 小时, 在 07:00 和 19:59 之间", descriptor.getDescription("0 25 7-19/13 ? * *"))
        self.assertEqual("在每小时的 25 分, 每 13 小时, 在 07:00 和 20:59 之间", descriptor.getDescription("0 25 7-20/13 ? * *"))


if __name__ == '__main__':
  unittest.main()
