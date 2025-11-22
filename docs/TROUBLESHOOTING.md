# Troubleshooting Guide

## Common Issues

### 1. SSL Certificate Warnings
**Issue**: Browser shows a security warning when accessing `https://branchloans.com`.
**Fix**: This is expected because we are using a self-signed certificate. You can safely proceed by clicking "Advanced" -> "Proceed to branchloans.com (unsafe)".

### 2. Domain Not Found
**Issue**: Browser cannot find `branchloans.com`.
**Fix**: Ensure you have added the domain to your hosts file:
- **Windows**: `C:\Windows\System32\drivers\etc\hosts`
- **Linux/Mac**: `/etc/hosts`
Add the line: `127.0.0.1 branchloans.com`

### 3. Database Connection Failed
**Issue**: API logs show "OperationalError: could not connect to server".
**Fix**:
- Check if the database container is healthy: `docker ps`
- Ensure the `backend` network is correctly defined in `docker-compose.yml`.
- Check logs: `docker-compose logs db`

### 4. Permission Denied in Docker
**Issue**: "permission denied" errors when running the container.
**Fix**: This might happen due to the non-root user setup. Ensure the `appuser` has permissions to write to necessary directories (though the Dockerfile handles this for `/app`).

## Verification Steps
1. **Check Containers**: `docker-compose ps` should show `api`, `db`, and `nginx` as "Up".
2. **Check Logs**: `docker-compose logs -f` to see real-time logs.
3. **Health Check**: Visit `https://branchloans.com/health`.
