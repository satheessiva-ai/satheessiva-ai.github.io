'use strict';
document.documentElement.classList.add('js');

const menuToggle = document.querySelector('.menu-toggle');
const navigation = document.getElementById('navigation');
function closeMenu() {
  navigation.classList.remove('is-open');
  menuToggle.setAttribute('aria-expanded', 'false');
  menuToggle.setAttribute('aria-label', 'Open navigation');
  menuToggle.querySelector('span').textContent = '+';
}
menuToggle.addEventListener('click', () => {
  const isOpen = navigation.classList.toggle('is-open');
  menuToggle.setAttribute('aria-expanded', String(isOpen));
  menuToggle.setAttribute('aria-label', isOpen ? 'Close navigation' : 'Open navigation');
  menuToggle.querySelector('span').textContent = isOpen ? '−' : '+';
});
navigation.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && navigation.classList.contains('is-open')) {
    closeMenu();
    menuToggle.focus();
  }
});
document.addEventListener('click', event => {
  if (!navigation.contains(event.target) && !menuToggle.contains(event.target)) closeMenu();
});

const filters = document.querySelector('[data-filters]');
const filterButtons = Array.from(document.querySelectorAll('[data-filter]'));
const cases = Array.from(document.querySelectorAll('[data-category]'));
filters.hidden = false;
filterButtons.forEach(button => button.addEventListener('click', () => {
  const category = button.dataset.filter;
  let visibleCount = 0;
  filterButtons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  cases.forEach(story => {
    story.hidden = category !== 'all' && story.dataset.category !== category;
    if (!story.hidden) visibleCount++;
  });
  document.getElementById('filter-status').textContent = `${visibleCount} project ${visibleCount === 1 ? 'story' : 'stories'} shown.`;
}));

const copyButton = document.querySelector('[data-copy-email]');
if (navigator.clipboard && window.isSecureContext) {
  copyButton.hidden = false;
  copyButton.addEventListener('click', async () => {
    const status = document.getElementById('copy-status');
    try {
      await navigator.clipboard.writeText('satheess@outlook.com');
      status.textContent = 'Email address copied.';
      copyButton.textContent = 'Copied';
      window.setTimeout(() => { copyButton.textContent = 'Copy'; }, 2500);
    } catch {
      status.textContent = 'Please select the email address to copy it.';
    }
  });
}
