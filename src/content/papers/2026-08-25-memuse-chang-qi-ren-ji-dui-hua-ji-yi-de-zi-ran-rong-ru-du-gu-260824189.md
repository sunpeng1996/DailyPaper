---
title: 'MemUse: Moving Memory Evaluation from Direct QA to Natural Integration in
  Long-Term Human-AI Conversation'
title_zh: MemUse：长期人机对话记忆的自然融入度评估基准
authors:
- Ryuichi Sumida
- Koji Inoue
- Tatsuya Kawahara
affiliations:
- Graduate School of Informatics, Kyoto University
arxiv_id: '2608.24189'
url: https://arxiv.org/abs/2608.24189
pdf_url: https://arxiv.org/pdf/2608.24189
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: Agent 长期对话记忆评估优化
tags:
- LLM Memory
- Conversational Agent
- Evaluation Benchmark
- User Satisfaction
- RAG
- Long Context
one_liner: 发现对话记忆Direct QA评测与用户满意度无关，提出自然融入导向的MEMUSE评估基准
practical_value: '- 做电商导购、客服类对话Agent时，不要以Direct QA准确率为记忆系统核心优化目标，优先迭代用户主动触发记忆场景的自然融入率，后者才和用户满意度正相关

  - 记忆系统选型无需盲目堆叠长上下文长度或RAG召回容量，在基础对话摘要上额外加容量对实际记忆使用效果提升极小，反而会推高延迟；优先选用Mem0、MemGPT类优化记忆融入的组件

  - 尽量少做系统主动的记忆召回（如主动提及用户过往浏览商品），70%的主动召回会被用户忽略，时机错误的召回会让满意度下降0.48个用户内标准差

  - 内部评估记忆系统可复用MEMUSE思路，从真实业务会话中挖掘用户主动cue记忆的case构造评测集，比人工构造的QA集更贴近实际业务效果'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
长对话LLM记忆系统长期默认Direct QA（直接提问过往对话事实）准确率越高，用户满意度越好，但这一假设从未经过长期真实部署验证，大量优化工作可能投入到了用户无感知的方向。
### 方法关键点
- 4个月真人部署实验：40名用户与AI日记助手交互，共1872个会话，随机分配7种记忆条件：仅摘要、长上下文（LC）10/50/100%、RAG 10/50/100%，每个会话收集1-7分用户满意度评分
- MEMUSE基准构造：从真实会话中筛选72个用户主动触发记忆的场景，统一评估三个维度：自然融入度（响应是否自然用到对应记忆）、Direct QA准确率、事实引用率（响应中是否出现QA可答对的事实）
### 关键结果
- 7种记忆条件的Direct QA准确率从19.7%提升至70.1%，但用户满意度波动不足0.06个用户内标准差，无显著差异
- 同模型同上下文下，Direct QA准确率达78.8%，但自然对话中实际引用对应事实的比例仅7.9%，存在71个百分点的检索-融入gap
- 自然融入度与用户满意度相关系数ρ=0.29，显著正相关；Direct QA准确率与满意度相关系数ρ=0.03，完全无关
- 系统主动触发的记忆召回无正向收益，时机错误的召回会使满意度下降0.48个用户内标准差
### 核心结论
对话记忆的核心瓶颈不是检索能力，而是自然融入能力，单纯堆叠检索容量无法提升用户体验
