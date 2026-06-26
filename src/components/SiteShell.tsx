import { NavLink, Outlet } from "react-router-dom";
import { Newspaper } from "lucide-react";

const navItems = [
  { to: "/", label: "今日" },
  { to: "/archive", label: "归档" },
  { to: "/tag/agent", label: "Agent" },
  { to: "/tag/multimodal", label: "Multimodal" },
];

export function SiteShell() {
  return (
    <div className="site-shell">
      <header className="top-nav">
        <NavLink className="brand" to="/">
          <Newspaper size={22} />
          <span>AI Daily</span>
        </NavLink>
        <nav aria-label="主导航">
          {navItems.map((item) => (
            <NavLink key={item.to} to={item.to}>
              {item.label}
            </NavLink>
          ))}
        </nav>
      </header>
      <Outlet />
    </div>
  );
}
