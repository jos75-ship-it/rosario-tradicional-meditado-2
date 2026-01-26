# 📐 Arquitetura Modular - Santo Rosário PWA

## 🎯 Objetivo
Particionamento profissional do `index.html` monolítico em estrutura modular, mantendo 100% das funcionalidades.

---

## 📁 Estrutura de Diretórios

```
rosario-app/
├── index.html                  # HTML minimalista (apenas estrutura)
├── manifest.json               
├── sw.js                       
├── config.js                   # Firebase config (NÃO VERSIONAR)
│
├── css/                        # Estilos modulares
│   ├── variables.css           # Design tokens (cores, fontes, espaçamentos)
│   ├── base.css                # Reset global, body, animações
│   ├── auth.css                # Tela de autenticação
│   ├── navigation.css          # Bottom nav + tabs
│   ├── home.css                # Tab Home (welcome screen)
│   ├── prayer.css              # Tela de oração (beads, meditações)
│   ├── calendar.css            # Tab Calendário
│   ├── friends.css             # Tab Amigos
│   ├── profile.css             # Tab Perfil
│   ├── modals.css              # Modais (avatar, etc)
│   └── responsive.css          # Media queries
│
├── js/                         # JavaScript modular
│   ├── config.js               # LINK SIMBÓLICO para ../config.js
│   │
│   ├── data/                   # Dados estáticos
│   │   ├── prayers.js          # Textos das orações (export TEXTS)
│   │   └── montfort.js         # Meditações Montfort (export MONTFORT)
│   │
│   ├── utils/                  # Funções auxiliares
│   │   ├── avatar-helper.js    # getAvatarHTML() global
│   │   ├── date-helpers.js     # formatDate(), getDayOfWeek(), etc
│   │   └── firebase-errors.js  # Traduções de erros Firebase
│   │
│   ├── components/             # Componentes reutilizáveis
│   │   ├── audio-system.js     # AudioSystem (sons das contas)
│   │   ├── avatar-system.js    # Sistema de seleção de avatares
│   │   └── calendar-widget.js  # Renderização do calendário
│   │
│   ├── core/                   # Lógica principal
│   │   ├── prayer-app.js       # app object (start, next, prev, etc)
│   │   └── bead-generator.js   # generateBeads() (separado do app)
│   │
│   ├── features/               # Features isoladas
│   │   ├── auth-manager.js     # login, register, logout
│   │   ├── friends-manager.js  # searchFriend, accept/reject
│   │   └── stats-tracker.js    # Salvar estatísticas no Firebase
│   │
│   ├── templates/              # Templates HTML (injetar via JS)
│   │   ├── home.js             # HTML da tab Home
│   │   ├── rosary.js           # HTML da tab Rosary
│   │   ├── calendar.js         # HTML da tab Calendar
│   │   ├── friends.js          # HTML da tab Friends
│   │   └── profile.js          # HTML da tab Profile
│   │
│   ├── firebase-auth.js        # Módulo Firebase (ES6 module)
│   └── init.js                 # Inicialização global (DOMContentLoaded)
│
├── img/                        
│   └── avatars/                # Imagens de avatares
│       ├── therese.png
│       ├── pius.png
│       ├── thomas.png
│       ├── kolbe.jpg
│       ├── madonna.png
│       ├── agoustine.png
│       └── francis.jpg
│
└── docs/                       
    ├── ARCHITECTURE.md         # Este documento
    ├── DEPLOY_RAPIDO.md        
    └── README.md               
```

---

## 🧩 Detalhamento dos Módulos

### 1. **CSS Modular**

#### `css/variables.css` (✅ CRIADO)
```css
:root {
    /* Colors, Typography, Spacing, Transitions */
}
```

#### `css/base.css` (✅ CRIADO)
```css
/* Reset, body styles, utility classes, global animations */
```

#### `css/auth.css`
```css
/* #auth-screen, .auth-container, forms, tabs, errors */
```

#### `css/navigation.css`
```css
/* .bottom-nav, .nav-item, .tab-content */
```

#### `css/home.css`
```css
/* .home-cross, .home-title, .menu-section, .btn-mystery */
```

#### `css/prayer.css`
```css
/* #prayer-screen, .rosary-rail, .bead, .prayer-main */
/* Animações das contas, trilho, meditations-box */
```

#### `css/calendar.css`
```css
/* #calendar-grid, .calendar-day, navegação mês */
```

#### `css/friends.css`
```css
/* .friend-card, #friend-profile-view, search */
```

#### `css/profile.css`
```css
/* #profile-avatar, .stat, logout button */
```

#### `css/modals.css`
```css
/* #avatar-modal, .avatar-grid, .avatar-option */
```

#### `css/responsive.css`
```css
/* @media queries para mobile, landscape, etc */
```

---

### 2. **JavaScript Modular**

#### `js/data/prayers.js` (✅ CRIADO)
```javascript
export const TEXTS = { cross, credo, pater, ave, gloria, fatima, salve };
```

#### `js/data/montfort.js`
```javascript
export const MONTFORT = {
    intro: [...],
    gozosos: { name, mysteries: [...] },
    dolorosos: { name, mysteries: [...] },
    gloriosos: { name, mysteries: [...] }
};
```

#### `js/utils/avatar-helper.js`
```javascript
// Função global já existente
window.getAvatarHTML = function(avatarValue, size = '100%') {
    if (!avatarValue) return '👤';
    if (avatarValue.indexOf('.') > -1) {
        return `<img src="img/avatars/${avatarValue}" class="avatar-img" ...>`;
    }
    return `<div ...>${avatarValue}</div>`;
};
```

#### `js/utils/date-helpers.js`
```javascript
export function getTodayMystery() {
    const dayMap = { 0: 'Gloriosos', 1: 'Gozosos', ... };
    return dayMap[new Date().getDay()];
}

export function formatDateKey(date) {
    return `${date.getFullYear()}-${String(date.getMonth() + 1).padStart(2, '0')}-${String(date.getDate()).padStart(2, '0')}`;
}
```

#### `js/utils/firebase-errors.js`
```javascript
export function getFirebaseErrorMessage(errorCode) {
    const errors = {
        'auth/email-already-in-use': 'Este nome de usuário já está em uso!',
        ...
    };
    return errors[errorCode] || 'Erro desconhecido';
}
```

#### `js/components/audio-system.js`
```javascript
export const AudioSystem = {
    ctx: null,
    enabled: false,
    init() { ... },
    playBead(type) { ... },
    playBell() { ... },
    playComplete() { ... },
    toggle() { ... }
};
```

#### `js/components/avatar-system.js`
```javascript
const AVATARS = ['therese.png', 'pius.png', ...];
let selectedAvatar = AVATARS[0];

export function renderAvatarGrid() { ... }
export function selectAvatar(filename, element) { ... }

window.openAvatarModal = function() { ... };
window.closeAvatarModal = function() { ... };
window.saveAvatar = async function() { ... };
```

#### `js/components/calendar-widget.js`
```javascript
export let currentCalendarMonth = new Date().getMonth();
export let currentCalendarYear = new Date().getFullYear();

export function renderCalendar() {
    // Lógica de renderização do calendário
}

export function navigateToPrevMonth() { ... }
export function navigateToNextMonth() { ... }
```

#### `js/core/bead-generator.js`
```javascript
import { MONTFORT } from '../data/montfort.js';

export function generateBeads(type) {
    const beads = [];
    let id = 0;
    const add = (beadType, name, textKey, meditation = '', meta = {}) => {
        beads.push({ id: id++, beadType, name, textKey, meditation, ...meta });
    };
    
    // Lógica de geração de contas
    add('special', 'Sinal da Cruz', 'cross', ...);
    add('special', 'Creio', 'credo', ...);
    // ... resto da lógica
    
    return beads;
}
```

#### `js/core/prayer-app.js`
```javascript
import { AudioSystem } from '../components/audio-system.js';
import { TEXTS } from '../data/prayers.js';
import { generateBeads } from './bead-generator.js';

export const app = {
    state: { type: null, beads: [], index: 0, showText: false },
    els: {},
    
    init() {
        this.els = { /* cache de elementos DOM */ };
        this.setupGestures();
        this.setupKeyboard();
    },
    
    start(type) { ... },
    next() { ... },
    prev() { ... },
    update() { ... },
    toggleText() { ... },
    complete() { ... }
};
```

#### `js/features/auth-manager.js`
```javascript
import { getAuth, createUserWithEmailAndPassword, ... } from 'firebase/auth';
import { getDatabase, ref, set } from 'firebase/database';
import { getFirebaseErrorMessage } from '../utils/firebase-errors.js';

function usernameToEmail(username) {
    return username.toLowerCase().replace(/\s+/g, '') + '@rosario.app';
}

export async function registerUser(username, displayName, password) { ... }
export async function loginUser(username, password) { ... }
export async function logoutUser() { ... }
```

#### `js/features/friends-manager.js`
```javascript
import { getDatabase, ref, get, update, remove } from 'firebase/database';

export async function searchFriend(username) { ... }
export async function sendFriendRequest(targetUid) { ... }
export async function loadFriends() { ... }
export async function acceptFriendRequest(friendUid) { ... }
export async function rejectFriendRequest(friendUid) { ... }
export function viewFriendProfile(uid, user) { ... }
export function backToFriendsList() { ... }
```

#### `js/features/stats-tracker.js`
```javascript
import { getDatabase, ref, get, update } from 'firebase/database';

export async function saveRosaryCompletion(aves, paters) {
    // Lógica de salvar estatísticas + calcular streak
}
```

#### `js/templates/home.js`
```javascript
export const HOME_TEMPLATE = `
<div class="home-screen-content">
    <div class="home-cross">
        <div class="home-cross-glow"></div>
    </div>
    <h1 class="home-title">Rosário</h1>
    ...
</div>
`;

// No init.js:
document.getElementById('tab-home').innerHTML = HOME_TEMPLATE;
```

#### `js/templates/rosary.js`
```javascript
export const ROSARY_TEMPLATE = `
<div style="padding: 24px;">
    <h2>Escolha o Rosário</h2>
    <button onclick="app.start('gozosos')">Mistérios Gozosos</button>
    ...
</div>
`;
```

#### `js/templates/calendar.js`
```javascript
export const CALENDAR_TEMPLATE = `
<div style="padding: 24px;">
    <h2>Calendário</h2>
    <div id="calendar-grid"></div>
    ...
</div>
`;
```

#### `js/templates/friends.js`
```javascript
export const FRIENDS_TEMPLATE = `
<div id="friends-main-view">
    <input id="friend-search-input" ...>
    <div id="friends-list"></div>
</div>
<div id="friend-profile-view" style="display:none;">...</div>
`;
```

#### `js/templates/profile.js`
```javascript
export const PROFILE_TEMPLATE = `
<div style="padding: 24px;">
    <div id="profile-avatar" onclick="openAvatarModal()">👤</div>
    <h2 id="profile-name">Usuário</h2>
    ...
</div>
`;
```

#### `js/firebase-auth.js` (ES6 Module)
```javascript
import { firebaseConfig } from './config.js';
import { initializeApp } from 'firebase/app';
import { getAuth, onAuthStateChanged } from 'firebase/auth';
import { getDatabase, ref, get } from 'firebase/database';

const firebaseApp = initializeApp(firebaseConfig);
const auth = getAuth(firebaseApp);
const database = getDatabase(firebaseApp);

// Export para uso global
window.firebaseAuth = auth;
window.firebaseDatabase = database;

// Observer de autenticação
onAuthStateChanged(auth, async (user) => {
    if (user) {
        // Carregar perfil
        const userRef = ref(database, 'users/' + user.uid);
        const snapshot = await get(userRef);
        if (snapshot.exists()) {
            window.userProfile = snapshot.val();
            window.currentUser = user;
            updateUserInterface();
        }
    } else {
        // Mostrar tela de login
        document.getElementById('main-app').classList.add('hidden');
        document.getElementById('auth-screen').classList.remove('hidden');
    }
});

function updateUserInterface() {
    // Atualizar todos os elementos da UI
}
```

#### `js/init.js` (Inicialização Global)
```javascript
import { app } from './core/prayer-app.js';
import { HOME_TEMPLATE } from './templates/home.js';
import { ROSARY_TEMPLATE } from './templates/rosary.js';
import { CALENDAR_TEMPLATE } from './templates/calendar.js';
import { FRIENDS_TEMPLATE } from './templates/friends.js';
import { PROFILE_TEMPLATE } from './templates/profile.js';

document.addEventListener('DOMContentLoaded', () => {
    // 1. Injetar templates HTML
    document.getElementById('tab-home').innerHTML = HOME_TEMPLATE;
    document.getElementById('tab-rosary').innerHTML = ROSARY_TEMPLATE;
    document.getElementById('tab-calendar').innerHTML = CALENDAR_TEMPLATE;
    document.getElementById('tab-friends').innerHTML = FRIENDS_TEMPLATE;
    document.getElementById('tab-profile').innerHTML = PROFILE_TEMPLATE;
    
    // 2. Inicializar app
    app.init();
    
    // 3. Event listeners gerais
    setupAuthTabs();
    setupNavigation();
    setupCalendarControls();
    setupFriendsSearch();
});

function setupAuthTabs() {
    document.querySelectorAll('.auth-tab').forEach(tab => {
        tab.addEventListener('click', () => { /* ... */ });
    });
}

function setupNavigation() {
    document.querySelectorAll('.nav-item[data-tab]').forEach(btn => {
        btn.addEventListener('click', () => { /* ... */ });
    });
}

function setupCalendarControls() {
    document.getElementById('prev-month-btn').addEventListener('click', navigateToPrevMonth);
    document.getElementById('next-month-btn').addEventListener('click', navigateToNextMonth);
}

function setupFriendsSearch() {
    const input = document.getElementById('friend-search-input');
    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') searchFriend();
    });
}
```

---

## 🔄 Fluxo de Execução

1. **Carregamento inicial:**
   - HTML carrega → CSS carrega
   - Scripts carregam em ordem:
     1. Templates (home.js, rosary.js, etc)
     2. Firebase Auth (type="module")
     3. Componentes (audio, avatar)
     4. Core (prayer-app)
     5. Init.js (orquestra tudo)

2. **Autenticação:**
   - `firebase-auth.js` observa estado
   - Se logado → `updateUserInterface()` popula dados
   - Se deslogado → Mostra `#auth-screen`

3. **Navegação:**
   - Clique em tab → `.nav-item.active` muda
   - `.tab-content.active` mostra conteúdo
   - Features específicas (friends, calendar) carregam dados

4. **Oração:**
   - `app.start(type)` → `generateBeads()` → renderiza contas
   - Gestos/teclado → `app.next()`/`app.prev()`
   - `app.complete()` → salva estatísticas via `stats-tracker.js`

---

## ✅ Benefícios da Modularização

1. **Manutenibilidade:** Cada arquivo tem responsabilidade única
2. **Testabilidade:** Módulos podem ser testados isoladamente
3. **Performance:** Code splitting (carrega só o necessário)
4. **Escalabilidade:** Adicionar features não polui outros arquivos
5. **Colaboração:** Múltiplos devs podem trabalhar sem conflitos
6. **Legibilidade:** Estrutura clara e intuitiva

---

## 🚀 Próximos Passos

1. Criar todos os arquivos CSS conforme especificado
2. Criar todos os arquivos JS conforme especificado
3. Testar cada módulo isoladamente
4. Validar integração completa
5. Verificar que 100% das funcionalidades foram preservadas
6. Atualizar `sw.js` com novos caminhos de cache
7. Atualizar `README.md` com nova estrutura

---

## 📝 Notas Importantes

- **config.js NUNCA deve ser versionado** (já está no .gitignore)
- Todos os módulos JS usam ES6 modules (`import`/`export`)
- Funções globais necessárias (onclick no HTML) são atribuídas a `window`
- Firebase é carregado como módulo ES6, não via CDN script tags
- Templates HTML podem ser migrados para JSX/TSX no futuro

---

**Autor:** Sistema de Refatoração Profissional  
**Data:** Janeiro 2026  
**Versão:** 1.0  
