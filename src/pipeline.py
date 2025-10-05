"""
Main orchestrator for the Dev.to Automation Pipeline.
"""

import asyncio
import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

from src.agents.scraper import ScraperAgent
from src.agents.filter import FilterAgent
from src.agents.research import ResearchAgent
from src.agents.writer import WriterAgent
from src.agents.publisher import PublisherAgent
from src.utils.config import Config
from src.utils.monitoring import setup_logging

class Pipeline:
    """Main pipeline orchestrator."""

    def __init__(self, config_path: str = "config/config.yaml", data_dir: Optional[Path] = None):
        """Initialize pipeline.
        
        Args:
            config_path: Path to configuration file
            data_dir: Optional path to data directory
        """
        self.config = Config(config_path)
        self.data_dir = data_dir or Path("data")
        setup_logging(self.config.get('log_level', 'INFO'))
        self.logger = logging.getLogger(__name__)
        
        # Initialize agents
        self.scraper = ScraperAgent(
            self.config.get_agent_config('scraper'),
            self.data_dir
        )
        self.filter = FilterAgent(
            self.config.get_agent_config('filter'),
            self.data_dir
        )
        self.researcher = ResearchAgent(
            self.config.get_agent_config('research'),
            self.data_dir
        )
        self.writer = WriterAgent(
            self.config.get_agent_config('writer'),
            self.data_dir
        )
        self.publisher = PublisherAgent(
            self.config.get_agent_config('publisher'),
            self.data_dir
        )

    async def run(self):
        """Execute complete pipeline."""
        try:
            # Step 1: Scrape content
            self.logger.info("Starting content scraping...")
            articles = await self.scraper.execute(None)
            
            if not articles:
                self.logger.warning("No articles found")
                return
                
            # Step 2: Filter content
            self.logger.info("Filtering content...")
            filtered_articles = await self.filter.execute(articles)
            
            if not filtered_articles:
                self.logger.warning("No articles passed filtering")
                return
                
            # Step 3: Research
            self.logger.info("Conducting research...")
            researched_articles = await self.researcher.execute(filtered_articles)
            
            # Step 4: Write articles
            self.logger.info("Writing articles...")
            written_articles = await self.writer.execute(researched_articles)
            
            # Step 5: Publish
            self.logger.info("Publishing articles...")
            published_articles = await self.publisher.execute(written_articles)
            
            self.logger.info(f"Pipeline completed. Published {len(published_articles)} articles.")
            
        except Exception as e:
            self.logger.error(f"Pipeline error: {str(e)}")
            raise

async def main():
    """Main entry point."""
    pipeline = Pipeline()
    await pipeline.run()

if __name__ == "__main__":
    asyncio.run(main())