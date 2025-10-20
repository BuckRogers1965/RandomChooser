#!/usr/bin/env python3
"""
Random Generator - A data-driven tool for generating random combinations
from JSON-defined categories and lists.
"""

import json
import random
import sys
from pathlib import Path


def load_definition(filepath):
    """Load and parse JSON definition file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in '{filepath}': {e}")
        sys.exit(1)


def pick_random_items(definition):
    """Generate random picks from all categories in the definition."""
    results = {}
    
    for category_name, category_data in definition.get('categories', {}).items():
        items = category_data.get('items', [])
        if not items:
            continue
            
        # Check if there's a custom pick count, default to 1
        pick_count = category_data.get('pick_count', 1)
        
        # Don't pick more items than available
        pick_count = min(pick_count, len(items))
        
        if pick_count == 1:
            results[category_name] = random.choice(items)
        else:
            results[category_name] = random.sample(items, pick_count)
    
    return results


def format_output(definition, results):
    """Format the results for display."""
    title = definition.get('title', 'Random Generation Results')
    description = definition.get('description', '')
    
    output = []
    output.append("=" * 70)
    output.append(title.center(70))
    output.append("=" * 70)
    
    if description:
        output.append(f"\n{description}\n")
    
    # Get display order if specified, otherwise use dictionary order
    category_order = definition.get('display_order', list(results.keys()))
    
    for category_name in category_order:
        if category_name not in results:
            continue
            
        # Get the display label from the definition
        category_data = definition['categories'].get(category_name, {})
        label = category_data.get('label', category_name.replace('_', ' ').title())
        
        result = results[category_name]
        
        output.append(f"\n{label}:")
        
        if isinstance(result, list):
            for item in result:
                output.append(f"  • {item}")
        else:
            output.append(f"  {result}")
    
    output.append("\n" + "=" * 70)
    
    return "\n".join(output)


def main():
    """Main program entry point."""
    if len(sys.argv) < 2:
        print("Usage: python random_generator.py <json_file>")
        print("\nExample: python random_generator.py fantasy_adventure.json")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    # Load the definition
    definition = load_definition(filepath)
    
    # Generate random picks
    results = pick_random_items(definition)
    
    # Display results
    print(format_output(definition, results))
    
    # Optional: Support multiple generations with a prompt
    if definition.get('allow_regenerate', True):
        print("\nPress Enter to generate another, or Ctrl+C to quit...")
        try:
            while True:
                input()
                results = pick_random_items(definition)
                print("\n" + format_output(definition, results))
                print("\nPress Enter to generate another, or Ctrl+C to quit...")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")


if __name__ == "__main__":
    main()
