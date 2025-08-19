-- Enable uuid extension
create extension if not exists "pgcrypto";

-- Create users table
create table if not exists public.users (
  id uuid primary key default uuid_generate_v4(),
  email text not null unique,
  created_at timestamp with time zone default now()
);

-- Create generations table
create table if not exists public.generations (
  id uuid primary key default uuid_generate_v4(),
  user_id uuid references public.users(id) on delete cascade,
  generation jsonb not null,
  created_at timestamp with time zone default now()
);
