# Data Protection Design Generation

## Required Inputs
- `docs/helix/01-frame/compliance-requirements.md` - Compliance requirements
- `docs/helix/02-design/data-design.md` - Data model

## Produced Output
- `docs/helix/02-design/data-protection.md` - Data protection design

## Prompt

You are designing data protection controls. Your goal is to ensure data is protected throughout its lifecycle.

Design the following:

1. **Data Classification**
   | Level | Description | Examples | Controls |
   |-------|-------------|----------|----------|
   | Public | No restrictions | Marketing content | None |
   | Internal | Limited distribution | Documentation | Access control |
   | Confidential | Need-to-know | PII, financials | Encryption + access |
   | Restricted | Highest protection | Credentials, keys | Encryption + audit |

2. **Encryption Strategy**
   - At-rest encryption (database, files, backups)
   - In-transit encryption (TLS, mTLS)
   - Key management approach
   - Encryption algorithms

3. **Data Lifecycle**
   - Creation/collection
   - Processing
   - Storage
   - Sharing
   - Retention
   - Deletion

4. **Privacy Controls**
   - PII handling
   - Consent management
   - Data subject rights implementation
   - Anonymization/pseudonymization

Use the template at `workflows/helix/phases/02-design/artifacts/data-protection/template.md`.

## Completion Criteria
- [ ] All data types classified
- [ ] Encryption approach defined
- [ ] Lifecycle controls documented
- [ ] Privacy requirements addressed
