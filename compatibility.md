---
---

<!-- SPDX-License-Identifier: CC-BY-4.0 -->
<!-- Copyright Contributors to the Zowe project. -->

<style>
  #menu-compatibility a.nav-link {
    background-color: #eeeeee;
    color: black !important;
  }

  #menu-compatibility.nav-item {
    background-color: #eeeeee;
  }

  .compatibility-table th {
    background-color: #145391;
    color: white;
    font-weight: 600;
    border: 1px solid #0e3f73;
    white-space: nowrap;
  }

  .compatibility-table .section-header td {
    background-color: #1a6bb5;
    color: white;
    font-weight: 700;
    font-size: 1em;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    border: 1px solid #0e3f73;
  }

  .compatibility-table td {
    vertical-align: middle;
    border: 1px solid #dee2e6;
  }

  .compatibility-table tbody tr:not(.section-header):nth-child(odd) {
    background-color: #ffffff;
  }

  .compatibility-table tbody tr:not(.section-header):nth-child(even) {
    background-color: #f8f9fa;
  }

  .compatibility-table tbody tr:not(.section-header):hover {
    background-color: #e9ecef;
  }

  .badge-automated {
    display: inline-block;
    background-color: #28a745;
    color: white;
    padding: 0.2em 0.55em;
    border-radius: 0.25rem;
    font-size: 0.82em;
    font-weight: 600;
    white-space: nowrap;
  }

  .badge-community {
    display: inline-block;
    background-color: #17a2b8;
    color: white;
    padding: 0.2em 0.55em;
    border-radius: 0.25rem;
    font-size: 0.82em;
    font-weight: 600;
    white-space: nowrap;
  }

  .badge-nosupport {
    display: inline-block;
    background-color: red;
    color: white;
    padding: 0.2em 0.55em;
    border-radius: 0.25rem;
    font-size: 0.82em;
    font-weight: 600;
    white-space: nowrap;
  }

  .compat-nosupport {
    color: red;
    font-weight: 700;
    font-size: 1.1em;
  }
</style>

<section class="whitebackground">
  <h1>Compatibility Matrix</h1>
  <p>Validate whether your z/OS environment meets the necessary prerequisites to operate Zowe server side. In the case of z/OS, Java, Node.js we had older versions that we used to support and no longer support.</p>

  <div style="overflow-x: auto">
    <table class="table table-bordered table-sm compatibility-table">
      <thead>
        <tr>
          <th>Version</th>
          <th>Zowe V2 Compatibility</th>
          <th>Zowe V3 Compatibility</th>
          <th>Testing Status</th>
        </tr>
      </thead>
      <tbody>
        <tr class="section-header">
          <td colspan="4">z/OS</td>
        </tr>
        <tr>
          <td>2.5</td>
          <td>&gt;= 2.13</td>
          <td>All versions</td>
          <td><span class="badge-automated">Automated Testing by Community</span></td>
        </tr>
        <tr>
          <td>3.1</td>
          <td>&gt;= 2.18.2</td>
          <td>All versions</td>
          <td><span class="badge-community">Tested by Community Member</span></td>
        </tr>
        <tr>
          <td>3.2</td>
          <td>&gt;= 2.18.4</td>
          <td>&gt;= 3.3</td>
          <td><span class="badge-community">Tested by Community Member</span></td>
        </tr>
        <tr class="section-header">
          <td colspan="4">Java</td>
        </tr>
        <tr>
          <td>8</td>
          <td>&gt;= 2.0</td>
          <td><span class="compat-nosupport">✗</span></td>
          <td><span class="badge-automated">Automated Testing by Community</span></td>
        </tr>
        <tr>
          <td>11</td>
          <td>&gt;= 2.0</td>
          <td><span class="compat-nosupport">✗</span></td>
          <td><span class="badge-automated">Automated Testing by Community</span></td>
        </tr>
        <tr>
          <td>17</td>
          <td>&gt;= 2.15</td>
          <td>All versions</td>
          <td><span class="badge-automated">Automated Testing by Community</span></td>
        </tr>
        <tr>
          <td>21</td>
          <td>&gt;= 2.18.5</td>
          <td>&gt;= 3.3</td>
          <td><span class="badge-community">Tested by Community Member</span></td>
        </tr>
        <tr>
          <td>25</td>
          <td><span class="compat-nosupport">✗</span></td>
          <td><span class="compat-nosupport">✗</span></td>
          <td><span class="badge-nosupport">No Support Yet</span></td>
        </tr>
        <tr class="section-header">
          <td colspan="4">Node.js</td>
        </tr>
        <tr>
          <td>20</td>
          <td>&gt;= 2.13</td>
          <td>All versions</td>
          <td><span class="badge-automated">Automated Testing by Community</span></td>
        </tr>
        <tr>
          <td>22</td>
          <td><span class="compat-nosupport">✗</span></td>
          <td>&gt;= 3.0</td>
          <td><span class="badge-automated">Automated Testing by Community</span></td>
        </tr>
        <tr>
          <td>24</td>
          <td><span class="compat-nosupport">✗</span></td>
          <td>&gt;= 3.3</td>
          <td><span class="badge-community">Tested by Community Member</span></td>
        </tr>
      </tbody>
    </table>
  </div>

  <h2>Looking for something else?</h2>
  <p>Let us know <a href="https://github.com/zowe/community/issues/new?template=zowe-org-request.md">here</a> by opening new issue. </p>
</section>
