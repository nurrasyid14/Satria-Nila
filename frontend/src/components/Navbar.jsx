import React from 'react'
import { Link, useLocation } from 'react-router-dom'
import { Droplet, Activity, LayoutDashboard, Home } from 'lucide-react'

function Navbar() {
  const location = useLocation()

  const isActive = (path) => location.pathname === path

  return (
    <header className="fixed top-0 left-0 w-full z-50 bg-slate-950/70 backdrop-blur-xl border-b border-slate-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        
        {/* Branding Logo */}
        <Link to="/" className="flex items-center gap-2 group">
          <div className="p-2 bg-gradient-to-br from-teal-500 to-cyan-500 rounded-xl text-slate-950 shadow-lg shadow-teal-500/10 group-hover:scale-105 transition-transform duration-300">
            <Droplet className="w-5 h-5 fill-current" />
          </div>
          <div className="flex flex-col">
            <span className="font-extrabold text-lg leading-none tracking-wider bg-gradient-to-r from-teal-400 to-cyan-400 bg-clip-text text-transparent">
              SATRIA
            </span>
            <span className="text-[10px] text-slate-500 font-semibold tracking-widest mt-0.5">
              AQUACULTURE
            </span>
          </div>
        </Link>

        {/* Navigation Links */}
        <nav className="flex items-center gap-2">
          <Link
            to="/"
            className={`flex items-center gap-1.5 px-4 py-2 rounded-xl text-sm font-semibold transition-all duration-200 ${
              isActive('/')
                ? 'bg-slate-900 text-teal-400 shadow-inner'
                : 'text-slate-400 hover:text-slate-100 hover:bg-slate-900/40'
            }`}
          >
            <Home className="w-4 h-4" />
            <span>Beranda</span>
          </Link>
          
          <Link
            to="/dashboard"
            className={`flex items-center gap-1.5 px-4 py-2 rounded-xl text-sm font-semibold transition-all duration-200 ${
              isActive('/dashboard')
                ? 'bg-slate-900 text-teal-400 shadow-inner'
                : 'text-slate-400 hover:text-slate-100 hover:bg-slate-900/40'
            }`}
          >
            <LayoutDashboard className="w-4 h-4" />
            <span>Dashboard</span>
          </Link>
        </nav>

      </div>
    </header>
  )
}

export default Navbar
