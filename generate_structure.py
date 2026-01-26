#!/usr/bin/env python3
"""
Script para gerar estrutura modular completa do Rosário PWA
Uso: python3 generate_structure.py
"""

import os
import json

# Estrutura de diretórios
DIRECTORIES = [
    'css',
    'js/data',
    'js/utils',
    'js/components',
    'js/core',
    'js/features',
    'js/templates',
    'img/avatars',
    'docs'
]

# Arquivos CSS com placeholders
CSS_FILES = {
    'css/auth.css': '''/* ==========================================
   AUTHENTICATION SCREEN
   ========================================== */

#auth-screen {
    position: fixed;
    inset: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    padding: 28px 28px 60px;
    overflow-y: auto;
    z-index: 200;
    transition: opacity 0.6s var(--ease-out), visibility 0.6s;
}

#auth-screen.hidden {
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
}

.auth-container {
    width: 100%;
    max-width: 380px;
    text-align: center;
}

.auth-logo {
    width: 50px;
    height: 70px;
    position: relative;
    margin: 0 auto 24px;
}

.auth-logo::before,
.auth-logo::after {
    content: '';
    position: absolute;
    background: linear-gradient(180deg, var(--gold-bright) 0%, var(--gold) 50%, var(--gold-dim) 100%);
    border-radius: 2px;
}

.auth-logo::before {
    width: 4px;
    height: 100%;
    left: 50%;
    transform: translateX(-50%);
}

.auth-logo::after {
    width: 40px;
    height: 4px;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
}

.auth-title {
    font-family: var(--font-display);
    font-size: 1.8rem;
    font-weight: 500;
    letter-spacing: 0.2em;
    color: var(--text-primary);
    margin-bottom: 6px;
}

.auth-subtitle {
    font-family: var(--font-body);
    font-size: 1rem;
    font-style: italic;
    color: var(--text-muted);
    margin-bottom: 20px;
}

.auth-info {
    background: rgba(212, 168, 85, 0.1);
    border: 1px solid var(--border-subtle);
    border-radius: 8px;
    padding: 16px;
    margin-bottom: 24px;
    font-size: 0.9rem;
    color: var(--text-secondary);
    line-height: 1.6;
}

.auth-tabs {
    display: flex;
    margin-bottom: 28px;
    border-bottom: 1px solid var(--border-subtle);
}

.auth-tab {
    flex: 1;
    padding: 14px;
    background: none;
    border: none;
    font-family: var(--font-display);
    font-size: 0.75rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--text-muted);
    cursor: pointer;
    transition: all 0.3s;
    position: relative;
}

.auth-tab::after {
    content: '';
    position: absolute;
    bottom: -1px;
    left: 50%;
    transform: translateX(-50%);
    width: 0;
    height: 2px;
    background: var(--gold);
    transition: width 0.3s var(--ease-out);
}

.auth-tab.active {
    color: var(--gold);
}

.auth-tab.active::after {
    width: 60%;
}

.auth-form {
    display: none;
}

.auth-form.active {
    display: block;
}

.input-group {
    margin-bottom: 18px;
    text-align: left;
}

.input-label {
    display: block;
    font-family: var(--font-display);
    font-size: 0.6rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--text-dim);
    margin-bottom: 8px;
}

.input-field {
    width: 100%;
    padding: 14px 16px;
    background: #0f0d10;
    border: 1px solid var(--border-subtle);
    border-radius: 4px;
    font-family: var(--font-body);
    font-size: 1.05rem;
    color: var(--text-primary);
    transition: all 0.3s;
}

.input-field:focus {
    outline: none;
    border-color: var(--gold-dim);
    box-shadow: 0 0 0 3px rgba(212, 168, 85, 0.1);
}

.input-field::placeholder {
    color: var(--text-dim);
}

.auth-btn {
    width: 100%;
    padding: 16px;
    margin-top: 8px;
    background: linear-gradient(135deg, var(--gold) 0%, var(--gold-dim) 100%);
    border: none;
    border-radius: 4px;
    font-family: var(--font-display);
    font-size: 0.85rem;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: var(--bg-deep);
    cursor: pointer;
    transition: all 0.3s;
}

.auth-btn:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(212, 168, 85, 0.3);
}

.auth-btn:disabled {
    opacity: 0.6;
    cursor: not-allowed;
}

.auth-error,
.auth-success {
    margin-top: 16px;
    padding: 12px;
    border-radius: 4px;
    font-size: 0.9rem;
    display: none;
}

.auth-error {
    background: rgba(180, 60, 60, 0.15);
    border: 1px solid rgba(180, 60, 60, 0.3);
    color: #e07070;
}

.auth-success {
    background: rgba(74, 158, 107, 0.15);
    border: 1px solid rgba(74, 158, 107, 0.3);
    color: #70e070;
}

.auth-error.visible,
.auth-success.visible {
    display: block;
}
''',

    'css/navigation.css': '''/* ==========================================
   BOTTOM NAVIGATION & TABS
   ========================================== */

#main-app {
    position: fixed;
    inset: 0;
    display: flex;
    flex-direction: column;
    transition: opacity 0.6s var(--ease-out), visibility 0.6s;
    z-index: 100;
}

#main-app.hidden {
    opacity: 0;
    visibility: hidden;
    pointer-events: none;
}

.app-content {
    flex: 1;
    overflow-y: auto;
    overflow-x: hidden;
    padding-bottom: 70px;
}

.tab-content {
    display: none;
    width: 100%;
    min-height: 100%;
    overflow-y: auto;
    overflow-x: hidden;
    position: relative;
}

.tab-content.active {
    display: block;
}

/* Shadow gradient para tabs */
.tab-content::after {
    content: '';
    position: fixed;
    bottom: 70px;
    left: 0;
    right: 0;
    height: 60px;
    background: linear-gradient(to top, rgba(8, 7, 9, 1) 0%, rgba(8, 7, 9, 0.8) 50%, transparent 100%);
    pointer-events: none;
    z-index: 50;
}

/* Bottom Navigation */
.bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    height: 70px;
    background: linear-gradient(180deg, var(--bg-primary) 0%, var(--bg-deep) 100%);
    border-top: 1px solid var(--border-subtle);
    display: flex;
    justify-content: space-around;
    align-items: center;
    padding: 0 10px;
    z-index: 150;
}

.nav-item {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 10px 0;
    background: none;
    border: none;
    cursor: pointer;
    transition: all 0.3s;
    position: relative;
}

.nav-icon {
    width: 26px;
    height: 26px;
    color: var(--text-dim);
    transition: all 0.3s;
    margin-bottom: 4px;
}

.nav-label {
    font-family: var(--font-display);
    font-size: 0.5rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-dim);
    transition: all 0.3s;
}

.nav-item.active .nav-icon {
    color: var(--gold);
    filter: drop-shadow(0 0 8px var(--gold-glow));
}

.nav-item.active .nav-label {
    color: var(--gold);
}

.nav-item::before {
    content: '';
    position: absolute;
    top: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 0;
    height: 2px;
    background: var(--gold);
    transition: width 0.3s var(--ease-out);
}

.nav-item.active::before {
    width: 40px;
}
'''
}

# Mapeamento de arquivos a criar
FILES_TO_CREATE = {
    'ARCHITECTURE.md': '# (Já criado)',
    'README_NEW.md': '# README atualizado (ver ARCHITECTURE.md)',
}

def create_directories():
    """Cria estrutura de diretórios"""
    print("📁 Criando diretórios...")
    for dir_path in DIRECTORIES:
        os.makedirs(dir_path, exist_ok=True)
        print(f"   ✓ {dir_path}")

def create_css_files():
    """Cria arquivos CSS"""
    print("\n🎨 Criando arquivos CSS...")
    for file_path, content in CSS_FILES.items():
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"   ✓ {file_path}")

def create_placeholder_files():
    """Cria arquivos placeholder para JS"""
    print("\n📄 Criando placeholders JS...")
    
    js_files = [
        'js/data/montfort.js',
        'js/utils/avatar-helper.js',
        'js/utils/date-helpers.js',
        'js/utils/firebase-errors.js',
        'js/components/audio-system.js',
        'js/components/avatar-system.js',
        'js/components/calendar-widget.js',
        'js/core/bead-generator.js',
        'js/core/prayer-app.js',
        'js/features/auth-manager.js',
        'js/features/friends-manager.js',
        'js/features/stats-tracker.js',
        'js/templates/home.js',
        'js/templates/rosary.js',
        'js/templates/calendar.js',
        'js/templates/friends.js',
        'js/templates/profile.js',
        'js/firebase-auth.js',
        'js/init.js'
    ]
    
    for file_path in js_files:
        with open(file_path, 'w', encoding='utf-8') as f:
            module_name = os.path.basename(file_path).replace('.js', '').replace('-', ' ').title()
            f.write(f'''/* ==========================================
   {module_name.upper()}
   Ver ARCHITECTURE.md para implementação completa
   ========================================== */

// TODO: Implementar conforme especificação
export default {{}};
''')
        print(f"   ✓ {file_path}")

def create_summary_report():
    """Cria relatório de migração"""
    print("\n📊 Criando relatório...")
    
    report = """# 📊 Relatório de Refatoração

## Status
✅ Estrutura de diretórios criada
✅ Arquivos CSS base criados
✅ Placeholders JS criados
⏳ Implementação dos módulos pendente

## Próximos Passos

### 1. Implementar Módulos JS
Consulte `ARCHITECTURE.md` para implementação detalhada de cada módulo.

### 2. Completar Arquivos CSS
- [ ] css/home.css
- [ ] css/prayer.css
- [ ] css/calendar.css
- [ ] css/friends.css
- [ ] css/profile.css
- [ ] css/modals.css
- [ ] css/responsive.css

### 3. Migrar Conteúdo do index.html Original
- [ ] Copiar HTML dos templates
- [ ] Migrar lógica JS para módulos
- [ ] Testar cada feature isoladamente

### 4. Testes
- [ ] Autenticação
- [ ] Navegação entre tabs
- [ ] Oração (geração de contas, gestos)
- [ ] Calendário
- [ ] Amigos
- [ ] Avatar
- [ ] Estatísticas

### 5. Deploy
- [ ] Atualizar service worker com novos paths
- [ ] Validar PWA no Lighthouse
- [ ] Testar em dispositivos reais
- [ ] Deploy em produção

## Arquivos Principais

```
rosario-refactored/
├── index.html (NOVO - minimalista)
├── ARCHITECTURE.md (Documentação completa)
└── generate_structure.py (Este script)
```

## Comandos Úteis

```bash
# Gerar estrutura
python3 generate_structure.py

# Servir localmente
python3 -m http.server 8000

# Validar HTML
npm install -g html-validator-cli
html-validator --file=index.html

# Analisar bundle size
npm install -g bundlesize
```

---
Gerado automaticamente em """ + __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open('MIGRATION_REPORT.md', 'w', encoding='utf-8') as f:
        f.write(report)
    print("   ✓ MIGRATION_REPORT.md")

def main():
    print("🚀 Iniciando geração da estrutura modular...\n")
    
    create_directories()
    create_css_files()
    create_placeholder_files()
    create_summary_report()
    
    print("\n✨ Estrutura criada com sucesso!")
    print("\n📖 Próximos passos:")
    print("   1. Leia ARCHITECTURE.md para entender a estrutura")
    print("   2. Leia MIGRATION_REPORT.md para checklist de implementação")
    print("   3. Implemente os módulos JS conforme especificado")
    print("   4. Complete os arquivos CSS faltantes")
    print("   5. Teste cada feature isoladamente")

if __name__ == '__main__':
    main()
