import React, { useState } from 'react'
import { Sparkles, ShieldCheck, AlertTriangle, Skull, RotateCcw } from 'lucide-react'

// Define the 3 preset water quality scenarios
const PRESETS = {
  optimal: {
    temperature: 28.5,
    turbidity: 45.0,
    dissolved_oxygen: 6.8,
    bod: 3.5,
    co2: 6.0,
    ph: 7.3,
    alkalinity: 120.0,
    hardness: 110.0,
    calcium: 85.0,
    ammonia: 0.02,
    nitrite: 0.01,
    phosphorus: 0.05,
    h2s: 0.002,
    plankton_count: 5500
  },
  stressed: {
    temperature: 23.5,
    turbidity: 15.0,
    dissolved_oxygen: 3.8,
    bod: 8.5,
    co2: 12.5,
    ph: 6.2,
    alkalinity: 65.0,
    hardness: 45.0,
    calcium: 200.0,
    ammonia: 0.15,
    nitrite: 0.08,
    phosphorus: 1.5,
    h2s: 0.03,
    plankton_count: 1500
  },
  hazardous: {
    temperature: 16.0,
    turbidity: 5.0,
    dissolved_oxygen: 1.8,
    bod: 14.5,
    co2: 16.5,
    ph: 4.5,
    alkalinity: 260.0,
    hardness: 340.0,
    calcium: 360.0,
    ammonia: 0.85,
    nitrite: 3.5,
    phosphorus: 3.8,
    h2s: 0.08,
    plankton_count: 250
  }
}

const INITIAL_STATE = {
  temperature: '',
  turbidity: '',
  dissolved_oxygen: '',
  bod: '',
  co2: '',
  ph: '',
  alkalinity: '',
  hardness: '',
  calcium: '',
  ammonia: '',
  nitrite: '',
  phosphorus: '',
  h2s: '',
  plankton_count: ''
}

function FormInput({ onSubmit, isLoading }) {
  const [formData, setFormData] = useState(INITIAL_STATE)

  const handleInputChange = (e) => {
    const { name, value } = e.target
    setFormData(prev => ({
      ...prev,
      [name]: value
    }))
  }

  const applyPreset = (presetName) => {
    setFormData(PRESETS[presetName])
  }

  const resetForm = () => {
    setFormData(INITIAL_STATE)
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    
    // Validate that all fields are filled
    const allFilled = Object.values(formData).every(value => value !== '')
    if (!allFilled) {
      alert("Harap isi semua 14 parameter atau gunakan salah satu Preset Instan!")
      return
    }

    // Convert values to Float numbers before submitting
    const numericData = {}
    Object.keys(formData).forEach(key => {
      numericData[key] = parseFloat(formData[key])
    })

    onSubmit(numericData)
  }

  return (
    <div className="glass-panel rounded-3xl p-6 sm:p-8 relative overflow-hidden">
      
      {/* Visual Accent background glow */}
      <div className="absolute -top-12 -right-12 w-32 h-32 bg-teal-500/10 rounded-full blur-2xl pointer-events-none"></div>
      
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4 mb-6 pb-6 border-b border-slate-800">
        <div>
          <h2 className="text-xl font-bold flex items-center gap-2">
            <Sparkles className="w-5 h-5 text-teal-400" />
            Parameter Sensor Air
          </h2>
          <p className="text-slate-500 text-xs mt-1">Isi data fisikokimia atau pilih preset demo di bawah ini.</p>
        </div>
        <button 
          type="button" 
          onClick={resetForm}
          className="text-xs flex items-center gap-1 text-slate-500 hover:text-slate-100 transition-colors py-1.5 px-3 rounded-lg hover:bg-slate-800"
        >
          <RotateCcw className="w-3.5 h-3.5" />
          Reset Form
        </button>
      </div>

      {/* 3 Quick Presets Section */}
      <div className="mb-6">
        <label className="text-xs font-bold text-slate-400 block mb-3 uppercase tracking-wider">
          Demo Presets (Satu-Klik Isi Otomatis)
        </label>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
          <button
            type="button"
            onClick={() => applyPreset('optimal')}
            className="flex items-center justify-center gap-2 py-2.5 px-4 bg-slate-900 border border-emerald-500/20 hover:border-emerald-500/60 hover:bg-emerald-950/20 text-emerald-400 rounded-xl text-sm font-semibold transition-all duration-200 hover:scale-[1.02]"
          >
            <ShieldCheck className="w-4 h-4" />
            Air Ideal (Optimal)
          </button>
          
          <button
            type="button"
            onClick={() => applyPreset('stressed')}
            className="flex items-center justify-center gap-2 py-2.5 px-4 bg-slate-900 border border-amber-500/20 hover:border-amber-500/60 hover:bg-amber-950/20 text-amber-400 rounded-xl text-sm font-semibold transition-all duration-200 hover:scale-[1.02]"
          >
            <AlertTriangle className="w-4 h-4" />
            Air Stress (Sedang)
          </button>

          <button
            type="button"
            onClick={() => applyPreset('hazardous')}
            className="flex items-center justify-center gap-2 py-2.5 px-4 bg-slate-900 border border-rose-500/20 hover:border-rose-500/60 hover:bg-rose-950/20 text-rose-400 rounded-xl text-sm font-semibold transition-all duration-200 hover:scale-[1.02]"
          >
            <Skull className="w-4 h-4" />
            Air Bahaya (Kritis)
          </button>
        </div>
      </div>

      {/* Main Parameters Form */}
      <form onSubmit={handleSubmit} className="space-y-6">
        
        {/* Category: Physical (Fisik) */}
        <div>
          <h3 className="text-xs font-extrabold text-slate-400 uppercase tracking-wider mb-3 pb-1.5 border-b border-slate-800/40">
            Faktor Fisik
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div>
              <label className="text-xs text-slate-400 block mb-1.5">Suhu (°C)</label>
              <input
                type="number" step="any" required name="temperature" value={formData.temperature} onChange={handleInputChange}
                placeholder="misal: 28.5"
                className="w-full bg-slate-950/80 border border-slate-800 focus:border-teal-500/60 focus:ring-1 focus:ring-teal-500/30 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder:text-slate-700 outline-none transition-all"
              />
            </div>
            <div>
              <label className="text-xs text-slate-400 block mb-1.5">Kekeruhan / Turbidity (cm)</label>
              <input
                type="number" step="any" required name="turbidity" value={formData.turbidity} onChange={handleInputChange}
                placeholder="misal: 45"
                className="w-full bg-slate-950/80 border border-slate-800 focus:border-teal-500/60 focus:ring-1 focus:ring-teal-500/30 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder:text-slate-700 outline-none transition-all"
              />
            </div>
          </div>
        </div>

        {/* Category: Chemical (Kimia) */}
        <div>
          <h3 className="text-xs font-extrabold text-slate-400 uppercase tracking-wider mb-3 pb-1.5 border-b border-slate-800/40">
            Faktor Kimia
          </h3>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
            <div>
              <label className="text-xs text-slate-400 block mb-1.5">pH</label>
              <input
                type="number" step="any" required name="ph" value={formData.ph} onChange={handleInputChange}
                placeholder="0 - 14"
                className="w-full bg-slate-950/80 border border-slate-800 focus:border-teal-500/60 focus:ring-1 focus:ring-teal-500/30 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder:text-slate-700 outline-none transition-all"
              />
            </div>
            <div>
              <label className="text-xs text-slate-400 block mb-1.5">Dissolved Oxygen (mg/L)</label>
              <input
                type="number" step="any" required name="dissolved_oxygen" value={formData.dissolved_oxygen} onChange={handleInputChange}
                placeholder="misal: 6.8"
                className="w-full bg-slate-950/80 border border-slate-800 focus:border-teal-500/60 focus:ring-1 focus:ring-teal-500/30 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder:text-slate-700 outline-none transition-all"
              />
            </div>
            <div>
              <label className="text-xs text-slate-400 block mb-1.5">BOD (mg/L)</label>
              <input
                type="number" step="any" required name="bod" value={formData.bod} onChange={handleInputChange}
                placeholder="misal: 3.2"
                className="w-full bg-slate-950/80 border border-slate-800 focus:border-teal-500/60 focus:ring-1 focus:ring-teal-500/30 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder:text-slate-700 outline-none transition-all"
              />
            </div>
            <div>
              <label className="text-xs text-slate-400 block mb-1.5">CO₂ (mg/L)</label>
              <input
                type="number" step="any" required name="co2" value={formData.co2} onChange={handleInputChange}
                placeholder="misal: 6.0"
                className="w-full bg-slate-950/80 border border-slate-800 focus:border-teal-500/60 focus:ring-1 focus:ring-teal-500/30 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder:text-slate-700 outline-none transition-all"
              />
            </div>
            <div>
              <label className="text-xs text-slate-400 block mb-1.5">Alkalinitas (mg/L)</label>
              <input
                type="number" step="any" required name="alkalinity" value={formData.alkalinity} onChange={handleInputChange}
                placeholder="misal: 120"
                className="w-full bg-slate-950/80 border border-slate-800 focus:border-teal-500/60 focus:ring-1 focus:ring-teal-500/30 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder:text-slate-700 outline-none transition-all"
              />
            </div>
            <div>
              <label className="text-xs text-slate-400 block mb-1.5">Kekerasan / Hardness</label>
              <input
                type="number" step="any" required name="hardness" value={formData.hardness} onChange={handleInputChange}
                placeholder="misal: 110"
                className="w-full bg-slate-950/80 border border-slate-800 focus:border-teal-500/60 focus:ring-1 focus:ring-teal-500/30 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder:text-slate-700 outline-none transition-all"
              />
            </div>
            <div>
              <label className="text-xs text-slate-400 block mb-1.5">Kalsium (mg/L)</label>
              <input
                type="number" step="any" required name="calcium" value={formData.calcium} onChange={handleInputChange}
                placeholder="misal: 85"
                className="w-full bg-slate-950/80 border border-slate-800 focus:border-teal-500/60 focus:ring-1 focus:ring-teal-500/30 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder:text-slate-700 outline-none transition-all"
              />
            </div>
            <div>
              <label className="text-xs text-slate-400 block mb-1.5">Amonia (mg/L)</label>
              <input
                type="number" step="any" required name="ammonia" value={formData.ammonia} onChange={handleInputChange}
                placeholder="misal: 0.02"
                className="w-full bg-slate-950/80 border border-slate-800 focus:border-teal-500/60 focus:ring-1 focus:ring-teal-500/30 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder:text-slate-700 outline-none transition-all"
              />
            </div>
            <div>
              <label className="text-xs text-slate-400 block mb-1.5">Nitrit (mg/L)</label>
              <input
                type="number" step="any" required name="nitrite" value={formData.nitrite} onChange={handleInputChange}
                placeholder="misal: 0.01"
                className="w-full bg-slate-950/80 border border-slate-800 focus:border-teal-500/60 focus:ring-1 focus:ring-teal-500/30 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder:text-slate-700 outline-none transition-all"
              />
            </div>
            <div>
              <label className="text-xs text-slate-400 block mb-1.5">Fosfor / Phosphorus</label>
              <input
                type="number" step="any" required name="phosphorus" value={formData.phosphorus} onChange={handleInputChange}
                placeholder="misal: 0.05"
                className="w-full bg-slate-950/80 border border-slate-800 focus:border-teal-500/60 focus:ring-1 focus:ring-teal-500/30 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder:text-slate-700 outline-none transition-all"
              />
            </div>
            <div>
              <label className="text-xs text-slate-400 block mb-1.5">H₂S (mg/L)</label>
              <input
                type="number" step="any" required name="h2s" value={formData.h2s} onChange={handleInputChange}
                placeholder="misal: 0.002"
                className="w-full bg-slate-950/80 border border-slate-800 focus:border-teal-500/60 focus:ring-1 focus:ring-teal-500/30 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder:text-slate-700 outline-none transition-all"
              />
            </div>
          </div>
        </div>

        {/* Category: Biological (Biologi) */}
        <div>
          <h3 className="text-xs font-extrabold text-slate-400 uppercase tracking-wider mb-3 pb-1.5 border-b border-slate-800/40">
            Faktor Biologi
          </h3>
          <div className="grid grid-cols-1 gap-4">
            <div>
              <label className="text-xs text-slate-400 block mb-1.5">Kepadatan Plankton (Individu/L)</label>
              <input
                type="number" step="any" required name="plankton_count" value={formData.plankton_count} onChange={handleInputChange}
                placeholder="misal: 5500"
                className="w-full bg-slate-950/80 border border-slate-800 focus:border-teal-500/60 focus:ring-1 focus:ring-teal-500/30 rounded-xl px-4 py-2.5 text-sm text-slate-100 placeholder:text-slate-700 outline-none transition-all"
              />
            </div>
          </div>
        </div>

        {/* Submit Button */}
        <button
          type="submit"
          disabled={isLoading}
          className="w-full py-4 px-6 bg-gradient-to-r from-teal-500 to-cyan-500 hover:from-teal-400 hover:to-cyan-400 text-slate-950 font-bold rounded-2xl shadow-lg shadow-teal-500/20 hover:shadow-teal-500/40 text-sm tracking-wider uppercase transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed hover:scale-[1.01]"
        >
          {isLoading ? 'Menganalisis Kualitas Air...' : 'Mulai Analisis Air'}
        </button>

      </form>
    </div>
  )
}

export default FormInput
