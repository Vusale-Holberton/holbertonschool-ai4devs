## Task 1 - CRUD Endpoint
**Requirements**: Implement POST /users with validation.
**Inputs**: JSON {name, email}
**Outputs**: Stored user with ID
**Acceptance Criteria**:
- Returns 201 on success
- Returns 400 on invalid email

## Task 2 - Data Transformation
**Requirements**: Create a function to convert a list of transactions into a monthly summary.
**Inputs**: List of objects {date, amount, category}
**Outputs**: Object grouped by month with total spending
**Acceptance Criteria**:
- Correctly sums amounts for the same month
- Handles empty input lists without crashing

## Task 3 - UI Component
**Requirements**: Build a responsive React button component with loading state.
**Inputs**: Props {label, isLoading, onClick}
**Outputs**: Rendered HTML button
**Acceptance Criteria**:
- Button is disabled when isLoading is true
- Spinner is visible during loading state