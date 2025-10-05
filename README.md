# Dev.to Article Automation Pipeline

An intelligent pipeline using specialized agents to automate Dev.to article creation.

## Features

- **Web Scraping Agent**: Collects content and ideas from various sources
- **Content Filter Agent**: Analyzes and filters content for relevance
- **Research Agent**: Conducts in-depth research using Perplexity API
- **Article Writer Agent**: Creates well-structured article drafts
- **Dev.to Publisher Agent**: Posts drafts to Dev.to platform

## Project Structure

```
devto-automation/
├── src/
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── scraper.py      # Web scraping agent
│   │   ├── filter.py       # Content filtering agent
│   │   ├── research.py     # Research agent
│   │   ├── writer.py       # Article writing agent
│   │   └── publisher.py    # Dev.to publishing agent
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py       # Configuration utilities
│   │   ├── monitoring.py   # Monitoring and logging
│   │   └── text.py        # Text processing utilities
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── fixtures/
│   │   └── conftest.py     # Test fixtures
│   ├── unit/
│   │   ├── test_scraper.py
│   │   ├── test_filter.py
│   │   ├── test_research.py
│   │   ├── test_writer.py
│   │   └── test_publisher.py
│   └── integration/
│       └── test_pipeline.py
├── config/
│   └── config.example.yaml # Example configuration
├── docs/
│   └── CONTRIBUTING.md    # Contribution guidelines
├── .env.example          # Example environment variables
├── .gitignore           # Git ignore file
├── LICENSE              # AGPL-3.0 License
├── README.md            # This file
└── requirements.txt     # Python dependencies
```

## Requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`
- API keys for:
  - Dev.to API
  - OpenAI GPT-4
  - Perplexity API
  - LinkedIn API (optional)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/westbigben/devto-automation.git
   cd devto-automation
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Copy example configuration:
   ```bash
   cp config/config.example.yaml config/config.yaml
   cp .env.example .env
   ```

5. Edit configuration files with your API keys and preferences.

## Configuration

1. Set up API keys in `.env`:
   ```ini
   DEVTO_API_KEY=your_devto_api_key
   DEVTO_USER_ID=your_devto_user_id
   OPENAI_API_KEY=your_openai_api_key
   PERPLEXITY_API_KEY=your_perplexity_api_key
   LINKEDIN_API_KEY=your_linkedin_api_key
   ```

2. Configure `config/config.yaml` with your preferences:
   - Scraping sources
   - Content filters
   - Writing style
   - Publishing preferences

## Development

1. Setup development environment:
   ```bash
   pip install -r requirements.txt
   ```

2. Run tests:
   ```bash
   pytest -v --cov=src tests/
   ```

3. Check code style:
   ```bash
   black .
   isort .
   pylint src/ tests/
   ```

## Contributing

Please read [CONTRIBUTING.md](docs/CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the GNU Affero General Public License v3.0 with additional terms - see the [LICENSE](LICENSE) file for details.

### Key License Points:

1. You must preserve copyright notices and share modifications under the same license
2. Network service providers must disclose use of this software
3. Commercial use requires explicit permission
4. All modifications must be documented
5. Full license terms are in the LICENSE file

## Support

- Create an issue for bug reports
- Start a discussion for feature requests
- Check documentation for common issues

## Author

Nitin S Bharadwaj (@westbigben)