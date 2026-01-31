"""
    获取logging的logger对象
"""
import logging
import os
import time
from configparser import ConfigParser


def get_logger():
    """初始化并返回配置好的logger"""
    # 1. 获取项目根目录（conf的上一级目录）
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 2. 读取配置文件
    config = ConfigParser(interpolation=None)  # 👉 核心修复：禁用 %(...) 插值
    config_path = os.path.join(project_root, 'utils', 'log_conf.ini')
    config.read(config_path, encoding='utf-8')

    # 3. 生成日志目录路径（相对于项目根目录）
    log_dir = os.path.join(project_root, config.get('log', 'log_dir'))
    os.makedirs(log_dir, exist_ok=True)

    # 4. 生成当前日期格式的文件名
    log_date = time.strftime('%Y-%m-%d', time.localtime())
    log_file = os.path.join(log_dir, config.get('handler_file', 'filename').replace('{date}', log_date))

    # 5. 配置logger
    logger = logging.getLogger(__name__)
    logger.setLevel(config.get('logger_root', 'level'))

    # 6. 配置控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(config.get('handler_console', 'level'))
    console_handler.setFormatter(
        logging.Formatter(
            config.get('formatter_default', 'format'),
            datefmt=config.get('formatter_default', 'datefmt')
        )
    )

    # 7. 配置文件处理器
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(config.get('handler_file', 'level'))
    file_handler.setFormatter(
        logging.Formatter(
            config.get('formatter_default', 'format'),
            datefmt=config.get('formatter_default', 'datefmt')
        )
    )

    # 8. 添加处理器到logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger