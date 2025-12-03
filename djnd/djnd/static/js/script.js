document.addEventListener("alpine:init", () => {
  Alpine.data("subscribe", () => ({
    loading: false,

    subscribeToNewsletter(id, newsletter_name) {
      this.loading = true;

      const email = document.getElementById(`subscribe-email-${id}`).value;

      let campaign_slug = "danes-je-nov-dan";
      let segment_id = 21; // default id = Občasnik
      if (newsletter_name === "programmers_newsletter") {
        campaign_slug = "programerski-novicnik";
        segment_id = 37; // Programerski novičnik
      }

      // const options = {
      //   method: "POST",
      //   headers: {
      //     "Content-Type": "application/json",
      //   },
      //   body: JSON.stringify({
      //     email: email,
      //     segment_id: segment_id,
      //   }),
      // };

      // fetch("https://podpri.lb.djnd.si/api/subscribe/", options)
      //   .then((response) => response.json())
      //   .then((data) => {
      //     this.loading = false;
      //     if (data.msg === "mail sent") {
      //       alert(window.NEWSLETTER_TEXT_SUCCESS);
      //       document.getElementById(`subscribe-email-${id}`).value = "";
      //       document.getElementById(`subscribe-consent-${id}`).checked = false;
      //     } else {
      //       alert(window.NEWSLETTER_TEXT_FAILURE);
      //     }
      //   })
      //   .catch((error) => {
      //     this.loading = false;
      //     console.error(error);
      //   });

      let url = `https://moj.djnd.si/${campaign_slug}/prijava?segment_id=${segment_id}`;
      url += `&email=${encodeURIComponent(email)}`;
      window.open(`${url}`, `_blank`);
      this.loading = false;
    },
  }));
});

function loadMoreOnHomePage(button) {
  const loader = button.closest(".grid").querySelector("#loader-container");
  loader.style.display = "";
  loader.removeAttribute("hx-disable");
  const container = button.closest(".absolute");
  container.remove();
  htmx.process(loader);
}

function filterOurWork() {
  document.getElementById("our-work-form").submit();
}

function homepageLinkedSentences() {
  const introEl = document.querySelector("[data-introduction]");
  const boxEls = document.querySelectorAll("[data-linked-sentence]");

  if (!introEl || !boxEls.length) return;

  // Wrap linked sentences in span elements
  boxEls.forEach((boxEl, i) => {
    const sentence = boxEl.dataset.linkedSentence;
    const color = boxEl.dataset.color;
    const introChildren = introEl.querySelectorAll(":scope > *");
    introChildren.forEach((introChild) => {
      if (introChild.textContent.includes(sentence)) {
        const href = boxEl.closest("a")?.getAttribute("href");
        introChild.innerHTML = introChild.innerHTML.replace(
          sentence,
          `<a href="${href}" data-linked-box-index="${i}" class="theme-color-${color}">${sentence}</a>`
        );
      }
    });
  });

  // Insert icons before every linked sentence
  const sentenceEls = introEl.querySelectorAll("[data-linked-box-index]");
  sentenceEls.forEach((sentenceEl) => {
    const i = sentenceEl.dataset.linkedBoxIndex;
    const iconEl = boxEls[i].querySelector("img").cloneNode(true);
    iconEl.style.display = "inline-block";
    iconEl.style.width = "1.25em";
    iconEl.style.height = "1.25em";
    iconEl.style.marginTop = "-0.25em";
    iconEl.style.overflow = "hidden";
    const iconContainer = document.createElement("span");
    iconContainer.appendChild(iconEl);
    iconContainer.appendChild(document.createTextNode(" "));
    sentenceEl.parentElement.insertBefore(iconContainer, sentenceEl);
  });

  // On box hover, highlight the corresponding sentence
  boxEls.forEach((box, i) => {
    box.addEventListener("mouseenter", () => {
      const sentenceEl = introEl.querySelector(
        `[data-linked-box-index="${i}"]`
      );
      if (!sentenceEl) return;
      sentenceEl.classList.add("forced-animated-bg-show");
      sentenceEl.classList.remove("forced-animated-bg-hide");
    });
    box.addEventListener("mouseleave", () => {
      const sentenceEl = introEl.querySelector(
        `[data-linked-box-index="${i}"]`
      );
      if (!sentenceEl) return;
      if (sentenceEl.classList.contains("forced-animated-bg-show")) {
        sentenceEl.classList.remove("forced-animated-bg-show");
        sentenceEl.classList.add("forced-animated-bg-hide");
      }
    });
  });

  // On sentence hover, highlight the corresponding box
  sentenceEls.forEach((sentenceEl) => {
    const i = sentenceEl.dataset.linkedBoxIndex;
    sentenceEl.addEventListener("mouseenter", () => {
      sentenceEl.classList.add("forced-animated-bg-show");
      sentenceEl.classList.remove("forced-animated-bg-hide");
      boxEls[i].classList.add("forced-box-scale");
    });
    sentenceEl.addEventListener("mouseleave", () => {
      sentenceEl.classList.remove("forced-animated-bg-show");
      sentenceEl.classList.add("forced-animated-bg-hide");
      boxEls[i].classList.remove("forced-box-scale");
    });
  });

  window.addEventListener("pageshow", (event) => {
    if (event.persisted) {
      // Clear all highlights on browser back-forward navigation
      sentenceEls.forEach((sentenceEl) => {
        const i = sentenceEl.dataset.linkedBoxIndex;
        sentenceEl.classList.remove("forced-animated-bg-show");
        sentenceEl.classList.remove("forced-animated-bg-hide");
        boxEls[i].classList.remove("forced-box-scale");
      });
    }
  });
}

function clickableActivityCards() {
  const setupClickHandler = (card) => {
    card.style.cursor = "pointer";
    card.addEventListener("click", (event) => {
      // Don't navigate if text is selected
      const selectedText = window.getSelection().toString();
      if (selectedText) return;

      if (!event.target.closest("a")) {
        const link = card.querySelector(".js-activity-card-link");
        if (link) {
          link.click();
        }
      }
    });
  };

  // handle existing cards
  document.querySelectorAll(".js-activity-card").forEach(setupClickHandler);

  // handle dynamically added cards
  new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      mutation.addedNodes.forEach((node) => {
        if (node.classList?.contains("js-activity-card")) {
          setupClickHandler(node);
        }
        node
          .querySelectorAll?.(".js-activity-card")
          ?.forEach(setupClickHandler);
      });
    });
  }).observe(document.body, { childList: true, subtree: true });
}

document.addEventListener("DOMContentLoaded", function () {
  homepageLinkedSentences();
  clickableActivityCards();

  const menuButton = document.querySelector("#menu-button");
  const sidebar = document.querySelector("#sidebar");

  menuButton.addEventListener("click", () => {
    const isClosed = sidebar.classList.contains("md-max:-translate-x-full");
    if (isClosed) {
      sidebar.classList.remove("md-max:-translate-x-full");
      menuButton.setAttribute("aria-expanded", "true");
      menuButton.querySelector('img[alt="Open menu"]').classList.add("hidden");
      menuButton
        .querySelector('img[alt="Close menu"]')
        .classList.remove("hidden");
    } else {
      sidebar.classList.add("md-max:-translate-x-full");
      menuButton.setAttribute("aria-expanded", "false");
      menuButton
        .querySelector('img[alt="Open menu"]')
        .classList.remove("hidden");
      menuButton.querySelector('img[alt="Close menu"]').classList.add("hidden");
    }
  });
});
