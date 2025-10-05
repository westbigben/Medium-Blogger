# Contributing to Dev.to Automation Pipeline

Thank you for considering contributing to this project! This document outlines the guidelines for contributing to the Dev.to Automation Pipeline.

## Code of Conduct

This project adheres to a Code of Conduct. By participating, you are expected to uphold this code.

## Important Notice

This project is licensed under AGPL-3.0 with additional terms. Before contributing, please ensure you understand and agree to these terms:

1. All contributions will be licensed under AGPL-3.0
2. Commercial use requires explicit permission
3. All modifications must be documented
4. Network service providers must disclose use of this software

## How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Update documentation as needed
5. Add entry to CHANGES.md
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to your fork (`git push origin feature/amazing-feature`)
8. Create a Pull Request

## Development Guidelines

### Setting Up Development Environment

1. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Code Style

- Follow PEP 8
- Use type hints
- Document classes and functions
- Keep functions focused and small
- Write meaningful commit messages

### Testing

- Write unit tests for new features
- Maintain test coverage above 80%
- Run tests before submitting PR:
  ```bash
  pytest -v --cov=src tests/
  ```

### Documentation

- Update README.md if needed
- Document new features
- Add docstrings to functions
- Update CHANGES.md

## Pull Request Process

1. Update README.md with details of changes
2. Update CHANGES.md with your modifications
3. The PR template will guide you through required information
4. A maintainer will review your PR
5. Changes may be requested before merging

## Issue Reporting

1. Use issue templates when available
2. Provide detailed reproduction steps
3. Include relevant logs and screenshots
4. Mention your environment details

## License

By contributing, you agree that your contributions will be licensed under the project's AGPL-3.0 license with additional terms.

## Questions?

Feel free to create an issue for:
- Feature suggestions
- Bug reports
- Documentation improvements
- General questions

Thank you for contributing!