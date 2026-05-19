import React from 'react'
import { CheckCircle2, AlertOctagon, Info, Droplet, ShieldAlert } from 'lucide-react'

const TIER_STYLES = {
  "Good Suitability": {
    themeColor: 'from-emerald-500 to-teal-600',
    borderColor: 'border-emerald-500/30',
    textColor: 'text-emerald-400',
    bgColor: 'bg-emerald-950/15',
    icon: CheckCircle2,
    badgeText: 'Kondisi Optimal',
    description: 'Kualitas air berada dalam kondisi sangat sehat dan optimal bagi siklus pertumbuhan biota akuakultur (Ikan Nila). Tidak memerlukan tindakan darurat.',
    recommendations: [
      'Pertahankan jadwal pembersihan kolam dan monitoring harian.',
      'Beri pakan sesuai dosis standar (3% dari biomassa ikan).',
      'Lakukan pengujian berkala 1 minggu sekali.'
    ]
  },
  "Reduced Suitability": {
    themeColor: 'from-amber-500 to-orange-600',
    borderColor: 'border-amber-500/30',
    textColor: 'text-amber-400',
    bgColor: 'bg-amber-950/15',
    icon: AlertOctagon,
    badgeText: 'Kondisi Stress (Siaga)',
    description: 'Kondisi air mengalami penurunan kualitas dan berada di ambang toleransi kenyamanan ikan. Terdeteksi adanya faktor stress ringan.',
    recommendations: [
      'Nyalakan aerator cadangan untuk meningkatkan asupan Dissolved Oxygen (DO).',
      'Kurangi kapasitas pemberian pakan sementara waktu (puasakan ikan jika perlu) untuk menekan limbah amonia.',
      'Lakukan pergantian air kolam sebanyak 20% secara perlahan.'
    ]
  },
  "Unsuitable": {
    themeColor: 'from-rose-500 to-red-600',
    borderColor: 'border-rose-500/30',
    textColor: 'text-rose-400',
    bgColor: 'bg-rose-950/15',
    icon: ShieldAlert,
    badgeText: 'Kondisi Bahaya (Kritis)',
    description: 'Tingkat keasaman, gas beracun (H₂S/Amonia), atau kadar oksigen berada pada level ekstrem yang mengancam nyawa ikan nila. Risiko kematian massal sangat tinggi.',
    recommendations: [
      'HENTIKAN pemberian pakan segera untuk mencegah pembusukan zat organik di dasar kolam.',
      'Lakukan pergantian air secara masif (minimal 40-50%) secepatnya.',
      'Tambahkan kapur dolomit/pertanian (jika pH terlalu asam) atau zeolit (jika amonia terlalu tinggi).'
    ]
  }
}

function ResultsCard({ result }) {
  if (!result) {
    // Elegant Idle State
    return (
      <div className="glass-panel rounded-3xl p-8 flex flex-col items-center justify-center text-center min-h-[400px] border-dashed border-2 border-slate-800">
        <div className="p-4 bg-slate-900/60 rounded-full text-slate-600 mb-4 animate-pulse">
          <Droplet className="w-12 h-12" />
        </div>
        <h3 className="text-lg font-bold text-slate-300">Menunggu Analisis Air</h3>
        <p className="text-slate-500 text-xs mt-2 max-w-sm">
          Silakan isi form parameter air di sebelah kiri dan klik **"Mulai Analisis Air"** untuk melihat klasifikasi kelayakan air dan rekomendasi dari model SATRIA.
        </p>
      </div>
    )
  }

  const { prediction, confidence, isMock } = result
  
  // Safe-mapping to handle unexpected classes
  const cleanPrediction = TIER_STYLES[prediction] ? prediction : "Reduced Suitability"
  const styles = TIER_STYLES[cleanPrediction]
  const Icon = styles.icon

  return (
    <div className={`glass-panel rounded-3xl p-6 sm:p-8 border ${styles.borderColor} overflow-hidden relative`}>
      
      {/* Decorative Gradient Background Aura */}
      <div className={`absolute -bottom-16 -left-16 w-44 h-44 bg-gradient-to-tr ${styles.themeColor} opacity-5 rounded-full blur-3xl pointer-events-none`}></div>

      {/* Demo Mode Badge */}
      {isMock && (
        <div className="mb-4 inline-flex items-center gap-1.5 py-1 px-3 bg-teal-500/10 border border-teal-500/25 rounded-full text-[10px] text-teal-400 font-bold uppercase tracking-wider">
          <Info className="w-3.5 h-3.5" />
          Inference Fallback (Offline Mode)
        </div>
      )}

      {/* Main Status Header */}
      <div className="flex items-center gap-4 mb-6">
        <div className={`p-3.5 rounded-2xl bg-gradient-to-br ${styles.themeColor} text-slate-950 shadow-lg shadow-black/20`}>
          <Icon className="w-6 h-6" />
        </div>
        <div>
          <span className={`text-[10px] uppercase font-extrabold tracking-widest ${styles.textColor}`}>
            Hasil Klasifikasi Model
          </span>
          <h3 className="text-2xl font-black mt-0.5 tracking-tight">{cleanPrediction}</h3>
        </div>
      </div>

      {/* Description Panel */}
      <div className={`p-4 rounded-2xl ${styles.bgColor} border border-slate-800/40 text-sm leading-relaxed text-slate-300 mb-6`}>
        {styles.description}
      </div>

      {/* Confidence circular progress bar */}
      <div className="mb-8 flex items-center justify-between p-4 bg-slate-950/40 border border-slate-900 rounded-2xl">
        <div className="flex flex-col">
          <span className="text-xs font-bold text-slate-400">Tingkat Keyakinan Model</span>
          <span className="text-xs text-slate-600 mt-0.5">Probabilitas klasifikasi model</span>
        </div>
        <div className="flex items-center gap-3">
          {/* Visual Percentage Progress */}
          <div className="relative w-14 h-14 flex items-center justify-center">
            <svg className="w-full h-full transform -rotate-90">
              <circle cx="28" cy="28" r="23" stroke="#1e293b" strokeWidth="4.5" fill="transparent" />
              <circle 
                cx="28" 
                cy="28" 
                r="23" 
                stroke="currentColor" 
                strokeWidth="4.5" 
                fill="transparent"
                className={styles.textColor}
                strokeDasharray={2 * Math.PI * 23}
                strokeDashoffset={2 * Math.PI * 23 * (1 - confidence)}
              />
            </svg>
            <span className="absolute text-xs font-extrabold">{Math.round(confidence * 100)}%</span>
          </div>
        </div>
      </div>

      {/* Actionable Recommendations List */}
      <div>
        <h4 className="text-xs font-extrabold text-slate-400 uppercase tracking-widest mb-4 flex items-center gap-1.5">
          <Droplet className="w-4 h-4 text-teal-400" />
          Rekomendasi Tindakan Mitigasi
        </h4>
        <ul className="space-y-3">
          {styles.recommendations.map((rec, index) => (
            <li key={index} className="flex items-start gap-2.5 text-sm text-slate-300 bg-slate-950/20 p-3 rounded-xl border border-slate-900/60">
              <span className={`flex items-center justify-center w-5 h-5 rounded-full text-xs font-bold bg-slate-900 border border-slate-800 ${styles.textColor} shrink-0`}>
                {index + 1}
              </span>
              <span>{rec}</span>
            </li>
          ))}
        </ul>
      </div>

    </div>
  )
}

export default ResultsCard
