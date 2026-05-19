import React from 'react'
import { Link } from 'react-router-dom'
import { ShieldCheck, Activity, Award, ArrowRight, Droplet, Fish } from 'lucide-react'

function Home() {
  return (
    <div className="relative min-h-[calc(100vh-4rem)] flex flex-col justify-between overflow-hidden">
      
      {/* Decorative Blur Backgrounds */}
      <div className="absolute top-1/4 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[500px] h-[500px] bg-teal-500/10 rounded-full blur-3xl pointer-events-none"></div>
      <div className="absolute bottom-10 right-10 w-[300px] h-[300px] bg-blue-500/5 rounded-full blur-3xl pointer-events-none"></div>

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 sm:py-24 flex-grow flex flex-col justify-center relative">
        
        {/* Academic Course Badge */}
        <div className="flex justify-center mb-6">
          <div className="inline-flex items-center gap-1.5 py-1.5 px-4 bg-slate-900/80 border border-slate-800 rounded-full text-xs font-semibold text-teal-400 backdrop-blur-md">
            <Award className="w-4 h-4 text-teal-400" />
            PBL Teknologi Web Service x MLOps
          </div>
        </div>

        {/* Hero Headline */}
        <div className="text-center max-w-4xl mx-auto mb-10">
          <h1 className="text-4xl sm:text-6xl font-black tracking-tight leading-none mb-6">
            Early Warning System
            <span className="block mt-2 text-gradient-teal">
              Kelayakan Air Akuakultur
            </span>
          </h1>
          <p className="text-slate-400 text-base sm:text-lg leading-relaxed max-w-2xl mx-auto">
            Aplikasi berbasis Machine Learning untuk melakukan klasifikasi otomatis kelayakan kualitas air budidaya ikan nila dan memberikan saran mitigasi risiko secara real-time.
          </p>
        </div>

        {/* CTA Buttons */}
        <div className="flex flex-col sm:flex-row justify-center items-center gap-4 mb-16">
          <Link
            to="/dashboard"
            className="flex items-center gap-2 py-4 px-8 bg-gradient-to-r from-teal-500 to-cyan-500 hover:from-teal-400 hover:to-cyan-400 text-slate-950 font-bold rounded-2xl shadow-lg shadow-teal-500/10 hover:shadow-teal-500/30 transition-all duration-300 hover:scale-105 text-base tracking-wide"
          >
            Buka Monitor Dashboard
            <ArrowRight className="w-5 h-5" />
          </Link>
          <a
            href="https://github.com/nurrasyid14/Satria-Nila"
            target="_blank"
            rel="noreferrer"
            className="flex items-center gap-2 py-4 px-8 bg-slate-900 border border-slate-800 hover:border-slate-700 text-slate-300 hover:text-slate-100 font-bold rounded-2xl transition-all duration-300 hover:bg-slate-900/60 text-base"
          >
            Repository Git
          </a>
        </div>

        {/* Feature Grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 max-w-6xl mx-auto">
          
          <div className="glass-panel p-6 rounded-2xl hover:border-slate-800 transition-colors">
            <div className="w-10 h-10 rounded-xl bg-teal-500/10 flex items-center justify-center text-teal-400 mb-4">
              <ShieldCheck className="w-5 h-5" />
            </div>
            <h3 className="text-base font-bold mb-2">14 Parameter Fisikokimia</h3>
            <p className="text-slate-500 text-sm leading-relaxed">
              Mengevaluasi secara detail parameter fisik (Suhu, Turbidity), kimia (pH, DO, Amonia, Nitrit, H₂S), serta biologi kolam secara menyeluruh.
            </p>
          </div>

          <div className="glass-panel p-6 rounded-2xl hover:border-slate-800 transition-colors">
            <div className="w-10 h-10 rounded-xl bg-cyan-500/10 flex items-center justify-center text-cyan-400 mb-4">
              <Activity className="w-5 h-5" />
            </div>
            <h3 className="text-base font-bold mb-2">Klasifikasi Cerdas</h3>
            <p className="text-slate-500 text-sm leading-relaxed">
              Menggunakan model prediktif yang telah ditransfer dari PyCaret ke manual pipeline dengan tingkat keyakinan (*confidence score*) yang akurat.
            </p>
          </div>

          <div className="glass-panel p-6 rounded-2xl hover:border-slate-800 transition-colors">
            <div className="w-10 h-10 rounded-xl bg-blue-500/10 flex items-center justify-center text-blue-400 mb-4">
              <Fish className="w-5 h-5" />
            </div>
            <h3 className="text-base font-bold mb-2">Mitigasi Budidaya</h3>
            <p className="text-slate-500 text-sm leading-relaxed">
              Menghasilkan saran tindakan budidaya yang dipersonalisasi untuk mencegah kematian ikan dan menjaga kelestarian ekosistem kolam Anda.
            </p>
          </div>

        </div>

      </div>

    </div>
  )
}

export default Home
