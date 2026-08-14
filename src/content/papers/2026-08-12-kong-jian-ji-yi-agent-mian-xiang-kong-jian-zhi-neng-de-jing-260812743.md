---
title: 'Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence'
title_zh: 空间记忆Agent：面向空间智能的经验驱动过程记忆框架
authors:
- Haokai Zhang
- Yuhang Ding
- Yunshu Zhou
- Xinze Du
- Shengtao Zhang
- Zhiyue Zhao
- Yuling Xi
- Hao Chen
affiliations:
- Zhejiang University
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
arxiv_id: '2608.12743'
url: https://arxiv.org/abs/2608.12743
pdf_url: https://arxiv.org/pdf/2608.12743
published: '2026-08-12'
collected: '2026-08-14'
category: Agent
direction: Agent 过程记忆优化空间推理能力
tags:
- Spatial Reasoning
- Agent Memory
- VLM
- Transferable Experience
- TRS
- Zero Parameter Update
one_liner: 无需更新VLM参数或调用外部工具，通过经验蒸馏记忆与TRS评分提升VLM空间推理性能
practical_value: '- 记忆检索可复用「语义过滤+可信度加权排序」两段式设计，替代纯语义匹配RAG，解决相似内容实际迁移效果差的问题，可落地于电商导购Agent、多模态商品理解场景

  - 可复用Transfer Reliability Score(TRS)在线校准机制：基于历史检索后的业务反馈更新记忆可信度，无需人工标注记忆质量，适合动态积累用户交互反馈优化记忆库

  - 经验蒸馏阶段可参考「禁止直接输出答案，仅提炼可迁移规则/避坑点/检查步骤」的prompt设计，避免记忆泄露样本标签，提升记忆泛化性

  - 记忆库构建优先用一次性写入机制，而非持续写入，可降低冗余、提升可信度校准效率，适合长周期运行的业务Agent降低存储和检索成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有提升VLM空间推理能力的方案分为两类：一类需微调更新参数，训练成本高、跨场景适配性差；另一类推理时依赖外部深度估计、3D重建等空间工具，推理延迟高、部署链路复杂。同时现有文本Agent的记忆方案多依赖纯语义匹配，无法区分表面相似和实际可迁移的经验，缺乏无参数更新的空间推理自进化路径。

### 方法关键点
- 全程冻结VLM参数，分为记忆写入、TRS校准、只读部署三个阶段，推理无需调用外部工具
- 记忆写入阶段：基于验证器反馈，通过反射模型将推理经验蒸馏为结构化记忆卡，包含任务摘要、可迁移规则/避坑点/检查步骤，禁止直接存储样本答案避免泄露
- 提出Transfer Reliability Score(TRS)：基于记忆被检索后获得的任务奖励在线校准，量化记忆的实际迁移可靠性
- 两段式检索：先通过任务语义相似度过滤候选，再结合归一化语义相似度与TRS加权排序选TopK记忆引导推理

### 关键结果
在5个空间推理基准、4个不同规模冻结Qwen VLM上测试：
- SMA在所有4个VLM上均取得最高平均准确率，相对最强非SMA基线分别提升2.6、2.9、1.7、2.8个百分点，Qwen3.6-27B上相对无记忆基线提升6.5个百分点
- 相对训练-based的SpatialEvo-7B基线，SMA平均准确率提升16.4个百分点
- 记忆库支持跨模型、跨基准迁移，跨模型迁移最高带来9.4个百分点的准确率提升

### 核心结论
最优的记忆不一定是语义最相似的记忆，迁移可靠性将检索从语义匹配转化为证据加权的过程选择
