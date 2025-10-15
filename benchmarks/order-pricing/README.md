# Order Pricing System - BDD Benchmark

E-commerce order pricing system with multiple promotion strategies, developed using strict Behavior-Driven Development methodology.

## Features

- **Threshold Discount**: Apply fixed discount when order reaches minimum amount
- **Buy-One-Get-One (BOGO)**: Add free item for cosmetics category purchases
- **Double Eleven Promotion**: 20% off per 10 items of same product
- **Multiple Promotions Stacking**: Support combining all promotions simultaneously

## Tech Stack

- **Language**: Python 3.11
- **BDD Framework**: Behave
- **Code Formatter**: Black (line-length=79)

## Project Structure

```markdown
order-pricing/
├── src/
│   └── order/
│       ├── entities/          # Domain entities
│       │   ├── product.py
│       │   ├── order_item.py
│       │   └── order.py
│       └── service/           # Business logic
│           └── order_service.py
├── features/                  # BDD feature files
│   ├── order.feature
│   ├── double_eleven.feature
│   ├── environment.py
│   └── steps/
│       └── order_steps.py
├── tasks/                     # Requirements & design docs
│   ├── BDD.prompt
│   ├── order.feature
│   ├── double_eleven.feature
│   ├── ERD.png
│   └── OOD.png
└── tests results/
    └── pretty.output
```

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
behave --no-capture

# Run specific feature
behave features/order.feature --no-capture
behave features/double_eleven.feature --no-capture

# Format code
black src/ features/
```

## Test Coverage

- **2 features**: order.feature, double_eleven.feature
- **10 scenarios**: All promotion combinations covered
- **42 test steps**: All passing
- **Test Duration**: ~0.002s

## BDD Development Process

This benchmark strictly follows Red-Green-Refactor cycle:

1. **Red Phase**: Write step definitions and empty implementations, confirm test fails with value errors (not framework errors)
2. **Green Phase**: Implement minimal code to pass tests, verify all tests pass
3. **Refactor Phase**: Improve code structure while keeping tests green

Each scenario was developed one at a time with all others marked as `@skip`.

## Design

Refer to `tasks/ERD.png` and `tasks/OOD.png` for entity relationships and object-oriented design.

### Promotion Logic

All promotion logic is encapsulated in `OrderService`:

- `_apply_threshold_discount()`: Threshold-based discount
- `_apply_bogo_promotion()`: Buy-one-get-one logic
- `_apply_double_eleven_discount()`: Bulk purchase discount

Promotions are applied independently and can be stacked.
