'use client';
import React, { useCallback } from 'react';
import { useEditor, EditorContent } from '@tiptap/react';
import StarterKit from '@tiptap/starter-kit';
import Link from '@tiptap/extension-link';
import Image from '@tiptap/extension-image';
import { supabase } from '@/lib/supabaseClient';

/**
 * PRD rich-text editor component with TipTap.
 * Supports basic formatting, links, images, and file uploads to Supabase Storage.
 */
export const PRDEditor = ({ initialContent = '', onChange }: {
  initialContent?: string;
  onChange?: (html: string) => void;
}) => {
  const editor = useEditor({
    immediatelyRender: false, // disable SSR rendering to avoid hydration mismatches
    extensions: [
      StarterKit,
      Link.configure({ openOnClick: false }),
      Image
    ],
    content: initialContent,
    onUpdate: ({ editor }) => {
      onChange?.(editor.getHTML());
    }
  });

  const uploadFile = useCallback(async (file: File) => {
    const fileExt = file.name.split('.').pop();
    const fileName = `${Date.now()}.${fileExt}`;
    const filePath = `uploads/${fileName}`;
    const { error } = await supabase.storage.from('prd-files').upload(filePath, file);
    if (error) {
      console.error('File upload error:', error);
      return null;
    }
    const { data } = supabase.storage.from('prd-files').getPublicUrl(filePath);
    return data.publicUrl;
  }, []);

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!editor || !e.target.files?.[0]) {
      return;
    }
    const file = e.target.files[0];
    const url = await uploadFile(file);
    if (!url) {
      return;
    }
    if (file.type.startsWith('image/')) {
      editor.chain().focus().setImage({ src: url }).run();
    } else {
      // Insert a link to non-image files
      editor.chain().focus()
        .extendMarkRange('link')
        .setLink({ href: url })
        .insertContent(file.name)
        .run();
    }
    e.target.value = '';
  };

  return (
    <div className="border rounded p-4">
      <div className="mb-2 flex gap-2">
        <button
          type="button"
          onClick={() => editor?.chain().focus().toggleBold().run()}
          className="px-2 py-1 border rounded hover:bg-gray-200"
        >Bold</button>
        <button
          type="button"
          onClick={() => editor?.chain().focus().toggleItalic().run()}
          className="px-2 py-1 border rounded hover:bg-gray-200"
        >Italic</button>
        <button
          type="button"
          onClick={() => editor?.chain().focus().toggleBulletList().run()}
          className="px-2 py-1 border rounded hover:bg-gray-200"
        >Bullet List</button>
        <button
          type="button"
          onClick={() => editor?.chain().focus().toggleOrderedList().run()}
          className="px-2 py-1 border rounded hover:bg-gray-200"
        >Numbered List</button>
        <input
          type="file"
          onChange={handleFileChange}
          className="ml-auto"
        />
      </div>
      <EditorContent editor={editor} className="min-h-[300px]" />
    </div>
);
};

export default PRDEditor;
