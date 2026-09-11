---
title: 'When Agents Disagree: Bayesian Backward Reasoning as a Label-Free Anchor for
  Multi-Agent Collective Decision-Making'
title_zh: 多智能体意见分歧场景下基于贝叶斯反向推理的无标签决策锚定方法
authors:
- Ken Chen
- Wei Wang
- Sachith Seneviratne
- Hansani Weeratunge
- Saman Halgamuge
affiliations:
- The University of Melbourne
- Sri Lanka Institute of Information Technology
arxiv_id: '2609.11709'
url: https://arxiv.org/abs/2609.11709
pdf_url: https://arxiv.org/pdf/2609.11709
published: '2026-09-10'
collected: '2026-09-11'
category: MultiAgent
direction: 多智能体 · 集体决策优化
tags:
- Multi-Agent
- Collective Decision Making
- Bayesian Reasoning
- Jensen-Shannon Divergence
- Label-free
one_liner: 提出无标签贝叶斯反向锚定框架，解决多LLM智能体集体决策的正向相关误差问题
practical_value: '- 多Agent召回/排序结果融合场景，可复用反向锚定思路，避免正向投票/LLM judge的共通误差，比如电商多召回策略结果融合，无需额外标注即可做权重校准

  - 可直接复用JS散度跨路径一致性作为排序信号，给不同prompt/模型生成的候选结果做无标签权重分配，比如商品文案生成的多结果择优，无需人工标注即可选优

  - 多Agent决策遇到分歧时，优先用LogLin融合策略，固定wR=0.2即可获得稳定收益，无需额外调参，适合工程快速落地

  - 若有少量标注数据，可复用两阶段校准方法优化反向锚，进一步提升融合效果，冷启动场景性价比极高'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多LLM智能体集体决策依赖投票、LLM judge等正向推理方法，所有参与方都沿证据到结论的同一路径推理，容易产生相关误差，多数出现幻觉时投票或judge也会跟随犯错，缺乏可靠的无标签外部参考解决分歧。

### 方法关键点
- 基于贝叶斯定理构造反向后验R：将输入拆分为上下文证据a和补充证据e，假设条件独立结构a→d→e，通过P(e|d)似然和P(d|a)先验计算反向后验，与正向智能体的后验F_i属于不同因式分解，误差相关性更低
- 用Jensen-Shannon divergence计算每个F_i和R的跨路径一致性，作为无标签排序信号，设计3种training-free聚合策略：MinJS选和R最接近的正向智能体，FwdJS基于一致性给正向结果软加权，LogLin以0.2固定权重把R直接融入融合结果
- 若有少量标注数据，可通过两阶段校准优化反向锚R，不需要重训LLM就能进一步提升效果

### 关键结果
在DDXPlus医疗诊断数据集上测试5个主流LLM backbone，对比随机选择、各类投票规则、LLM judge等baseline：LogLin在智能体分歧子集上比最优正向基线高1.2~4.7pp，所有场景下均为最优；FwdJS比最强基线高0.4~3.5pp；MinJS在所有backbone上都优于随机选择；即使反向后验R单独预测准确率比正向平均低7.8~26.4pp，作为锚点仍能带来稳定提升。

最值得记住的结论：**反向锚的价值不取决于自身的预测准确率，而取决于它和正向池的误差相关性是否足够低，哪怕本身不准，只要能提供差异化的误差分布，就能大幅提升多智能体融合效果**
