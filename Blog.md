---
title: "Blog"
---



## Sharing With the Lab

Every now and then someone has something worth sharing — a slide deck from a talk, meeting notes, a Word doc, an HTML export, anything — that doesn't need its own page but is still useful for others to have. This page is a running, dated collection of that kind of thing, grouped by month.

## Contributing

1. Copy the [`Blog/TEMPLATE`](https://github.com/HaganLab/LabOps/tree/main/Blog/TEMPLATE) folder into `Blog/`, renamed to something short and unique (e.g. `Blog/jane-hpc-tips/`).
2. Drop your file into that folder — any format is fine.
3. Fill in `metadata.json` (contributor, title, date, description, and an optional format tag).
4. Commit/push or open a PR.

Full instructions and a filled-in example are in [`Blog/TEMPLATE/README.md`](https://github.com/HaganLab/LabOps/blob/main/Blog/TEMPLATE/README.md). The list below updates automatically within a week of a new submission being merged, via a scheduled GitHub Action — no need to touch this page.

## Recent Submissions

<div id="blog-list">Loading…</div>

<script>
fetch('blog-manifest.json')
  .then(function (response) { return response.json(); })
  .then(function (entries) { renderBlogList(entries); })
  .catch(function () {
    document.getElementById('blog-list').innerHTML =
      '<p><em>Could not load the submissions list. Try refreshing, or check <a href="blog-manifest.json">blog-manifest.json</a> directly.</em></p>';
  });

function renderBlogList(entries) {
  var container = document.getElementById('blog-list');

  if (!entries || entries.length === 0) {
    container.innerHTML = '<p><em>Nothing shared yet — be the first! See the Contributing section above.</em></p>';
    return;
  }

  var byMonth = {};
  var order = [];
  entries.forEach(function (entry) {
    var monthKey = entry.date.slice(0, 7); // YYYY-MM
    if (!byMonth[monthKey]) {
      byMonth[monthKey] = [];
      order.push(monthKey);
    }
    byMonth[monthKey].push(entry);
  });
  order.sort().reverse();

  var monthNames = ['January', 'February', 'March', 'April', 'May', 'June',
                     'July', 'August', 'September', 'October', 'November', 'December'];

  var html = '';
  order.forEach(function (monthKey) {
    var parts = monthKey.split('-');
    var label = monthNames[parseInt(parts[1], 10) - 1] + ' ' + parts[0];
    html += '<h3>' + label + '</h3><ul>';
    byMonth[monthKey].forEach(function (entry) {
      var href = 'Blog/' + encodeURIComponent(entry.folder) + '/' + encodeURIComponent(entry.file);
      var formatBadge = entry.format ? ' <em>(' + entry.format + ')</em>' : '';
      html += '<li><a href="' + href + '">' + entry.title + '</a>' + formatBadge +
              ' — ' + entry.contributor + ', ' + entry.date +
              '<br>' + entry.description + '</li>';
    });
    html += '</ul>';
  });

  container.innerHTML = html;
}
</script>
