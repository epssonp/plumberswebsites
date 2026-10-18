(function () {
  'use strict';

  var data = window.PLW_ACADEMY;
  if (!data) {
    return;
  }

  function normalize(s) {
    return (s || '').toLowerCase().trim();
  }

  function buildSearchIndex() {
    var index = [];

    (data.categories || []).forEach(function (cat) {
      index.push({
        type: 'Category',
        title: cat.title,
        description: cat.description,
        url: cat.url.replace('https://plumberswebsites.com', ''),
        keywords: cat.title,
        categoryId: cat.id,
      });
      (cat.subcategories || []).forEach(function (sub) {
        index.push({
          type: 'Section',
          title: sub.title,
          description: sub.description,
          url: sub.url.replace('https://plumberswebsites.com', ''),
          keywords: sub.title + ' ' + cat.title,
          categoryId: cat.id,
        });
      });
    });

    (data.publishedArticles || []).forEach(function (art) {
      if (art.status !== 'published' || !art.url) {
        return;
      }
      index.push({
        type: 'Guide',
        title: art.title,
        description: art.summary || '',
        url: art.url.replace('https://plumberswebsites.com', ''),
        keywords: (art.title + ' ' + (art.keywords || '')).trim(),
        categoryId: art.categoryId || null,
      });
    });

    return index;
  }

  var searchIndex = buildSearchIndex();
  var form = document.getElementById('academy-search-form');
  var input = document.getElementById('academy-search-input');
  var resultsEl = document.getElementById('academy-search-results');
  var browseResults = document.getElementById('academy-browse-results');
  var categoryFilter = document.getElementById('academy-category-filter');
  var clearBtn = document.getElementById('academy-clear-search');

  function itemMatchesFilter(item, categoryId) {
    if (!categoryId) {
      return true;
    }
    if (item.type === 'Category') {
      return String(item.categoryId) === String(categoryId);
    }
    return String(item.categoryId) === String(categoryId);
  }

  function renderResults(container, query, categoryId) {
    if (!container) {
      return;
    }
    container.innerHTML = '';
    var q = normalize(query);
    var hasQuery = q.length > 0;
    var hasFilter = Boolean(categoryId);

    if (!hasQuery && !hasFilter) {
      var idle = document.createElement('p');
      idle.className = 'academy-results-message';
      idle.textContent =
        'Search categories and sections, or choose a category filter. Published guides will appear here when available.';
      container.appendChild(idle);
      return;
    }

    var matches = searchIndex.filter(function (item) {
      if (item.type === 'Guide') {
        return false;
      }
      if (!itemMatchesFilter(item, categoryId)) {
        return false;
      }
      if (!hasQuery) {
        return true;
      }
      var hay = normalize(item.title + ' ' + item.description + ' ' + item.keywords);
      return hay.indexOf(q) !== -1;
    });

    (data.publishedArticles || []).forEach(function (art) {
      if (art.status !== 'published' || !art.url) {
        return;
      }
      if (categoryId && String(art.categoryId) !== String(categoryId)) {
        return;
      }
      var hay = normalize(art.title + ' ' + (art.summary || '') + ' ' + (art.keywords || ''));
      if (hasQuery && hay.indexOf(q) === -1) {
        return;
      }
      matches.push({
        type: 'Guide',
        title: art.title,
        description: art.summary || '',
        url: art.url.replace('https://plumberswebsites.com', ''),
      });
    });

    if (matches.length === 0) {
      var msg = document.createElement('p');
      msg.className = 'academy-results-message';
      msg.textContent = 'No matches found. Try a different term or clear filters.';
      container.appendChild(msg);
      return;
    }

    matches.slice(0, 24).forEach(function (item) {
      var div = document.createElement('div');
      div.className = 'academy-result-item';
      div.innerHTML =
        '<div class="academy-result-type">' +
        item.type +
        '</div>' +
        '<a href="' +
        item.url +
        '">' +
        item.title +
        '</a>' +
        (item.description
          ? '<p class="academy-result-desc">' + item.description.slice(0, 160) + '</p>'
          : '');
      container.appendChild(div);
    });

    if (matches.length > 24) {
      var more = document.createElement('p');
      more.className = 'academy-results-message';
      more.textContent =
        'Showing 24 of ' + matches.length + ' matches. Refine your search for narrower results.';
      container.appendChild(more);
    }
  }

  function runSearch() {
    var q = input ? input.value : '';
    var cat = categoryFilter ? categoryFilter.value : '';
    renderResults(resultsEl, q, cat);
    renderResults(browseResults, q, cat);
  }

  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      runSearch();
      var browse = document.getElementById('academy-browse');
      if (browse) {
        browse.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  }

  if (categoryFilter) {
    categoryFilter.addEventListener('change', runSearch);
  }

  if (clearBtn) {
    clearBtn.addEventListener('click', function () {
      if (input) {
        input.value = '';
      }
      if (categoryFilter) {
        categoryFilter.value = '';
      }
      runSearch();
      if (input) {
        input.focus();
      }
    });
  }

  runSearch();
})();
