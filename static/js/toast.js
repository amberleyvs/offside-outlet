// static/js/toast.js
(() => {
// ---------- utils ----------
const cls = (...a) => a.filter(Boolean).join(' ');
const el = (tag, { className = '', text = '', attrs = {} } = {}) => {
const n = document.createElement(tag);
if (className) n.className = className;
if (text) n.textContent = text;
for (const [k, v] of Object.entries(attrs)) n.setAttribute(k, v);
return n;
 };
// ---------- root ----------
let root = document.getElementById('toast-root');
if (!root) {
root = el('div', {
attrs: { id: 'toast-root', 'aria-live': 'polite', 'aria-atomic': 'true' },
className: cls(
'fixed top-6 left-1/2 -translate-x-1/2 z-[60]',
'w-full max-w-[92vw] sm:max-w-md',
'pointer-events-none space-y-3'
 )
 });
document.body.appendChild(root);
 }
// ---------- themes ----------
const THEME = {
success: { wrap: 'bg-emerald-50 border border-emerald-200 text-emerald-900', btn: 'text-emerald-600 hover:bg-emerald-100', icon: '✅' },
error: { wrap: 'bg-rose-50 border border-rose-200 text-rose-900', btn: 'text-rose-600 hover:bg-rose-100', icon: '⛔' },
info: { wrap: 'bg-sky-50 border border-sky-200 text-sky-900', btn: 'text-sky-600 hover:bg-sky-100', icon: 'ℹ️' },
warning: { wrap: 'bg-amber-50 border border-amber-200 text-amber-900', btn: 'text-amber-600 hover:bg-amber-100', icon: '⚠️' },
normal: { wrap: 'bg-white border border-gray-200 text-gray-900', btn: 'text-gray-600 hover:bg-gray-100', icon: '💬' },
 };
// ---------- build ----------
function makeToast(title, message, type) {
const t = THEME[type] || THEME.normal;
const wrap = el('div', {
className: cls(
'pointer-events-auto flex items-start gap-3 p-4 rounded-xl shadow-md',
'transition-all duration-300 opacity-0 translate-y-1',
'backdrop-blur-sm',
t.wrap
 ),
attrs: { role: 'status' }
 });
const icon = el('div', { className: 'text-xl leading-none flex-shrink-0', text: t.icon });
const content = el('div', { className: 'flex-1 min-w-0' });
const titleEl = el('h3', { className: 'font-semibold text-sm mb-0.5 truncate', text: title || '' });
const msgEl = el('p', { className: 'text-sm opacity-90 line-clamp-2', text: message || '' });
content.append(titleEl, msgEl);
const close = el('button', {
className: cls('flex-shrink-0 w-6 h-6 flex items-center justify-center rounded-md text-sm font-medium transition-colors', t.btn),
text: '×',
attrs: { type: 'button', 'aria-label': 'Close' }
 });
wrap.append(icon, content, close);
close.addEventListener('click', () => removeToast(wrap));
return wrap;
 }
// ---------- animate & remove ----------
function animateIn(node) {
requestAnimationFrame(() => node.classList.remove('opacity-0', 'translate-y-1'));
 }
function removeToast(node) {
node.classList.add('opacity-0', 'translate-y-1');
setTimeout(() => node.remove(), 220);
 }
// ---------- public API ----------
window.showToast = (title, message, type = 'normal', duration = 3000) => {
const node = makeToast(title, message, type);
root.appendChild(node);
animateIn(node);
// auto-hide with hover pause
let timer = null, remaining = duration, start = Date.now();
const startTimer = () => {
if (duration <= 0) return;
clearTimeout(timer);
start = Date.now();
timer = setTimeout(() => removeToast(node), remaining);
 };
const pause = () => {
if (!timer) return;
remaining -= Date.now() - start;
clearTimeout(timer);
 };
const resume = () => {
if (remaining > 0) startTimer();
 };
node.addEventListener('mouseenter', pause);
node.addEventListener('mouseleave', resume);
startTimer();
 };
})();