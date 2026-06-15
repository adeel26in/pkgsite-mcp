# pkgsite-mcp

A lightweight Model Context Protocol (MCP) server for querying Go module and package metadata using the official pkg.go.dev API. It provides structured tools for searching, inspecting, and analyzing Go modules, packages, symbols, dependencies, and vulnerabilities for AI agents and developer tooling.

* * *

## Overview

pkgsite-mcp wraps the official pkg.go.dev/v1beta API and exposes it as MCP tools, enabling structured programmatic access to Go ecosystem metadata. It replaces direct HTTP calls with reliable tool interfaces designed for agents and automation systems.

* * *

## Features

- Search Go packages across the Go ecosystem
- Retrieve full module and package metadata
- List exported and internal symbols (functions, structs, interfaces, constants, variables)
- Discover reverse dependencies (imported-by graph)
- Check security vulnerabilities in modules and packages
- List all packages contained within a module

All data is retrieved directly from the official pkg.go.dev API.

* * *

## Installation

### Clone the repository

```
git clone https://github.com/adeel26in/pkgsite-mcp.git
cd pkgsite-mcp
```

### Install dependencies

```
pip install fastmcp httpx
```

Or using uv:

```
uv pip install fastmcp httpx
```

* * *

## Usage

Start the MCP server:

```
python main.py
```

Once running, all tools are automatically registered with the MCP runtime.

* * *

## Using with MCP Clients

pkgsite-mcp works with MCP-compatible clients such as Claude Desktop, Cursor, and VS Code extensions that support MCP servers.

Start the server first:

```
python main.py
```

* * *

### Claude Desktop Setup

Add the MCP server configuration:

```
{
  "mcpServers": {
    "pkgsite-mcp": {
      "command": "python",
      "args": ["main.py"]
    }
  }
}
```

Restart Claude Desktop after saving.

* * *

### Cursor Setup

Cursor supports MCP servers natively in AI workflows.

```
{
  "mcpServers": {
    "pkgsite-mcp": {
      "command": "python",
      "args": ["main.py"]
    }
  }
}
```

Restart Cursor to enable tool discovery.

* * *

### VS Code Setup

VS Code can use MCP servers through compatible AI extensions or agent frameworks.

```
{
  "mcpServers": {
    "pkgsite-mcp": {
      "command": "python",
      "args": ["main.py"]
    }
  }
}
```

Restart VS Code after configuration.

* * *

## Available Tools

### Get package information

```
info_about_package(package_path: str)
```

Example:

```
info_about_package("github.com/google/go-cmp/cmp")
```

* * *

### Get module information

```
info_about_module(module_path: str)
```

* * *

### List packages in a module

```
info_about_packages_at_module(module_path: str)
```

* * *

### Search packages

```
search_results(query: str)
```

Examples:

```
uuid
json parser
http client
```

* * *

### List symbols in a package

```
list_symbols_at_package_path(package_path: str)
```

Includes functions, structs, interfaces, constants, variables.

* * *

### Reverse dependencies

```
list_of_packages_importing(package_path: str)
```

* * *

### Vulnerability lookup

```
list_vulnerabilities(module_or_package_path: str)
```

* * *

## API Reference

```
/v1beta/package/{path}
/v1beta/module/{path}
/v1beta/packages/{path}
/v1beta/search
/v1beta/symbols/{path}
/v1beta/imported-by/{path}
/v1beta/vulns/{path}
```

All requests use httpx with a 15-second timeout.

## Project Structure

```
server.py
MCP server with all tool definitions
```

* * *

## Requirements

- Python 3.9+
- fastmcp
- httpx

* * *

## Notes

- Uses asynchronous HTTP requests for performance
- Returns raw JSON responses from pkg.go.dev
- Failed requests return structured error dictionaries with status codes

* * *

## License

BSD-3-Clause
