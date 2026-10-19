(function () {
  "use strict";

  var form = document.getElementById("contact-form");
  if (!form) {
    return;
  }

  var statusEl = document.getElementById("contact-form-status");
  var submitButton = form.querySelector('button[type="submit"]');
  var turnstileMount = document.getElementById("contact-turnstile");
  var turnstileWidgetId = null;

  function setStatus(message, type) {
    if (!statusEl) {
      return;
    }
    statusEl.textContent = message;
    statusEl.hidden = !message;
    statusEl.classList.remove(
      "contact-form-status--success",
      "contact-form-status--error"
    );
    if (type) {
      statusEl.classList.add("contact-form-status--" + type);
    }
  }

  function setSubmitting(isSubmitting) {
    if (submitButton) {
      submitButton.disabled = isSubmitting;
      submitButton.setAttribute("aria-busy", isSubmitting ? "true" : "false");
    }
    form.querySelectorAll("input, textarea, button").forEach(function (el) {
      if (el !== submitButton) {
        el.disabled = isSubmitting;
      }
    });
  }

  function renderTurnstile(siteKey) {
    if (!turnstileMount || !siteKey || !window.turnstile) {
      return;
    }
    turnstileWidgetId = window.turnstile.render(turnstileMount, {
      sitekey: siteKey,
      theme: "light",
    });
  }

  fetch("/api/contact", { headers: { Accept: "application/json" } })
    .then(function (response) {
      return response.json();
    })
    .then(function (config) {
      if (config && config.turnstileSiteKey) {
        var script = document.createElement("script");
        script.src =
          "https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit";
        script.async = true;
        script.defer = true;
        script.onload = function () {
          renderTurnstile(config.turnstileSiteKey);
        };
        document.head.appendChild(script);
      }
    })
    .catch(function () {
      /* Turnstile is optional */
    });

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    setStatus("", null);

    var formData = new FormData(form);
    var payload = {
      name: formData.get("name"),
      email: formData.get("email"),
      subject: formData.get("subject"),
      message: formData.get("message"),
      company_website: formData.get("company_website"),
    };

    if (window.turnstile && turnstileWidgetId !== null) {
      payload.turnstileToken = window.turnstile.getResponse(turnstileWidgetId);
    }

    setSubmitting(true);

    fetch("/api/contact", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify(payload),
    })
      .then(function (response) {
        return response.json().then(function (data) {
          return { ok: response.ok, data: data };
        });
      })
      .then(function (result) {
        if (result.ok && result.data.ok) {
          form.reset();
          if (window.turnstile && turnstileWidgetId !== null) {
            window.turnstile.reset(turnstileWidgetId);
          }
          setStatus(
            "Thank you — your message was sent. We will reply to the email address you provided.",
            "success"
          );
          return;
        }
        setStatus(
          (result.data && result.data.error) ||
            "We could not send your message. Please try again.",
          "error"
        );
      })
      .catch(function () {
        setStatus(
          "We could not send your message. Please check your connection and try again.",
          "error"
        );
      })
      .finally(function () {
        setSubmitting(false);
      });
  });
})();
