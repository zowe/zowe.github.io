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
{% if site.data.question_of_month %}  
  {% for feedback in site.data.question_of_month %}
    {% assign fromFeedback = feedback.from | date: '%s' | plus: 0 %}
    {% assign toFeedback = feedback.to | date: '%s' | plus: 0 %}
      {% if currentTime > fromFeedback %}
        {% if toFeedback == 0 or currentTime < toFeedback %}
<div id="feedback-closed" class=" feedback-hide" onclick="toggleFeedback();">
  <div style="padding-top: 12px; padding-left: 15px; color: white;">
      <span class="question-name">Question for Jan</span>
    </div>
</div>
<div id="feedback">
  <div class="feedback-header" onclick="toggleFeedback();"><span class="question-name" style="font-size: smaller;">Question for August</span> <div style="float: right; cursor: pointer;"><i class="fa-solid fa-circle-xmark"></i></div></div>
  <div>
    <iframe class="feedback-container" src="{{feedback.link}}"></iframe>
  </div>
</div>
        {% endif %}
      {% endif %}
  {% endfor %}
{% endif %}


{% assign announcements = site.data.announcements %}
{% assign release_date_v2 = site.data.releases.v2[0].release_date | date: '%s' | plus: 0 %}
{% assign release_date_v1 = site.data.releases.v1[0].release_date | date: '%s' | plus: 0 %}
{% assign week_time = 1209600 %}
{% assign today_minus_week = currentTime | minus: week_time %}
{% if release_date_v1 > today_minus_week %}
  {% capture version_v1_announcements %}
    <strong>Zowe version {{ site.data.releases.v1[0].version }} is now available. You can download the installers for this release from the <a href="/download">Download</a> page. To learn what's new in this release, see the <a href="https://docs.zowe.org/v1.28.x/getting-started/release-notes/{{ site.data.releases.v1[0].release_notes }}">Release notes</a>.</strong>
  {% endcapture %}
  {% assign version_v1_announcements= version_v1_announcements | split: "~" %}
  {% assign announcements = version_v1_announcements | concat: announcements %}
{% endif %}
{% if release_date_v2 > today_minus_week %}
  {% capture version_v2_announcements %}
    <strong>Zowe version {{ site.data.releases.v2[0].version }} is now available. You can download the installers for this release from the <a href="/download">Download</a> page. To learn what's new in this release, see the <a href="https://docs.zowe.org/stable/getting-started/release-notes/{{ site.data.releases.v2[0].release_notes }}">Release notes</a>.</strong>
  {% endcapture %}
  {% assign version_v2_announcements= version_v2_announcements | split: "~" %}
  {% assign announcements = version_v2_announcements | concat: announcements %}
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
{% assign minimum_difference = 9999999 %}
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
{% for release in site.data.releases.future.v1 %}
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
    <p>Next release: v{{next_version}} GA {{next_version_date}} | <a href="https://github.com/zowe/zowe.github.io/raw/master/assets/roadmap/Zowe%20Roadmap%20CY24Q2.pdf">View roadmap</a>
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
        <a href="/learn">Learn</a>
        <p style="margin-top: 1rem">Learn how Zowe works and what it can do for you</p>
      </div>
      <div class="col-sm bg-light animated-tile">
        <img src="/assets/img/use.png" />
        <a href="https://docs.zowe.org/stable/user-guide/installandconfig.html">Use</a>
        <p style="margin-top: 1rem">Get started from planning to install and use Zowe</p>
      </div>
      <div class="col-sm bg-light animated-tile">
        <img src="/assets/img/create.png" />
        <a href="/extend">Create</a>
        <p style="margin-top: 1rem">Build extensions, services, plug-ins or apps on top of Zowe</p>
      </div>
      <div class="col-sm bg-light animated-tile">
        <img src="/assets/img/contribute.png" />
        <a href="/contribute">Contribute</a>
        <p style="margin-top: 1rem">Contribute to the open source community developing Zowe</p>
      </div>
    </div>
    <div style="margin-top: 1.5%" class="text-left vertical-align-gap4">
    <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg> <a href="https://github.com/zowe/community/issues">Report Zowe issue</a> | <a href="https://github.com/zowe/zowe.github.io/issues">Report website issue</a>
    </div>
</div> 

  {% if site.data.upcoming_events.size >= 1 %}
  <section id="events" style="margin-top: 3%">
    <div style="padding: 0% 5%">
      <h2 class="mb-3" style="color: black !important">Upcoming and recent events</h2>
      <div class="row py-4">
        {% for events in site.data.upcoming_events limit:3 %}
        <div class="col-md-4 px-3 pb-4 pb-md-0"> <!-- ml-auto mr-auto -->
          <div class="w-100 px-4 py-4 rounded shadow bg-light h-100 animated-tile">
          {% if events.url %}
            <h5 class="border-bottom border-primary pb-2"><a href="{{ events.url }}">{{ events.event }}</a></h5>
          {% else %}
            <h5 class="border-bottom border-primary pb-2">{{ events.event }}</h5>
          {% endif %}
          {% assign currentTime = 'now' | date: '%s' | plus: 0 %}
          {% assign fromEvent = events.from | date: '%s' | plus: 0 %} 
          {% assign toEvent = events.to | date: '%s' | plus: 0 %}
          {% if currentTime > toEvent %}
            <span class="past" style="font-weight: 600"><i class="fa-solid fa-circle-check"></i> {{ events.schedule }}</span>
          {% else %}
            <span style="font-weight: 600"><i class="fa-solid fa-circle-check future"></i> {{ events.schedule }}</span>
          {% endif %}
            <br>
            <span class="text-muted small">{{ events.description }}</span>
          </div>
        </div>
        {% endfor %}
      </div>
      <div class="row py-4">
        {% for events in site.data.upcoming_events limit:3 offset:3 %}
        <div class="col-md-4 px-3 pb-4 pb-md-0"> <!-- ml-auto mr-auto -->
          <div class="w-100 px-4 py-4 rounded shadow bg-light h-100 animated-tile">
          {% if events.url %}
            <h5 class="border-bottom border-primary pb-2"><a href="{{ events.url }}">{{ events.event }}</a></h5>
          {% else %}
            <h5 class="border-bottom border-primary pb-2">{{ events.event }}</h5>
          {% endif %}
          {% assign currentTime = 'now' | date: '%s' | plus: 0 %}
          {% assign fromEvent = events.from | date: '%s' | plus: 0 %} 
          {% assign toEvent = events.to | date: '%s' | plus: 0 %}
          {% if currentTime > toEvent %}
            <span class="past" style="font-weight: 600"><i class="fa-solid fa-circle-check"></i> {{ events.schedule }}</span>
          {% else %}
            <span style="font-weight: 600"><i class="fa-solid fa-circle-check future"></i> {{ events.schedule }}</span>
          {% endif %}
            <br>
            <span class="text-muted small">{{ events.description }}</span>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
  </section>
  {% endif %}

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

<div id="metrics" class="bg-light"> 
  <h2 class="text-center" style="margin-bottom: 5%">Zowe by the numbers</h2>
  <div class="row" style="margin-bottom: 2%">
    <div class="col-md text-center">
      <span style="color: initial; text-decoration: none"><img style="width:15%" src="assets/img/logo-cli-download.svg" />
        <h3 class="mb-0" id="cli-downloads"></h3>
        <h6>Zowe CLI Downloads</h6>
      </span>
    </div>
    <div class="col-md text-center">
      <a style="color: initial; text-decoration: none" href="{{ site.vscode_marketplace_url }}"><img style="width:15%" src="assets/img/logo-explorer-download.svg" />
        <h3 class="mb-0" id="explorer-downloads"><img style="width: 80px;" src="https://img.shields.io/visual-studio-marketplace/d/Zowe.vscode-extension-for-zowe.svg?color=f8f9fa&label=" /></h3>
        <h6>Zowe Explorer Downloads</h6>
      </a>
    </div>
    <div class="col-md text-center">
      <span style="color: initial; text-decoration: none"><img style="width:15%" src="assets/img/logo-zowe-build-download.svg">
        <h3 class="mb-0" id="server-downloads"></h3>
        <h6>Zowe z/OS Build Downloads</h6>
      </span>
    </div>
  </div>
  <div class="row">
    <div class="col-md text-center">
      <span style="color: initial; text-decoration: none"><img style="width:15%" src="assets/img/logo-github-back.svg" />
        <h3 class="mb-0" id="github-contributors"></h3>
        <h6>Contributors</h6>
      </span>
    </div>
    <div class="col-md text-center">
      <span style="color: initial; text-decoration: none" ><img style="width:15%" src="assets/img/logo-vendor-product.svg" />
        <h3 class="mb-0" id="conformant-product-value"></h3>
        <h6>Zowe Conformant Products</h6>
      </span>
    </div>
  </div>
</div>

<div id="blogs" style="padding: 4% 7% 5% 7%">
  <div style="margin-bottom: 4%">
    <h2 class="text-center" style="color: black !important; margin-bottom: 5%">From Zowe blog</h2>
  </div>
  <div>
    <div id="retainable-rss-embed" data-rss="https://medium.com/feed/zowe"
        data-maxcols="3" 
        data-layout="slider" 
        data-poststyle="external" 
        data-readmore="Read the rest" 
        data-buttonclass="btn btn-primary" 
        data-offset="-100">
    </div>
  </div>
  
  <div style="margin-bottom: 4%">
    <a href="{{ site.zowe_medium_blog_url }}"><h5 class="text-right"><svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg> Check our other blogs</h5></a>
  </div>    
</div>

<script src="assets/retainable.js" ></script>
<script src="assets/feedback.js" ></script>
  
<link rel="stylesheet" type="text/css" href="{{ '/assets/css/retainable.css' | relative_url }}" />

<div>
