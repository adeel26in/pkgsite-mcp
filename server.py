from fastmcp import FastMCP
import httpx

mcp = FastMCP("pkgsite-mcp", version="0.1.0")

@mcp.tool
async def info_about_package(package_path: str):
    """ Get info about package at a path such as from GitHub or Gitlab etc."""
    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(f"https://pkg.go.dev/v1beta/package/{package_path}")
        if response.status_code != 200:
            return {"error": f"Failed to fetch package info: {response.status_code}"}
    return response.json()

@mcp.tool
async def info_about_module(module_path: str):
    """Get info about module at a path such as GitHub or Gitlab etc."""
    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(f"https://pkg.go.dev/v1beta/module/{module_path}")
        if response.status_code != 200:
            return {"error": f"Failed to fetch module info: {response.status_code}"}
    return response.json()

@mcp.tool
async def info_about_packages_at_module(module_path: str):
    """Get info about packages at a module path such as GitHub or Gitlab etc."""
    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(f"https://pkg.go.dev/v1beta/packages/{module_path}")
        if response.status_code != 200:
            return {"error": f"Failed to fetch packages info at module: {response.status_code}"}
        return response.json()

@mcp.tool
async def search_results(query: str):
    """Gets search results for a query."""
    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(f"https://pkg.go.dev/v1beta/search?q={query}")
        if response.status_code != 200:
            return {"error": f"Failed to fetch search results:{response.status_code}"}
    return response.json()

@mcp.tool
async def list_symbols_at_package_path(package_path: str):
    """Gets a list of symbols for a package"""
    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(f"https://pkg.go.dev/v1beta/symbols/{package_path}")
        if response.status_code != 200:
            return {"error": f"Failed to fetch symbols at a package path: {response.status_code}"}
    return response.json()

@mcp.tool
async def list_of_packages_importing(package_path: str):
    """Gets a list of packages importing a package"""
    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(f"https://pkg.go.dev/v1beta/imported-by/{package_path}")
        if response.status_code != 200:
            return {"error": f"Failed to fetch list of packages importing a package: {response.status_code}"}
    return response.json()

@mcp.tool
async def list_vulnerabilities(module_or_package_path: str):
    """Gets a list of vulnerabilities for a module or package"""
    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(f"https://pkg.go.dev/v1beta/vulns/{module_or_package_path}")
        if response.status_code != 200:
            return {"error": f"Failed to fetch list of vulnerabilities for a module or package: {response.status_code}"}
    return response.json()

if __name__ == "__main__":
    mcp.run()
