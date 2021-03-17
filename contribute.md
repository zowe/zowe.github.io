---
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<section class="whitebackground">
  <h1 id="download" style="margin-bottom: 1.5rem">Join The Zowe Community</h1>
  <p>Here are some of the best ways to engage with the Zowe community!</p>

  <div class="card-deck">
  <div class="card border-dark mb-3">
    <div class="card-body">
      <h5 class="card-title text-center">Slack</h5>
      <a class="col-md-3" href="{{ site.slack_url }}"><button type="button" class="btn btn-primary btn-lg btn-block" style="white-space: break-spaces">Join our Slack community</button></a>
      <p class="card-text">Hosted by the Open Mainframe Project, this is a messaging board where you can directly engage with Zowe users and contributors - ask questions, engage in discussions, and contribute your ideas!</p>
      <p>Some popular channels to get started: <ul>
      <li>#zowe-onboarding</li> 
      <li>#zowe-user</li> 
      <li>#zowe-cli</li> 
      <li>#zowe-explorer</li> 
      <li>#zowe-api</li>
      <li>#zowe-doc</li> 
      </ul>
      </p>
    </div>
  </div>
  <div class="card border-dark mb-3">
    <div class="card-body">
      <h5 class="card-title text-center">Meetings</h5>
      <a class="col-md-3" href="{{ site.omp_calendar_url }}"><button type="button" class="btn btn-primary btn-lg btn-block" style="white-space: break-spaces">Check the calendar</button></a>
      <p class="card-text">All scheduled meetings in the Zowe community are placed in the Mainframe Project Calendar, from the scrum status of a squad to meetings of the Zowe Leadership Committee. </p>
      <p>You are welcome to drop in on and contribute to any of these meetings! Check out the detailed introduction to squad meetings and other recurring meetings! </p>
    </div>
  </div>
  <div class="card border-dark mb-3">
    <div class="card-body">
      <h5 class="card-title text-center">GitHub</h5>
      <a class="col-md-3" href="{{ site.github_repo_url }}"><button type="button" class="btn btn-primary btn-lg btn-block" style="white-space: break-spaces">Visit Zowe repos</button></a>
      <p class="card-text">This is where all of Zowe’s code is, and where you can find detailed information about each project and how to collaborate and contribute. This is the place to open issues, give feedback, and contribute code.</p>
      <p>Some good repos to get started: <ul>
      <li><a href="{{ site.zowe_community_repo_url }}">community</a></li> 
      <li><a href="{{ site.zowe_zlc_repo_url }}">zlc</a></li> 
      <li><a href="{{ site.zowe_docs_repo_url }}">docs-site</a></li>  
      </ul>
      </p>
    </div>
  </div>
</div>

  <div style="padding-top: 2%">
    <h2 style="margin-bottom: 1.5rem">Upcoming Events</h2>
    <p>Here are some of the exciting community events coming up in the next few months!</p>
    <div>
      {% if site.data.upcoming_events %}
        <div class="row">
          {% for events in site.data.upcoming_events limit:4 %}
            <p class="col-md-4"><strong>{{ events.event}}</strong></p>
            <p class="col-md-8">{{ events.description }}
              {% if events.link %}
                <a href="{{ events.link }}">register here</a>
              {% endif %}
            </p>
            <br>
          {% endfor %}
        </div>
      {% endif %}
    </div>
  </div>

  <div style="padding-top: 2%">
    <h2 style="margin-bottom: 1.5rem">Join A Squad Call!</h2>
    <p>Zowe is an open source project - this means that anyone can contribute to any part of it, and that includes you! The best ways to first get involved are <a href="{{ site.create_zowe_issue_url }}">opening issues on GitHub</a>, saying hi on Slack, or joining the weekly calls of one of the squads listed below.</p>
    <p>Zowe’s most frequent and dedicated contributors work in teams called “squads”. If you have specific questions or are excited about a particular part of Zowe, connect with the relevant squad using the table below!</p>
    {% if site.data.squad_call %}
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
                <a href="{{ squad.github-link }}"><p>Github</p></a>
              </td>
              <td colspan="2">{{ squad.description }}</td>
              <td>
                {% if squad.day %}
                  <p style="margin-bottom: 0rem">{{ squad.day }}</p>
                {% endif %}
                {% if squad.slack %}
                  <p style="margin-bottom: 0rem">Slack Channel: {{ squad.slack }}</p>
                {% endif %}
                {% if squad.meeting-link %}
                  <a href="{{ squad.meeting-link }}">Join this squad’s meeting</a>
                {% endif %}
                <br>
                {% if squad.meeting-topic %}
                  <a href="{{ squad.meeting-topic }}">Submit a meeting topic</a>
                {% endif %}
              </td>
            </tr>
          {% endfor %}
        </tbody>
      </table>
    </div>
    {% endif %}
  </div>
</section>
