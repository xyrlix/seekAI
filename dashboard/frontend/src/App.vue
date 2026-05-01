<template>
  <div class="dashboard">
    <header class="header">
      <h1>📚 seekAI 学习中心</h1>
      <div class="user-info">
        <span>学习者</span>
      </div>
    </header>

    <main class="main-content">
      <!-- 统计卡片 -->
      <div class="stats-cards">
        <el-card class="stat-card">
          <div class="stat-icon">✅</div>
          <div class="stat-value">{{ stats.completed_tasks }}/{{ stats.total_tasks }}</div>
          <div class="stat-label">已完成任务</div>
        </el-card>

        <el-card class="stat-card">
          <div class="stat-icon">📊</div>
          <div class="stat-value">{{ progress.avg_score || 0 }}</div>
          <div class="stat-label">平均分数</div>
        </el-card>

        <el-card class="stat-card">
          <div class="stat-icon">🔥</div>
          <div class="stat-value">{{ stats.current_streak }}</div>
          <div class="stat-label">完成数量</div>
        </el-card>

        <el-card class="stat-card">
          <div class="stat-icon">🏆</div>
          <div class="stat-value">{{ stats.achievements_count }}</div>
          <div class="stat-label">获得成就</div>
        </el-card>
      </div>

      <!-- 进度图表 -->
      <div class="charts-section">
        <el-card class="chart-card">
          <template #header>
            <span>📈 各阶段进度</span>
          </template>
          <div ref="progressChartRef" class="chart"></div>
        </el-card>

        <el-card class="chart-card">
          <template #header>
            <span>🎯 能力雷达图</span>
          </template>
          <div ref="radarChartRef" class="chart"></div>
        </el-card>
      </div>

      <!-- 任务列表 -->
      <el-card class="tasks-card">
        <template #header>
          <div class="tasks-header">
            <span>📝 任务列表</span>
            <el-select v-model="selectedPhase" placeholder="筛选阶段" clearable>
              <el-option label="全部" :value="null" />
              <el-option label="Phase 1" :value="1" />
              <el-option label="Phase 2" :value="2" />
              <el-option label="Phase 3" :value="3" />
              <el-option label="Phase 4" :value="4" />
            </el-select>
          </div>
        </template>

        <div class="tasks-list">
          <div
            v-for="task in filteredTasks"
            :key="task.id"
            class="task-item"
            :class="{ completed: task.status === 'completed' }"
          >
            <div class="task-info">
              <span class="task-phase">P{{ task.phase }}-W{{ task.week }}</span>
              <span class="task-name">{{ task.name }}</span>
            </div>
            <div class="task-status">
              <el-tag v-if="task.status === 'completed'" type="success" size="small">
                ✅ 已完成
              </el-tag>
              <el-tag v-else type="info" size="small">
                ⬜ 待完成
              </el-tag>
              <span v-if="task.score" class="task-score">{{ task.score }}/10</span>
            </div>
          </div>
        </div>
      </el-card>

      <!-- 成就列表 -->
      <el-card class="achievements-card">
        <template #header>
          <span>🏅 成就徽章</span>
        </template>
        <div class="achievements-grid">
          <div
            v-for="achievement in achievements"
            :key="achievement.id"
            class="achievement-item"
            :class="{ unlocked: achievement.unlocked_at }"
          >
            <div class="achievement-icon">{{ achievement.icon }}</div>
            <div class="achievement-name">{{ achievement.name }}</div>
            <div class="achievement-desc">{{ achievement.description }}</div>
          </div>
        </div>
      </el-card>
    </main>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import * as echarts from 'echarts'
import { getProgress, getTasks, getStats, getAchievements } from './api'

const progress = ref({ total: 0, completed: 0, avg_score: 0, phases: [] })
const taskList = ref({ tasks: [] })
const stats = ref({ total_tasks: 0, completed_tasks: 0, current_streak: 0, achievements_count: 0 })
const achievements = ref([])
const selectedPhase = ref(null)
const progressChartRef = ref(null)
const radarChartRef = ref(null)

const filteredTasks = computed(() => {
  if (!selectedPhase.value) return taskList.value.tasks
  return taskList.value.tasks.filter(t => t.phase === selectedPhase.value)
})

function initProgressChart() {
  if (!progressChartRef.value) return

  const chart = echarts.init(progressChartRef.value)
  const phaseNames = ['Python基础', '机器学习', '深度学习', 'LLM应用']
  const data = progress.value.phases.map(p => ({
    name: phaseNames[p.phase - 1] || `Phase ${p.phase}`,
    value: p.total > 0 ? Math.round((p.completed / p.total) * 100) : 0
  }))

  chart.setOption({
    tooltip: { trigger: 'axis' },
    xAxis: { type: 'category', data: data.map(d => d.name) },
    yAxis: { type: 'value', max: 100, axisLabel: { formatter: '{value}%' } },
    series: [{
      type: 'bar',
      data: data.map(d => d.value),
      itemStyle: {
        color: function(params) {
          return params.value >= 100 ? '#67C23A' : params.value >= 50 ? '#E6A23C' : '#909399'
        }
      },
      label: { show: true, formatter: '{c}%' }
    }]
  })
}

function initRadarChart() {
  if (!radarChartRef.value) return

  const chart = echarts.init(radarChartRef.value)

  // 根据已完成任务计算能力值
  const completedByPhase = {}
  taskList.value.tasks.forEach(t => {
    if (t.status === 'completed') {
      completedByPhase[t.phase] = (completedByPhase[t.phase] || 0) + 1
    }
  })

  const maxByPhase = { 1: 24, 2: 24, 3: 30, 4: 36 }
  const radarData = [1, 2, 3, 4].map(phase => ({
    name: ['Python', 'ML', 'DL', 'LLM'][phase - 1],
    value: maxByPhase[phase] > 0 ? Math.round(((completedByPhase[phase] || 0) / maxByPhase[phase]) * 100) : 0
  }))

  chart.setOption({
    tooltip: {},
    radar: {
      indicator: radarData.map(d => ({ name: d.name, max: 100 })),
      radius: '60%'
    },
    series: [{
      type: 'radar',
      data: [{ value: radarData.map(d => d.value), name: '能力值' }],
      areaStyle: { color: 'rgba(64, 158, 255, 0.3)' },
      lineStyle: { color: '#409EFF' }
    }]
  })
}

async function loadData() {
  try {
    const [p, t, s, a] = await Promise.all([
      getProgress(),
      getTasks(),
      getStats(),
      getAchievements()
    ])
    progress.value = p
    taskList.value = t
    stats.value = s
    achievements.value = a

    // 初始化图表
    setTimeout(() => {
      initProgressChart()
      initRadarChart()
    }, 100)
  } catch (error) {
    console.error('加载数据失败:', error)
  }
}

onMounted(() => {
  loadData()
})
</script>

<style scoped>
.dashboard {
  min-height: 100vh;
  background: #f5f7fa;
}

.header {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 20px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.header h1 {
  margin: 0;
  font-size: 24px;
}

.main-content {
  padding: 20px 40px;
  max-width: 1400px;
  margin: 0 auto;
}

.stats-cards {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-bottom: 20px;
}

.stat-card {
  text-align: center;
  padding: 20px;
}

.stat-icon {
  font-size: 32px;
  margin-bottom: 10px;
}

.stat-value {
  font-size: 28px;
  font-weight: bold;
  color: #409EFF;
}

.stat-label {
  color: #909399;
  margin-top: 5px;
}

.charts-section {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 20px;
}

.chart-card {
  min-height: 300px;
}

.chart {
  width: 100%;
  height: 250px;
}

.tasks-card {
  margin-bottom: 20px;
}

.tasks-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.tasks-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  max-height: 400px;
  overflow-y: auto;
}

.task-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 12px 16px;
  background: #f9fafb;
  border-radius: 8px;
  border-left: 4px solid #909399;
}

.task-item.completed {
  background: #f0f9eb;
  border-left-color: #67C23A;
}

.task-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.task-phase {
  background: #ecf5ff;
  color: #409EFF;
  padding: 2px 8px;
  border-radius: 4px;
  font-size: 12px;
}

.task-name {
  font-weight: 500;
}

.task-status {
  display: flex;
  align-items: center;
  gap: 10px;
}

.task-score {
  font-weight: bold;
  color: #67C23A;
}

.achievements-card {
  margin-bottom: 20px;
}

.achievements-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 15px;
}

.achievement-item {
  text-align: center;
  padding: 15px;
  background: #f5f7fa;
  border-radius: 8px;
  opacity: 0.5;
  filter: grayscale(1);
}

.achievement-item.unlocked {
  opacity: 1;
  filter: none;
  background: linear-gradient(135deg, #fdfbfb 0%, #ebedee 100%);
}

.achievement-icon {
  font-size: 36px;
  margin-bottom: 8px;
}

.achievement-name {
  font-weight: bold;
  margin-bottom: 4px;
}

.achievement-desc {
  font-size: 12px;
  color: #909399;
}

@media (max-width: 1024px) {
  .stats-cards {
    grid-template-columns: repeat(2, 1fr);
  }
  .charts-section {
    grid-template-columns: 1fr;
  }
  .achievements-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
</style>
