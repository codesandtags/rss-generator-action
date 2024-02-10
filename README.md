# RSS Generator Action

Custom Github Action to run the RSS generator.

## How to use it?

In your `workflow.yml` o Github actions YML file, include the `step`

```yaml
    - name: Run RSS Generator
      uses: codesandtags/rss-generator-action@main
```

Here is a full example:

```yaml
name: Generate RSS Feed
on: [push]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repo
      uses: actions/checkout@v4
    - name: Run RSS Generator
      uses: codesandtags/rss-generator-action@main
    
```
