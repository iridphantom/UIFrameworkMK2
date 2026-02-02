import datetime
import unittest
import HTMLTestRunner_cn

from pathlib import Path
from utils.get_logger import get_logger

if __name__ == '__main__':
    """
        ===== 1.初始化日志 =====
    """
    logger = get_logger()
    logger.info("=== 测试运行开始 ===")


    """
        ===== 2.配置测试报告 =====
    """
    report_dir = Path(__file__).parent / 'reports'  # 获取当前脚本所在目录，并构建 reports 子目录的路径。
    report_dir.mkdir(parents=True, exist_ok=True)  # 创建目录，exist_ok=True 表示如果目录已存在也不会报错
    report_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-3]  # 生成带毫秒的时间戳字符串。使用切片 [:-3] 截取字符串，保留到毫秒级别
    report_filename = report_dir / f"{report_time}_report.html"  # 构建完整的报告文件路径
    logger.info(f"报告保存路径: {report_filename}")

    print(f"report_dir: {report_dir}")  # report_dir: D:\Project\Python\UIFrameworkMK2\reports
    print(f"report_dir的数据类型为：{type(report_dir)}")   # report_dir的数据类型为：<class 'pathlib.WindowsPath'>，注意数据类型，可能要强转。
    print(f"report_time: {report_time}")    # report_time: 20260131_163941_131
    print(f"report_filename: {report_filename}")    # report_filename: D:\Project\Python\UIFrameworkMK2\reports\20260131_163941_131_report.html


    """
        ===== 3.发现测试用例 =====
    """
    suite = unittest.TestSuite() # 相当于创建了一个空的list
    # 基于discover添加测试用例：
    test_dir = Path(__file__).parent / 'testcases'  # D:\Project\Python\UIFrameworkMK2\testcases
    discover = unittest.defaultTestLoader.discover(
        start_dir=str(test_dir),
        pattern='test_*.py',
        top_level_dir=str(Path(__file__).parent)
    )
    logger.info(f"发现测试套件: {discover.countTestCases()} 个用例")


    """
        ===== 4.运行测试套件 =====
    """
    try:
        # 使用HTMLTestRunner运行测试
        # 测试报告生成
        current_date = datetime.datetime.now().strftime('%Y-%m-%d') # 获取当前日期：2026-02-02
        with open(report_filename, 'wb') as report_file:
            runner = HTMLTestRunner_cn.HTMLTestRunner(
                stream=report_file,
                verbosity=2,    # 显示详细执行结果
                title=f'UI自动化测试报告 ({current_date})',
                description='基于unittest + DDT + YAML关键字驱动框架'
            )
            runner.run(discover)  # 直接运行discover（它已是TestSuite对象）

        logger.info("✓ 测试执行完成，报告已生成")
        logger.info(f"▶ 报告路径: {report_filename}")
    except FileNotFoundError as e:
        logger.error(f"报告目录创建失败：{e}")
    except Exception as e:
        logger.error(f"测试执行异常: {e}", exc_info=True)  # exc_info=True 记录完整堆栈
        raise
    finally:
        logger.info("=== 测试运行结束 ===")