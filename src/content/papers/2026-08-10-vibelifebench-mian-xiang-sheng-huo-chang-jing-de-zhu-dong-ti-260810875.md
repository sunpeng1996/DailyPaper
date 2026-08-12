---
title: 'VibeLifeBench: Can Your Life Agent Be Proactive and Persistent in a Living
  World?'
title_zh: VibeLifeBench：面向生活场景的主动持久型智能体评测基准
authors:
- Xiaohongshu Inc
affiliations:
- Xiaohongshu Dots Studio
- Evolvent AI
arxiv_id: '2608.10875'
url: https://arxiv.org/abs/2608.10875
pdf_url: https://arxiv.org/pdf/2608.10875
published: '2026-08-10'
collected: '2026-08-12'
category: Agent
direction: Agent 生活场景长周期能力评测
tags:
- Agent Benchmark
- Proactive Agent
- Long-horizon Agent
- LLM Agent Evaluation
- Life Agent
one_liner: 推出覆盖10个生活领域200个长周期任务的主动持久型生活Agent评测基准
practical_value: '- 电商/本地生活个人助理Agent可复用「静默突变事件+主动感知」设计思路，埋点检测Agent是否主动查询订单/物流/库存变动而非等待用户触发，降低投诉率

  - 长周期任务的评分体系可直接复用：分阶段加权+跨阶段约束校验+最终状态核验，比仅看最终结果更适合大促筹备、长周期出行服务等场景的Agent效果评估

  - Agent状态持久化设计可参考结论：必须将用户预算、约束、订单记录等关键信息显式写入持久化存储（如note、数据库）而非仅存于上下文，可大幅降低长周期任务的信息遗忘率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent评测多聚焦静态环境下的短周期单任务，无法衡量生活场景下智能体必需的主动感知、动态环境适配、长周期一致性能力。诸如多周旅行规划、租房纠纷处理等真实场景，环境会自主变化、存在大量未明确说明的隐含约束，仅能被动响应的Agent完全无法胜任，业界缺乏对应评测基准。

### 方法关键点
- 任务设计：覆盖10个生活领域共200个长周期任务，中位模拟时长29天，最长达111天；每个任务是带独立时钟的模拟世界，搭载22个mock服务、288个工具接口
- 事件机制：设置4类事件，其中19.9%为无通知的静默突变（如航班悄悄取消、钓鱼邮件入箱），只有主动重查环境的Agent才能感知，直接量化主动性
- 评分体系：共12261条加权校验规则，分为单阶段校验、跨阶段约束校验、最终状态核验三层，高权重倾斜安全、预算红线等核心约束，仅基于Agent留下的可观测artifact评分，不依赖模型内部推理

### 关键实验
评测7个前沿大模型，最强Claude Opus 5的avg@3仅32.5，best-of-3上限max@3仅41.2，最弱DeepSeek-V4-Pro avg@3仅21.1；所有模型跨阶段校验通过率比单阶段低10-15个百分点，任务后期通过率比前期低10-15个百分点，主动感知相关校验通过率最高仅33.6。

### 核心结论
当前前沿LLM Agent的长周期主动服务能力远未达到生活场景实用要求，主动感知、状态持久化、跨阶段约束一致性是最核心的优化方向。
