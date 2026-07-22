import { Button } from "@/components/ui/button";

const foundations = [
  "Next.js and TypeScript",
  "FastAPI service",
  "PostgreSQL with pgvector",
  "Redis cache",
  "Neo4j knowledge graph",
];

export default function Home() {
  return (
    <main className="mx-auto flex min-h-screen max-w-5xl items-center px-6 py-16">
      <section className="grid w-full gap-10 rounded-3xl border bg-card p-8 shadow-sm md:grid-cols-[1.4fr_1fr] md:p-12">
        <div className="space-y-6">
          <span className="inline-flex rounded-full bg-secondary px-3 py-1 text-sm font-medium text-secondary-foreground">
            Phase 0 foundation
          </span>
          <div className="space-y-3">
            <h1 className="text-4xl font-semibold tracking-tight md:text-5xl">
              Your knowledge, connected.
            </h1>
            <p className="max-w-xl text-lg leading-8 text-slate-600">
              The Personal Knowledge Agent workspace is ready for incremental
              development. Knowledge ingestion and AI features begin in later
              phases.
            </p>
          </div>
          <Button asChild>
            <a href="http://localhost:8000/docs">Open API documentation</a>
          </Button>
        </div>

        <div className="rounded-2xl bg-slate-950 p-6 text-slate-100">
          <p className="mb-4 text-sm font-medium uppercase tracking-widest text-emerald-300">
            Services configured
          </p>
          <ul className="space-y-3 text-sm">
            {foundations.map((foundation) => (
              <li className="flex items-center gap-3" key={foundation}>
                <span className="h-2 w-2 rounded-full bg-emerald-400" />
                {foundation}
              </li>
            ))}
          </ul>
        </div>
      </section>
    </main>
  );
}

