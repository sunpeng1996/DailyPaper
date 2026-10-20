---
title: 'KEEP-Bench: Evaluating Evidence Preservation in Context Compression'
title_zh: KEEP-Bench：上下文压缩的证据留存能力评估基准
authors:
- Ziqing Man
- Di Wu
- Jia-Chen Gu
- Junyi Zhang
- Kai-Wei Chang
- Nanyun Peng
affiliations:
- University of California, Los Angeles
arxiv_id: '2610.26827'
url: https://arxiv.org/abs/2610.26827
pdf_url: https://arxiv.org/pdf/2610.26827
published: '2026-10-19'
collected: '2026-10-20'
category: Eval
direction: LLM 上下文压缩保真度评估
tags:
- Context Compression
- RAG
- Evaluation Benchmark
- Faithfulness
- LLM Efficiency
one_liner: 提出直接评估上下文压缩证据留存的基准及效率指标，覆盖三类复杂证据结构
practical_value: '- 做电商/Agent场景的RAG上下文压缩时，不要仅用下游QA准确率评估，需补充命题级证据留存校验，避免遗漏规格、时效、地域限定、歧义实体关联这类关键业务信息

  - 压缩器选型优先考虑4B~8B规模的开源LLM，其EPR（证据留存效率）最高，平衡效果与推理成本，比盲目用大模型或专用压缩器性价比更高

  - 若业务涉及并行证据（同一关键词对应多商品）、条件证据（不同人群/地区的优惠规则）、不平衡证据（小众商品冷门属性），可复用KEEP-Bench的用例构造方法，搭建业务适配的压缩效果测试集'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有上下文压缩评估依赖下游QA准确率，存在严重误导性：即使压缩结果失真丢失关键证据，LLM也可能依靠参数知识或任务捷径答对，导致证据丢失被低估；同时现有评估很少覆盖并行歧义、条件限定、小众视角这类复杂证据结构，无法反映真实场景下的压缩保真度。

### 方法关键点
- 构建4102个诊断用例，覆盖3种高难度证据结构：并行证据（同一歧义实体对应两条独立推理链）、条件证据（事实附带前置生效限定）、不平衡证据（主流/小众视角的支持文本量差异大）
- 直接评估压缩上下文本身而非下游任务结果，将证据拆分为独立自洽的命题，用All-Rec指标（所有命题均保留才得分）衡量保真度
- 提出EPR（Evidence Preservation Return）指标，量化单位推理算力的证据留存效率

### 关键结果数字
测试17种压缩配置（含专用压缩器、不同规模LLM），核心结论：
1. 专用压缩器整体All-Rec低于10%，10B以下开源LLM低于30%；最强开源模型Gemma-4-31B-it All-Rec仅66.8%，最强闭源模型Claude-Haiku-4.5仅61.6%，即使输入上下文平均仅3.1K tokens，远低于模型支持的上下文窗口
2. 同一模型在不同证据结构下表现差异可达2倍以上，单结构评估结果存在严重偏差
3. EPR在4B~8B模型规模达到峰值，额外增加输出预算仅对强模型有明显提升，反而会拉大强弱模型的能力差距

**最值得记住的一句话**：上下文压缩的核心价值是降本且不丢失关键信息，优先优化压缩器的结构识别与证据留存能力，比单纯堆模型规模、放大输出预算更具业务实用性。
