---
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<style>
table, th, td {
  border: 1px solid black;
  padding: 4px;
}

.faq-hide {
  display: none;
}

.bluebackground.conformance-criteria h5, .bluebackground.conformance-criteria .card-text, .bluebackground.conformance-criteria .card-body {
  color: #145391;
}

p .card-black {
  color: black;
}
</style>
<script src="https://cdn.jsdelivr.net/remarkable/1.7.1/remarkable.min.js"></script>

<section class="whitebackground">
  <h1 id="download" style="margin-bottom: 1.5rem">Table of Contents</h1>

  <div class="d-flex flex-column">
      {% if site.data.vnext_announcements %}
        <a href="#latest-announcements" class="card-link" style="margin-left: 1.25rem">
        <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
        Latest Announcements 
        </a>
      {% endif %}
      {% if site.data.vnext_changes%}
        <a href="#coming-changes" class="card-link">
        <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
        Coming changes to the functionality
        </a>
      {% endif %}
      {% if site.data.vnext_conformance_criteria %}
        <a href="#conformance-changes" class="card-link">
        <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
        Changes to the Conformance Criteria
        </a>
      {% endif %}
      {% if site.data.vnext_office_hours %}
        <a href="#office-hours" class="card-link">
        <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
        Office Hours
        </a>
      {% endif %}
      {% if site.data.vnext_faq %}
        {% if site.data.vnext_faq.general %}
          <a href="#faq" class="card-link">
          <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
          Frequently Asked Questions
          </a>
        {% endif %}
        {% if site.data.vnext_faq.consumers %} 
          <a href="#faq-users" class="card-link">
          <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
          Frequently Asked Questions - User focused
          </a>
          {% for squad in site.data.vnext_faq.consumers %}
            <a href="#{{ squad.id }}-hours" class="card-link" style="margin-left: 30px;">
            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
            {{ squad.name }}
            </a>          
          {% endfor %}
        {% endif %}
        {% if site.data.vnext_faq.extenders %}
          <a href="#faq-extenders" class="card-link">
          <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
          Frequently Asked Questions - Extender focused
          </a>
          {% for squad in site.data.vnext_faq.extenders %}
            <a href="#{{ squad.id }}-hours" class="card-link" style="margin-left: 30px;">
            <svg width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-arrow-right-circle" fill="currentColor" xmlns="http://www.w3.org/2000/svg"> <path fill-rule="evenodd" d="M8 15A7 7 0 1 0 8 1a7 7 0 0 0 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/> <path fill-rule="evenodd" d="M7.646 11.354a.5.5 0 0 1 0-.708L10.293 8 7.646 5.354a.5.5 0 1 1 .708-.708l3 3a.5.5 0 0 1 0 .708l-3 3a.5.5 0 0 1-.708 0z"/> <path fill-rule="evenodd" d="M4.5 8a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1H5a.5.5 0 0 1-.5-.5z"/></svg>
            {{ squad.name }}
            </a>        
          {% endfor %}
        {% endif %}
      {% endif %}
  </div>

  <div>
    <h2 style="margin-bottom: 1.5rem; margin-top: 2%" id="latest-announcements">Latest Announcements</h2>
    {% if site.data.vnext_announcements %}
      {% for announcement in site.data.vnext_announcements %}
      <p class="md-transform">{{ announcement.announcement }}</p>
      {% endfor %}
    {% endif %}
  </div>

  <h2 id="coming-changes">Coming changes to the functionality</h2>
  {% if site.data.vnext_changes %}
    {% for squad in site.data.vnext_changes %}
      <div class="card mb-3">
        <div class="card-body">
          <div class="d-flex align-items-baseline">
            <h5 class="text-left"><a href="{{ squad.homepage_link }}">{{ squad.name }}</a></h5>
          </div>
          <div class="row">
            <div class="col-md-7 col-sm order-last order-sm-first md-transform">
              {{ squad.description}}
            </div>
            <div class="col-md-3 col-sm order-first order-sm-last">
              <img class="image-zowe-use" src="{{ squad.image }}">
            </div>
          </div>
        </div>
      </div>
    {% endfor %}
  {% endif %}

<section class="bluebackground conformance-criteria">

  <h2 id="conformance-changes">Changes to the Conformance Criteria (For Extenders) </h2>

  <p>The final version of V2 Conformance Criteria is published here. Each of the section links to th PDF for the specific criteria.</p>

  {% if site.data.vnext_conformance_criteria %}
    {% for conformance in site.data.vnext_conformance_criteria %}
      <div class="card mb-3">
        <div class="card-body">
          <div class="d-flex align-items-baseline">
            <h5 class="text-left">{{ conformance.name }}</h5>
          </div>
          <div class="md-transform">{{ conformance.description }}</div>
        </div>
      </div>
    {% endfor %}
  {% endif %}
</section>

<section class="whitebackground">
  <div id="office-hours">
    <h2 style="margin-bottom: 1.5rem; margin-top: 2%">Office Hours</h2>
    <p>Check out the <a href="https://lists.openmainframeproject.org/g/zowe-dev/calendar">OMP Calendar</a> for specific time of the V2 office hours.</p>
    <h3 style="margin-bottom: 1.5rem; margin-top: 2%">Consumer Focused Office Hours</h3>
    <table>
    <tr>
    <td><b>Date</b></td>
    <td><b>Topic</b></td>
    <td><b>Link to the meeting</b></td>
    <td><b>Link to the recording</b></td>
    <td><b>Links to the materials</b></td>
    </tr>
    {% if site.data.vnext_office_hours.consumers %}
      {% for meeting in site.data.vnext_office_hours.consumers %}
        <tr>
          <td>{{ meeting.date }}</td>
          <td>{{ meeting.topic }}</td>
          <td><a href="{{ meeting.meeting_link }}">{{ meeting.meeting_link }}</a></td>
          <td>
            {% if meeting.recording_link %}
              <a href="{{ meeting.meeting_link }}">Zoom recording</a>
            {% endif %}
          </td>
          <td>
            {% if meeting.materials_link %}
              <a href="{{ meeting.materials_link }}">Presentation</a>
            {% endif %}
          </td>
        </tr>
      {% endfor %}
    {% endif %}
    </table>
    <h3 style="margin-bottom: 1.5rem; margin-top: 2%">Extender Focused Office Hours</h3>
    <table>
    <tr>
    <td><b>Date</b></td>
    <td><b>Topic</b></td>
    <td><b>Link to the meeting</b></td>
    <td><b>Link to the recording</b></td>
    <td><b>Links to the materials</b></td>
    </tr>
    {% if site.data.vnext_office_hours.extenders %}
      {% for meeting in site.data.vnext_office_hours.extenders %}
        <tr>
          <td>{{ meeting.date }}</td>
          <td>{{ meeting.topic }}</td>
          <td><a href="{{ meeting.meeting_link }}">{{ meeting.meeting_link }}</a></td>
          <td>
            {% if meeting.recording_link %}
              <a href="{{ meeting.meeting_link }}">Zoom recording</a>
            {% endif %}
          </td>
          <td>
            {% if meeting.materials_link %}
              <a href="{{ meeting.materials_link }}">Presentation</a>
            {% endif %}
          </td>
        </tr>
      {% endfor %}
    {% endif %}
    </table>
  </div>

</section>

<section class="bluebackground">

  <script>
    function toggle(id) {
      var x = document.getElementById(id);
      if (x.className.indexOf("faq-hide") == -1) {
        x.className += " faq-hide";
      } else {
        x.className = x.className.replace(" faq-hide", "");
      }
    }
  </script>

  <div>
    {% if site.data.vnext_faq.general %}
      <h2 style="margin-bottom: 1.5rem; margin-top: 2%" id="faq">Frequently Asked Questions</h2>
      {% for question in site.data.vnext_faq.general %}
      <div>
        <button onclick="toggle('question-{{ question.number }}')" class="w3-button w3-block w3-left-align">
        {{ question.number }}. {{ question.question }}</button>
        <div id="question-{{ question.number }}" class="w3-container faq-hide md-transform">
          {{ question.answer }}
        </div>
      </div>
      {% endfor %}
    {% endif %}
    {% if site.data.vnext_faq.extenders %}
      <h2 style="margin-bottom: 1.5rem; margin-top: 2%" id="faq-extenders">Frequently Asked Questions - Extenders Focused</h2>
      <div>
      {% for consumer in site.data.vnext_faq.extenders %}
        <button id="{{ consumer.id }}-hours" onclick="toggle('{{ consumer.id }}')" class="w3-button w3-block w3-left-align">
        {{ consumer.name }}</button>
        <div id="{{ consumer.id }}" class="w3-container faq-hide">
          {% for question in consumer.questions %}
          <div>
            <button onclick="toggle('{{ consumer.id }}-{{ question.number }}')" class="w3-button w3-block w3-left-align">
              {{ question.number }}. {{ question.question }}
            </button>
            <div id="{{ consumer.id }}-{{ question.number }}" class="w3-container faq-hide md-transform">
              {{ question.answer}}
            </div>
          </div>
          {% endfor %}
        </div>
      {% endfor %}
      </div>
    {% endif %}
    {% if site.data.vnext_faq.consumers %}
      <h2 style="margin-bottom: 1.5rem; margin-top: 2%" id="faq-users">Frequently Asked Questions - Users Focused</h2>
      <div>
      {% for consumer in site.data.vnext_faq.consumers %}
        <button id="{{ consumer.id }}-hours" onclick="toggle('{{ consumer.id }}')" class="w3-button w3-block w3-left-align">
        {{ consumer.name }}</button>
        <div id="{{ consumer.id }}" class="w3-container faq-hide">
          {% for question in consumer.questions %}
          <div>
            <button onclick="toggle('{{ consumer.id }}-{{ question.number }}')" class="w3-button w3-block w3-left-align">
              {{ question.number }}. {{ question.question }}
            </button>
            <div id="{{ consumer.id }}-{{ question.number }}" class="w3-container faq-hide md-transform">
              {{ question.answer}}
            </div>
          </div>
          {% endfor %}
        </div>
      {% endfor %}
      </div>
    {% endif %}
  </div> 

</section>

<script type="text/javascript" defer>
  var md = new Remarkable();
  var elementsToTransform = document.getElementsByClassName("md-transform");
  for (var i = 0; i < elementsToTransform.length; i++) {
    elementsToTransform[i].innerHTML = md.render(elementsToTransform[i].innerHTML);
  }
</script>