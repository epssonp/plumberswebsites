(function () {
  "use strict";

  var WEB3FORMS_URL = "https://api.web3forms.com/submit";

  var form = document.getElementById("contact-form");
  if (!form) {
    return;
  }

  var statusEl = document.getElementById("contact-form-status");
  var submitButton = form.querySelector('button[type="submit"]');

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

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    setStatus("", null);

    var formData = new FormData(form);
    if (formData.get("company_website")) {
      form.reset();
      setStatus(
        "Thank you — your message was sent. We will reply to the email address you provided.",
        "success"
      );
      return;
    }

    setSubmitting(true);

    fetch(WEB3FORMS_URL, {
      method: "POST",
      body: formData,
      headers: { Accept: "application/json" },
    })
      .then(function (response) {
        return response.json();
      })
      .then(function (data) {
        if (data && data.success) {
          form.reset();
          setStatus(
            "Thank you — your message was sent. We will reply to the email address you provided.",
            "success"
          );
          return;
        }
        setStatus(
          (data && data.message) ||
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
