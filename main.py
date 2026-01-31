import datetime
import os
import unittest
import HTMLTestRunner_cn

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
    report_dir = os.path.join(os.path.dirname(__file__), 'reports')
    os.makedirs(report_dir, exist_ok=True)  # 递归创建目录（比mkdir更安全）
    report_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-3]  # 截取到毫秒
    report_filename = os.path.join(report_dir, f"{report_time}_report.html")  # 使用os.path.join安全拼接
    logger.info(f"报告保存路径: {report_filename}")

    print(f"report_dir: {report_dir}")  # report_dir: D:\Project\Python\UIFrameworkMK2\reports
    print(f"report_time: {report_time}")    # report_time: 20260131_163941_131
    print(f"report_filename: {report_filename}")    # report_filename: D:\Project\Python\UIFrameworkMK2\reports\20260131_163941_131_report.html


    """
        ===== 3.发现测试用例 =====
    """
    suite = unittest.TestSuite() # 相当于创建了一个空的list
    # 基于discover添加测试用例：
    test_dir = os.path.join(os.path.dirname(__file__), 'testcases')  # D:\Project\Python\UIFrameworkMK2\testcases
    """
        os.path.dirname(__file__)：获取当前脚本所在的目录路径；
        'testcases'：指定子目录名称；
        os.path.join()：将当前脚本目录与子目录名拼接成完整路径
    """
    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='test_*.py',
        top_level_dir=os.path.dirname(__file__)  # 显式指定顶层目录，避免导入问题
    )
    logger.info(f"发现测试套件: {discover.countTestCases()} 个用例")


    """
        ===== 4.运行测试套件 =====
    """
    try:
        # 使用HTMLTestRunner运行测试
        with open(report_filename, 'wb') as report_file:
            runner = HTMLTestRunner_cn.HTMLTestRunner(
                stream=report_file,
                verbosity=2,
                title='UI自动化测试报告',
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