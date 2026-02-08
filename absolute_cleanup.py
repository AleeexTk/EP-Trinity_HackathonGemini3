
import re
import os
import shutil

def ultimate_purge():
    translations = {
        "Инициализация мониторинга когерентности...": "Initializing coherence monitoring...",
        "Инициализация мониторинга": "Initializing monitoring",
        "Завершение работы Trinity System...": "Shutting down Trinity System...",
        "Ошибка сохранения": "Save error",
        "Система завершена. Всего взаимодействий": "System terminated. Total interactions",
        "Финальная когерентность": "Final coherence",
        "ТОЧКА ВХОДА": "ENTRY POINT",
        "ВЫПОЛНЕНИЕ ЗАВЕРШЕНО": "EXECUTION COMPLETE",
        "Интегрированная система Trinity": "Integrated Trinity System",
        "Инициализация ядра": "Engine initialization",
        "Состояние системы": "System state",
        "Автосохранение": "Autosave",
        "Сессия": "Session",
        "Настройка автосохранения": "Autosave setup",
        "минут": "minutes",
        "Основной метод коммуникации": "Main communication method",
        "Обработка через движок": "Processing through engine",
        "Обновление статистики": "Statistics update",
        "Здесь можно добавить логику сбора статистики": "Statistics collection logic can be added here",
        "Получение полного отчета системы": "Getting full system report",
        "Сохранение состояния системы": "Saving system state",
        "Корректное завершение работы": "Graceful shutdown",
        "Завершение работы": "Shutting down",
        "Всего взаимодействий": "Total interactions",
        "Финальная": "Final",
        "Уровни когерентности": "Coherence levels",
        "система нестабильна": "system unstable",
        "частичные нарушения": "partial violations",
        "минимальные отклонения": "minimal deviations",
        "полная когерентность": "full coherence",
        "Естественный отбор": "Natural Selection",
        "Парсинг RED ввода": "Parsing RED input",
        "Валидация JSON структуры": "JSON structure validation",
        "Извлекаем результаты": "Extracting results",
        "Расчет итоговой когерентности": "Calculating final coherence",
        "Проверка формы (кавычки)": "Form check (quotes)",
        "Объяснимость": "Explainability",
        "Проверка формы (вопрос)": "Form check (question)",
        "Проверка провокативности": "Provocativity check",
        "Проверка формы (JSON tag)": "Form check (JSON tag)",
        "Текстовый документ.txt": "source_data.txt",
        "Инициализация": "Initialization",
        "Инициализация мониторинга...": "Initializing monitoring...",
        "мониторинга когерентности": "coherence monitoring",
        "Парсинг": "Parsing",
        "инъекций": "injections"
    }

    target_files = [
        'core/trinity_core.py',
        'core/evolution_protocol.py',
        'src/bridge_gemini.py',
        'src/main.py',
        'src/vision_monitor.py',
        'start_hackathon_demo.py'
    ]

    # Create archive if not exists
    if not os.path.exists('_archive'):
        os.makedirs('_archive')

    for rel_path in target_files:
        abs_path = os.path.join(os.getcwd(), rel_path)
        if not os.path.exists(abs_path):
            print(f"⚠️ Skipping missing file: {rel_path}")
            continue

        # Backup
        backup_path = os.path.join('_archive', os.path.basename(rel_path) + '.bak')
        shutil.copy2(abs_path, backup_path)

        with open(abs_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Apply specific translations
        for ru, en in translations.items():
            content = content.replace(ru, en)

        # Catch-all for remaining Cyrillic (e.g. in comments)
        def fallback_translator(match):
            word = match.group(0)
            # Simplistic mapping for common words found in comments during manual review
            fallback_map = {
                "Парсинг": "Parsing",
                "Валидатор": "Validator",
                "форма": "form",
                "семантика": "semantics",
                "архитектура": "architecture",
                "кавычки": "quotes",
                "вопрос": "question"
            }
            return fallback_map.get(word, "[ENG]")

        # Replace any remaining Cyrillic blocks
        processed_content = re.sub(r'[а-яА-ЯёЁ]+', fallback_translator, content)

        with open(abs_path, 'w', encoding='utf-8') as f:
            f.write(processed_content)
        
        print(f"✅ Absolute cleanup of {rel_path} complete. Backup saved to _archive.")

if __name__ == "__main__":
    ultimate_purge()
