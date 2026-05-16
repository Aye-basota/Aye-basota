# Rebranding Guide: From "Student/Fork" to "Professional Project"

## 1. Отвязка от форка (если проект — форк)

GitHub не позволяет "отфоркать" репозиторий через UI. Есть 2 пути:

### Вариант А: Импорт через GitHub Importer (рекомендуется)
1. Сохрани локальную копию: `git clone --mirror <fork-url>`
2. На GitHub: **+ → Import repository**
3. Вставь URL своего форка, задай **новое имя**
4. После импорта — удали старый форк
5. **Важно:** история коммитов сохранится, но связи с оригиналом не будет

### Вариант Б: Заливаем как новый репозиторий
```bash
# Клонируем форк локально
git clone https://github.com/you/old-fork.git new-project-name
cd new-project-name

# Удаляем remote на оригинал
git remote remove origin

# Создаём новый репо на GitHub (пустой, без README)
# Добавляем новый remote
git remote add origin https://github.com/you/new-project-name.git

# Перезаливаем
git push -u origin main
```

### Вариант В: Полная перезапись истории (если хочешь скрыть чужие коммиты)
```bash
# Создаём новый orphan branch
git checkout --orphan new-main

# Добавляем все файлы
git add -A
git commit -m "init: project setup"

# Удаляем старую ветку, переименовываем новую
git branch -D main
git branch -m main

# Форс-пуш в новый репозиторий
git push -f origin main
```
> ⚠️ Используй только если уверен, что это не нарушает лицензию оригинала!

---

## 2. Переименование проекта

### Правила хорошего имени:
- ❌ `ml-course-homework-3`, `stepik-dl`, `forked-cool-project`
- ✅ `sentiment-analyzer-api`, `credit-risk-predictor`, `image-super-resolution-pytorch`

**Шаблоны названий:**
- `<task>-<tech>` — `text-classification-bert`
- `<domain>-<solution>` — `medical-image-segmentation`
- `<what-it-does>` — `price-predictor`, `anomaly-detector`

### Что поменять внутри репозитория:
```bash
# Найди все упоминания старого названия
grep -r "old-project-name" . --include="*.py" --include="*.md" --include="*.yaml"

# Замени в:
# - README.md (заголовок, ссылки, shields.io badges)
# - setup.py / pyproject.toml (name, url)
# - docker-compose.yml (service names, container names)
# - CI/CD configs (.github/workflows/*.yml)
# - Внутри кода: docstrings, комментарии
```

---

## 3. Чеклист "убираем учебный вид"

### README — что заменить:
| ❌ Было | ✅ Стало |
|---------|---------|
| "Это домашнее задание курса..." | "Production-ready solution for..." |
| "Выполнил: Иванов И.И." | Убрать полностью |
| "Задание 3. Нейросети." | "Deep Learning Pipeline for X" |
| "Результат на Kaggle: ..." (если это единственная ценность) | "Achieved X% accuracy on benchmark dataset" |
| "Спасибо автору курса..." | Перенести в секцию Acknowledgements (внизу) или убрать |
| Скриншоты Jupyter с `In [12]:` | Оформить как код-блоки или убрать |

### Код — что поправить:
- Убрать hardcoded пути типа `C:/Users/Student/Downloads/...`
- Вынести конфиги в `.yaml` / `.env` / `hydra`
- Добавить `requirements.txt` с pinned версиями
- Добавить `setup.py` или `pyproject.toml`
- Убрать закомментированный код "для отладки"
- Добавить `tests/` (хотя бы базовые)

### Репозиторий — что добавить:
- [ ] `.gitignore` (Python, Jupyter, IDE, data/)
- [ ] `LICENSE` (MIT — если нет ограничений)
- [ ] `docker-compose.yml`
- [ ] `.github/workflows/ci.yml` (lint + tests)
- [ ] `assets/` со скриншотами/диаграммами
- [ ] Теги (topics) на GitHub: `python`, `pytorch`, `machine-learning` и т.д.

---

## 4. Оформление коммитов

Если переписываешь историю — используй conventional commits:
```
feat: add data preprocessing pipeline
feat: implement ResNet50 backbone
fix: correct normalization in inference
docs: update README with benchmark results
test: add unit tests for API endpoints
chore: add Docker support
```

---

## 5. Финальная проверка перед публикацией

- [ ] Нет упоминаний "курс", "домашка", "учебный", "student", "homework"
- [ ] Нет ссылок на личные папки / Google Drive / Яндекс.Диск
- [ ] Нет датасетов в репозитории (только `.gitignore` + инструкция по скачиванию)
- [ ] Все бейджи в README рабочие
- [ ] `docker-compose up` запускается без ошибок
- [ ] API отвечает по `/health` или `/docs`
- [ ] Есть хотя бы 1 скриншот / GIF / диаграмма архитектуры

---

> 💡 **Совет:** Сделай 1-2 проекта идеально по этому шаблону — остальные можно оформить проще, но в том же стиле. Качество > количество.
