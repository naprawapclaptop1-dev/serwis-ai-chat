CREATE TABLE IF NOT EXISTS conversations(
 id TEXT PRIMARY KEY,
 customer_name TEXT NOT NULL DEFAULT 'Klient',
 customer_email TEXT NOT NULL DEFAULT '',
 mode TEXT NOT NULL DEFAULT 'ai',
 created_at TEXT NOT NULL,
 updated_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_conversations_updated ON conversations(updated_at DESC);