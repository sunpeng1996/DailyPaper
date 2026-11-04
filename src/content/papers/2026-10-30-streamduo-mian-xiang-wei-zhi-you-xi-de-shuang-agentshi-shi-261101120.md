---
title: 'StreamDuo: A Live Commentator and a Research Agent for Unseen Games'
title_zh: StreamDuo：面向未知游戏的双Agent实时解说系统
authors:
- Zixian Gao
- Penghao Luo
- Xiangcheng Cao
- Lixin Xiu
- Ziqi Cai
- Zhen Li
- Erwin Wu
- Kaipeng Zhang
affiliations:
- Alaya Lab
- The University of Tokyo
- Georgia Institute of Technology
- Peking University
- Institute of Science Tokyo
arxiv_id: '2611.01120'
url: https://arxiv.org/abs/2611.01120
pdf_url: https://arxiv.org/pdf/2611.01120
published: '2026-10-30'
collected: '2026-11-04'
category: Agent
direction: 双Agent协作 · 实时多模态生成
tags:
- MultiAgent
- Multimodal
- Streaming
- RAG
- LoRA
- On-policy Distillation
one_liner: 双智能体解说系统仅单游戏训练，即可实现10款未知游戏低泄露实时解说
practical_value: '- 多Agent分工架构可直接迁移：将业务系统的通用能力（如电商导购的话术生成、时机决策）和动态领域知识（商品库、活动规则）解耦，通用模块仅需单域训练即可适配不同品类/活动场景，无需全量重训

  - 信息增益触发检索机制可复用：推荐/导购Agent无需逐次调用RAG，仅当外部信息能显著提升生成内容和业务目标的匹配度时才触发检索，大幅降低latency和冗余检索成本

  - 带特权信息的on-policy自蒸馏trick可用：用能访问正确答案的特权模型蒸馏业务模型，仅更新LoRA参数即可解决RAG返回噪声大、模型不会用外部信息的问题，同时保留原有模型的时序决策能力

  - 跨域幻觉抑制方法可复用：训练时随机重命名源域实体，切断模型对源域特定实体的记忆依赖，跨品类/跨场景迁移时可将源域知识泄露率降低一个数量级'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有游戏直播解说模型仅能在训练过的游戏上生效，跨未知游戏迁移时仅能保留说话时机把控能力，实体相关知识完全无法迁移，易出现源游戏实体幻觉（源域泄露）；提前加载全量游戏维基的方案几乎无效，无法匹配当前画面的实时实体，逐秒检索又会造成上下文过载、延迟过高。
### 方法关键点
- 双Agent分工架构：可训练的解说Agent负责实时接收流数据、决策何时说话/提问；冻结的研究Agent仅在被触发时接收当前帧，通过多模态理解+维基BM25检索返回最多3条实体条目，2s延迟后汇入解说上下文
- 两阶段训练策略：1）信息增益标签训练提问头：仅当外部答案能显著提升解说与人工标注的匹配度时标记为需要提问，避免无效调用；训练时随机重命名源游戏实体，切断模型对实体的记忆依赖；2）on-policy自蒸馏优化答案利用：用能访问理想答案的冻结特权模型作为教师，仅更新LoRA参数，让学生模型学会过滤噪声检索结果，同时保留原有时序决策能力
- 异步处理机制：提问后直播流不中断，答案延迟汇入上下文，每秒独立执行解说决策
### 关键实验
仅用《博德之门3》的10286条解说片段训练，测试集覆盖10款完全未知游戏的2470条片段，对比同结构基线Proact-VL：实体召回从0.082提升至0.116，源域泄露率从9.9%降至1.0%，时序偏差更小，LLM评测的解说生动度、整体质量均为最优。
### 核心结论
跨域实时生成任务中，让模型学会「什么时候该调用外部工具」比盲目喂全量知识库、堆砌工具能力的收益高得多
