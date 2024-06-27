---
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<style>
  #menu-community a.nav-link {
    background-color: #eeeeee;
    color: black !important;
  }

  #menu-community.nav-item {
    background-color: #eeeeee;
  }
</style>

<section class="whitebackground">
  <h1 id="download" style="margin-bottom: 1.5rem">Join The Zowe Community</h1>
  <p>Here are some of the best ways to engage with the Zowe community!</p>

  <div class="card-deck">
  <div class="card mb-3 animated-tile">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.slack_url }}">Slack</a></h5>
        <img class="ml-2" style="height: 20px" src="assets/img/slack-community.svg">
      </div>
      <p class="card-text">Hosted by the Open Mainframe Project, this is a messaging board where you can directly engage with Zowe users and contributors - ask questions, engage in discussions, and contribute your ideas!</p>
      <p>Some popular channels to get started: <ul>
      <li><a href="{{ site.zowe_onboarding_slack_url }}">#zowe-onboarding</a></li> 
      <li><a href="{{ site.zowe_user_slack_url }}">#zowe-help</a></li> 
      <li><a href="{{ site.zowe_cli_slack_url }}">#zowe-cli</a></li> 
      <li><a href="{{ site.zowe_explorer_slack_url }}">#zowe-explorer</a></li> 
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
      <p class="card-text">All scheduled meetings in the Zowe community are placed in the Open Mainframe Project Calendar, from the scrum status of a squad to meetings of the Technical Steering Committee and the Zowe Advisory Council. </p>
      <p>You are welcome to drop in on and contribute to any of these meetings! Check out the detailed introduction to squad meetings and other recurring meetings! </p>
    </div>
  </div>
  <div class="card mb-3 animated-tile">
    <div class="card-body">
      <div class="d-flex align-items-baseline">
        <h5 class="text-left"><a href="{{ site.github_repo_url }}">GitHub</a></h5>
        <img class="ml-2" style="height: 20px" src="assets/img/github-community.svg">
      </div>
      <p class="card-text">This is where all of Zowe’s code is, and where you can find detailed information about each project and how to collaborate and contribute. This is the place to open issues, give feedback, and contribute code.</p>
      <p>Some good repos to get started: <ul>
      <li><a href="{{ site.zowe_community_repo_url }}">community</a></li> 
      <li><a href="{{ site.zowe_docs_repo_url }}">docs-site</a></li>  
      </ul>
      </p>
    </div>
  </div>
</div>

  <div>
    <h2 style="margin-bottom: 1.5rem; margin-top: 2%">Join a squad call</h2>
    <p>Zowe is an open source project - this means that anyone can contribute to any part of it, and that includes you! The best ways to first get involved are <a href="{{ site.create_zowe_issue_url }}">opening issues on GitHub</a>, saying hi on Slack, or joining the weekly calls of one of the squads listed below.</p>
    <p>Zowe’s most frequent and dedicated contributors work in teams called “squads”. If you have specific questions or are excited about a particular part of Zowe, connect with the relevant squad using the table below! Occasionally, some of the meetings might be changed, cancelled or rescheduled. Stay up to date on meetings in the <a href="{{ site.omp_calendar_url }}">Zowe meeting calendar</a> or the Slack channels.</p>
    <iframe class="mt-4" src="https://zoom-lfx.platform.linuxfoundation.org/meetings/zowe" style="border: 0" width="100%" height="600" frameborder="0" scrolling="no"></iframe>
  </div>
</section>

<!-- Manual Editable Calendar-->
<!-- {% if site.data.squad_call %}
    <div>
      <table class="table table-bordered">
        <thead>
          <tr>
            <th scope="col">Squad Name</th>
            <th scope="col" colspan="2">Description</th>
            <th scope="col">Meeting Details</th>
          </tr>
        </thead>
        <tbody>
          {% for squad in site.data.squad_call %}
            <tr>
              <td>
                <p style="margin-bottom: 0">{{ squad.squad-name }}</p>
                <a href="{{ squad.github-link }}"><p>GitHub</p></a>
              </td>
              <td colspan="2">{{ squad.description }}</td>
              <td>
                {% if squad.day %}
                  <p style="margin-bottom: 0rem">{{ squad.day }}</p>
                {% endif %}
                {% if squad.slack %}
                  <p style="margin-bottom: 0rem"><b>Slack Channel:</b> {{ squad.slack }}</p>
                {% endif %}
                {% if squad.meeting-link %}
                  <a href="{{ squad.meeting-link }}">Join this squad’s meeting</a>
                {% endif %}
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
    {% endif %}
  </div>
  <div>
    <h2 style="margin-bottom: 1.5rem; margin-top: 2%">Join other meetings</h2>
    <p>Check out other great discussions that are happening each week!</p>
    {% if site.data.other_call %}
    <div>
      <table class="table table-bordered">
        <thead>
          <tr>
            <th scope="col" style="width: auto">Meeting</th>
            <th scope="col">Description</th>
            <th scope="col" colspan="2" style="width: 480px">Meeting Details</th>
          </tr>
        </thead>
        <tbody>
          {% for squad in site.data.other_call %}
            <tr>
              <td>
                <p style="margin-bottom: 0">{{ squad.squad-name }}</p>
                <a href="{{ squad.github-link }}"><p>GitHub</p></a>
              </td>
              <td>{{ squad.description }}</td>
              <td colspan="2">
                {% if squad.day %}
                  <p style="margin-bottom: 0rem">{{ squad.day }}</p>
                {% endif %}
                {% if squad.slack %}
                  <p style="margin-bottom: 0rem">Slack Channel: {{ squad.slack }}</p>
                {% endif %}
                {% if squad.meeting-link %}
                  <a href="{{ squad.meeting-link }}">Join this meeting</a>
                {% endif %}
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
  {% endif %} -->
