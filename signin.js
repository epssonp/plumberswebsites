(function () {
  'use strict';

  /** Matches worker `APP_ORIGIN` / deployed customer app. */
  var APP_ORIGIN = 'https://app.plumberswebsites.com';
  var MAGIC_LINK_PATH = '/api/auth/magic-link';
  var APP_SIGN_IN_PATH = '/sign-in';

  var DEFAULT_SUCCESS_MESSAGE =
    "If this address is eligible, we've sent a secure sign-in link. Check your inbox.";

  var form = document.getElementById('signin-form');
  var emailInput = document.getElementById('signin-email');
  var submitButton = document.getElementById('signin-submit');
  var fieldError = document.getElementById('signin-field-error');
  var formError = document.getElementById('signin-form-error');
  var formSection = document.getElementById('signin-form-section');
  var successSection = document.getElementById('signin-success-section');
  var successMessage = document.getElementById('signin-success-message');
  var crossOriginNotice = document.getElementById('signin-cross-origin-notice');

  if (!form || !emailInput || !submitButton) {
    return;
  }

  function normalizeAccountEmail(raw) {
    return String(raw).trim().toLowerCase();
  }

  function isPlausibleAccountEmail(email) {
    if (!email) return false;
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  function magicLinkUrl() {
    return APP_ORIGIN.replace(/\/$/, '') + MAGIC_LINK_PATH;
  }

  function appSignInUrl() {
    return APP_ORIGIN.replace(/\/$/, '') + APP_SIGN_IN_PATH;
  }

  /**
   * Production Worker CORS (`worker/cors.ts`) allows only `APP_ORIGIN` (plus localhost in dev).
   * Magic-link POST does not set session cookies; credentials are not required for this call.
   */
  function canCallMagicLinkApiFromThisPage() {
    var pageOrigin = window.location.origin;
    var appOrigin = APP_ORIGIN.replace(/\/$/, '');

    if (pageOrigin === appOrigin) {
      return true;
    }

    if (/^https?:\/\/(localhost|127\.0\.0\.1)(:\d+)?$/.test(pageOrigin)) {
      return true;
    }

    return false;
  }

  function setFieldError(message) {
    if (!fieldError) return;
    if (message) {
      fieldError.textContent = message;
      fieldError.hidden = false;
      emailInput.setAttribute('aria-invalid', 'true');
    } else {
      fieldError.textContent = '';
      fieldError.hidden = true;
      emailInput.removeAttribute('aria-invalid');
    }
  }

  function setFormError(message) {
    if (!formError) return;
    if (message) {
      formError.textContent = message;
      formError.hidden = false;
    } else {
      formError.textContent = '';
      formError.hidden = true;
    }
  }

  function setSubmitting(submitting) {
    submitButton.disabled = submitting;
    submitButton.setAttribute('aria-busy', submitting ? 'true' : 'false');
    emailInput.disabled = submitting;
    submitButton.textContent = submitting ? 'Sending…' : 'Email me my sign-in link';
  }

  function showSuccess(message) {
    if (successMessage) {
      successMessage.textContent = message || DEFAULT_SUCCESS_MESSAGE;
    }
    if (formSection) {
      formSection.hidden = true;
    }
    if (successSection) {
      successSection.hidden = false;
    }
    if (crossOriginNotice) {
      crossOriginNotice.hidden = true;
    }
  }

  async function parseJsonResponse(response) {
    var text = await response.text();
    var body = null;
    if (text) {
      try {
        body = JSON.parse(text);
      } catch (err) {
        body = { error: text };
      }
    }
    if (!response.ok) {
      var message =
        body &&
        typeof body === 'object' &&
        !Array.isArray(body) &&
        typeof body.error === 'string'
          ? body.error
          : 'Request failed (' + response.status + ')';
      throw new Error(message);
    }
    return body;
  }

  async function requestMagicLink(accountEmail) {
    var response = await fetch(magicLinkUrl(), {
      method: 'POST',
      credentials: 'omit',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ accountEmail: accountEmail }),
    });

    var data = await parseJsonResponse(response);
    if (data && typeof data.message === 'string' && data.message.length > 0) {
      return data.message;
    }
    return DEFAULT_SUCCESS_MESSAGE;
  }

  if (crossOriginNotice && !canCallMagicLinkApiFromThisPage()) {
    crossOriginNotice.hidden = false;
  }

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    setFieldError(null);
    setFormError(null);

    var normalized = normalizeAccountEmail(emailInput.value);
    if (!isPlausibleAccountEmail(normalized)) {
      setFieldError('Enter a valid email address.');
      emailInput.focus();
      return;
    }

    if (!canCallMagicLinkApiFromThisPage()) {
      window.location.assign(appSignInUrl());
      return;
    }

    setSubmitting(true);

    requestMagicLink(normalized)
      .then(function (message) {
        showSuccess(message);
      })
      .catch(function () {
        setFormError(
          'We could not send a sign-in link right now. Check your connection and try again, or continue on the secure app sign-in page.',
        );
        var fallback = document.getElementById('signin-app-fallback');
        if (fallback) {
          fallback.hidden = false;
        }
      })
      .finally(function () {
        setSubmitting(false);
      });
  });
})();
