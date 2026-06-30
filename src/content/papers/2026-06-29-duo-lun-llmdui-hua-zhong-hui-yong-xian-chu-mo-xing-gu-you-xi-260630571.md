---
title: Attractor States Emerge in Multi-Turn LLM Conversations
title_zh: 多轮LLM对话中会涌现出模型固有吸引子状态
authors:
- Ting-Wen Ko
- Jonas Geiping
affiliations:
- Max Planck Institute for Intelligent Systems
- ELLIS Institute Tübingen
- Tübingen AI Center
arxiv_id: '2606.30571'
url: https://arxiv.org/abs/2606.30571
pdf_url: https://arxiv.org/pdf/2606.30571
published: '2026-06-29'
collected: '2026-06-30'
category: MultiAgent
direction: 多智能体Agent 交互动力学分析
tags:
- MultiAgent
- LLM
- Attractor Dynamics
- Conversation
- Agent Interaction
one_liner: 通过自对战/混对战对比实验，发现多轮LLM交互中存在不对称模型吸引子
practical_value: '- 部署多模型混合Agent系统（如电商客服多Agent、选品Agent集群）时，可提前评估模型的吸引子属性，把高稳定性、低可塑性模型锚定核心角色，高可塑性模型做执行角色

  - 长期运行的自主多Agent系统会自发收敛到模型固有吸引子，需要提前针对目标行为风格做对齐干预，避免不可控的集体行为漂移

  - 需要统一多Agent对话/行为风格时，可搭配少量高吸引力模型作为锚点，就能低成本稳定整体系统的行为特征'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM越来越多地被用于开放域多Agent自主协作、辩论、任务执行等场景，但现有研究多聚焦带明确目标的任务，对开放场景下长期多轮LLM-LLM交互的动态规律认知不足，理解这种规律是设计可预测、可管控的自主Agent系统的基础。

### 方法关键点
- 实验设计：选取20个争议性社会话题，让7种不同开源/闭源LLM开展20轮辩论，设置两个对比场景：1）self-play（自对战）：两个Agent均来自同一模型，分持正反立场；2）mixed-play（混对战）：两个Agent来自不同模型，保持立场分配；额外设置无立场消融实验验证稳定性
- 量化框架：对所有对话做SBERT嵌入，经主题中心化处理后，将self-play中各模型最终收敛的潜在空间区域定义为模型固有吸引子盆；通过分解混对战终点位置相对于两个自对战吸引子的位移，量化伙伴牵引、收缩率、影响力不对称性等指标

### 关键结果
所有模型的吸引子盆分离得分Sbasin均大于1，说明不同模型的吸引子可区分且稳定，不受话题、随机种子影响；混对战平均端点收缩率为23.6%，即不同模型交互后端点距离平均缩短23.6%，且影响高度不对称：Claude Haiku平均伙伴牵引α仅0.266，是影响力最强的稳定吸引子，会将伙伴拉向自身的元评论话语风格；GPT-4.1 nano平均α达0.665，可塑性最高，最易被其他模型改变。同时模型的固有话语特质会明确转移给交互伙伴。

最值得记住的结论：多轮多Agent LLM交互不是随机漂移，而是被模型固有不对称吸引子结构化塑造
