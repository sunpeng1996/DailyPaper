---
title: 'Agent Sociodrama: Social-Dynamics-Guided Persona Recasting for LLM Agent Teams'
title_zh: Agent Sociodrama：基于社会动力学的LLM多智能体团队人设重铸框架
authors:
- Yirui Qi
- Xiaoming Zhang
- Jaehong Yoon
affiliations:
- Beihang University
- Nanyang Technological University, Singapore
arxiv_id: '2610.15788'
url: https://arxiv.org/abs/2610.15788
pdf_url: https://arxiv.org/pdf/2610.15788
published: '2026-10-10'
collected: '2026-10-14'
category: MultiAgent
direction: 多智能体协作 · 人设动态优化
tags:
- MultiAgent
- Persona Optimization
- Social Dynamics
- Collaborative Agent
- LLM Agent
one_liner: 基于动态社会关系与情绪建模的多智能体人设重铸框架，大幅提升协作任务表现
practical_value: '- 电商多智能体客服/内容运营协作场景可复用动态情绪+定向关系建模逻辑，快速定位协作卡点（如沉默专家智能体信息未流出、强势智能体带偏决策）

  - 可直接复用TPR（Trajectory-Guided Persona Recasting）逻辑，基于交互轨迹自动迭代优化智能体人设，减少人工调试prompt的成本，适配不同协作任务

  - 广告/电商资源协商、供应链议价等模拟场景可复用双阶段紧急度排序发言机制、社会保真度校验逻辑，提升协商效率与帕累托最优解占比'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多智能体协作系统普遍采用静态人设+固定交互流程，容易出现信息持有者沉默、主导发言者带偏群体决策、规则违反无人纠正等典型社会类故障，这类问题无法通过常规的prompt、拓扑、工作流优化解决，行业缺乏对动态社会关系的可解释建模与有效干预手段。
### 方法关键点
- 提出Agent Sociodrama框架，每个智能体同时维护固定人设、动态情绪值（0-1，越低越负面）、定向不对称关系（包含好感度、关系类型、交互记忆三个维度），每轮交互后由统一外部LLM裁判更新状态
- 采用双阶段发言生成逻辑：先并行输出发言紧急度、模式、目标、意图，再按紧急度降序依次发言，沉默智能体跳过不产生推理成本，消除发言顺序带来的不公平性
- 提出Trajectory-Guided Persona Recasting（TPR）控制器，根据交互transcripts+情绪/关系轨迹诊断故障点，迭代重铸智能体人设，最多3轮迭代即可收敛
### 关键结果
实验覆盖6个主流LLM backbone、5类社交场景、4个协作基准任务，对比SOTOPIA、AgentVerse等基线：
1. 社会保真度方面，与人类标注的关系更新方向一致性达76.2%，情绪更新方向一致性达88.2%
2. 任务表现方面，相较初始人设最高提升83.3%p的准确率，在协商任务上帕累托率最高领先基线37.5%p，4类对比任务中3类表现最优

**最值得记住的结论**：多智能体团队的协作故障本质上很多是社会动力学问题，而非单个智能体的能力问题，可通过建模动态社会状态实现可解释的干预优化
