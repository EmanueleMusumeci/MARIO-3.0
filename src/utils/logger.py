"""Logging utilities for MARIO project."""

import logging
import sys
from pathlib import Path
from typing import Optional


def setup_logger(
    name: str,
    config
) -> logging.Logger:
    """
    Set up a logger with the specified configuration.

    Args:
        name: Logger name (usually __name__ of the module).
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
        log_format: Log message format string.
        log_file: Optional path to log file. If None, logs to console only.

    Returns:
        Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, config.logging.level.upper()))

    # Remove existing handlers to avoid duplicates
    logger.handlers.clear()

    # Create formatter
    formatter = logging.Formatter(config.logging.format)

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, config.logging.level.upper()))
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # TODO fare doppio livello per console e file
    # TODO trovare modo di usare questa setup_logger anche in tutti gli altri file che usano logging.getLogger

    # File handler (if specified)
    if config.logging.file is not None:
        log_file = Path(config.logging.file)
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(getattr(logging, config.logging.level.upper()))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
