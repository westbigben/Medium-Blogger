"""
Base Agent class providing common functionality for all agents.
"""

from abc import ABC, abstractmethod
from pathlib import Path
import asyncio
import json
import logging
from typing import Any, Dict, List, Optional

from src.utils.config import Config
from src.utils.monitoring import monitor

class BaseAgent(ABC):
    """Base class for all agents in the pipeline."""

    def __init__(self, config: Dict[str, Any], data_dir: Optional[Path] = None):
        """Initialize base agent with configuration.
        
        Args:
            config: Agent-specific configuration dictionary
            data_dir: Optional path to data directory
        """
        self.config = config
        self.data_dir = data_dir or Path("data")
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    async def process(self, input_data: Any) -> Any:
        """Process input data and return results.
        
        Args:
            input_data: Input data to process
            
        Returns:
            Processed data
        """
        pass

    async def rate_limit(self):
        """Implement rate limiting."""
        await asyncio.sleep(1)  # Default 1 request per second

    def save_data(self, data: Any, filename: str, subdir: str):
        """Save data to JSON file.
        
        Args:
            data: Data to save
            filename: Name of file
            subdir: Subdirectory under data_dir
        """
        save_path = self.data_dir / subdir
        save_path.mkdir(parents=True, exist_ok=True)
        
        file_path = save_path / f"{filename}.json"
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)

    def load_data(self, filename: str, subdir: str) -> Any:
        """Load data from JSON file.
        
        Args:
            filename: Name of file
            subdir: Subdirectory under data_dir
            
        Returns:
            Loaded data
        """
        file_path = self.data_dir / subdir / f"{filename}.json"
        with open(file_path) as f:
            return json.load(f)

    @monitor
    async def execute(self, input_data: Any) -> Any:
        """Execute agent processing with monitoring.
        
        Args:
            input_data: Input data to process
            
        Returns:
            Processed data
        """
        try:
            await self.rate_limit()
            return await self.process(input_data)
        except Exception as e:
            self.logger.error(f"Error in {self.__class__.__name__}: {str(e)}")
            raise