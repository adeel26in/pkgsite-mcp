# pkgsite-mcp

A lightweight Model Context Protocol (MCP) server for querying Go module and package metadata using the official pkg.go.dev API. It provides structured tools for searching, inspecting, and analyzing Go modules, packages, symbols, dependencies, and vulnerabilities for AI agents and developer tooling.

## Overview

pkgsite-mcp wraps the official pkg.go.dev/v1beta API and exposes it as MCP tools, enabling structured programmatic access to Go ecosystem metadata. It replaces direct HTTP calls with reliable tool interfaces designed for agents and automation systems.

## Features

- Search Go packages across the Go ecosystem
- Retrieve full module and package metadata
- List exported and internal symbols (functions, structs, interfaces, constants, variables)
- Discover reverse dependencies (imported-by graph)
- Check security vulnerabilities in modules and packages
- List all packages contained within a module

All data is retrieved directly from the official pkg.go.dev API.

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

## Usage

Start the MCP server:

```
python main.py
```

Once running, all tools are automatically registered with the MCP runtime.

## Available Tools

### Get package information

```
info_about_package(package_path: str)
```

Returns metadata for a Go package.

```
info_about_package("github.com/google/go-cmp/cmp")
```

### Get module information

```
info_about_module(module_path: str)
```

Returns metadata about a Go module.

### List packages in a module

```
info_about_packages_at_module(module_path: str)
```

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

### List symbols in a package

```
list_symbols_at_package_path(package_path: str)
```

Includes functions, structs, interfaces, constants, and variables.

### Reverse dependencies

```
list_of_packages_importing(package_path: str)
```

### Vulnerability lookup

```
list_vulnerabilities(module_or_package_path: str)
```

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

All requests are executed using httpx with a 15-second timeout.

## Project Structure

```
main.py
MCP server with all tool definitions
```

## Requirements

- Python 3.9+
- fastmcp
- httpx

## Notes

- Uses asynchronous HTTP requests for performance
- Returns raw JSON responses from pkg.go.dev
- Failed requests return structured error dictionaries with status codes

## License

BSD-3-Clause
