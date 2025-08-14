# 🤖 InterviewAI: AI-Powered Interview Analysis Platform

**InterviewAI** — это веб-приложение, предназначенное для автоматизации и улучшения процесса проведения технических собеседований. Платформа использует современные AI-технологии для анализа резюме, подготовки планов интервью, транскрибации видеозаписей и формирования подробных отчетов по компетенциям кандидатов.

## ✨ Ключевые возможности

  * **Умная подготовка к интервью**: Автоматически генерирует структурированный план интервью, ключевые темы для обсуждения и список вопросов (технических и поведенческих) на основе резюме кандидата и требований вакансии.
  * **Анализ видео-интервью**: Загружает видеозапись собеседования из Google Drive, транскрибирует аудио в текст с помощью AssemblyAI и анализирует его.
  * **Оценка по матрице компетенций**: Оценивает кандидата по предоставленной матрице (например, `SENIOR.pdf`), выставляя баллы по категориям: `technical`, `communication`, `leadership`, `cultural` и `overall`.
  * **Генерация подробных отчетов**: Формирует комплексный отчет, включающий финальную рекомендацию (`RECOMMEND HIRE`, `CONSIDER`, `DO NOT RECOMMEND`), сильные стороны, зоны для улучшения и список обсуждавшихся тем.
  * **Экспорт отчетов**: Позволяет экспортировать сгенерированные отчеты в форматы `.pdf` и `.docx` для дальнейшего использования и обмена.
  * **Современный и адаптивный интерфейс**: Интуитивно понятный пользовательский интерфейс, построенный на React и `shadcn/ui`, который отлично выглядит как на десктопе, так и на мобильных устройствах.

-----

## 🛠️ Технологический стек

  * **Framework**: [React](https://react.dev/)
  * **Язык**: [TypeScript](https://www.typescriptlang.org/)
  * **Сборщик**: [Vite](https://vitejs.dev/)
  * **UI-компоненты**: [shadcn/ui](https://ui.shadcn.com/)
  * **Стилизация**: [Tailwind CSS](https://tailwindcss.com/)
  * **HTTP-клиент**: Fetch API
  * **Генерация PDF**: [jsPDF](https://github.com/parallax/jsPDF) & [jspdf-autotable](https://github.com/simonbengtsson/jspdf-autotable)
  * **Framework**: [FastAPI](https://fastapi.tiangolo.com/)
  * **Язык**: [Python](https://www.python.org/)
  * **AI Модели**: [Google Gemini (через `google-adk`)](https://www.google.com/search?q=%5Bhttps://ai.google.dev/%5D\(https://ai.google.dev/\))
  * **Транскрибация**: [AssemblyAI API](https://www.assemblyai.com/)
  * **Работа с файлами**: [Google Drive API](https://developers.google.com/drive)
  * **Генерация DOCX**: [python-docx](https://python-docx.readthedocs.io/)
  * **Асинхронный сервер**: [Uvicorn](https://www.uvicorn.org/)

-----

## 🚀 Начало работы

### Предварительные требования

1.  **Python** 3.10+
2.  **Node.js** 18+ и **npm**
3.  **Google Cloud Project**:
      * Включены **Gemini API** и **Google Drive API**.
      * Создан **сервисный аккаунт** с правами доступа к Google Drive.
      * Скачан JSON-ключ для сервисного аккаунта.
4.  **API ключ** от [AssemblyAI](https://www.assemblyai.com/).

### Установка и запуск

#### 1\. Бэкенд

```bash
# 1. Перейдите в корневую директорию проекта
cd /path/to/ai-hiring-tool

# 2. Создайте и активируйте виртуальное окружение
python -m venv .venv
source .venv/bin/activate  # Для Windows: .venv\Scripts\activate

# 3. Установите зависимости
pip install -r backend/requirements.txt

# 4. Настройте переменные окружения
#    Создайте файл .env в корневой директории проекта и заполните его по примеру ниже:
```

**Пример файла `.env`:**

```env
# backend/core/config.py
GOOGLE_API_KEY="your_gemini_api_key_here"
ASSEMBLYAI_API_KEY="your_assemblyai_api_key_here"
GOOGLE_APPLICATION_CREDENTIALS="path/to/your/google-service-account-credentials.json"
```

```bash
# 5. Запустите backend-сервер
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Сервер будет доступен по адресу `http://localhost:8000`.

#### 2\. Фронтенд

```bash
# 1. Откройте новый терминал и перейдите в корневую директорию проекта
cd /path/to/ai-hiring-tool

# 2. Установите frontend-зависимости
npm install

# 3. Настройте прокси для API запросов
#    В файле vite.config.ts (если его нет, создайте) укажите,
#    чтобы все запросы к /api перенаправлялись на ваш бэкенд:
```

**Пример `vite.config.ts`:**

```ts
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import path from "path"

export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    }
  }
})
```

```bash
# 4. Запустите frontend-приложение
npm run dev
```

Приложение будет доступно по адресу `http://localhost:5173` (или другому порту, указанному Vite).

-----

## 📖 Как использовать

### 1\. Подготовка к интервью

1.  Перейдите на вкладку **Interview Preparation**.
2.  **Загрузите CV кандидата** в формате `.pdf` или `.docx`.
3.  **Вставьте текст** с описанием вакансии и фидбэком от рекрутера в поле "Candidate Profile".
4.  Нажмите кнопку **Generate Interview Preparation**.
5.  Система проанализирует данные и сгенерирует **ключевые темы** для обсуждения и **список вопросов**.
6.  Сгенерированный план можно экспортировать в **PDF**.

### 2\. Анализ результатов интервью

1.  Перейдите на вкладку **Interview Results**.
2.  Вставьте **ссылку на видеозапись** интервью из Google Drive. Убедитесь, что у вашего сервисного аккаунта (email которого указан в `credentials.json`) есть **доступ на чтение** к этому файлу.
3.  Загрузите **матрицу компетенций** в формате `.pdf` или `.docx`.
4.  Нажмите кнопку **Analyze Interview with AI**.
5.  Платформа скачает видео, транскрибирует его и проведет полный анализ.
6.  Результаты будут отображены на экране, включая **финальную рекомендацию**, **оценки по компетенциям**, **сильные и слабые стороны** и **список обсуждавшихся тем**.
7.  Полный отчет можно экспортировать в **DOCX**.