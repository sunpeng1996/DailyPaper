---
title: 'WILDTRACE: Benchmarking Natural Evidence Trails in Long-Context Reasoning'
title_zh: WILDTRACE：长上下文推理的自然证据链路基准测试集
authors:
- Zixin Chen
- Peng Liu
- Haobo Li
- Rui Sheng
- Jianhong Tu
- Xiaodong Deng
- Fei Huang
- Kashun Shum
- Dayiheng Liu
- Huamin Qu
affiliations:
- Hong Kong University of Science and Technology
- Qwen Team, Alibaba Group
arxiv_id: '2607.09328'
url: https://arxiv.org/abs/2607.09328
pdf_url: https://arxiv.org/pdf/2607.09328
published: '2026-07-10'
collected: '2026-07-13'
category: Eval
direction: 长上下文推理 · 基准评估
tags:
- Long-Context
- Reasoning
- Benchmark
- Multi-hop QA
- Evaluation
one_liner: 提出基于文档原生证据结构的长上下文推理基准，消除人工植入证据的评估偏差
practical_value: '- 做长文档类Agent（如售后工单根因分析、长用户评论需求归因、商品手册信息提取）时，可复用其7种证据几何结构分类拆解推理需求，针对性优化模型链路

  - 评估长上下文大模型业务效果时，可借鉴「source-first」标注流程：先从业务原生文档挖掘证据链路再构造测试用例，避免人工构造测试集的分布偏差

  - 多跳推理任务的校验逻辑可复用其leave-one-out消融方法，确保推理必须依赖全部分散证据，而非单条线索即可回答，避免高估模型业务能力'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有长上下文推理基准多采用人工植入事实、反向构造多跳链路的方式，证据分布、风格与真实原生文档差异大，无法准确衡量模型在真实场景下整合分散证据的能力，和业务场景的真实表现关联性弱。

### 方法关键点
- 采用source-first构造流程：先从214份原生长文档（技术事故报告、文学作品）中抽取实体、事件、关系构建文档内部图，再挖掘7种证据几何结构（前向链、交集、对比、时序重建、因果归因、溯因解释、反事实分支）的自然证据链路，最后基于链路生成问题、答案和评分规则
- 多阶段校验：通过无文档测试过滤公开知识捷径、留一法消融确保多跳必要性、源接地校验确保所有答案有文档支撑，最终3506个候选仅留存481个测试用例，留存率13.7%
- 评估时仅向模型提供完整文档和问题，隐藏所有证据位置、链路结构信息，采用多模型评委按评分规则打分，更贴合真实业务场景

### 关键结果
测试18个前沿长上下文模型，最强模型Gemini-3.1-Pro仅达到75.3%准确率，反事实推理类任务平均准确率仅49%，即使上下文长度足够，模型在因果归因、反事实分支等复杂推理几何上仍存在明显短板。

**最值得记住的一句话**：长上下文能力的核心不是能容纳多少token，而是能否基于问题构建保留关键关系的证据状态，在过滤冗余信息的同时不丢失答案依赖的证据关联。
