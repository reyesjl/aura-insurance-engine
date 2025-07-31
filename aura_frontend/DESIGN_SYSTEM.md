# AURA Insurance Engine - Design System

## Typography Hierarchy (Swiss Design Inspired)

### Main Titles

- **Classes**: `text-4xl md:text-5xl font-semibold leading-tight`
- **Usage**: Primary product titles, main page headers
- **Examples**: "AURA Intake", "AURA Bridge", "AURA Insight"

### Section Headers

- **Classes**: `text-2xl md:text-3xl font-medium`
- **Usage**: Secondary headers, section titles
- **Examples**: "Our Mission", "Select Type", "Questions Preview"

### Subtitles

- **Classes**: `text-lg italic opacity-80`
- **Usage**: Product descriptions, feature subtitles
- **Examples**: "Unified Multi-line Submission Intelligence", "Powered by MCP Servers"

### Body Text

- **Classes**: `text-xl leading-relaxed`
- **Usage**: Main content paragraphs, descriptions
- **Examples**: Main content sections, product descriptions

### Feature Titles

- **Classes**: `text-lg font-semibold`
- **Usage**: Feature headings, benefit titles
- **Examples**: "Seamless Portal Integration", "Context-Aware Matching"

### Feature Descriptions

- **Classes**: `text-base opacity-80 leading-relaxed`
- **Usage**: Feature descriptions, supporting text
- **Examples**: Feature explanations, secondary content

### Navigation Text

- **Classes**: `text-base hover:underline underline-offset-4 hover:underline-offset-6 transition-all`
- **Usage**: Navigation links, CTA links
- **Examples**: NavBar links, footer links

## Consistent Spacing

### Section Gaps

- **Mobile**: `gap-8`
- **Desktop**: `gap-16`
- **Usage**: Between main content sections

### Content Gaps

- **All Devices**: `gap-6`
- **Usage**: Between paragraphs and content blocks

### Grid Gaps

- **All Devices**: `gap-8`
- **Usage**: Between grid items (cards, features)

### Section Margins

- **All Devices**: `mb-12`
- **Usage**: Below section headers

## Button Styles

### Primary Buttons

- **Classes**: `px-6 py-3 bg-black text-white hover:bg-gray-700 duration-300 rounded-lg text-base font-semibold`
- **Usage**: Main CTAs, important actions

### Secondary Buttons

- **Classes**: `px-6 py-3 bg-gray-200 text-black hover:bg-black hover:text-white duration-300 rounded-lg text-base font-semibold`
- **Usage**: Secondary actions, alternative options

## Card Styles

### Standard Cards

- **Classes**: `p-8 rounded-lg duration-300`
- **Usage**: Information displays, content containers

### Interactive Cards

- **Classes**: `p-8 cursor-pointer hover:bg-black hover:text-white duration-300 rounded-lg`
- **Usage**: Clickable cards, navigation elements

## Color Palette

### Primary Colors

- **Black**: `#000000` - Primary text, buttons
- **White**: `#ffffff` - Background, contrast text
- **Beige**: `#eee7e3` - Section backgrounds

### Text Opacity

- **Primary Text**: `opacity-100` (default)
- **Secondary Text**: `opacity-80`
- **Tertiary Text**: `opacity-60`

## Responsive Design

### Breakpoints

- **Mobile**: Default (below 768px)
- **Desktop**: `md:` prefix (768px and above)

### Responsive Typography

- Use `md:` prefixes for larger desktop sizes
- Example: `text-4xl md:text-5xl`

### Responsive Spacing

- Use `md:` prefixes for desktop-specific spacing
- Example: `gap-8 md:gap-16`

## Implementation Guidelines

### 1. Always use the defined typography hierarchy

- Don't create custom font sizes outside the system
- Stick to the established classes for consistency

### 2. Maintain consistent spacing

- Use the defined gap and margin classes
- Avoid custom spacing that breaks the rhythm

### 3. Interactive elements

- Always include hover states and transitions
- Use `duration-300` for smooth transitions
- Maintain consistent underline behavior for links

### 4. Component consistency

- Apply the same patterns across all components
- Use consistent padding and margin values
- Maintain the same border-radius values

### 5. Accessibility

- Maintain proper contrast ratios
- Use semantic heading hierarchy
- Include proper focus states

## Examples of Proper Implementation

### Product Section

```vue
<Section mode="beige" padding="large">
  <div class="flex flex-col gap-8 md:gap-16 md:flex-row">
    <div class="w-full md:w-1/2">
      <div class="flex flex-col gap-4">
        <div class="text-4xl md:text-5xl font-semibold leading-tight">AURA Product</div>
        <div class="text-lg italic opacity-80">Product Subtitle</div>
      </div>
    </div>
    <div class="w-full md:w-1/2 flex flex-col gap-6">
      <div class="text-xl leading-relaxed">
        Product description content goes here.
      </div>
    </div>
  </div>
</Section>
```

### Feature Grid

```vue
<div class="grid md:grid-cols-2 gap-8 mt-12">
  <div class="flex flex-col gap-3">
    <div class="text-lg font-semibold">Feature Title</div>
    <div class="text-base opacity-80 leading-relaxed">
      Feature description goes here.
    </div>
  </div>
</div>
```

### Button Implementation

```vue
<button
  class="px-6 py-3 bg-black text-white hover:bg-gray-700 duration-300 rounded-lg text-base font-semibold"
>
  Primary Action
</button>
```

This design system ensures consistency, scalability, and maintainability across the entire AURA frontend application.
