"""
Configuration management utilities.
"""

import os
from pathlib import Path
from typing import Any, Dict
import yaml
from dotenv import load_dotenv

class Config:
    """Configuration manager."""
    
    def __init__(self, config_path: str = "config/config.yaml"):
        """Initialize configuration.
        
        Args:
            config_path: Path to configuration file
        """
        load_dotenv()  # Load environment variables
        
        with open(config_path) as f:
            self.config = yaml.safe_load(f)
            
        self._inject_env_vars()
        
    def _inject_env_vars(self):
        """Inject environment variables into configuration."""
        def replace_env_vars(obj: Any) -> Any:
            if isinstance(obj, dict):
                return {k: replace_env_vars(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [replace_env_vars(item) for item in obj]
            elif isinstance(obj, str) and obj.startswith("${") and obj.endswith("}"):
                env_var = obj[2:-1]
                return os.getenv(env_var)
            return obj
            
        self.config = replace_env_vars(self.config)
        
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value.
        
        Args:
            key: Configuration key
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        return self.config.get(key, default)
        
    def get_agent_config(self, agent_name: str) -> Dict[str, Any]:
        """Get agent-specific configuration.
        
        Args:
            agent_name: Name of agent
            
        Returns:
            Agent configuration dictionary
        """
        return self.config.get(agent_name, {})