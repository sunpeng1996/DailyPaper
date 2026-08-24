---
title: 'CLEAR: Continuous Latent Adapter Routing for Utility-Preserving LLM Safety
  Alignment'
title_zh: CLEAR：基于连续隐态适配器路由的效用保留型LLM安全对齐
authors:
- Chengxiao Wang
- Enyi Jiang
- Xiaojing Liao
- Sanmi Koyejo
affiliations:
- University of Illinois at Urbana-Champaign
- Stanford University
arxiv_id: '2608.21278'
url: https://arxiv.org/abs/2608.21278
pdf_url: https://arxiv.org/pdf/2608.21278
published: '2026-08-20'
collected: '2026-08-24'
category: LLM
direction: LLM安全对齐 · 轻量参数高效微调
tags:
- LoRA
- Safety Alignment
- Parameter Efficient Fine-Tuning
- Conditional Routing
- LLM Alignment
one_liner: 通过隐态门控动态调节安全LoRA激活强度，大幅降低LLM安全对齐的效用损失
practical_value: '- 做垂直领域LoRA适配时可参考动态门控机制：比如给营销文案生成、推荐理由生成的合规LoRA加隐态门，仅当内容涉及敏感类query时激活，避免合规微调导致正常生成效果下降

  - 门控训练的trick可复用：对难分样本（比如电商里的擦边营销query、合规边缘query）加权重+ pairwise margin loss，提升门控分类的区分度，降低误判率

  - 不需要额外部署独立的内容审核模型，基于LLM内部隐态的轻量MLP门控参数仅百万级，推理 overhead 极低，适合端侧/低延时的Agent、推荐文案生成场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM安全对齐方法多全局修改模型参数，会显著降低模型在正常query上的推理、生成能力（即对齐税），还容易出现对安全边缘query的过度拒绝，无法兼顾安全与业务效用。

### 方法关键点
- 冻结LLM主干，仅训练安全LoRA+轻量隐态门控模块：门控基于LLM中间层的隐态输出连续[0,1]的风险评分g，动态调节安全LoRA的作用强度 `h'=(W+g∆W)h`，正常query g接近0保留主干能力，有害query g接近1激活安全对齐
- 门控训练优化：对难分的对抗性安全/有害样本加权，新增hard pairwise margin loss拉大有害与正常样本的门控得分差，降低误判
- 安全LoRA仅在有害样本上训练，避免学习正常样本的特征干扰主干能力

### 关键实验
在Llama-3-8B-Instruct、Gemma-2-2B-it等模型上验证，对比全局SFT、全局LoRA等基线：
- Llama-3-8B-Instruct上，HarmBench攻击成功率从32.3%降到0.5%，GSM8K准确率73.46%，比全局SFT/LoRA高出7.1个百分点，XSTest有害请求拒绝率提升到92.5%，过度拒绝率仅4.8%
- 门控模块参数仅66万，远小于Llama Guard等外部审核模型，路由效果优于同等参数的外部分类器

### 核心结论
对齐的核心是按需干预，而不是全局修改模型，用轻量条件路由可以用极低的成本平衡安全与业务效用
