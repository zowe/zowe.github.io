---
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<style>
  #menu-community a.nav-link {
    background-color: #eeeeee;
    background-color: #eeeeee;
    color: black !important;
  }

  #menu-community.nav-item {
    background-color: #eeeeee;
  }
</style>

<section class="whitebackground">
    <h1 id="download" style="margin-bottom: 1.5rem">Interested in joining or reaching out to the Zowe community?</h1>
    <p>Find out how we collaborate, where we share knowledge, and how best to engage with us!</p>
    <div class="card-deck">
        <div class="card mb-3 animated-tile">
            <div class="card-body">
                <div class="d-flex align-items-baseline">
                    <h5 class="text-left"><a href="{{ site.slack_url }}">Slack</a></h5>
                    <img class="ml-2" style="height: 20px" src="assets/img/slack-community.svg">
                </div>
                <p class="card-text">Hosted by the Open Mainframe Project, this is a messaging board where you can
                    directly engage with Zowe users and contributors. Ask questions, engage in discussions, and contribute your ideas!</p>
                <p>Some popular channels to get started:
                <ul>
                    <li><a href="{{ site.zowe_onboarding_slack_url }}">#zowe-onboarding</a></li>
                    <li><a href="{{ site.zowe_user_slack_url }}">#zowe-help</a></li>
                    <li><a href="{{ site.zowe_cli_slack_url }}">#zowe-cli</a></li>
                    <li><a href="{{ site.zowe_explorer_slack_url }}">#zowe-explorer-vscode</a></li>
                    <li><a href="{{ site.apiml_slack_url }}">#zowe-api</a></li>
                    <li><a href="{{ site.zowe_doc_slack_url }}">#zowe-doc</a></li>
                </ul>
                </p>
            </div>
        </div>
        <div class="card mb-3 animated-tile">
            <div class="card-body">
                <div class="d-flex align-items-baseline">
                    <h5 class="text-left"><a href="{{ site.omp_calendar_url }}">Meetings</a></h5>
                    <img class="ml-2" style="height: 20px" src="assets/img/calendar-community.svg">
                </div>
                <p class="card-text">All scheduled meetings in the Zowe community can be found in the Open Mainframe
                    Project Calendar. Meetings can range from the scrum status of a squad to meetings of the Technical Steering Committee
                    and the Zowe Advisory Council. </p>
                <p>You are welcome to drop in and contribute to any of these meetings. Check out the detailed
                    introduction to squad meetings and other recurring meetings. </p>
            </div>
        </div>
        <div class="card mb-3 animated-tile">
            <div class="card-body">
                <div class="d-flex align-items-baseline">
                    <h5 class="text-left"><a href="{{ site.github_repo_url }}">GitHub</a></h5>
                    <img class="ml-2" style="height: 20px" src="assets/img/github-community.svg">
                </div>
                <p class="card-text">This is where all of the Zowe code is located, and where you can find detailed information
                    about each Zowe project and how to collaborate and contribute. This is the place to open issues, give
                    feedback, and contribute code.</p>
                <p>Some good repos to get started:
                <ul>
                    <li><a href="{{ site.zowe_community_repo_url }}">community</a></li>
                    <li><a href="{{ site.zowe_docs_repo_url }}">docs-site</a></li>
                </ul>
                </p>
            </div>
        </div>
    </div>
    <div class="card-deck">
        <div class="card mb-3 animated-tile">
            <div class="card-body">
                <div class="d-flex align-items-baseline">
                    <h5 class="text-left"><a href="https://medium.com/zowe">Articles</a></h5>
                    <img class="ml-2" style="height: 20px" src="assets/img/medium.png">
                </div>
                <p class="card-text">Visit <a href="https://medium.com/zowe">medium.com/zowe</a></p>
            </div>
        </div>
        <div class="card mb-3 animated-tile">
            <div class="card-body">
                <div class="d-flex align-items-baseline">
                    <h5 class="text-left"><a href="https://www.youtube.com/playlist?list=PL8REpLGaY9QHtnElqPosteBFpITStkAxo">Videos</a></h5>
                    <img class="ml-2" style="height: 20px" src="assets/img/video.png">
                </div>
                <p class="card-text">Visit <a href="https://www.youtube.com/playlist?list=PL8REpLGaY9QHtnElqPosteBFpITStkAxo">Zowe Youtube Channel</a></p>
            </div>
        </div>
    </div>
    <div>
        <h2 style="margin-bottom: 1.5rem; margin-top: 2%">Join a squad call</h2>
        <p>Zowe is an open source project. This means that anyone can contribute to any part of it, and that can include
            you! The best ways to first get involved are <a href="{{ site.create_zowe_issue_url }}">opening issues on
                GitHub</a>, saying hi on Slack, or joining the weekly calls of one of the squads listed below.</p>
        <p>Zowe’s most frequent and dedicated contributors work in teams called “squads.” If you have specific questions
            or are excited about a particular part of Zowe, connect with the relevant squad using the table below.
            Occasionally, some of the meetings might be changed, cancelled, or rescheduled. Stay up to date on meetings
            in the <a href="{{ site.omp_calendar_url }}">Zowe meeting calendar</a> or the Slack channels.</p>
        <iframe class="mt-4" src="https://zoom-lfx.platform.linuxfoundation.org/meetings/zowe" style="border: 0"
                width="100%" height="600" frameborder="0" scrolling="no"></iframe>
    </div>
    <div>
        <h2 style="margin-bottom: 1.5rem; margin-top: 2%">Find products and services that integrate with Zowe</h2>
        <p>Vendors and consumers publish extensions and participate in <a href="https://openmainframeproject.org/our-projects/zowe-conformance-program/">Open Mainframe Project's Zowe Vx
            Conformance Program</a> to ensure they are interoperable with the specific Zowe Vx Version. All are free to download and use. Find participating, conformant extensions below. Click the card to view conformance statistics. See a list of products and solutions that have achieved V2 and V3 conformance in the <a href="https://omp.landscape2.io/embed/embed.html?base-path=&classify=category&key=zowe-conformant&headers=true&category-header=false&category-in-subcategory=false&title-uppercase=false&title-alignment=left&title-font-family=sans-serif&title-font-size=13&style=shadowed&bg-color=%230033a1&fg-color=%23ffffff&item-modal=false&item-name=true&size=md&items-alignment=left&item-name-font-size=11" target="_blank">V2 and V3 Conformant Landscape</a> view presented below (use the slide on the right of the page to advance the card view).</p>
        <iframe src="https://omp.landscape2.io/embed/embed.html?base-path=&classify=category&key=zowe-conformant&headers=true&category-header=false&category-in-subcategory=false&title-uppercase=false&title-alignment=left&title-font-family=sans-serif&title-font-size=13&style=shadowed&bg-color=%230033a1&fg-color=%23ffffff&item-modal=false&item-name=true&size=md&items-alignment=left&item-name-font-size=11" style="width:100%;display:block;border:none;" height="600"></iframe>
    </div>
    <div>
        <h2 style="margin-bottom: 1.5rem; margin-top: 2%">Find Zowe support providers</h2>
        <p>Vendors have the ability to participate in our <a href="https://openmainframeproject.org/our-projects/zowe-conformant-support-provider-program/">Open Mainframe Project Zowe Vx Support Provider Conformance program</a>. Vendor offerings that earn this badge have satisfied the requirements necessary to ensure they are capable of providing support for the specific Zowe core component(s). Note: the "Comprehensive Support" designation indicates the offering is capable of providing support for ALL of the Zowe components designated as "core" for the specific Zowe version. Take a look at the landscape below to find an offering.</p>
        <iframe src="https://omp.landscape2.io/embed/embed.html?base-path=&classify=category&key=zowe-conformant-support-provider&headers=true&category-header=false&category-in-subcategory=false&title-uppercase=false&title-alignment=left&title-font-family=sans-serif&title-font-size=13&style=shadowed&bg-color=%230033a1&fg-color=%23ffffff&item-modal=false&item-name=true&size=md&items-alignment=left&item-name-font-size=11" style="width:100%;display:block;border:none;" height="600"></iframe>
    </div>
</section>
