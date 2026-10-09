---
title: 'REMORY: Learning Residual Memory for Context Compaction'
title_zh: REMORY：面向长上下文压缩的残差记忆学习方法
authors:
- Hanchen Xia
- Baoyou Chen
- Yutang Ge
- Naihao Deng
- Senqiao Yang
- Zilong Dong
- Weihao Yuan
- Siyu Zhu
affiliations:
- Shanghai Academy of AI for Science
- Fudan University
- Shanghai Jiao Tong University
- University of Michigan
- Alibaba Group
arxiv_id: '2610.11287'
url: https://arxiv.org/abs/2610.11287
pdf_url: https://arxiv.org/pdf/2610.11287
published: '2026-10-07'
collected: '2026-10-09'
category: Agent
direction: 长程Agent上下文压缩 · 残差软记忆
tags:
- Agent
- Context Compaction
- Residual Memory
- Soft Token
- Long-context LLM
one_liner: 在文本摘要基础上拼接可学习软记忆token，实现低信息损失的长上下文压缩
practical_value: '- 电商导购Agent、智能客服等长对话场景做上下文压缩时，可复用「文本摘要+软记忆token」架构，既保留可读可审计的摘要，又补充摘要丢失的细粒度信息，减少重复询问用户、重复调用工具的问题

  - 训练可迁移的记忆模块时，可复用两阶段训练范式：第一阶段做上下文重建预训练，第二阶段用冻结LLM的师生反向KL蒸馏对齐全上下文输出，无需修改业务已有的基座LLM权重

  - 长会话电商推荐的用户建模场景，可参考该残差记忆设计，在用户行为摘要后拼接小体量可学习软特征，控制上下文长度的同时提升个性化推荐精度

  - 该方案仅用5.2%的上下文token量即可接近全上下文效果，可直接复用降低长会话场景的token成本和推理延迟'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长 horizon Agent的交互历史、工具输出、决策记录会持续累积，超出LLM上下文窗口上限，现有纯文本摘要压缩方案会丢失细粒度上下文信息，导致后续决策出错、工具调用重复率高，无法满足长周期任务的信息需求。

### 方法关键点
- 提出残差记忆模块REMORY，输入全量历史和生成的文本摘要，输出固定长度的软记忆token，拼接在摘要后共同输入LLM，类似序列维度的残差连接，无需修改基座LLM权重
- 两阶段训练：第一阶段重建任务，让记忆模块学习保留全量上下文的核心信息；第二阶段摘要条件续答任务，用冻结基座的师生反向KL损失，让压缩后的上下文输出对齐全上下文的输出分布
- 层级压缩机制：每1024个源token生成64个软token，最终记忆长度上限为4096，保留源序列顺序

### 关键结果
- SummHay数据集上，仅用5.2%的全上下文token量，联合分数接近全上下文效果，引用F1比纯摘要提升4.04个点，覆盖度几乎不变
- 长程Agent基准测试：Qwen3.8-27B在BrowseComp、Terminal-Bench2.1上分数分别提升3.0、4.5个点，工具重复输出降17.9%~29.8%，工具错误降25.3%~49.7%，多数场景token成本下降
- 同token预算下，软记忆的信息保留效果显著优于额外补充的文本摘要

### 核心结论
上下文压缩不需要在「人类可读的文本摘要」和「模型可用的连续表征」之间二选一，两者结合可以同时满足可审计性和任务性能需求。
