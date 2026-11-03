---
title: 'TRIAGE: Reliability- and Load-Conditioned Escalation for Two-Tier LLM Serving
  with a Semantic Evidence Judge'
title_zh: TRIAGE：带语义证据判别的两层LLM服务负载感知路由策略
authors:
- Basavaraj R M
- Aryan Bharat Kumar
affiliations:
- Independent Researcher
arxiv_id: '2611.01174'
url: https://arxiv.org/abs/2611.01174
pdf_url: https://arxiv.org/pdf/2611.01174
published: '2026-10-31'
collected: '2026-11-03'
category: LLM
direction: LLM 两层服务路由与成本优化
tags:
- LLM-serving
- routing
- semantic-judge
- cost-optimization
- RAG
- two-tier-cascade
one_liner: 提出带语义证据校验和负载动态定价的两层LLM路由机制，实测收益边界与成本变化规律
practical_value: '- 做电商RAG导购、客服Agent时，不要仅用prompt做路由，必须加入检索证据的语义校验，prompt-only路由在证据污染场景下AUROC仅0.5，完全无区分度

  - 两层LLM服务的升级成本非固定值，1rps到10rps下成本上涨21.9倍，峰值流量下可动态调高升级阈值，优先保障服务SLO，牺牲少量精度换取成本下降

  - 上线级联路由前必须用足量hold-out集验证大小模型的效果gap，不要用小样本gate评估，本文66样本gate测出13.6pp gap，实际626条测试集仅2.88pp，导致路由完全无收益

  - 若大小模型的API/算力成本比低于3倍，不建议部署两层路由，实测2-3倍成本比下，路由效果劣于随机路由，反而增加系统复杂度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
两层LLM级联是LLM服务降本的主流方案，但现有prompt-only路由无法感知RAG检索证据是否可支撑答案，且默认升级GPU成本为固定值，实际部署中精度、成本收益往往不达预期。

### 方法关键点
- TRIAGE控制器路由决策同时参考小模型生成后的可靠性状态（token不确定性、自一致性、证据校验等）和负载动态计算的GPU升级成本，支持停止、验证、升级等8种干预动作
- 理论证明仅依赖prompt的路由在证据污染场景下AUROC恒为0.5，必须引入语义证据判别
- 引入Jev语义证据法官，替换原有lexical余弦相似度校验，从证据充分性、答案与证据一致性等维度做语义校验

### 关键结果
- 语义证据法官将证据污染检测AUROC从原lexical方案的0.571提升到0.846，冷启未见过的物品上达0.926，预测小模型错误的AUROC达0.90-0.96
- GPT-3.5→GPT-4级联（成本比17倍）下，效果仅比纯GPT-4低3pp，成本下降79.5%；但大小模型成本比2-3倍的开源模型对下，路由效果差于随机路由
- 单A40卡上，升级成本从1rps到10rps上涨21.9倍，KV cache剩余空间和升级成本无单调相关性
- 66样本小gate测出的7B→32B精度差为13.6pp，实际626条hold-out集上仅2.88pp，导致端到端路由无收益

### 核心结论
两层LLM级联要拿到实际收益，前提是大小模型的精度差足够大且经过足量数据验证，仅靠prompt的路由在RAG场景下完全不可用，负载动态定价是峰值流量下保SLO的有效手段
