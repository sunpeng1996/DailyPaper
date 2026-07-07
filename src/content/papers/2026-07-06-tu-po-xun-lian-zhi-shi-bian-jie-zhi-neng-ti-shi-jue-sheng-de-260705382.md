---
title: 'Search Beyond What Can Be Taught: Evolving the Knowledge Boundary in Agentic
  Visual Generation'
title_zh: 突破训练知识边界：智能体视觉生成的搜索协同进化框架
authors:
- Haozhe Wang
- Weijia Feng
- Jinpeng Yu
- Che Liu
- Ping Nie
- Fangzhen Lin
- Jiaming Liu
- Ruihua Huang
- Jimmy Lin
- Wenhu Chen
affiliations:
- Hong Kong University of Science and Technology
- University of Waterloo
- Qwen Applications
- Imperial College London
arxiv_id: '2607.05382'
url: https://arxiv.org/abs/2607.05382
pdf_url: https://arxiv.org/pdf/2607.05382
published: '2026-07-06'
collected: '2026-07-07'
category: Agent
direction: Agent 工具调用与生成器协同优化
tags:
- Agentic Generation
- RAG
- Visual Generation
- Knowledge Boundary
- Co-training
- Tool Use
one_liner: 提出适配生成器动态知识边界的搜索-生成协同训练框架，解决视觉生成的世界知识幻觉问题
practical_value: '- 工具调用策略可复用：采用「gate-filter-integrate」三阶段流水线，判断是否触发搜索、过滤检索噪声、将多模态检索结果转化为结构化生成指令，避免检索噪声破坏原生生成质量，可直接迁移到电商AI作图、商品文案生成等场景的RAG
  pipeline

  - 协同训练范式落地路径：先通过DPO让生成器内化高频检索到的稳定知识，再用拒绝采样微调工具调用策略适配更新后的生成器知识边界，用小模型就能逼近大模型Oracle的工具调用效果，降低线上推理成本

  - 长尾知识评估方法可参考：构建场景化知识敏感评估项（如电商商品属性校验、IP形象还原度）+ 通用生成质量评估项的拆解评估框架，精准定位知识幻觉问题而非生成能力问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有视觉生成模型受训练语料cutoff限制，对长尾实体、新事件、地域文化等开放世界知识的生成幻觉严重，现有基准无法覆盖这类问题；而naive全量搜索会引入噪声，破坏模型本来能正确生成的内容，核心瓶颈是未适配生成器动态变化的知识边界。

### 方法关键点
- 构建SEARCHGEN系列数据集：包含20.8K跨22个领域、12类知识缺失场景的中英双语prompt，配套1M条预缓存多模态搜索语料，支持离线可复现的搜索增强生成研究
- 设计抗噪声智能体搜索流水线：三阶段gate（判断是否需要搜索、选择搜索模态）→ filter（筛选仅填补知识缺口的检索结果）→ integrate（将多模态检索结果转成结构化文本指令，避免像素级噪声污染）
- 提出「先教后搜」协同训练框架：Phase0 用专家标注SFT预热搜索智能体；Phase1 用在线DPO让生成器内化稳定可学习的知识，向外扩展知识边界；Phase2 用拒绝采样微调智能体，适配更新后的生成器边界，仅搜索生成器无法内化的知识

### 关键结果
在SEARCHGEN-BENCH上，开源生成器原生得分仅21-28/100，比带内置搜索的商业生成器低40分；协同训练后，8B小搜索智能体+4B生成器的组合，整体得分31.8，超过同生成器搭配万亿参数Gemini Oracle的31.2分，同时在不需要搜索的prompt上得分提升7分，无性能退化。

### 核心结论
工具调用策略不是通用的，必须和下游生成模型的知识边界动态对齐，才能最大化检索增强的收益同时避免噪声损害。
