<template>
  <div class="min-h-screen bg-slate-950 text-slate-100">
    <!-- Header -->
    <header class="bg-slate-900/80 backdrop-blur-lg border-b border-slate-800 sticky top-0 z-50">
      <div class="max-w-[1600px] mx-auto px-6 py-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-5">
            <div class="w-12 h-12 bg-gradient-to-br from-indigo-600 via-purple-600 to-pink-500 rounded-xl flex items-center justify-center text-xl font-bold text-white shadow-lg shadow-indigo-500/25">
              S
            </div>
            <div>
              <h1 class="text-xl font-bold text-white">seekAI</h1>
              <p class="text-sm text-slate-400">AI 专家成长系统</p>
            </div>
          </div>
          <div class="flex items-center gap-8">
            <div class="flex items-center gap-6 text-sm">
              <div class="text-center">
                <p class="text-2xl font-bold text-emerald-400">{{ completedCount }}</p>
                <p class="text-slate-500">已完成</p>
              </div>
              <div class="text-center">
                <p class="text-2xl font-bold text-amber-400">{{ stats.total_score || 0 }}</p>
                <p class="text-slate-500">平均分</p>
              </div>
              <div class="text-center">
                <p class="text-2xl font-bold text-indigo-400">{{ unlockedAbilities }}</p>
                <p class="text-slate-500">能力</p>
              </div>
            </div>
            <div class="h-10 w-px bg-slate-700"></div>
            <div class="text-right">
              <p class="text-white font-semibold">{{ progressPercent }}%</p>
              <p class="text-xs text-slate-500">总体进度</p>
            </div>
          </div>
        </div>
      </div>
    </header>

    <main class="max-w-[1600px] mx-auto px-6 py-8">
      <!-- Learning Roadmap -->
      <section class="mb-10">
        <div class="flex items-center justify-between mb-6">
          <div>
            <h2 class="text-2xl font-bold text-white">学习路线图</h2>
            <p class="text-slate-400 mt-1">完整的 AI 专家成长路径</p>
          </div>
          <div class="flex items-center gap-3">
            <span class="text-sm text-slate-400">选择 Phase</span>
            <div class="flex gap-2">
              <button v-for="phase in roadmap" :key="phase.id"
                @click="selectedPhase = phase.id"
                class="w-10 h-10 rounded-lg font-bold text-sm transition-all"
                :class="selectedPhase === phase.id
                  ? 'bg-indigo-600 text-white shadow-lg shadow-indigo-500/30'
                  : 'bg-slate-800 text-slate-400 hover:bg-slate-700 hover:text-white'">
                {{ phase.id }}
              </button>
            </div>
          </div>
        </div>

        <!-- Roadmap Timeline -->
        <div class="bg-slate-900/60 rounded-2xl p-6 border border-slate-800">
          <div class="relative">
            <!-- Progress Bar -->
            <div class="absolute top-8 left-0 right-0 h-1.5 bg-slate-800 rounded-full"></div>
            <div class="absolute top-8 left-0 h-1.5 bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-500 rounded-full transition-all duration-700"
                 :style="{ width: progressPercent + '%' }"></div>

            <!-- Phase Nodes -->
            <div class="relative flex justify-between">
              <div v-for="phase in roadmap" :key="phase.id"
                class="flex flex-col items-center relative group cursor-pointer"
                @click="selectedPhase = phase.id">
                <div class="w-16 h-16 rounded-2xl flex items-center justify-center text-2xl font-bold border-2 transition-all duration-300 z-10 mb-4"
                  :class="phase.completed === phase.tasks
                    ? 'bg-emerald-600 border-emerald-500 text-white'
                    : phase.completed > 0
                      ? 'bg-indigo-600 border-indigo-500 text-white'
                      : 'bg-slate-800 border-slate-700 text-slate-400 hover:border-slate-600'">
                  <span v-if="phase.completed === phase.tasks" class="text-emerald-300">✓</span>
                  <span v-else>{{ phase.id }}</span>
                </div>
                <p class="text-sm font-semibold text-center" :class="selectedPhase === phase.id ? 'text-white' : 'text-slate-400'">
                  {{ phase.name }}
                </p>
                <p class="text-xs text-slate-500 mt-1">{{ phase.completed }}/{{ phase.tasks }}</p>
                <p class="text-xs text-slate-600 mt-1">{{ phase.weeks }} 周</p>

                <!-- Hover Card -->
                <div class="absolute top-full mt-4 opacity-0 group-hover:opacity-100 transition-all duration-200 bg-slate-800 rounded-xl p-4 text-sm w-56 z-30 shadow-2xl border border-slate-700"
                     style="transform: translateX(-50%) translateX(50%); left: 50%;">
                  <p class="font-bold text-white mb-2">{{ phase.name }}</p>
                  <p class="text-slate-400 mb-3">{{ phase.description }}</p>
                  <div class="flex items-center gap-2 text-xs">
                    <span class="px-2 py-1 bg-indigo-600/30 text-indigo-300 rounded">{{ phase.completed }} 已完成</span>
                    <span class="px-2 py-1 bg-slate-700 text-slate-300 rounded">{{ phase.tasks - phase.completed }} 待完成</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Main Content Grid -->
      <div class="grid grid-cols-12 gap-6">
        <!-- Left Column: Tasks -->
        <div class="col-span-12 lg:col-span-8">
          <!-- Phase Tasks -->
          <section class="bg-slate-900/60 rounded-2xl p-6 border border-slate-800 mb-6">
            <div class="flex items-center justify-between mb-6">
              <div>
                <h3 class="text-xl font-bold text-white flex items-center gap-3">
                  <span>{{ currentPhaseInfo?.icon }}</span> {{ currentPhaseInfo?.name }}
                </h3>
                <p class="text-slate-400 mt-1">{{ currentPhaseInfo?.description }}</p>
              </div>
              <div class="flex items-center gap-3">
                <select v-model="filterWeek"
                  class="bg-slate-800 text-slate-200 text-sm rounded-lg px-4 py-2 border border-slate-700 focus:border-indigo-500 focus:outline-none">
                  <option :value="null">全部 Week</option>
                  <option v-for="w in currentPhaseInfo?.weekCount || 6" :key="w" :value="w">Week {{ w }}</option>
                </select>
              </div>
            </div>

            <!-- Task Grid -->
            <div class="grid grid-cols-2 md:grid-cols-3 xl:grid-cols-4 gap-4">
              <div v-for="task in phaseTasks" :key="task.id"
                class="bg-slate-800/60 rounded-xl p-4 border transition-all cursor-pointer group"
                :class="task.status === 'completed'
                  ? 'border-emerald-600/50 hover:border-emerald-500'
                  : 'border-slate-700 hover:border-indigo-500/50'"
                @click="openTask(task)">
                <div class="flex items-center justify-between mb-3">
                  <div class="w-10 h-10 rounded-lg flex items-center justify-center text-sm font-bold"
                    :class="task.status === 'completed'
                      ? 'bg-emerald-600 text-white'
                      : 'bg-slate-700 text-slate-300'">
                    {{ task.id }}
                  </div>
                  <span v-if="task.score" class="text-amber-400 text-sm font-bold">⭐ {{ task.score }}</span>
                </div>
                <h4 class="text-white font-medium text-sm mb-1 group-hover:text-indigo-400 transition-colors">
                  {{ task.name.replace('task' + task.id + '_', '').replace('_', ' ') }}
                </h4>
                <p class="text-xs text-slate-500">Week {{ task.week }}</p>
                <div class="mt-3 flex items-center gap-2">
                  <span v-if="task.status === 'completed'"
                    class="inline-flex items-center gap-1 text-xs text-emerald-400 bg-emerald-400/10 px-2 py-1 rounded-full">
                    [OK]
                  </span>
                  <span v-else
                    class="inline-flex items-center gap-1 text-xs text-slate-400 bg-slate-700/50 px-2 py-1 rounded-full">
                    [...]
                  </span>
                </div>
              </div>
            </div>
          </section>

          <!-- All Tasks Quick View -->
          <section class="bg-slate-900/60 rounded-2xl p-6 border border-slate-800">
            <div class="flex items-center justify-between mb-4">
              <h3 class="text-lg font-bold text-white">所有任务</h3>
              <div class="flex items-center gap-4 text-sm">
                <span class="text-slate-400">{{ completedCount }} 已完成</span>
                <span class="text-slate-600">|</span>
                <span class="text-slate-400">{{ totalCount - completedCount }} 待完成</span>
              </div>
            </div>
            <div class="space-y-2 max-h-64 overflow-y-auto">
              <div v-for="task in allTasks" :key="task.id"
                class="flex items-center gap-4 p-3 bg-slate-800/40 rounded-lg hover:bg-slate-800/80 transition-colors cursor-pointer"
                @click="openTask(task)">
                <div class="w-8 h-8 rounded-lg flex items-center justify-center text-xs font-bold"
                  :class="task.status === 'completed' ? 'bg-emerald-600 text-white' : 'bg-slate-700 text-slate-400'">
                  {{ task.id }}
                </div>
                <div class="flex-1">
                  <p class="text-slate-200 text-sm">{{ task.name }}</p>
                  <p class="text-slate-500 text-xs">Phase {{ task.phase }} · Week {{ task.week }}</p>
                </div>
                <span v-if="task.score" class="text-amber-400 text-sm font-bold">⭐ {{ task.score }}</span>
                <span v-else class="text-slate-600 text-sm">[未评分]</span>
              </div>
            </div>
          </section>
        </div>

        <!-- Right Column: Abilities & Stats -->
        <div class="col-span-12 lg:col-span-4 space-y-6">
          <!-- Ability Radar -->
          <section class="bg-slate-900/60 rounded-2xl p-6 border border-slate-800">
            <h3 class="text-lg font-bold text-white mb-4">能力雷达图</h3>
            <div ref="radarChartRef" class="h-72"></div>
            <div class="mt-4 grid grid-cols-2 gap-2">
              <div v-for="layer in abilityLayers" :key="layer.id"
                class="flex items-center gap-2 p-2 rounded-lg bg-slate-800/50">
                <span class="text-lg">{{ layer.icon }}</span>
                <div class="flex-1">
                  <p class="text-slate-300 text-xs">{{ layer.name }}</p>
                  <p class="text-indigo-400 text-sm font-bold">{{ layer.level }}%</p>
                </div>
              </div>
            </div>
          </section>

          <!-- Ability Knowledge Graph -->
          <section class="bg-slate-900/60 rounded-2xl p-6 border border-slate-800">
            <h3 class="text-lg font-bold text-white mb-4">知识图谱</h3>
            <div ref="graphChartRef" class="h-64"></div>
            <p class="text-slate-500 text-xs mt-3 text-center">37 项能力 · 7 大维度</p>
          </section>

          <!-- Recent Achievements -->
          <section class="bg-slate-900/60 rounded-2xl p-6 border border-slate-800">
            <h3 class="text-lg font-bold text-white mb-4">最近成就</h3>
            <div class="space-y-3">
              <div v-for="task in recentCompleted" :key="task.id"
                class="flex items-center gap-3 p-3 bg-slate-800/50 rounded-lg">
                <div class="w-10 h-10 bg-emerald-600/20 rounded-lg flex items-center justify-center">
                  <span class="text-emerald-400">[OK]</span>
                </div>
                <div class="flex-1">
                  <p class="text-slate-200 text-sm">{{ task.name }}</p>
                  <p class="text-slate-500 text-xs">Phase {{ task.phase }}</p>
                </div>
                <span v-if="task.score" class="text-amber-400 text-sm font-bold">⭐{{ task.score }}</span>
              </div>
              <p v-if="recentCompleted.length === 0" class="text-slate-500 text-sm text-center py-4">
                暂无完成的任务
              </p>
            </div>
          </section>
        </div>
      </div>
    </main>

    <!-- Code Editor Modal -->
    <div v-if="showEditor" class="fixed inset-0 bg-slate-950/98 z-50 flex flex-col">
      <div class="bg-slate-900 px-6 py-4 flex items-center justify-between border-b border-slate-800">
        <div class="flex items-center gap-4">
          <h3 class="text-white font-bold text-lg">{{ currentTask?.name }}</h3>
          <span class="text-slate-500 text-sm">Phase {{ currentTask?.phase }} · Week {{ currentTask?.week }}</span>
        </div>
        <div class="flex items-center gap-4">
          <button @click="runCode"
            class="bg-emerald-600 hover:bg-emerald-700 text-white px-5 py-2 rounded-lg font-medium text-sm flex items-center gap-2 transition-colors">
            <span>▶</span> 运行代码
          </button>
          <button @click="showEditor = false" class="text-slate-400 hover:text-white transition-colors">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
            </svg>
          </button>
        </div>
      </div>

      <div class="flex-1 flex">
        <!-- Code Editor -->
        <div class="flex-1 p-4 flex flex-col">
          <div class="flex items-center gap-4 mb-3">
            <span class="text-sm text-slate-400">Python 代码编辑器</span>
            <div class="flex-1 h-px bg-slate-800"></div>
          </div>
          <div class="flex-1 bg-slate-900 rounded-xl border border-slate-800 overflow-hidden flex flex-col">
            <div class="bg-slate-900 px-4 py-2 border-b border-slate-800 flex items-center gap-2">
              <span class="w-3 h-3 rounded-full bg-red-500"></span>
              <span class="w-3 h-3 rounded-full bg-amber-500"></span>
              <span class="w-3 h-3 rounded-full bg-emerald-500"></span>
              <span class="ml-4 text-xs text-slate-500">main.py</span>
            </div>
            <textarea
              v-model="code"
              @keydown.tab.prevent="insertTab"
              class="flex-1 w-full bg-slate-900 text-slate-100 p-4 font-mono text-sm resize-none focus:outline-none leading-relaxed"
              :class="{'text-slate-400 placeholder-slate-600': !code}"
              placeholder="# 在此编写 Python 代码...&#10;# 按 Tab 键插入缩进&#10;# 代码将发送到后端执行"
              spellcheck="false"
            ></textarea>
          </div>
        </div>

        <!-- Output Panel -->
        <div class="w-[400px] border-l border-slate-800 flex flex-col">
          <div class="bg-slate-900 px-4 py-2 border-b border-slate-800 flex items-center justify-between">
            <span class="text-sm text-slate-300">输出</span>
            <div class="flex items-center gap-2">
              <button @click="clearOutput" class="text-xs text-slate-500 hover:text-slate-300">清除</button>
            </div>
          </div>
          <div class="flex-1 p-4 overflow-auto bg-slate-950">
            <pre class="text-sm font-mono whitespace-pre-wrap leading-relaxed"
              :class="outputError ? 'text-red-400' : 'text-slate-300'">{{ output || '运行代码后显示输出结果...' }}</pre>
          </div>
        </div>
      </div>
    </div>

    <footer class="border-t border-slate-900 py-6 mt-8">
      <div class="max-w-[1600px] mx-auto px-6 text-center">
        <p class="text-slate-600 text-sm">seekAI 学习系统 · 持续学习 · 成就未来</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch, nextTick } from 'vue'
import * as echarts from 'echarts'
import { getProgress, getTasks, getStats, getAbilities, getTaskContent } from './api'

const progress = ref({ phases: [] })
const taskList = ref({ tasks: [] })
const stats = ref({ completed_tasks: 0, total_score: 0 })
const abilities = ref([])
const selectedPhase = ref(1)
const filterWeek = ref(null)
const showEditor = ref(false)
const currentTask = ref(null)
const code = ref('')
const output = ref('')
const outputError = ref(false)
const radarChartRef = ref(null)
const graphChartRef = ref(null)
const pyodideInstance = ref(null)

// 监听 phase 变化，重新加载任务
watch(selectedPhase, async (newPhase) => {
  try {
    const data = await getTasks(newPhase)
    taskList.value = { tasks: data.tasks || data }
    filterWeek.value = null
  } catch (e) {
    console.error('Failed to load tasks:', e)
  }
})

// Roadmap data
const roadmap = computed(() => [
  { id: 1, name: 'Python基础', icon: '🐍', tasks: 30, completed: 0, weeks: 7, description: 'Python语法、数据结构、函数编程、numpy/pandas、矩阵运算' },
  { id: 2, name: '机器学习', icon: '🤖', tasks: 12, completed: 0, weeks: 2, description: '监督学习、无监督学习、特征工程、模型评估' },
  { id: 3, name: '深度学习', icon: '🧠', tasks: 15, completed: 0, weeks: 3, description: '神经网络、CV、NLP、强化学习' },
  { id: 4, name: '模型优化', icon: '⚡', tasks: 3, completed: 0, weeks: 1, description: '模型裁剪、量化、知识蒸馏' },
  { id: 5, name: 'LLM应用', icon: '💬', tasks: 6, completed: 0, weeks: 2, description: 'Prompt工程、上下文工程、API调用' },
  { id: 6, name: 'AI框架', icon: '🔧', tasks: 3, completed: 0, weeks: 1, description: 'LangChain、LangGraph、LlamaIndex' },
  { id: 7, name: 'AI Infra', icon: '🚀', tasks: 4, completed: 0, weeks: 2, description: 'Agent开发、微调部署、AI工作流' },
].map(p => {
  const tasks = taskList.value.tasks?.filter(t => t.phase === p.id) || []
  const completed = tasks.filter(t => t.status === 'completed').length
  return { ...p, completed }
}))

const currentPhaseInfo = computed(() => roadmap.value.find(r => r.id === selectedPhase.value))

const phaseTasks = computed(() => {
  let tasks = taskList.value.tasks?.filter(t => t.phase === selectedPhase.value) || []
  if (filterWeek.value) tasks = tasks.filter(t => t.week === filterWeek.value)
  return tasks
})

const allTasks = computed(() => taskList.value.tasks || [])
const totalCount = computed(() => taskList.value.tasks?.length || 48)
const completedCount = computed(() => taskList.value.tasks?.filter(t => t.status === 'completed').length || 0)
const progressPercent = computed(() => totalCount.value ? Math.round((completedCount.value / totalCount.value) * 100) : 0)
const unlockedAbilities = computed(() => abilities.value.filter(a => a.level > 0).length)

const recentCompleted = computed(() =>
  taskList.value.tasks?.filter(t => t.status === 'completed').slice(-5).reverse() || []
)

const abilityLayers = computed(() => [
  { id: 0, name: '认知与思维', icon: '🔮', level: 50 },
  { id: 1, name: '数学与理论', icon: '📐', level: getPhaseLevel(1) },
  { id: 2, name: '核心技术', icon: '🧠', level: getPhaseLevel(2) },
  { id: 3, name: '大模型专项', icon: '💬', level: getPhaseLevel(3) },
  { id: 4, name: '工程与落地', icon: '🏗️', level: getPhaseLevel(4) },
  { id: 5, name: '行业应用', icon: '🎯', level: getPhaseLevel(5) },
  { id: 6, name: '软技能', icon: '🤝', level: getPhaseLevel(6) },
])

function getPhaseLevel(phase) {
  const tasks = taskList.value.tasks?.filter(t => t.phase === phase) || []
  if (!tasks.length) return 0
  const completed = tasks.filter(t => t.status === 'completed').length
  return Math.round((completed / tasks.length) * 100)
}

async function openTask(task) {
  currentTask.value = task
  showEditor.value = true
  code.value = '# ' + task.name + '\n\n'
  output.value = ''
  outputError.value = false
  try {
    const result = await getTaskContent(task.id)
    if (result.content) {
      code.value = result.content
    }
  } catch (e) {
    console.error('Failed to load task content:', e)
  }
}

function insertTab(e) {
  const start = e.target.selectionStart
  const end = e.target.selectionEnd
  code.value = code.value.substring(0, start) + '    ' + code.value.substring(end)
  nextTick(() => {
    e.target.selectionStart = e.target.selectionEnd = start + 4
  })
}

async function loadPyodideInstance() {
  if (!pyodideInstance.value) {
    output.value = 'Loading Python environment...\n'
    pyodideInstance.value = await window.loadPyodide()
    output.value = 'Python environment ready.\n'
  }
  return pyodideInstance.value
}

async function runCode() {
  if (!code.value.trim()) {
    output.value = '请先编写代码'
    outputError.value = true
    return
  }
  output.value = 'Running in browser (Pyodide)...\n'
  outputError.value = false
  try {
    const pyodide = await loadPyodideInstance()

    // Capture stdout
    pyodide.runPython(`
import sys
from io import StringIO
sys.stdout = StringIO()
sys.stderr = StringIO()
`)

    // Run user code
    await pyodide.runPythonAsync(code.value)

    // Get output
    const stdout = pyodide.runPython('sys.stdout.getvalue()')
    const stderr = pyodide.runPython('sys.stderr.getvalue()')

    if (stderr && stderr.trim()) {
      output.value = stdout + '\n[Error] ' + stderr
      outputError.value = true
    } else {
      output.value = stdout || '(无输出)'
      outputError.value = false
    }
  } catch (e) {
    output.value = '[Error] ' + e.message
    outputError.value = true
  }
}

function clearOutput() {
  output.value = ''
  outputError.value = false
}

function initRadarChart() {
  if (!radarChartRef.value) return
  const chart = echarts.init(radarChartRef.value)
  chart.setOption({
    tooltip: { trigger: 'item', backgroundColor: 'rgba(30, 41, 59, 0.95)', borderColor: '#475569' },
    radar: {
      indicator: abilityLayers.value.slice(1).map(l => ({ name: l.name, max: 100 })),
      axisName: { color: '#94a3b8', fontSize: 11 },
      splitNumber: 4,
      splitLine: { lineStyle: { color: 'rgba(100, 116, 139, 0.2)' } },
      splitArea: { areaStyle: { color: ['rgba(30, 41, 59, 0.3)', 'rgba(30, 41, 59, 0.5)'] } },
      axisLine: { lineStyle: { color: 'rgba(100, 116, 139, 0.3)' } }
    },
    series: [{
      type: 'radar',
      data: [{
        value: abilityLayers.value.slice(1).map(l => l.level),
        name: '能力值',
        areaStyle: { color: 'rgba(99, 102, 241, 0.4)' },
        lineStyle: { color: '#6366f1', width: 2 },
        itemStyle: { color: '#6366f1' }
      }]
    }]
  })
}

function initGraphChart() {
  if (!graphChartRef.value) return
  const chart = echarts.init(graphChartRef.value)

  // Build knowledge graph from abilities
  const phaseNames = ['认知与思维', '数学与理论', '核心技术', '大模型专项', '工程与落地', '行业应用', '软技能']
  const phaseColors = ['#8b5cf6', '#06b6d4', '#10b981', '#f59e0b', '#ef4444', '#ec4899', '#6366f1']

  const nodes = abilities.value.map(a => ({
    name: a.name,
    value: a.level,
    draggable: true
  }))

  // Create links between abilities in same phase
  const links = []
  const phaseAbilities = {}
  abilities.value.forEach(a => {
    if (!phaseAbilities[a.phase]) phaseAbilities[a.phase] = []
    phaseAbilities[a.phase].push(a.name)
  })
  Object.values(phaseAbilities).forEach(abilities => {
    for (let i = 0; i < abilities.length - 1; i++) {
      links.push({ source: abilities[i], target: abilities[i + 1] })
    }
  })

  chart.setOption({
    tooltip: { trigger: 'item', backgroundColor: 'rgba(30, 41, 59, 0.95)', borderColor: '#475569' },
    series: [{
      type: 'graph',
      layout: 'force',
      nodes: nodes.map(n => ({
        name: n.name,
        value: n.value,
        symbolSize: Math.max(20, n.value / 5),
        itemStyle: { color: '#6366f1' }
      })),
      links: links.map(l => ({ ...l, lineStyle: { color: '#475569', width: 1 } })),
      roam: true,
      label: { show: true, fontSize: 9, color: '#94a3b8' },
      force: { repulsion: 50, edgeLength: 80 }
    }]
  })
}

async function loadData() {
  try {
    const [p, t, s, a] = await Promise.all([
      getProgress(),
      getTasks(),
      getStats(),
      getAbilities()
    ])
    progress.value = p
    taskList.value = t
    stats.value = s
    abilities.value = a
    setTimeout(() => {
      initRadarChart()
      initGraphChart()
    }, 100)
  } catch (e) {
    console.error('Load error:', e)
  }
}

onMounted(loadData)
</script>
