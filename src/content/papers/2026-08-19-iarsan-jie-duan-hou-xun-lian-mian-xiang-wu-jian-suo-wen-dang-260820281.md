---
title: 'Inject, Align, Recover: Staged Post-Training for Retrieval-Free Document Knowledge
  Internalization'
title_zh: IAR三阶段后训练：面向无检索文档知识内化的适配方法
authors:
- Qian Kou
- Xiaofeng Shi
- Xiaosong Qiu
- Hua Zhou
affiliations:
- Beijing Academy of Artificial Intelligence (BAAI)
arxiv_id: '2608.20281'
url: https://arxiv.org/abs/2608.20281
pdf_url: https://arxiv.org/pdf/2608.20281
published: '2026-08-19'
collected: '2026-08-21'
category: Training
direction: LLM领域适配 · 三阶段后训练
tags:
- Post-Training
- Knowledge Internalization
- Catastrophic Forgetting
- Model Merging
- Domain Adaptation
one_liner: 提出IAR三阶段后训练框架，实现无检索知识内化且大幅缓解灾难性遗忘
practical_value: '- 做垂直领域Agent（如电商客服、商品知识问答）时，可复用IAR三阶段流程：先通过文档续写/重构任务密集注入领域知识，再做QA对齐，最后和基座模型合并恢复通用能力，比直接SFT的效果更均衡

  - 适配垂直领域LLM时，不必盲目堆QA数据量，Inject阶段的三种文档生成任务能以更低的标注成本覆盖更全的领域知识，可直接复用这三类数据构造模板

  - 领域适配后通用能力下降时，可直接复用Recover阶段的模型合并策略（SLERP/TIES/DARE等），通过小网格搜索即可在损失不到1%领域精度的前提下，恢复10%+的通用能力，工程实现成本极低

  - 做模型效果评估时，可参考其「领域优先、通用指标做护栏」的选择策略，避免为了单一领域指标牺牲模型的基础指令遵循能力，适配业务落地的效果权衡需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
RAG是当前文档问答的主流落地方案，但存在推理延迟高、隐私泄露风险，对延迟/隐私敏感的场景（如端侧Agent、内部知识库问答），无检索的文档知识内化需求迫切。传统的持续预训练（CPT）或直接SFT方案存在明显缺陷：CPT无法对齐问答行为，SFT的知识覆盖稀疏，且两者都会引发灾难性遗忘，大幅降低模型的通用指令遵循能力，领域精度与通用能力的权衡一直是落地痛点。
### 方法关键点
- **Inject阶段**：设计三类结构化文档生成任务（前缀续写、骨架重构、指令引导的全文重建），以密集监督注入文档知识，信号质量优于普通CPT的无差别语言建模
- **Align阶段**：仅对答案部分计算损失，对注入知识后的模型做QA对齐，将参数化知识映射到问答交互接口
- **Recover阶段**：复用SLERP、TIES、DARE等现成模型合并算子，将领域适配后的模型与原指令基座合并，通过「领域优先、通用指标做护栏」的规则选择最优权衡点，恢复通用能力
### 关键结果
在CC、CCI两个公开数据集，覆盖Llama、Phi、Qwen、SmolLM四个模型族，对比Vanilla SFT、CPT+SFT、LoRA、FAPM等基线，IAR平均提升领域QA精度3.6pp，通用能力（IFEval+MMLU+MSBench均值）提升12.1pp；Qwen3 scaling实验中，Recover阶段仅损失不到1.1pp的领域精度，即可恢复14.9~24.1pp的通用能力。

**最值得记住的一句话**：无检索知识内化无需端到端单一微调，拆分知识注入、任务对齐、能力恢复三个独立阶段，能以极低工程成本得到更适合落地的域内-通用能力权衡点。
