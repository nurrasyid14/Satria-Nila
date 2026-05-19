import React, { useState } from 'react'
import FormInput from '../components/FormInput'
import ResultsCard from '../components/ResultsCard'
import { predictWaterQuality } from '../services/api'
import { Activity, Server, Database, TrendingUp } from 'lucide-react'

function Dashboard() {
  const [isLoading, setIsLoading] = useState(false)
  const [predictionResult, setPredictionResult] = useState(null)

  const handleFormSubmit = async (data) => {
    setIsLoading(true)
    setPredictionResult(null)
    
    try {
      const result = await predictWaterQuality(data)
      setPredictionResult(result)
    } catch (error) {
      console.error("Gagal melakukan prediksi:", error)
      alert("Terjadi kesalahan teknis saat menganalisis kualitas air.")
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      
      {/* Dashboard Top Header */}
      <div className="mb-8 flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-3xl font-black tracking-tight text-slate-100 flex items-center gap-2">
            <Activity className="w-8 h-8 text-teal-400" />
            Monitoring Panel
          </h1>
          <p className="text-slate-500 text-sm mt-1">
            Lakukan input parameter sensor air dan analisis kelayakan kualitas kolam ikan nila secara langsung.
          </p>
        </div>

        {/* Integration Status Badges */}
        <div className="flex flex-wrap items-center gap-2.5">
          <div className="inline-flex items-center gap-1.5 px-3 py-1.5 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-400">
            <Server className="w-3.5 h-3.5 text-teal-400" />
            <span>API: <strong className="text-teal-400 font-semibold">Active</strong></span>
          </div>
          <div className="inline-flex items-center gap-1.5 px-3 py-1.5 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-400">
            <Database className="w-3.5 h-3.5 text-cyan-400" />
            <span>Supabase: <strong className="text-cyan-400 font-semibold">Connected</strong></span>
          </div>
        </div>
      </div>

      {/* Main Grid: Form + Results */}
      <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
        
        {/* Left Side: Parameters Inputs (Grid Span 7) */}
        <div className="lg:col-span-7">
          <FormInput onSubmit={handleFormSubmit} isLoading={isLoading} />
        </div>

        {/* Right Side: Prediction Results & Actions (Grid Span 5) */}
        <div className="lg:col-span-5 lg:sticky lg:top-24">
          <ResultsCard result={predictionResult} />
          
          {/* Quick Informational Tip Card under results */}
          {!predictionResult && (
            <div className="mt-4 p-4 bg-slate-900/30 border border-slate-800/40 rounded-2xl flex items-start gap-3">
              <TrendingUp className="w-5 h-5 text-teal-500 shrink-0 mt-0.5" />
              <div className="text-xs text-slate-500 leading-relaxed">
                <span className="font-bold text-slate-400 block mb-1">Tips Demo:</span>
                Anda bisa menekan tombol **"Air Ideal"**, **"Air Stress"**, atau **"Air Bahaya"** pada form di sebelah kiri untuk mengisi seluruh parameter air secara instan.
              </div>
            </div>
          )}
        </div>

      </div>

    </div>
  )
}

export default Dashboard
