import React from 'react'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Home from './pages/Home'
import Dashboard from './pages/Dashboard'

function App() {
  return (
    <Router>
      <div className="flex flex-col min-h-screen bg-slate-950 text-slate-100 selection:bg-teal-500 selection:text-slate-950">
        {/* Sticky Header Navbar */}
        <Navbar />

        {/* Main Routed Content */}
        <main className="flex-grow pt-16">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/dashboard" element={<Dashboard />} />
          </Routes>
        </main>

        {/* Premium Modern Footer */}
        <footer className="border-t border-slate-900 bg-slate-950/80 backdrop-blur-md py-8 text-center text-sm text-slate-500">
          <div className="max-w-7xl mx-auto px-4 flex flex-col md:flex-row justify-between items-center gap-4">
            <div>
              <span className="font-bold text-teal-400">SATRIA</span> &mdash; Early Warning System
            </div>
            <div>
              &copy; {new Date().getFullYear()} PBL Web Service x MLOps. All rights reserved.
            </div>
          </div>
        </footer>
      </div>
    </Router>
  )
}

export default App
