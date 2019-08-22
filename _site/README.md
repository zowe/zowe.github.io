<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

# Welcome to Zowe website development

This GitHub repo is for management of the Zowe website. It uses [Github Pages](https://pages.github.com/) to automatically publish any commits to the master branch of the repo to https://zowe.org. GitHub Pages uses  [Jekyll](https://jekyllrb.com/) to publish this site from the content in your markdown files in this repo. For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

## Site organization

Most site updates can be made without changing the markdown files, but adjusting the [config settings](_config.yml). This includes doing new releases and changing the URLs to other resources.

The primary page content is in [index.md](index.md). The overall layout is in [_layouts/default.html](_layouts/default.html), and css and image files are in [assets](assets)

## Submitting site updates

Any site updates can be submitted as a pull request. We recommmend you [create a fork](https://help.github.com/en/articles/fork-a-repo) of this repo and make changes there so you can preview them using GitHub Pages on your GitHub account. You can also develop locally by [setting up Jeykll on your computer](https://help.github.com/en/articles/setting-up-your-github-pages-site-locally-with-jekyll).

This repo aligns with the general [Zowe project role definitions](https://github.com/zowe/zlc/blob/master/process/roles.md) and [License and Copyright guideance](https://github.com/zowe/zlc/blob/master/process/LicenseAndCopyrightGuidance.md)

## Governance

Committers to this repo are defined in the [COMMITTERS.md](COMMITTERS.md) file. You can request to the committers to become a committer after having successful commits to this repo. Committers are approved by an affirmative vote of the majority of committers.

# Questions and feedback

You can direct questions about the website to the Zowe ZLC [via email](https://lists.openmainframeproject.org/g/zowe-zlc) or on [Slack](https://slack.openmainframeproject.org).
