/**
 * seekAI Dashboard API 客户端
 */

import axios from 'axios'

const api = axios.create({
  baseURL: '/api',
  timeout: 5000
})

// 获取进度
export function getProgress() {
  return api.get('/progress').then(res => res.data)
}

// 获取任务列表
export function getTasks(phase = null) {
  const params = phase ? { phase } : {}
  return api.get('/tasks', { params }).then(res => res.data)
}

// 获取单个任务
export function getTask(taskId) {
  return api.get(`/tasks/${taskId}`).then(res => res.data)
}

// 提交评分
export function submitReview(data) {
  return api.post('/review', data).then(res => res.data)
}

// 获取统计
export function getStats() {
  return api.get('/stats').then(res => res.data)
}

// 获取成就
export function getAchievements() {
  return api.get('/achievements').then(res => res.data)
}

export default api
