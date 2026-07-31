---
title: 'Same Evidence, Different Target: Decoding How Diagnostic Evidence Bears on
  Causal Questions from Language-Model States'
title_zh: 相同证据不同目标：从大模型隐状态解码诊断证据对因果问题的作用
authors:
- Weiyi Kong
- Zhuoran Li
affiliations:
- University of Toronto
- The University of Hong Kong
arxiv_id: '2607.26929'
url: https://arxiv.org/abs/2607.26929
pdf_url: https://arxiv.org/pdf/2607.26929
published: '2026-07-29'
collected: '2026-07-31'
category: Reasoning
direction: 大模型因果推理 · 隐状态探测
tags:
- Causal Reasoning
- LLM Probing
- Linear Readout
- Hidden State
- Causal QA
one_liner: 通过配对提示范式验证大模型隐状态包含可线性解码的因果证据适配性信息
practical_value: '- Agent 决策场景可复用线性读头提取LLM倒数第二层隐状态，快速判断召回的证据是否适配当前因果决策问题，降低证据错配导致的幻觉

  - 电商营销/推荐因果归因场景可借鉴配对提示范式构造对照样本，排除prompt措辞、词汇重叠对模型因果判断的干扰，提升归因结果可靠性

  - LLM 下游任务评测可复用配对样本交叉验证思路，避免模型靠表层模式拟合而非真正理解任务，提升评测结果的鲁棒性'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
相同诊断证据对不同人群、 outcome、estimand的因果问题支撑性完全不同，现有LLM回答因果问题时容易受措辞、词汇重叠等表层特征干扰，无法判断模型是否真正理解证据与因果目标的匹配关系。

### 方法关键点
设计配对提示范式，固定诊断证据不变仅修改因果目标，标签分为Favors/Challenges/Unresolved/Wrong Target四类，仅当配对的两个提示都分类正确才算配对恢复；训练线性读头从Qwen2.5-7B-Instruct、Qwen3-8B、Llama-3.1-8B-Instruct的Transformer倒数第二层最后token隐状态解码匹配关系。

### 关键结果数字
9个诊断家族共49对基准样本上，三类模型平衡准确率0.654~0.659，可恢复18~21对配对样本；隐状态读头性能优于基于答案logits、文本基线的线性分类器，跨诊断家族泛化时仍可覆盖全部9个家族共21对样本，人工标注一致性达96.9%。
