document.addEventListener('alpine:init', () => {
  Alpine.data('subscribe', () => ({
    loading: false,

    subscribeToNewsletter(id) {
      this.loading = true;

      const email = document.getElementById(`subscribe-email-${id}`).value;
      console.log('email', email);
      console.log('id', id);

      const options = {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          email: email,
          segment_id: 21,
        }),
      };

      fetch('https://podpri.lb.djnd.si/api/subscribe/', options)
        .then((response) => response.json())
        .then((data) => {
          this.loading = false;
          if (data.msg === 'mail sent') {
            alert(
              '{% translate "Hvala! Poslali smo ti sporočilo s povezavo, na kateri lahko potrdiš prijavo!" %}'
            );
            document.getElementById(`subscribe-email-${id}`).value = '';
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
  document.getElementById('our-work-form').submit();
}
