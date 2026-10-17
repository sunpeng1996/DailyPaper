---
title: 'LEASH: Uncertainty-Aware Weak-to-Strong Escalation and Oversight for Computer-Use
  Agents'
title_zh: LEASH：面向计算机操作Agent的不确定性感知弱强协同框架
authors:
- Qingni Wang
- Changdae Oh
- Yuzhe Yang
- Sharon Li
- Jiachen Yang
- Ang Li
- Xin Eric Wang
affiliations:
- Simular
- University of Wisconsin–Madison
arxiv_id: '2610.22280'
url: https://arxiv.org/abs/2610.22280
pdf_url: https://arxiv.org/pdf/2610.22280
published: '2026-10-14'
collected: '2026-10-17'
category: Agent
direction: Agent 强弱模型协同成本优化
tags:
- Weak-to-Strong Escalation
- Uncertainty Estimation
- Computer-Use Agent
- Inference Efficiency
- LLM Agent
one_liner: 基于弱模型隐层不确定性的免训练强弱Agent协同框架，平衡任务成功率与推理成本
practical_value: '- 可复用现有小模型的隐层激活做强弱路由的不确定性信号，无需额外前向或训练，适合电商搜索推荐场景的大小模型级联：小模型处理常规请求，不确定请求转大模型重排/生成文案，几乎无额外开销

  - 隐层不确定性仅需少量离线标注的历史成败轨迹构建表征库即可冷启动，可迁移到个性化Query路由、商品推荐理由生成等场景，按需调用大模型控制成本

  - 弱模型转影子观察者的设计可复用现有小模型监控黑盒大模型的输出，无需额外部署监控模型，适合电商导购Agent、智能客服场景，低成本监控大模型回复的合规性与合理性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长周期Agent任务中，全流程调用前沿大模型推理成本过高，而单独使用轻量开源模型成功率不足；现有弱强升级方案要么需额外部署监控Agent推高成本，要么依赖标注数据训练专属监控模块落地门槛高，且升级后黑盒大模型的执行过程缺乏有效监控，容易偏离任务目标。

### 方法关键点
- 三层免训练架构：初始任务不确定性路由+步骤级运行时升级+升级后影子观察者监控，全程复用弱模型隐层状态作为不确定性信号，无额外训练或前向开销
- 离线构建弱模型隐层表征库，关联历史轨迹的成败标签，在线通过马氏距离计算当前隐态与成败表征的相对距离得到不确定性得分，得分越高对应失败概率越高
- 升级后弱模型转为影子观察者，每3步输入强Agent执行轨迹计算不确定性，得分过高则触发强Agent反思重执行
- 路由阈值通过参考集分位数校准，可灵活匹配预设的升级率预算

### 关键实验
在OSWorld基准数据集上测试4种开源弱模型与Claude Opus5强模型的组合；对比随机升级、StepWise、Progress Advantage等基线，同升级率下成功率比随机升级高6.55~11.94pp；用Qwen3.5-35B-A3B作为弱模型时，成功率73.66%与全程调用Claude Opus5的72.90%持平，推理成本降低19.2%。

### 核心结论
弱模型的隐层状态天然携带任务成败的语义信号，仅通过无训练的距离匹配就能同时支撑路由、升级、监控三个核心环节，是性价比极高的强弱模型协同信号。
