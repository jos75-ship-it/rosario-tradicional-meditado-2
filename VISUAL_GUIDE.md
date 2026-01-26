# 🎨 Guia Visual - Arquitetura Modular

## 📊 Diagrama de Arquitetura Geral

```
┌─────────────────────────────────────────────────────────────┐
│                      index.html                             │
│  (HTML minimalista - apenas estrutura DOM)                  │
└────────────┬────────────────────────────────────────────────┘
             │
             ├─────> CSS (Modular)
             │       ├─ variables.css (Design Tokens)
             │       ├─ base.css (Reset + Global)
             │       ├─ auth.css
             │       ├─ navigation.css
             │       ├─ home.css
             │       ├─ prayer.css
             │       ├─ calendar.css
             │       ├─ friends.css
             │       ├─ profile.css
             │       ├─ modals.css
             │       └─ responsive.css
             │
             └─────> JavaScript (Modular)
                     │
                     ├─ data/ (Conteúdo estático)
                     │  ├─ prayers.js → TEXTS {}
                     │  └─ montfort.js → MONTFORT {}
                     │
                     ├─ utils/ (Funções auxiliares)
                     │  ├─ avatar-helper.js → getAvatarHTML()
                     │  ├─ date-helpers.js → getTodayMystery()
                     │  └─ firebase-errors.js → getErrorMessage()
                     │
                     ├─ components/ (UI Components)
                     │  ├─ audio-system.js → AudioSystem
                     │  ├─ avatar-system.js → Avatar Modal
                     │  └─ calendar-widget.js → renderCalendar()
                     │
                     ├─ core/ (Lógica Principal)
                     │  ├─ bead-generator.js → generateBeads()
                     │  └─ prayer-app.js → app {}
                     │
                     ├─ features/ (Funcionalidades)
                     │  ├─ auth-manager.js → login/register
                     │  ├─ friends-manager.js → CRUD amigos
                     │  └─ stats-tracker.js → Salvar estatísticas
                     │
                     ├─ templates/ (HTML dinâmico)
                     │  ├─ home.js → HOME_TEMPLATE
                     │  ├─ rosary.js → ROSARY_TEMPLATE
                     │  ├─ calendar.js → CALENDAR_TEMPLATE
                     │  ├─ friends.js → FRIENDS_TEMPLATE
                     │  └─ profile.js → PROFILE_TEMPLATE
                     │
                     ├─ firebase-auth.js (ES6 Module)
                     │  └─ onAuthStateChanged()
                     │
                     └─ init.js (Orquestrador)
                        └─ DOMContentLoaded
```

---

## 🔄 Fluxo de Dados

### 1. **Autenticação**

```
┌──────────────┐
│  Usuário     │
│  digita      │
│  credenciais │
└──────┬───────┘
       │
       v
┌──────────────────────┐
│  auth-manager.js     │
│  loginUser()         │
└──────┬───────────────┘
       │
       v
┌──────────────────────┐
│  firebase-auth.js    │
│  signInWith...()     │
└──────┬───────────────┘
       │
       v
┌──────────────────────────┐
│  onAuthStateChanged()    │
│  ├─ get user profile     │
│  ├─ set window.userProfile│
│  └─ updateUI()           │
└──────┬───────────────────┘
       │
       v
┌──────────────────────┐
│  Esconde #auth-screen│
│  Mostra #main-app    │
│  Popula tabs         │
└──────────────────────┘
```

### 2. **Navegação entre Tabs**

```
┌────────────────┐
│ Click em Tab   │
└───────┬────────┘
        │
        v
┌────────────────────────┐
│  init.js               │
│  setupNavigation()     │
│  ├─ Remove .active     │
│  ├─ Add .active        │
│  └─ Show .tab-content  │
└───────┬────────────────┘
        │
        v
┌────────────────────────┐
│  Tab específica        │
│  ├─ Home: streak       │
│  ├─ Rosary: mistérios  │
│  ├─ Calendar: render   │
│  ├─ Friends: loadList  │
│  └─ Profile: stats     │
└────────────────────────┘
```

### 3. **Oração do Rosário**

```
┌──────────────────┐
│ app.start(type)  │
└────────┬─────────┘
         │
         v
┌──────────────────────┐
│ bead-generator.js    │
│ generateBeads(type)  │
│ ├─ Loop mysteries    │
│ ├─ Add Pater         │
│ ├─ Add 10 Aves       │
│ └─ Return beads[]    │
└────────┬─────────────┘
         │
         v
┌──────────────────────┐
│ prayer-app.js        │
│ ├─ Render beads      │
│ ├─ Setup gestures    │
│ └─ Listen keyboard   │
└────────┬─────────────┘
         │
         v
┌──────────────────────┐
│ User: next/prev      │
│ ├─ Update index      │
│ ├─ AudioSystem.play  │
│ └─ Update UI         │
└────────┬─────────────┘
         │
         v
┌──────────────────────┐
│ app.complete()       │
│ ├─ Show completion   │
│ └─ stats-tracker.js  │
└────────┬─────────────┘
         │
         v
┌──────────────────────────┐
│ Firebase: save stats     │
│ ├─ totalRosaries++       │
│ ├─ Calculate streak      │
│ └─ Update profile        │
└──────────────────────────┘
```

---

## 📦 Dependências entre Módulos

### **Nível 1: Sem Dependências** (Podem ser carregados primeiro)
- `data/prayers.js`
- `data/montfort.js`
- `utils/avatar-helper.js`
- `utils/date-helpers.js`
- `utils/firebase-errors.js`

### **Nível 2: Dependências de Nível 1**
- `components/audio-system.js` (standalone)
- `components/calendar-widget.js` (usa date-helpers)
- `core/bead-generator.js` (usa montfort.js)

### **Nível 3: Dependências de Nível 1 e 2**
- `core/prayer-app.js` (usa audio-system, bead-generator, prayers)
- `features/auth-manager.js` (usa firebase-errors)
- `components/avatar-system.js` (usa avatar-helper)

### **Nível 4: Firebase**
- `firebase-auth.js` (ES6 module, carrega Firebase SDK)

### **Nível 5: Orquestrador**
- `init.js` (depende de tudo, coordena inicialização)

---

## 🎯 Ordem de Carregamento Recomendada

```html
<!-- 1. Templates (injetam HTML) -->
<script src="js/templates/home.js"></script>
<script src="js/templates/rosary.js"></script>
<script src="js/templates/calendar.js"></script>
<script src="js/templates/friends.js"></script>
<script src="js/templates/profile.js"></script>

<!-- 2. Firebase Auth (ES6 Module) -->
<script type="module" src="js/firebase-auth.js"></script>

<!-- 3. Utilitários (sem dependências) -->
<script src="js/utils/avatar-helper.js"></script>
<script src="js/data/prayers.js"></script>

<!-- 4. Componentes -->
<script src="js/components/audio-system.js"></script>
<script src="js/components/avatar-system.js"></script>

<!-- 5. Core -->
<script src="js/core/prayer-app.js"></script>

<!-- 6. Inicializador (último) -->
<script src="js/init.js"></script>
```

---

## 🔍 Mapeamento: Onde Está Cada Funcionalidade?

### **Autenticação**
- HTML: `index.html` → `<div id="auth-screen">`
- CSS: `css/auth.css`
- JS: `js/features/auth-manager.js` + `js/firebase-auth.js`

### **Navegação**
- HTML: `index.html` → `<nav class="bottom-nav">`
- CSS: `css/navigation.css`
- JS: `js/init.js` (setupNavigation)

### **Home (Streak, Intenção)**
- HTML: `js/templates/home.js`
- CSS: `css/home.css`
- JS: `js/firebase-auth.js` (updateUserInterface)

### **Rosário (Oração)**
- HTML: `index.html` → `<div id="prayer-screen">`
- CSS: `css/prayer.css`
- JS: `js/core/prayer-app.js` + `js/core/bead-generator.js`

### **Calendário**
- HTML: `js/templates/calendar.js`
- CSS: `css/calendar.css`
- JS: `js/components/calendar-widget.js`

### **Amigos**
- HTML: `js/templates/friends.js`
- CSS: `css/friends.css`
- JS: `js/features/friends-manager.js`

### **Perfil**
- HTML: `js/templates/profile.js`
- CSS: `css/profile.css`
- JS: `js/firebase-auth.js` (updateUserInterface)

### **Avatar**
- HTML: `index.html` → `<div id="avatar-modal">`
- CSS: `css/modals.css`
- JS: `js/components/avatar-system.js`

### **Áudio**
- JS: `js/components/audio-system.js`

---

## 📋 Checklist de Migração

### ✅ **Fase 1: Estrutura Básica** (Feito)
- [x] Criar estrutura de diretórios
- [x] Criar index.html minimalista
- [x] Criar arquivos CSS base (variables, base, auth, navigation)
- [x] Criar placeholders JS

### ⏳ **Fase 2: CSS Completo**
- [ ] Implementar `css/home.css`
- [ ] Implementar `css/prayer.css` (mais complexo - beads, animations)
- [ ] Implementar `css/calendar.css`
- [ ] Implementar `css/friends.css`
- [ ] Implementar `css/profile.css`
- [ ] Implementar `css/modals.css`
- [ ] Implementar `css/responsive.css`

### ⏳ **Fase 3: JavaScript - Data & Utils**
- [ ] Implementar `js/data/montfort.js` (copiar do original)
- [ ] Implementar `js/utils/date-helpers.js`
- [ ] Implementar `js/utils/firebase-errors.js`

### ⏳ **Fase 4: JavaScript - Components**
- [ ] Implementar `js/components/audio-system.js` (copiar + export)
- [ ] Implementar `js/components/avatar-system.js`
- [ ] Implementar `js/components/calendar-widget.js`

### ⏳ **Fase 5: JavaScript - Core**
- [ ] Implementar `js/core/bead-generator.js`
- [ ] Implementar `js/core/prayer-app.js` (mais complexo)

### ⏳ **Fase 6: JavaScript - Features**
- [ ] Implementar `js/features/auth-manager.js`
- [ ] Implementar `js/features/friends-manager.js`
- [ ] Implementar `js/features/stats-tracker.js`

### ⏳ **Fase 7: JavaScript - Templates**
- [ ] Implementar `js/templates/home.js`
- [ ] Implementar `js/templates/rosary.js`
- [ ] Implementar `js/templates/calendar.js`
- [ ] Implementar `js/templates/friends.js`
- [ ] Implementar `js/templates/profile.js`

### ⏳ **Fase 8: JavaScript - Firebase & Init**
- [ ] Implementar `js/firebase-auth.js`
- [ ] Implementar `js/init.js`

### ⏳ **Fase 9: Testes**
- [ ] Testar autenticação (login, registro, logout)
- [ ] Testar navegação entre tabs
- [ ] Testar oração (start, next, prev, gestos, áudio)
- [ ] Testar calendário (render, navegação meses)
- [ ] Testar amigos (buscar, adicionar, aceitar, perfil)
- [ ] Testar avatar (selecionar, salvar)
- [ ] Testar estatísticas (salvar, streak)
- [ ] Testar responsividade (mobile, landscape)

### ⏳ **Fase 10: Deploy**
- [ ] Atualizar `sw.js` com novos paths
- [ ] Validar PWA (Lighthouse)
- [ ] Testar instalação (Android, iOS, Desktop)
- [ ] Deploy em produção

---

## 💡 Dicas de Implementação

### **1. Comece pelos Templates**
Os templates são mais fáceis: copie o HTML do original e exporte como string.

```javascript
// js/templates/home.js
export const HOME_TEMPLATE = `
<div class="home-screen-content">
    <!-- Copiar HTML aqui -->
</div>
`;
```

### **2. Dados Estáticos São Simples**
Copie os objetos TEXTS e MONTFORT do original, adicione `export`.

```javascript
// js/data/prayers.js
export const TEXTS = { /* copiar */ };
```

### **3. Componentes: Isole a Lógica**
Cada componente deve ter sua própria inicialização.

```javascript
// js/components/audio-system.js
export const AudioSystem = {
    init() { /* ... */ },
    playBead() { /* ... */ }
};
```

### **4. Use console.log para Debug**
Durante migração, adicione logs para verificar carregamento.

```javascript
console.log('[AUTH] Módulo carregado');
console.log('[PRAYER] App iniciado:', type);
```

### **5. Teste Progressivamente**
Não migre tudo de uma vez. Teste cada módulo antes de prosseguir.

---

## 🚀 Comandos Rápidos

```bash
# Gerar estrutura
python3 generate_structure.py

# Servir localmente
python3 -m http.server 8000
# ou
php -S localhost:8000

# Verificar sintaxe JS
node --check js/init.js

# Minificar CSS (depois de implementado)
npx csso css/home.css --output css/home.min.css

# Minificar JS (depois de implementado)
npx terser js/init.js --compress --mangle -o js/init.min.js
```

---

**Última atualização:** Janeiro 2026  
**Versão:** 1.0  
