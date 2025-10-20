# Random Generator

A flexible, data-driven Python tool for generating random combinations from JSON-defined categories. Perfect for game masters, writers, and anyone who needs creative inspiration through randomization.

## Overview

This tool reads JSON configuration files that define categories and items, then randomly selects from those items to generate unique combinations. It's designed to be completely customizable through JSON files without modifying the code.

## Features

- **Data-Driven Design**: All content is defined in external JSON files
- **Flexible Selection**: Support for picking multiple items from a single category
- **Custom Display Order**: Control the presentation order of results
- **Interactive Mode**: Generate multiple results in succession
- **Beautiful Output**: Formatted, easy-to-read results with proper labeling

## Requirements

- Python 3.x
- No external dependencies (uses only standard library)

## Installation

1. Clone or download the repository
2. Ensure `RandomChooser.py` is executable:
   ```bash
   chmod +x RandomChooser.py
   ```

## Usage

### Basic Usage

```bash
python RandomChooser.py <json_file>
```

### Examples

```bash
# Generate a fantasy adventure
python RandomChooser.py fantasy_adventure_json.json

# Create a character background
python RandomChooser.py fantasy_character_bg_json.json

# Pick tonight's board game
python RandomChooser.py boardgame_picker_json.json
```

### Interactive Mode

After generating results, press **Enter** to generate another set, or press **Ctrl+C** to quit.

## JSON Configuration Format

### Basic Structure

```json
{
  "title": "Your Generator Title",
  "description": "Brief description of what this generates",
  "allow_regenerate": true,
  "display_order": ["category1", "category2", "category3"],
  "categories": {
    "category_name": {
      "label": "Display Label",
      "pick_count": 1,
      "items": [
        "Item 1",
        "Item 2",
        "Item 3"
      ]
    }
  }
}
```

### Configuration Options

#### Top-Level Fields

- **title** (string): Main title displayed in output
- **description** (string): Optional description shown below title
- **allow_regenerate** (boolean): Enable/disable interactive regeneration mode
- **display_order** (array): List of category names in desired display order

#### Category Fields

- **label** (string): Human-readable name for the category
- **pick_count** (integer): Number of items to randomly select (default: 1)
- **items** (array): List of possible selections

### Example Categories

```json
"categories": {
  "difficulty": {
    "label": "Difficulty Level",
    "pick_count": 1,
    "items": [
      "Easy - Perfect for beginners",
      "Medium - Some challenge required",
      "Hard - Expert level only"
    ]
  },
  "mechanics": {
    "label": "Game Mechanics (2 will be chosen)",
    "pick_count": 2,
    "items": [
      "Dice Rolling",
      "Card Drafting",
      "Worker Placement"
    ]
  }
}
```

## Included Examples

### 1. Fantasy Adventure Generator
**File**: `fantasy_adventure_json.json`

Generates complete adventure frameworks for tabletop RPGs including:
- Master plot structures (based on 36 dramatic situations)
- Settings and themes
- Villains with motivations
- Plot twists and complications
- Key locations and rewards

### 2. Fantasy Character Background Generator
**File**: `fantasy_character_bg_json.json`

Creates detailed character backstories with:
- Race and origin
- Social background and childhood memories
- Defining moments and motivations
- Character flaws and secrets
- Important relationships and quirks
- Treasured possessions

### 3. Board Game Night Picker
**File**: `boardgame_picker_json.json`

Helps decide what game to play with:
- Game type and complexity
- Ideal player count
- Expected playtime
- Theme and mechanics
- Snack pairings!

## Creating Your Own Generators

1. Create a new JSON file following the format above
2. Define your categories and items
3. Set the display order
4. Run the tool with your custom file

### Tips for Good Generators

- **Use Descriptive Items**: Include context in item text (e.g., "Heavy - Complex rules, long playtime")
- **Balance Pick Counts**: Multiple picks work great for mechanics, tags, or traits
- **Order Matters**: Use `display_order` to tell a logical story
- **Keep It Focused**: 5-10 categories typically works best
- **Add Flavor**: Include descriptive text to make selections more evocative

## Output Format

```
======================================================================
                     Fantasy Adventure Generator                      
======================================================================

A high-level adventure creator for fantasy role-playing games

Master Plot (Based on 36 Dramatic Situations):
  Quest - Heroes seek a vital object, person, or place

Primary Setting:
  Ancient forest with sentient trees

Central Theme:
  Nature vs. civilization

...

======================================================================
```

## Use Cases

- **Game Masters**: Generate adventures, NPCs, and locations on the fly
- **Writers**: Overcome writer's block with random prompts
- **Game Designers**: Quick prototyping of game concepts
- **Decision Making**: Use for any situation requiring random selection
- **Creative Exercises**: Combine unexpected elements for inspiration

## Customization Ideas

Create generators for:
- Sci-fi scenarios
- Mystery plots
- Restaurant/meal suggestions
- Writing prompts
- Town/NPC generators
- Quest generators
- Magic item creators
- Business ideas
- Travel destinations
- Daily challenges

## Technical Details

### Code Structure

- `load_definition()`: Loads and validates JSON files
- `pick_random_items()`: Performs random selection based on pick_count
- `format_output()`: Creates formatted display output
- `main()`: Handles command-line interface and interactive loop

### Error Handling

- Missing files are reported with clear error messages
- Invalid JSON triggers helpful parsing errors
- Empty categories are safely skipped

## Contributing

To add new example generators:

1. Create a new JSON file following the schema
2. Test it thoroughly
3. Add documentation for the specific use case

## License

This tool is provided as-is for personal and commercial use.

## Credits

Inspired by the need for quick, customizable random generation in tabletop gaming and creative writing.

---

**Happy Generating!** 🎲