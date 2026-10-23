---
title: 'DuoCook: An Overcooked-Inspired Benchmark for Visual Planning and Coordination'
title_zh: 《DuoCook：受《胡闹厨房》启发的视觉规划与多智能体协同基准》
authors:
- Ziyi Jiao
- Heng Zhang
- Drishti Regmi
- Xiaokang Ye
- Lianhui Qin
- Peter Yichen Chen
affiliations:
- University of British Columbia
- University of California, San Diego
arxiv_id: '2610.31511'
url: https://arxiv.org/abs/2610.31511
pdf_url: https://arxiv.org/pdf/2610.31511
published: '2026-10-22'
collected: '2026-10-23'
category: Agent
direction: Agent 多智体协同评测基准
tags:
- VLM
- Multi-Agent
- Benchmark
- Embodied AI
- Task Planning
one_liner: 构建了受《胡闹厨房》启发的Unreal Engine基准，评测VLM集中控制双玩家的规划与协同能力
practical_value: '- 电商多角色协同调度场景（如大促期间多客服/多运营Agent分工、多仓补货调度）可复用集中式VLM控制多Agent架构，引擎处理导航、状态同步等底层逻辑，VLM仅输出高层动作，大幅降低工程复杂度

  - 共享记忆模块设计可直接迁移：采用「自写笔记+指数遗忘曲线+可信度分级+作者区分」的记忆机制，适合跨Agent共享状态场景，实测Claude、Qwen类模型开启记忆收益更高

  - 多维度ROI评估体系可复用：同时监控任务完成率、动作准确率、API调用成本三者联合评估，适合平衡Agent效果和调用开销，尤其适配大促等流量高峰时期的资源调度评估'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前VLM驱动的多Agent协同任务缺乏标准化评测基准，现有方案未覆盖设备竞争、动态地形、跨区域传递等复杂资源约束下的协同场景，也缺少视觉输入+集中式调度的统一评测环境，无法有效量化VLM在动态约束下的规划与多角色调度能力。
### 方法关键点
- 基于Unreal Engine构建20张地图，分5类：基础、共享设备、动态地形、动态地形+共享设备、分离工作区，覆盖从简单到高难度的协同场景
- 单VLM集中控制双玩家，输入包含俯视视觉图像+道具图例+实时状态JSON+合法操作列表+最近6步动作历史，可选共享自写笔记记忆模块；引擎接管导航、碰撞检测等底层逻辑，VLM仅需输出高层动作+网格坐标
- 评测指标包含总分、订单完成率、交付准确率、动作接受率、单episode API成本5个维度，同时做记忆消融实验对比有无共享笔记的效果差异
### 关键实验
对比gpt-6-astra、claude-opus-5、qwen3.8-27b、gemini-3.5-flash-lite四款主流VLM在20张地图上的表现：gpt-6-astra性能最优，订单完成率26.2%，动作接受率64.6%；claude-opus-5交付准确率达100%；记忆模块对不同模型效果差异显著，claude-opus-5开启记忆后平均得分提升4.8，gpt-6-astra和Gemini开启记忆后得分下降，所有模型开启记忆后API成本均上升
### 核心结论
集中式多Agent协同效果与基础模型能力强相关，共享记忆模块并非对所有模型都有正向收益，需要结合效果与成本综合决策
