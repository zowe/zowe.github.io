<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

[![Netlify Status](https://api.netlify.com/api/v1/badges/b4057863-5816-4a06-a503-f8989ec2062f/deploy-status)](https://app.netlify.com/sites/condescending-dubinsky-4645a9/deploys)
![License](https://img.shields.io/github/license/zowe/zowe.github.io)

# Welcome to Zowe website development

This GitHub repo is for management of the Zowe website. It uses [Github Pages](https://pages.github.com/) to automatically publish any commits to the master branch of the repo to https://zowe.org. GitHub Pages uses  [Jekyll](https://jekyllrb.com/) to publish this site from the content in your markdown files in this repo. For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

## Site organization

Most site updates can be made without changing the markdown files, but adjusting the [config settings](_config.yml). This includes doing new releases and changing the URLs to other resources.

The primary page content is in [index.md](index.md). The overall layout is in [_layouts/default.html](_layouts/default.html), and css and image files are in [assets](assets).

### Doing a new release

To do a new release, add a new entry at the top of [releases.yml](_data/releases.yml) right under the contents with this structure:

```yaml
- version: 1.4.0 # version number
  release_notes: https://zowe.github.io/docs-site/latest/getting-started/summaryofchanges.html#version-1-4-0-august-2019 # link to release notes
  release_date: 2019-08-09 # release date in YYYY-MM-DD format
  documentation: latest # path to docs ( minus the site url of https://docs.zowe.org )
```
### Add an announcement

To add an announcement, add an entry like below in [announcements.yml](_data/announcements.yml):

```yaml
- announcement: This is my announcement
  link: https://linktomyannouncementcalltoaction.org
```

## Submitting site updates

Any site updates can be submitted as a pull request. We recommmend you [create a fork](https://help.github.com/en/articles/fork-a-repo) of this repo and make changes there so you can preview them using GitHub Pages on your GitHub account. You can also develop locally with the following steps:
* [Set up Jekyll on your computer](https://jekyllrb.com/docs/installation/)
* Run `bundle install` to install the GitHub Pages gem
* Run `bundle exec jekyll serve` to host the site locally (at `http://localhost:4000`)

This repo aligns with the general [Zowe project role definitions](https://github.com/zowe/zlc/blob/master/process/roles.md) and [License and Copyright guidance] (https://github.com/zowe/zlc/blob/master/process/LicenseAndCopyrightGuidance.md)

## Governance

Committers to this repo are defined in the [COMMITTERS.csv](COMMITTERS.csv) file. You can request to the committers to become a committer after having successful commits to this repo. Committers are approved by an affirmative vote of the majority of committers.

# Questions and feedback

You can direct questions about the website to the Zowe ZLC [via email](https://lists.openmainframeproject.org/g/zowe-zlc) or on [Slack](https://slack.openmainframeproject.org).
