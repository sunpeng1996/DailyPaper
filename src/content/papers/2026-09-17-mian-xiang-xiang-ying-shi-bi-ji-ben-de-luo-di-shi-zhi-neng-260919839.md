---
title: 'Point, Revise, Review: Grounded Agentic Analysis in Reactive Notebooks with
  marimo-lens'
title_zh: 面向响应式笔记本的落地式智能体分析工具marimo-lens
authors:
- Péter Ferenc Gyarmati
- Trevor Manz
- Dominik Moritz
- Mennatallah El-Assady
affiliations:
- ETH Zürich
- CoreWeave, Inc.
- Carnegie Mellon University
arxiv_id: '2609.19839'
url: https://arxiv.org/abs/2609.19839
pdf_url: https://arxiv.org/pdf/2609.19839
published: '2026-09-17'
collected: '2026-09-18'
category: Agent
direction: Agent 人机协作数据分析工具
tags:
- Human-Agent Collaboration
- Visual Grounding
- Reactive Notebook
- Agentic Data Analysis
- Interactive Visualization
one_liner: 提出marimo-lens工具，打通响应式笔记本中人工标注、智能体执行、人类审核的端到端交互链路
practical_value: '- 做业务分析Agent时可复用双重接地思路：用户圈选推荐/广告效果报表区域提问时，自动绑定对应数据生成链路、上游策略/特征代码上下文，省去用户手动描述上下文的成本

  - Agent执行可观测设计：用`start_activity`/`reveal`/`resolve`三类API暴露执行状态与中间结果，支持用户随时中断、修正动作，避免黑盒执行，适配策略调优、效果分析等业务场景

  - 上下文裁剪工程技巧：按依赖拓扑排序优先取近上游单元，限定最多64个单元、总字符≤24000，既控制LLM上下文成本，又降低长上下文信息丢失风险，可直接复用在各类RAG/Agent的上下文处理逻辑中'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前响应式笔记本中的人机协作数据分析存在明显上下文断层：分析师可直接对着可视化输出圈选提问，但智能体仅能操作代码、依赖和运行时状态，无法自动关联用户指向的可视化内容与对应计算链路，用户需要手动描述指向目标、追溯Agent执行过程，交互成本高且易出现理解偏差。

### 方法关键点
- 落地式请求绑定：用户对渲染输出做圈选+文字提问时，自动关联输出对应的生成单元，通过依赖图广度优先遍历上游链路，生成限定范围的计算上下文（最多64个上游单元、总字符≤24000，按依赖拓扑排序输出，避免无关上下文干扰）
- 多模态接地：自动截取标注区域截图并叠加标记，配合多模态LLM理解用户指向的具体内容，同时提供DOM元数据、单元源代码、引用变量等结构化上下文
- 可观测交互协议：设计`start_activity`/`reveal`/`resolve`三类接口暴露Agent执行状态，执行结果直接返回到笔记本标注位置，留存提问标记和处理记录支持后续重开、修正

### 关键结果
基于美国国家美术馆公开数据集做了三轮多轮分析演示：用户依次圈选作品时间分布峰值、提问创作者分布、提问跨创作者作品共性，Agent均能精准理解需求并输出正确结果：1925-1945年的18128幅画作中18094幅属于美国设计索引项目，1936年峰值的创作者分布TOP1仅占1.9%，79位创作者才贡献了总量的一半。

### 核心结论
人机协作智能体分析的核心设计原则是人类注意力、智能体动作、人类审核三个环节必须全程打通，既保留人类对分析方向的控制权，又最大化发挥Agent的计算执行效率。
