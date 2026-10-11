const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.nav-links');

if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(open));
  });

  nav.addEventListener('click', (event) => {
    if (event.target.closest('a')) {
      nav.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
    }
  });
}

const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const revealItems = document.querySelectorAll('.reveal');

if (!reducedMotion && 'IntersectionObserver' in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  revealItems.forEach((item) => observer.observe(item));
} else {
  revealItems.forEach((item) => item.classList.add('is-visible'));
}

document.querySelectorAll('[data-year]').forEach((item) => {
  item.textContent = new Date().getFullYear();
});

document.querySelectorAll('[data-copy-target]').forEach((button) => {
  button.addEventListener('click', async () => {
    const target = document.getElementById(button.dataset.copyTarget);
    if (!target) return;
    const original = button.textContent;
    try {
      await navigator.clipboard.writeText(target.textContent.trim());
      button.textContent = 'Đã sao chép';
    } catch (_) {
      button.textContent = 'Hãy chọn văn bản để sao chép';
    }
    window.setTimeout(() => { button.textContent = original; }, 1800);
  });
});

// Tải bộ đếm lượt truy cập trên mọi trang mà không hiển thị tiện ích bản đồ của nó.
if (!document.getElementById('mapmyvisitors')) {
  const visitorCounter = document.createElement('div');
  visitorCounter.hidden = true;
  visitorCounter.setAttribute('aria-hidden', 'true');

  const visitorScript = document.createElement('script');
  visitorScript.type = 'text/javascript';
  visitorScript.id = 'mapmyvisitors';
  visitorScript.src = '//mapmyvisitors.com/map.js?d=Eqk94B7gSSYT-MjlvlBM58yL8NiiHN5avYHSIrHftqY&cl=ffffff&w=a';

  visitorCounter.appendChild(visitorScript);
  document.body.appendChild(visitorCounter);
}

// Tải Cloudflare Web Analytics trên mọi trang. Beacon này không có giao diện hiển thị.
if (!document.querySelector('script[data-cf-beacon]')) {
  const cloudflareBeacon = document.createElement('script');
  cloudflareBeacon.type = 'module';
  cloudflareBeacon.src = 'https://static.cloudflareinsights.com/beacon.min.js';
  cloudflareBeacon.dataset.cfBeacon = JSON.stringify({
    token: '704ec463af8d4b90b01c12d713ceed53'
  });
  document.head.appendChild(cloudflareBeacon);
}
