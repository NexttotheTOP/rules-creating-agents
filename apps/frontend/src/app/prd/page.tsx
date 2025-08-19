'use client';
import React, { useState } from 'react';
import PRDEditor from '@/components/PRDEditor';

export default function PRDPage() {
  const [content, setContent] = useState<string>('');
  return (
    <div className="flex flex-col h-screen bg-gray-100 dark:bg-gray-900">
      <header className="flex items-center justify-between px-8 py-4 bg-white dark:bg-gray-800 shadow">
        <h1 className="text-xl font-semibold text-gray-800 dark:text-gray-100">PRD Editor</h1>
        <button
          type="button"
          className="px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
        >
          Save PRD
        </button>
      </header>
      <main className="flex-1 p-8 overflow-auto">
        <div className="max-w-4xl mx-auto bg-white dark:bg-gray-800 rounded-lg shadow p-6">
          <PRDEditor initialContent={content} onChange={setContent} />
        </div>
      </main>
    </div>
  );
}
