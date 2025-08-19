#!/usr/bin/env bash

# Automate Supabase project setup and apply migrations.
set -euo pipefail

if [ -z "${SUPABASE_URL:-}" ] || [ -z "${SUPABASE_SERVICE_ROLE_KEY:-}" ] || [ -z "${SUPABASE_PROJECT_REF:-}" ]; then
  echo "Error: Ensure SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, and SUPABASE_PROJECT_REF are set."
  exit 1
fi

# Login to Supabase CLI
supabase login --token "$SUPABASE_SERVICE_ROLE_KEY"

# Link to the specified project
supabase link --project-ref "$SUPABASE_PROJECT_REF"

# Push database migrations
supabase db push --file supabase/migrations

echo "Supabase provisioning and migrations complete."
