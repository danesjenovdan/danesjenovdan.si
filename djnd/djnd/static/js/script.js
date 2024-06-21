document.addEventListener("alpine:init", () => {
  Alpine.data("subscribe", () => ({
    loading: false,

    subscribeToNewsletter(id) {
      this.loading = true;

      const email = document.getElementById(`subscribe-email-${id}`).value;
      console.log("email", email);
      console.log("id", id);

      const options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          email: email,
          segment_id: 21,
        }),
      };

      fetch("https://podpri.lb.djnd.si/api/subscribe/", options)
        .then((response) => response.json())
        .then((data) => {
          this.loading = false;
          if (data.msg === "mail sent") {
            alert(
              '{% translate "Hvala! Poslali smo ti sporočilo s povezavo, na kateri lahko potrdiš prijavo!" %}'
            );
            document.getElementById(`subscribe-email-${id}`).value = "";
            document.getElementById(`subscribe-consent-${id}`).checked = false;
          } else {
            alert('{% translate "Prišlo je do napake :(" %}');
          }
        })
        .catch((error) => {
          this.loading = false;
          console.error(error);
        });
    },
  }));
});

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
        introChild.innerHTML = introChild.innerHTML.replace(
          sentence,
          `<span data-linked-box-index="${i}" class="theme-color-${color}">${sentence}</span>`
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
      sentenceEl.classList.remove("forced-animated-bg-show");
      sentenceEl.classList.add("forced-animated-bg-hide");
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
      const boxEl = boxEls[i];
      sentenceEl.classList.remove("forced-animated-bg-show");
      sentenceEl.classList.add("forced-animated-bg-hide");
      boxEls[i].classList.remove("forced-box-scale");
    });
  });
}

document.addEventListener("DOMContentLoaded", function () {
  homepageLinkedSentences();

  const menuButton = document.querySelector("#menu-button");
  const sidebar = document.querySelector("#sidebar");

  menuButton.addEventListener("click", () => {
    sidebar.classList.toggle("md-max:-translate-x-full");
  });
});
