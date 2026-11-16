export function Logo({ className = "h-8 w-auto" }: { className?: string }) {
  return (
    <img
      src="/logo-declika.png"
      alt="Declika"
      width={640}
      height={164}
      className={className}
    />
  );
}
