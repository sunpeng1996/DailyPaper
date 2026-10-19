---
title: 'Beyond Large Language Models: A Mental World Model Framework for Mental Modeling,
  Simulation, Evolution, and Interpretability'
title_zh: 超越大语言模型：用于心理建模、模拟、演化与可解释性的心理世界模型框架
authors:
- Qingshi Wang
affiliations:
- University of Bristol
arxiv_id: '2610.23722'
url: https://arxiv.org/abs/2610.23722
pdf_url: https://arxiv.org/pdf/2610.23722
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent心智理论 · 心理世界动态建模
tags:
- Theory of Mind
- World Model
- Mental Modeling
- LLM Agent
- Behavior Prediction
one_liner: 提出多分支心理演化架构MMEA，显式建模主观认知与心理动态演化，大幅优于现有ToM方法与通用LLM
practical_value: '- 电商客服Agent可复用认知偏置+心理惯性机制，追踪用户多轮交互中的情绪、隐性需求变化，提升响应匹配度，降低历史情绪积累导致的客诉

  - 推荐系统用户建模可借鉴多分支主观世界构建思路，对用户同一行为的多种认知解释分别建模后加权，提升隐性偏好预测准确率，尤其适配行为与真实偏好冲突的场景

  - 多Agent交互模拟（如直播场域主播-观众互动仿真）可复用MMEA的心理动态演化框架，提升模拟的长期一致性与可解释性，辅助话术优化'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM与心智理论（ToM）方法仅从语义信息推断心理状态，缺乏主观世界构建、认知-心理交互、动态演化与历史依赖的统一机制，无法支撑长期、准确的用户心理与行为预测，限制了个性化交互、多Agent协作等场景的性能。

### 方法关键点
- 核心架构MMEA采用分层感知+多分支并行计算范式：输入事件序列后，先通过5级感知层（事件分解→事实提取→认知固定→组合激活→主观世界生成）构建最多3个并行的主观认知分支，平衡多样性与计算成本
- 引入两类历史依赖机制：Cognitive Bias存储历史认知倾向，在主观世界构建阶段引入历史影响；Mental Inertia存储历史心理状态，通过时间衰减加权融入当前心理计算，历史影响权重上限设为0.5避免覆盖当前事件响应
- 心理状态拆解为40个独立维度，按主观对象、想法、意志、心理学补充维度加权计算后，按各分支激活概率聚合得到全局状态，最终输出行为预测分布

### 关键实验结果
在DynToM、RecToM两个公开ToM基准上对比4款主流LLM、5种专用ToM方法：
- DynToM整体准确率96.48%，超最优LLM 12.13pct，超最优专用ToM方法15.63pct；Why子任务准确率97.50%，超最优LLM 53.75pct
- RecToM整体准确率94.00%，超最优LLM 4.5pct，超最优专用ToM方法13.75pct
- 长序列预测、历史敏感区分、隐性心理推断任务分别较最优LLM提升28.7、39.3、16.6个百分点

### 核心结论
对用户/Agent的心理建模不能仅依赖表层语义匹配，需显式构建主观认知分支、建模历史依赖的心理演化过程，才能实现长期稳定、可解释的行为预测。
