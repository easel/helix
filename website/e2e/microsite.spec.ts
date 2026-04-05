import { test, expect } from '@playwright/test'

test.describe('Homepage', () => {
  test('loads with hero and feature cards', async ({ page }) => {
    await test.step('navigate to homepage', async () => {
      await page.goto('/')
    })

    await test.step('verify hero content', async () => {
      await expect(page.getByText('Express intent once')).toBeVisible()
      await expect(page.getByText('Supervised autopilot')).toBeVisible()
    })

    await test.step('verify call-to-action buttons', async () => {
      await expect(page.getByRole('link', { name: 'Get Started' })).toBeVisible()
    })

    await test.step('verify feature cards', async () => {
      await expect(page.getByRole('heading', { name: 'Supervisory Autopilot' })).toBeVisible()
      await expect(page.getByRole('heading', { name: 'Tracker as Steering Wheel' })).toBeVisible()
      await expect(page.getByRole('heading', { name: 'Authority-Ordered Reconciliation' })).toBeVisible()
      await expect(page.getByRole('heading', { name: 'Cross-Model Verification' })).toBeVisible()
    })

    await test.step('capture full-page screenshot', async () => {
      await expect(page).toHaveScreenshot('homepage.png', { fullPage: true })
    })
  })
})

test.describe('Getting Started', () => {
  test('page loads with installation instructions', async ({ page }) => {
    await test.step('navigate to getting started', async () => {
      await page.goto('/docs/getting-started/')
    })

    await test.step('verify installation content', async () => {
      await expect(page.locator('article').getByText('helix run')).toBeVisible()
      await expect(page.locator('article').getByText('ddx init')).toBeVisible()
    })

    await test.step('verify tab content present', async () => {
      await expect(page.getByText('Plugin (recommended)')).toBeVisible()
    })

    await test.step('capture screenshot', async () => {
      await expect(page).toHaveScreenshot('getting-started.png', { fullPage: true })
    })
  })
})

test.describe('Workflow', () => {
  test('page explains phases and authority order', async ({ page }) => {
    await test.step('navigate to workflow', async () => {
      await page.goto('/docs/workflow/')
    })

    await test.step('verify phases content', async () => {
      await expect(page.getByRole('heading', { name: 'Workflow' })).toBeVisible()
      await expect(page.getByText('Frame')).toBeVisible()
      await expect(page.getByText('Design')).toBeVisible()
      await expect(page.getByText('Build')).toBeVisible()
    })

    await test.step('verify authority order', async () => {
      await expect(page.getByText('Authority Order')).toBeVisible()
    })

    await test.step('capture screenshot', async () => {
      await expect(page).toHaveScreenshot('workflow.png', { fullPage: true })
    })
  })
})

test.describe('CLI Reference', () => {
  test('page documents all commands', async ({ page }) => {
    await test.step('navigate to CLI reference', async () => {
      await page.goto('/docs/cli/')
    })

    await test.step('verify command documentation', async () => {
      await expect(page.getByRole('heading', { name: 'CLI Reference' })).toBeVisible()
      await expect(page.getByText('helix run')).toBeVisible()
      await expect(page.getByText('helix build')).toBeVisible()
    })

    await test.step('capture screenshot', async () => {
      await expect(page).toHaveScreenshot('cli-reference.png', { fullPage: true })
    })
  })
})

test.describe('Skills', () => {
  test('page lists all skills', async ({ page }) => {
    await test.step('navigate to skills', async () => {
      await page.goto('/docs/skills/')
    })

    await test.step('verify skills content', async () => {
      await expect(page.getByRole('heading', { name: 'Skills' })).toBeVisible()
    })

    await test.step('capture screenshot', async () => {
      await expect(page).toHaveScreenshot('skills.png', { fullPage: true })
    })
  })
})

test.describe('Glossary', () => {
  test('index page links to all sub-pages', async ({ page }) => {
    await test.step('navigate to glossary', async () => {
      await page.goto('/docs/glossary/')
    })

    await test.step('verify all category cards', async () => {
      await expect(page.getByRole('heading', { name: 'Glossary' })).toBeVisible()
      await expect(page.getByText('Phases')).toBeVisible()
      await expect(page.getByText('Artifacts')).toBeVisible()
      await expect(page.getByText('Actions')).toBeVisible()
      await expect(page.getByText('Concerns')).toBeVisible()
      await expect(page.getByText('Concepts')).toBeVisible()
      await expect(page.getByText('Tracker')).toBeVisible()
    })

    await test.step('capture screenshot', async () => {
      await expect(page).toHaveScreenshot('glossary.png', { fullPage: true })
    })
  })

  test('phases page covers all phases', async ({ page }) => {
    await test.step('navigate to phases', async () => {
      await page.goto('/docs/glossary/phases/')
    })

    await test.step('verify all phases present', async () => {
      await expect(page.getByText('Phase 0: Discover')).toBeVisible()
      await expect(page.getByText('Phase 1: Frame')).toBeVisible()
      await expect(page.getByText('Phase 2: Design')).toBeVisible()
      await expect(page.getByText('Phase 3: Test')).toBeVisible()
      await expect(page.getByText('Phase 4: Build')).toBeVisible()
      await expect(page.getByText('Phase 5: Deploy')).toBeVisible()
      await expect(page.getByText('Phase 6: Iterate')).toBeVisible()
    })
  })

  test('artifacts page covers all phases', async ({ page }) => {
    await test.step('navigate to artifacts', async () => {
      await page.goto('/docs/glossary/artifacts/')
    })

    await test.step('verify authority order and phase sections', async () => {
      await expect(page.getByText('Authority Order')).toBeVisible()
      await expect(page.getByText('Frame (Phase 1)')).toBeVisible()
      await expect(page.getByText('Design (Phase 2)')).toBeVisible()
    })
  })

  test('actions page documents all commands', async ({ page }) => {
    await test.step('navigate to actions', async () => {
      await page.goto('/docs/glossary/actions/')
    })

    await test.step('verify key actions', async () => {
      await expect(page.getByRole('heading', { name: 'build' })).toBeVisible()
      await expect(page.getByRole('heading', { name: 'check' })).toBeVisible()
      await expect(page.getByRole('heading', { name: 'run' })).toBeVisible()
      await expect(page.getByRole('heading', { name: 'frame' })).toBeVisible()
      await expect(page.getByRole('heading', { name: 'design' })).toBeVisible()
      await expect(page.getByRole('heading', { name: 'evolve' })).toBeVisible()
    })
  })

  test('concerns page lists the full library', async ({ page }) => {
    await test.step('navigate to concerns', async () => {
      await page.goto('/docs/glossary/concerns/')
    })

    await test.step('verify concern categories', async () => {
      await expect(page.getByText('Tech Stack Concerns')).toBeVisible()
      await expect(page.getByText('Quality Concerns')).toBeVisible()
      await expect(page.getByText('Infrastructure Concerns')).toBeVisible()
    })

    await test.step('verify key concerns listed', async () => {
      await expect(page.getByText('rust-cargo')).toBeVisible()
      await expect(page.getByText('typescript-bun')).toBeVisible()
      await expect(page.getByText('python-uv')).toBeVisible()
      await expect(page.getByText('security-owasp')).toBeVisible()
    })
  })

  test('concepts page covers core ideas', async ({ page }) => {
    await test.step('navigate to concepts', async () => {
      await page.goto('/docs/glossary/concepts/')
    })

    await test.step('verify key concepts', async () => {
      await expect(page.getByRole('heading', { name: 'Authority Order' })).toBeVisible()
      await expect(page.getByRole('heading', { name: 'Context Digest' })).toBeVisible()
      await expect(page.getByRole('heading', { name: 'Quality Ratchets' })).toBeVisible()
    })
  })

  test('tracker page documents beads and labels', async ({ page }) => {
    await test.step('navigate to tracker', async () => {
      await page.goto('/docs/glossary/tracker/')
    })

    await test.step('verify tracker content', async () => {
      await expect(page.getByText('ddx bead')).toBeVisible()
      await expect(page.getByText('Phase Labels')).toBeVisible()
      await expect(page.getByText('spec-id')).toBeVisible()
    })
  })
})

test.describe('Demos', () => {
  test('page shows all demo reels', async ({ page }) => {
    await test.step('navigate to demos', async () => {
      await page.goto('/docs/demos/')
    })

    await test.step('verify all demos listed', async () => {
      await expect(page.getByText('Quickstart: Full Lifecycle')).toBeVisible()
      await expect(page.getByText('Concerns: Preventing Technology Drift')).toBeVisible()
      await expect(page.getByText('Evolve: Threading Requirements Through the Stack')).toBeVisible()
    })

    await test.step('capture screenshot', async () => {
      await expect(page).toHaveScreenshot('demos.png', { fullPage: true })
    })
  })
})

test.describe('Navigation Workflows', () => {
  test('homepage → getting started → workflow', async ({ page }) => {
    await test.step('start at homepage', async () => {
      await page.goto('/')
    })

    await test.step('click Get Started', async () => {
      await page.getByRole('link', { name: 'Get Started' }).click()
      await expect(page).toHaveURL(/getting-started/)
    })

    await test.step('use next link to workflow', async () => {
      await page.getByRole('link', { name: 'Workflow' }).first().click()
      await expect(page).toHaveURL(/workflow/)
    })
  })

  test('top nav: glossary and demos', async ({ page }) => {
    await test.step('start at homepage', async () => {
      await page.goto('/')
    })

    await test.step('navigate to glossary via top nav', async () => {
      await page.getByRole('navigation').getByText('Glossary').click()
      await expect(page).toHaveURL(/glossary/)
    })

    await test.step('navigate to demos via top nav', async () => {
      await page.getByRole('navigation').getByText('Demos').click()
      await expect(page).toHaveURL(/demos/)
    })
  })

  test('glossary drill-down: index → phases → back', async ({ page }) => {
    await test.step('start at glossary index', async () => {
      await page.goto('/docs/glossary/')
    })

    await test.step('click into phases', async () => {
      await page.getByRole('link', { name: 'Phases' }).first().click()
      await expect(page).toHaveURL(/glossary\/phases/)
    })

    await test.step('verify phase content loaded', async () => {
      await expect(page.getByText('Phase 1: Frame')).toBeVisible()
    })
  })
})
