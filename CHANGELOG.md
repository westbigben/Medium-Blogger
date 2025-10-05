# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-10-05

### Changed
- Migrated from Medium to Dev.to API integration
- Updated environment variables (MEDIUM_API_TOKEN → DEVTO_API_KEY)
- Modified publisher agent to use Dev.to API endpoints
- Updated all documentation to reflect Dev.to integration
- Improved rate limiting to match Dev.to API requirements

### Added
- Dev.to API authentication system
- Direct markdown support for article publishing
- Enhanced error handling for Dev.to API responses

### Removed
- Medium.com API integration
- Medium-specific article formatting

## [0.1.0] - 2025-10-04

### Added
- Initial public release
- Core agent framework
  - Base agent implementation
  - Web scraping agent
  - Content filtering agent
  - Research agent
  - Article writing agent
  - Dev.to publishing agent
- Utility modules
  - Configuration management
  - Monitoring and logging
  - Text processing
- Testing infrastructure
  - Unit tests
  - Test fixtures
  - Coverage reporting
- Docker support
  - Multi-stage build
  - Development configuration
  - Production configuration
- Documentation
  - Installation guide
  - Configuration guide
  - Development setup
  - Docker usage
  - Security policy
  - Code of conduct

### Security
- Rate limiting implementation
- Content validation system
- Browser security features
- Monitoring setup
- Secure configuration handling

[0.2.0]: https://github.com/westbigben/medium-automation/releases/tag/v0.2.0
[0.1.0]: https://github.com/westbigben/medium-automation/releases/tag/v0.1.0