---
title: 'EviScope: Paired Counterfactual Evidence Diagnostics for Faithful and Efficient
  Grounded Language Models'
title_zh: EviScope：面向可信高效落地大模型的配对反事实证据诊断基准
authors:
- Suryadeep Singh Deswal
affiliations:
- Indian Institute of Technology Roorkee
arxiv_id: '2609.17081'
url: https://arxiv.org/abs/2609.17081
pdf_url: https://arxiv.org/pdf/2609.17081
published: '2026-09-15'
collected: '2026-09-16'
category: Eval
direction: RAG事实性评测 · 反事实干预
tags:
- RAG
- Evaluation
- Counterfactual
- Factuality
- Grounded LLM
- Benchmark
one_liner: 提出配对反事实的RAG评测基准EviScope，可揭示答案准确率掩盖的证据敏感性缺陷
practical_value: '- 电商RAG类应用（商品参数答疑、售后政策问答、客服Agent）评测时，不能只看答案准确率，可复用EviScope的4种证据扰动范式构造测试集，快速定位冲突失明、证据缺失乱答、抗干扰差等问题

  - 本地开源模型部署RAG时，不要盲目添加显式证据分类前置步骤，实测Qwen2.5、Llama3.1添加后QCS分别下降0.35、0.275，需针对业务场景做AB测试再上线

  - 高风险场景（如商品合规宣传、售后政策解答）的RAG系统，需单独监控冲突敏感度、证据缺失拒答率两个指标，避免错误输出导致客诉或合规风险

  - 可复用EviScope的规则化评估逻辑，无需LLM判分即可低成本完成RAG系统的细项能力评估，降低评测成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有RAG系统仅靠最终答案准确率评估存在严重缺陷：正确答案可能来自参数记忆、引用错误来源，甚至在证据不足/冲突时也能蒙对，这类错误无法被单一指标识别，也无法定位根因（如冲突失明、证据缺失时乱答、抗干扰能力差），难以支撑可信RAG的落地优化。
### 方法关键点
- 采用配对反事实评测范式：固定问题，仅修改证据上下文，生成4种变体：充足证据、加无关噪音证据、删除核心证据、插入矛盾证据，对应预期动作分别为回答+正确引用、抗干扰回答、拒答、标记冲突。
- 发布EviScope-V1.1基准：基于SQuAD构造40组共160个样本，标注答案别名、预期动作、支持/冲突文档ID、支持span，无需LLM判分，用规则即可自动化计算指标。
- 核心指标QCS（Quartet Consistency Score）：衡量同一问题在4种证据变体下均符合预期的比例，同时输出证据移除敏感度、抗噪鲁棒性、冲突敏感度等细项指标，精准定位能力短板。
### 关键结果
测试覆盖Qwen2.5-7B、Llama3.1-8B、Gemini3.5 Flash三个模型，对比普通RAG和显式证据分类gate两种prompt策略：
1. 显式证据gate在本地开源模型上表现反而更差：Qwen的QCS从0.5降至0.15，Llama的QCS从0.375降至0.1，且答案准确率完全无法反映该差异（Qwen两种策略答案准确率均为0.738）。
2. Gemini3.5 Flash的QCS最高可达0.875，但仍有5%的概率在证据冲突时直接回答，存在残余冲突失明问题。
### 核心结论
RAG系统评测不能只看答案正确性，必须测试系统对证据变化的敏感性，才能真正解决幻觉、错误引用等落地难题。
