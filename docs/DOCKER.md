# Docker Configuration

This project supports Docker containerization for consistent development and deployment environments.

## Prerequisites

- Docker
- Docker Compose

## Quick Start

1. Build the containers:
   ```bash
   docker-compose build
   ```

2. Run the tests:
   ```bash
   docker-compose run devto-automation pytest -v --cov=src tests/
   ```

3. Start the application:
   ```bash
   docker-compose up
   ```

## Configuration

### Environment Variables

Create a `.env` file in the root directory:
```ini
DEVTO_API_KEY=your_devto_api_key
DEVTO_USER_ID=your_devto_user_id
OPENAI_API_KEY=your_openai_api_key
PERPLEXITY_API_KEY=your_perplexity_api_key
REDIS_URL=redis://redis:6379/0
```

### Container Structure

- `/app` - Application root
  - `/app/src` - Source code
  - `/app/tests` - Test suite
  - `/app/data` - Data directories
    - `raw_content/` - Scraped content
    - `filtered_content/` - Processed content
    - `research/` - Research data
    - `drafts/` - Article drafts
    - `published/` - Published articles

## Services

### 1. devto-automation

Main application service:
- Python 3.11
- All dependencies from requirements.txt
- Volume mounted code for development
- Configured environment variables

### 2. redis

Supporting service:
- Redis for rate limiting and caching
- Persistent volume for data
- Exposed on port 6379

## Development Workflow

1. Start with mounted volumes:
   ```bash
   docker-compose up --build
   ```

2. Run tests:
   ```bash
   docker-compose run medium-automation pytest -v --cov=src tests/
   ```

3. Check logs:
   ```bash
   docker-compose logs -f
   ```

## Production Deployment

1. Build production image:
   ```bash
   docker-compose -f docker-compose.prod.yml build
   ```

2. Deploy:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

## Troubleshooting

### Common Issues

1. Redis Connection:
   - Verify Redis container: `docker ps`
   - Check Redis URL in .env
   - View Redis logs: `docker-compose logs redis`

2. Test Failures:
   - Check test logs: `docker-compose logs medium-automation`
   - Verify dependencies
   - Check file permissions

3. Volume Mounts:
   - Verify paths in docker-compose.yml
   - Check file ownership
   - Restart containers after changes

### Health Checks

Monitor service health:
```bash
docker-compose ps
docker-compose top
```

## Best Practices

1. Always use volume mounts in development
2. Keep production configuration separate
3. Use health checks for containers
4. Regularly update base images
5. Monitor container resources

## Security Notes

1. Never commit .env files
2. Use secrets management in production
3. Keep base images updated
4. Scan images for vulnerabilities
5. Use non-root users in containers