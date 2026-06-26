import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { SiteShell } from "@/components/SiteShell";
import Archive from "@/pages/Archive";
import FilterPage from "@/pages/FilterPage";
import Home from "@/pages/Home";
import PaperDetail from "@/pages/PaperDetail";

export default function App() {
  return (
    <Router basename={import.meta.env.BASE_URL}>
      <Routes>
        <Route element={<SiteShell />}>
          <Route path="/" element={<Home />} />
          <Route path="/archive" element={<Archive />} />
          <Route path="/paper/:id" element={<PaperDetail />} />
          <Route path="/tag/:tag" element={<FilterPage />} />
          <Route path="/source/:source" element={<FilterPage />} />
        </Route>
      </Routes>
    </Router>
  );
}
