---
redirect_from:
  - "/home"
  - "/home/"
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<script>
  fetch(`https://www.api.metrics.zowe.org/cli`)
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('#cli-downloads').innerHTML = data.downloads;
    });
  fetch(`https://www.api.metrics.zowe.org/server`)
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('#server-downloads').innerHTML = data.downloads;
    });
  fetch(`https://www.api.metrics.zowe.org/omp`)
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('#github-contributors').innerHTML = data.githubSubmittors;
    });
  fetch(`https://www.api.metrics.zowe.org/conformants`)
    .then((response) => response.json())
    .then((data) => {
      document.querySelector('#conformant-product-value').innerHTML = data.products;
    });
</script>


<style>
  .slider-post {
    padding: 5px;
    transition: transform 0.3s ease-in-out; /* Smooth transition for the scaling effect */
  }

  .slider-post:hover {
    transform: scale(1.05); /* Scales up the element by 5% when hovered over */
  }

  .slider-post a.post-image {
    display: block;
    height: 300px;
    background-size: contain;
  }

  .vertical-align-gap4 {
    display: flex;
    align-items: center;
    gap: 4px;
  }

  #menu-overview a.nav-link {
    background-color: #eeeeee;
    color: black !important;
  }

  #menu-overview.nav-item {
    background-color: #eeeeee;
  }
</style>

<script src="https://kit.fontawesome.com/f449f80794.js" crossorigin="anonymous"></script>
{% assign currentTime = 'now' | date: '%s' | plus: 0 %}
{% assign announcements = site.data.announcements %}
{% assign release_date_v3 = site.data.releases.v3[0].release_date | date: '%s' | plus: 0 %}
{% assign release_date_v2 = site.data.releases.v2[0].release_date | date: '%s' | plus: 0 %}
{% assign release_date_v1 = site.data.releases.v1[0].release_date | date: '%s' | plus: 0 %}
{% assign week_time = 1209600 %}
{% assign today_minus_week = currentTime | minus: week_time %}
{% if release_date_v2 > today_minus_week %}
  {% capture version_v2_announcements %}
    <strong>Zowe version {{ site.data.releases.v2[0].version }} is now available. You can download the installers for this release from the <a href="/download">Download</a> page. To learn what's new in this release, see the <a href="https://docs.zowe.org/stable/getting-started/release-notes/{{ site.data.releases.v2[0].release_notes }}">Release notes</a>.</strong>
  {% endcapture %}
  {% assign version_v2_announcements= version_v2_announcements | split: "~" %}
  {% assign announcements = version_v2_announcements | concat: announcements %}
{% endif %}
{% if release_date_v3 > today_minus_week %}
  {% capture version_v3_announcements %}
    <strong>Zowe version {{ site.data.releases.v3[0].version }} is now available. You can download the installers for this release from the <a href="/download">Download</a> page. To learn what's new in this release, see the <a href="https://docs.zowe.org/stable/getting-started/release-notes/{{ site.data.releases.v2[0].release_notes }}">Release notes</a>.</strong>
  {% endcapture %}
  {% assign version_v3_announcements= version_v3_announcements | split: "~" %}
  {% assign announcements = version_v3_announcements | concat: announcements %}
{% endif %}

<div class="announcementsection row" style="padding-left: 5%">
  <div class="row" style="margin-left: 0px; margin-right: 0px; width: 100%" >
    <div class="col-12 col-md-2">
      <div id="feedback-announcements" style="padding-top: 10px; padding-left: 10px; padding-botom: 10px; cursor: pointer;" onclick="toggle('remaining-rows');toggle('feedback-announcements-down');toggle('feedback-announcements-up');">
        <i id="feedback-announcements-down" class="fa-solid fa-chevron-down "></i><i id="feedback-announcements-up" class="fa-solid fa-chevron-up feedback-hide"></i> Announcements
      </div>
    </div>
    <div class="col-12 col-md-10" style="padding-top: 10px;">
      <div id="first-row">
          <strong>{% if announcements[0].announcement %}{{ announcements[0].announcement }}{% else %}{{ announcements[0] }}{% endif %}<br></strong>
      </div>
      <div id="remaining-rows" class=" feedback-hide">
        {% for announcement in announcements %}
          {% if forloop.index > 1 %}
          <hr class="w-100" style="margin-top: 0.25rem; margin-bottom: 0.25rem; border-top: 1px solid rgb(0 0 0 / 20%)">
          <strong>{% if announcement.announcement %}{{ announcement.announcement }}{% else %}{{ announcement }}{% endif %}<br></strong>
          {% endif %}
        {% endfor %}
      </div>
    </div>
  </div>
</div>

{% assign next_version = 2.7 %}
{% assign next_version_date = currentTime %}
{% assign minimum_difference = 15770000 %}  <!-- 6 months --> 
{% for release in site.data.releases.future.v3 %}
  {% assign current_release_date = release.release_date | date: '%s' | plus: 0 %}
  {% if current_release_date > currentTime %}
     {% assign difference_in_seconds = current_release_date | minus: currentTime %}
     {% if difference_in_seconds < minimum_difference %}
       {% assign minimum_difference = difference_in_seconds %}
       {% assign next_version_date = release.release_date %}
       {% assign next_version = release.version %}
     {% endif %}
  {% endif %}
{% endfor %}
{% for release in site.data.releases.future.v2 %}
  {% assign current_release_date = release.release_date | date: '%s' | plus: 0 %}
  {% if current_release_date > currentTime %}
     {% assign difference_in_seconds = current_release_date | minus: currentTime %}
     {% if difference_in_seconds < minimum_difference %}
       {% assign minimum_difference = difference_in_seconds %}
       {% assign next_version_date = release.release_date %}
       {% assign next_version = release.version %}
     {% endif %}
  {% endif %}
{% endfor %}

<div class="row main-zowe-descr">
  <div class="col-12 col-md-7">
    <p>Zowe, the integrated and extensible open source framework for z/OS, combines the past and present to build the future of mainframes.
    Like Mac OS, Windows, and others, Zowe comes with a core set of applications out of the box in combination with the APIs and OS capabilities 
    future applications will depend on.   
    </p>
    <p>Zowe offers modern interfaces to interact with z/OS similar to what you may experience on cloud platforms today. You can use these interfaces as delivered or through plug-ins and extensions that are created by clients or third-party vendors. 
    </p>
    <p>Did you know? The Zowe Community hosts a webinar each quarter called the Zowe Quarterly Update. Watch the replays on <a href="https://www.youtube.com/playlist?list=PL8REpLGaY9QHtnElqPosteBFpITStkAxo">Youtube</a>
    </p>
    <p>Next release: v{{next_version}} GA {{next_version_date}}
    </p>
  </div>
  <div class="col-12 col-md-5 zowe-video animated-tile-bigger">
    <iframe title="Introduction to Zowe" src="{{ site. latest_video_embed }}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen style="width: -webkit-fill-available; height: 100%"></iframe>
  </div>
</div>

<div id="intents">
    <h2 style="color: black !important; margin-bottom: 1.5%">What would you like to do with Zowe?</h2>
    <div class="row">
      <div class="col-sm bg-light animated-tile">
        <img src="/assets/img/learn.png" />
        <a href="https://docs.zowe.org">Learn</a>
        <p style="margin-top: 1rem">Learn how Zowe works and what it can do for you</p>
      </div>
      <div class="col-sm bg-light animated-tile">
        <img src="/assets/img/use.png" />
        <a href="https://docs.zowe.org/stable/user-guide/installandconfig.html">Use</a>
        <p style="margin-top: 1rem">Get started from planning to install and use Zowe</p>
      </div>
      <div class="col-sm bg-light animated-tile">
        <img src="/assets/img/create.png" />
        <a href="https://docs.zowe.org/stable/extend/extend-zowe-overview">Create</a>
        <p style="margin-top: 1rem">Build extensions, services, plug-ins or apps on top of Zowe</p>
      </div>
      <div class="col-sm bg-light animated-tile">
        <img src="/assets/img/contribute.png" />
        <a href="https://docs.zowe.org/stable/contribute/roadmap-contribute">Contribute</a>
        <p style="margin-top: 1rem">Contribute to the open source community developing Zowe</p>
      </div>
    </div>
    <div style="margin-top: 1.5%" class="text-left vertical-align-gap4">
    <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg> <a href="https://github.com/zowe/community/issues">Report Zowe issue</a> | <a href="https://github.com/zowe/zowe.github.io/issues">Report website issue</a>
    </div>
</div> 

<div id="components">
  <div style="margin-bottom: 35px;">
    <h2 style="color: black !important;">Zowe projects</h2>
    Zowe is composed of several projects, each improving the learning ability, accessibility, and possibility of mainframe development.
  </div>

  {% if site.data.projects.size >= 1 %}
    {% assign amount_of_rows = site.data.projects.size | divided_by: 3.0 | ceil %}
    {% assign range_rows = (1..amount_of_rows )%}
    <div>
      {% for current_row in range_rows %}
        <div class="row">
          {% assign current_row_number = forloop.index %}
          {% assign amount_of_rows = forloop.length %}
          {% for project in site.data.projects limit: 3 offset: continue %}
            {% if amount_of_rows == current_row_number %}
              <div class="animated-tile col-md-4 row-{{current_row_number}} column-{{forloop.index}} last" >
            {% else %}
              <div class="animated-tile col-md-4 row-{{current_row_number}} column-{{forloop.index}}" >
            {% endif %}
            
              <img class="image-zowe-use" src="{{ project.img_url }}">
              <a id="{{ project.name | replace: " ", "-" | downcase }}-intro"><h4>{{ project.name }}</h4></a>
              <p style="margin: 1rem auto">
                <span class="{{project.stage | replace: " ", "-" | downcase }} stage">{{project.stage}}</span> 
                <span class="{{project.dedication | replace: " ", "-" | downcase }} dedication">{{project.dedication}}</span>
                {% if project.component_type %}
                 <span class="{{project.component_type | replace: " ", "-" | downcase }} component_type">{{project.component_type}}</span>
                {% endif %}
              </p>
              <p style="margin: 1rem auto">{{project.description}}</p>
              <p>
                  {% if project.github_url %}
                    <a href="{{ project.github_url }}">Code on GitHub</a>&nbsp;|&nbsp;
                  {% endif %}
                  {% if project.slack_url %}              
                    <a href="{{ project.slack_url }}">Connect on Slack</a>&nbsp;|&nbsp;
                  {% endif %}
                  {% if project.doc_url %}              
                    <a href="{{ project.doc_url }}">Learn more</a>&nbsp;|&nbsp;
                  {% endif %}
                  {% if project.tour_url %}              
                    <a href="{{ project.tour_url }}">View Tour</a>
                  {% endif %}
              </p>
            </div>
          {% endfor %}
        </div>
      {% endfor %}
    </div>
  </div>
{% endif %}

<div>
