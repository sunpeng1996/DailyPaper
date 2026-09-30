---
title: 'Report: Progressive Disclosure of Agent Skills'
title_zh: Agent技能渐进式披露机制研究报告
authors:
- Guilin Zhang
- Kai Zhao
- Priyanka Mudgal
- Waleed Ammar
- Xiquan Cui
- Xu Chu
- Alet Blanken
affiliations:
- Workday AI Research
arxiv_id: '2609.35692'
url: https://arxiv.org/abs/2609.35692
pdf_url: https://arxiv.org/pdf/2609.35692
published: '2026-09-28'
collected: '2026-09-30'
category: Agent
direction: Agent 技能管理机制优化
tags:
- Agent Skill Management
- Progressive Loading
- LLM Agent
- Cost Optimization
- Skill Retrieval
one_liner: 实测对比Agent技能全量与渐进式加载的成本、时延、召回质量tradeoff并给出落地参考
practical_value: '- 电商客服Agent、推荐解释Agent等多技能场景可直接复用该渐进式加载框架：首轮仅加载所有技能的name+description元数据，命中后再加载完整技能内容，最多可省80%+token成本

  - 技能数量>20的生产Agent优先采用渐进式加载，规避全量加载下技能检索准确率随技能量上升暴跌的问题（14B模型下技能量从5涨到50时全量加载准确率从100%掉到13%）

  - 时延敏感场景可做折中：将高频常用技能全量加载，低频技能走渐进式加载，平衡成本、准确率与时延

  - 技能库建设可统一采用Agent Skills开放标准（name/description/body分层结构），方便适配渐进式加载逻辑，降低技能管理迭代成本'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
生产级LLM Agent普遍通过扩展技能库满足定制化需求，但全量加载所有技能的方案会随技能量上升大幅提升token成本，过长prompt还会降低技能召回准确率、引发上下文溢出，而业界常用的渐进式加载（懒加载）方案的时延、召回质量影响缺乏实测数据支撑，需明确tradeoff指导落地。

### 方法关键点
- 对比两种技能管理机制：全量加载（eager loading）将所有技能完整定义塞入prompt；渐进式加载仅先加载所有技能的name、description元数据，LLM输出结构化指令指定目标技能后，后续轮次再加载该技能完整内容
- 评估维度覆盖技能检索成功率、总token消耗、整体时延、上下文溢出率
- 实验控制技能库规模N为5/20/50/100，加入不同难度干扰技能，采用Qwen2.5-7B、Qwen3-8B、Qwen3-14B三款模型，vLLM部署在L40S GPU上测试

### 关键结果
- 成本：渐进式加载token节省随技能量上升提升，N=50时Qwen3-14B可省81.7%token；N=100时全量加载全部触发上下文溢出，渐进式加载无溢出
- 召回质量：技能量上升时全量加载准确率暴跌，Qwen3-14B在N=5时准确率100%，N=50时仅剩12.5%；渐进式加载在N=50时准确率仍达72%
- 时延：渐进式加载因多一次LLM调用平均时延提升15%左右（N=50时Qwen3-8B从1.75s涨到2.01s），时延差随技能量上升收窄

### 核心结论
技能库规模超过20的生产Agent，优先采用渐进式加载方案，可在仅小幅提升时延的前提下大幅降低成本、提升技能召回稳定性
