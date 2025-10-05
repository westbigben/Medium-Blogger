"""
Web scraping agent for collecting content from various sources.
"""

import asyncio
from typing import Any, Dict, List
from pathlib import Path

from src.agents.base import BaseAgent
from src.utils.config import Config

class ScraperAgent(BaseAgent):
    """Agent for scraping content from configured sources."""

    def __init__(self, config: Dict[str, Any], data_dir: Path = None):
        """Initialize scraper agent.
        
        Args:
            config: Scraper configuration dictionary
            data_dir: Optional path to data directory
        """
        super().__init__(config, data_dir)
        self.sources = config.get('sources', [])
        self.max_articles = config.get('max_articles', 10)
        self.retry_attempts = config.get('retry_attempts', 3)

    async def scrape_devto(self) -> List[Dict[str, Any]]:
        """Scrape articles from Dev.to.
        
        Returns:
            List of article data dictionaries
        """
        self.logger.info("Scraping from Medium")
        # Implementation details removed for public version
        return []

    async def scrape_devto(self) -> List[Dict[str, Any]]:
        """Scrape articles from Dev.to.
        
        Returns:
            List of article data dictionaries
        """
        self.logger.info("Scraping from Dev.to")
        # Implementation details removed for public version
        return []

    async def save_raw_content(self, articles: List[Dict[str, Any]]):
        """Save raw scraped content.
        
        Args:
            articles: List of article data to save
        """
        for article in articles:
            filename = article['title'].lower().replace(' ', '_')
            self.save_data(article, filename, 'raw_content')

    async def process(self, input_data: Any = None) -> List[Dict[str, Any]]:
        """Process scraping of all configured sources.
        
        Args:
            input_data: Not used for scraper
            
        Returns:
            Combined list of articles from all sources
        """
        all_articles = []
        
        for source in self.sources:
            try:
                if source == 'medium':
                    articles = await self.scrape_medium()
                elif source == 'dev.to':
                    articles = await self.scrape_devto()
                else:
                    self.logger.warning(f"Unknown source: {source}")
                    continue
                    
                all_articles.extend(articles[:self.max_articles])
                await self.save_raw_content(articles[:self.max_articles])
                    
            except Exception as e:
                self.logger.error(f"Error scraping {source}: {str(e)}")
                
        return all_articles