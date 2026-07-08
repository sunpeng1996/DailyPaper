---
title: 'Light-Omni: Reflex over Reasoning in Agentic Video Understanding with Long-Term
  Memory'
title_zh: Light-Omni：带长期记忆的反射式低时延多模态视频理解Agent框架
authors:
- Chang Nie
- Jiaju Wei
- Junlan Feng
- Chaoyou Fu
- Caifeng Shan
affiliations:
- Nanjing University
arxiv_id: '2607.05511'
url: https://arxiv.org/abs/2607.05511
pdf_url: https://arxiv.org/pdf/2607.05511
published: '2026-07-05'
collected: '2026-07-08'
category: Agent
direction: 多模态Agent · 长期记忆低时延优化
tags:
- Multimodal Agent
- Long-term Memory
- Low Latency
- Video Understanding
- Dual Context States
one_liner: 提出双上下文状态的反射式多模态视频Agent，无需迭代推理即可实现低延迟长时序视频理解
practical_value: '- 双状态记忆架构可复用在长会话电商导购Agent场景，异步睡眠时分层合并用户行为、交互历史为全局状态，避免实时推理依赖全量历史，大幅降低时延

  - 潜态语义对齐检索思路可优化电商RAG系统，无需显式query改写，直接通过端到端训练的隐向量修正查询分布，提升口语化等噪声query下的检索准确率

  - 多LoRA任务解耦训练技巧可复用在多任务推荐/Agent场景，避免记忆、生成、决策任务的优化冲突，降低微调成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有带长期记忆的视频Agent多依赖「侦探式」迭代推理补全上下文、弥合检索语义Gap，带来极高的推理成本与时延，本质是缺乏全局上下文建模、查询与记忆分布不对齐导致的，无法适配实时流式多模态交互场景。

### 方法关键点
- 构建三层结构化多模态长期记忆：用户画像+语义记忆+情景记忆，支持异步非阻塞的睡眠时内存整理，不阻塞实时交互
- 双上下文状态设计：全局状态为分层合并的非参数化多模态脚本，采用分辨率衰减的层次化合并策略，保留近期细节同时压缩长期上下文，控制在固定窗口内；潜态为参数化表示，通过软提示联合训练直接生成语义对齐的检索向量与动作决策，单轮前向即可完成全部推理
- 训练层面采用多LoRA解耦记忆、生成、决策三类任务，混合NTP+对比学习目标联合优化，额外叠加特征缓存、冗余token剪枝优化时延

### 关键实验结果
在VideoMME-long、LVBench等长视频基准测试，相比基线Qwen2.5-Omni-7B，准确率提升9.5%，速度提升20.5×，GPU显存占用降低3.3×；相比SOTA推理式Agent M3-Agent，准确率提升2.4%，速度提升12.1×，显存效率提升2.6×，噪声query下性能衰减仅1.3%，远低于普通RAG的5.1%。

### 核心结论
通过全局上下文预构建+隐空间语义对齐，可以将原本需要多轮迭代推理解决的检索对齐问题转化为单轮前向的反射式任务，在不损失效果的前提下大幅降低时延。
