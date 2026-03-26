# Feature Specification Generation Prompt
Create a single feature specification that is precise enough to support design and test planning.

## Focus
- Keep the artifact scoped to one feature with stable IDs and links to its stories.
- Describe the problem, requirements, dependencies, and scope.
- Keep implementation detail out unless it changes the requirement.
- Make it clear what belongs here versus the PRD or design docs.
- Leave real unknowns explicit instead of inventing detail.

## Completion Criteria
- The feature is scoped and testable.
- Requirements and story linkage are concrete.
- Open questions are clear.
