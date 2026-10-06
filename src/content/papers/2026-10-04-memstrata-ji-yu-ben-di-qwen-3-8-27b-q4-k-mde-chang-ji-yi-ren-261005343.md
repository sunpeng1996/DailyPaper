---
title: 'MemStrata: 95% and 90.91% Source-Aware Accuracy on LongMemEval-500 and LoCoMo-1540
  with a Local Qwen 3.8 27B Q4_K_M Reader'
title_zh: MemStrata：基于本地Qwen 3.8 27B Q4_K_M的长记忆任务源感知准确率达95%/90.91%
authors:
- Neeraj Yadav
affiliations:
- Called It Inc.
arxiv_id: '2610.05343'
url: https://arxiv.org/abs/2610.05343
pdf_url: https://arxiv.org/pdf/2610.05343
published: '2026-10-04'
collected: '2026-10-06'
category: RAG
direction: 长对话RAG · 来源感知证据组装
tags:
- RAG
- Long-Context
- Conversational-Memory
- Source-Aware-Evaluation
- Quantized-LLM
one_liner: 提出保留来源属性的长对话证据组装策略，在两个长记忆评测基准上取得领先准确率
practical_value: '- 对话式导购Agent的长记忆优化可直接复用「保留会话/轮次/时间/发言人元数据+去重+保护核心检索前缀」的证据组装策略，避免丢失上下文关联关系，降低幻觉

  - 长上下文RAG排序阶段可套用论文给出的固定lexical+semantic秩融合公式，无需额外调参即可取得优于纯BM25、纯dense retrieval的效果，仅用22%的全量上下文token即可达到和全量输入相当的效果

  - RAG效果评测可采用「源感知盲评」流程：先让评审模型对照全量源数据校验参考回答合理性，再盲评候选回答，解决传统参考-only评测漏判合理个性化答案、误判幻觉的问题

  - 本地部署Agent推理层可参考选型：Qwen 3.8 27B Q4_K_M量化模型在长记忆任务上效果接近GPT系列，成本远低于云端API，GLM 5.3 flash可作为平替'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有长对话RAG要么直接喂全量上下文导致token浪费、推理延迟高，要么检索截断丢失上下文的时间、发言人、修正关系等关键元信息；同时传统参考-only评测无法校验回答是否符合原始对话上下文，容易误判合理的个性化回答、漏判幻觉，无法满足对话类系统的真实效果评估需求。

### 方法关键点
- 证据组装层：保留所有检索片段的会话ID、轮次ID、时间、发言人、源哈希等元数据，先保留基线检索的核心前缀，再补充候选片段，严格去重重叠区间，总证据token上限设为24000，超预算片段直接跳过不切片
- 排序层：采用固定的lexical+semantic秩融合公式排序候选片段，优先保留跨会话的强相关片段，无额外调参成本
- 评测层：双端评测机制，参考-only端沿用传统语义匹配逻辑，源感知端先让GPT-5.5对照全量源数据校验参考回答的合理性，再盲评候选回答，消除参考偏差

### 关键结果
在LongMemEval-500（500道长对话记忆题）上源感知准确率达95.0%，参考-only准确率92.6%；在LoCoMo-1540（1540道多会话记忆题）上源感知准确率达90.91%，参考-only准确率78.25%；比纯BM25检索高7.6个百分点，比纯dense retrieval高3.2个百分点，仅用22%的全量上下文token就达到和全量上下文输入相当的效果。

最值得记住的一句话：长对话RAG的核心不是堆大上下文窗口，而是在有限token预算下保留上下文的关联属性，源感知评测比传统参考-only评测更贴合真实业务的回答合理性要求。
