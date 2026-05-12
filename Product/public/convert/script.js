document.addEventListener('DOMContentLoaded', function() {
  const params = new URLSearchParams(window.location.search);
  const variant = params.get('variant') || 'direct';
  const source = params.get('source') || 'unknown';

  trackEvent('convert_view', {
    variant: variant,
    source: source
  });

  document.querySelectorAll('.cta-buttons a, .card a').forEach(link => {
    link.addEventListener('click', function(e) {
      const linkType = this.classList.contains('primary') ? 'primary_cta' : 'secondary_cta';
      const docType = this.getAttribute('href').includes('claudekit') ? 'claudekit' : 'docs';

      trackEvent('convert_cta_click', {
        cta_type: linkType,
        doc_type: docType,
        href: this.getAttribute('href')
      });
    });
  });

  function trackEvent(event, data) {
    console.log('[Analytics]', event, data);

    if (typeof window.gtag !== 'undefined') {
      window.gtag('event', event, data);
    }
  }

  if (variant === 'soft') {
    document.querySelector('.cta').style.display = 'none';
  }
});