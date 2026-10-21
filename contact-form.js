(function () {
  "use strict";

  var WEB3FORMS_URL = "https://api.web3forms.com/submit";
  var EMAIL_PATTERN = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

  var form = document.getElementById("contact-form");
  if (!form) {
    return;
  }

  var statusEl = document.getElementById("contact-form-status");
  var submitButton = form.querySelector('button[type="submit"]');
  var isSubmitting = false;

  var fieldConfig = [
    {
      input: document.getElementById("contact-name"),
      label: "Name",
      validate: function (value) {
        if (!value.trim()) {
          return "Please enter your name.";
        }
        return "";
      },
    },
    {
      input: document.getElementById("contact-email"),
      label: "Email address",
      validate: function (value) {
        var trimmed = value.trim();
        if (!trimmed) {
          return "Please enter your email address.";
        }
        if (!EMAIL_PATTERN.test(trimmed)) {
          return "Please enter a valid email address.";
        }
        return "";
      },
    },
    {
      input: document.getElementById("contact-subject"),
      label: "Subject",
      validate: function (value) {
        if (!value.trim()) {
          return "Please enter a subject.";
        }
        return "";
      },
    },
    {
      input: document.getElementById("contact-message"),
      label: "Message",
      validate: function (value) {
        var trimmed = value.trim();
        if (!trimmed) {
          return "Please enter your message.";
        }
        if (trimmed.length < 10) {
          return "Please enter a message with at least 10 characters.";
        }
        return "";
      },
    },
  ];

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

  function clearFieldErrors() {
    fieldConfig.forEach(function (field) {
      if (field.input) {
        field.input.removeAttribute("aria-invalid");
      }
    });
  }

  function validateForm() {
    clearFieldErrors();
    for (var i = 0; i < fieldConfig.length; i++) {
      var field = fieldConfig[i];
      if (!field.input) {
        continue;
      }
      var message = field.validate(field.input.value);
      if (message) {
        field.input.setAttribute("aria-invalid", "true");
        field.input.focus();
        setStatus(field.label + ": " + message, "error");
        return false;
      }
    }
    setStatus("", null);
    return true;
  }

  function isHoneypotTripped() {
    var botcheck = form.querySelector('input[name="botcheck"]');
    return botcheck && botcheck.checked;
  }

  function setSubmitting(submitting) {
    isSubmitting = submitting;
    if (submitButton) {
      submitButton.disabled = submitting;
      submitButton.setAttribute("aria-busy", submitting ? "true" : "false");
    }
    form.querySelectorAll("input, textarea, button").forEach(function (el) {
      if (el !== submitButton) {
        el.disabled = submitting;
      }
    });
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    setStatus("", null);

    if (isSubmitting) {
      return;
    }

    if (!validateForm()) {
      return;
    }

    if (isHoneypotTripped()) {
      form.reset();
      clearFieldErrors();
      setStatus(
        "Thank you — your message was sent. We will reply to the email address you provided.",
        "success"
      );
      return;
    }

    var formData = new FormData(form);
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
          clearFieldErrors();
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
