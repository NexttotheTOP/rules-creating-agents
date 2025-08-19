import { createClient } from '@supabase/supabase-js';

/**
 * Supabase client for the frontend.
 * URL and anon key are loaded from environment variables.
 */
const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!;
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!;

export const supabase = createClient(supabaseUrl, supabaseAnonKey);
