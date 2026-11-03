---
title: Can Large Language Model Agents Learn by Watching Tutorial Videos?
title_zh: 大语言模型Agent能否通过观看教程视频实现自主学习
authors:
- Haoyu Zhao
- Zafeirios Fountas
- Jun Wang
affiliations:
- University College London
arxiv_id: '2611.01460'
url: https://arxiv.org/abs/2611.01460
pdf_url: https://arxiv.org/pdf/2611.01460
published: '2026-10-31'
collected: '2026-11-03'
category: Agent
direction: Agent无参数持续学习 · 视频知识蒸馏
tags:
- LLM Agent
- Continual Learning
- Non-parametric Learning
- Video Knowledge Distillation
- RAG
one_liner: 提出无需参数更新的TAL范式，让LLM Agent可从教程视频持续学习，配套VidLearn基准
practical_value: '- 可复用两阶段对抗式知识提纯思路：将电商场景下的直播教程、商品讲解、运营培训等视频内容，通过「生成难QA→迭代优化知识库」的流程，转化为可直接复用的结构化外部记忆，无需微调LLM即可实现领域知识沉淀

  - TOC检索可直接优化现有RAG系统：给电商商品知识库、售后知识库、运营规则库增加分层目录结构，让LLM自主选择相关章节替代纯embedding相似度检索，解决语义匹配与业务需求不匹配的问题，提升检索准确率

  - 跨模型可迁移的结构化记忆设计：一次构建的领域教程记忆可直接供给不同业务线的不同LLM使用，无需重复构建，大幅降低多Agent场景下的知识沉淀成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM Agent部署后能力冻结，大规模微调成本极高，互联网海量公开教程视频的结构化知识无法被高效利用；现有非参数学习方案中RAG依赖人工标注语料、CBR仅复用历史交互轨迹，均无法实现从公开教程中低成本持续获取可泛化知识。

### 方法关键点
- 两阶段对抗式知识整合：Stage1 对齐视频帧与字幕生成候选QA，仅保留冻结模型无法回答的有效难例形成问题库；Stage2 用问题库迭代优化结构化「教程书」记忆，修改后准确率提升才保留，确保性能单调上升
- TOC树检索：推理时让LLM先读取教程书目录匹配相关章节，再加载对应内容，检索与模型推理直接绑定，解决embedding相似度与任务relevance不匹配的问题

### 关键结果
- 数据集：自建VidLearn基准含72个国际象棋教程视频，补充Photoshop软件教程跨域测试集
- 对比基线覆盖vanilla MLLM、CoT、Transcript-RAG、Video-RAG、Mem0、ReasoningBank等主流方案
- 核心指标：VidLearn上相对vanilla MLLM最高获得113%训练集、91%测试集相对增益；象棋对弈中69%的局开局表现优于基线；Photoshop跨域测试集准确率达49.7%，较最强基线高10.9个百分点；生成的教程书记忆体积较原字幕语料减少82%

### 核心结论
无需参数更新的结构化外部记忆迭代，是LLM Agent低成本持续吸收公开领域知识的高性价比路径
