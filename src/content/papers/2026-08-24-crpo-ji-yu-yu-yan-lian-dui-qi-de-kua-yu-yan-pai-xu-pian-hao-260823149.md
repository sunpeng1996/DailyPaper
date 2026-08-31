---
title: 'Language Chain in Alignment: Cross-lingual Ranking Preference Optimization'
title_zh: CRPO：基于语言链对齐的跨语言排序偏好优化方法
authors:
- Seungyoon Lee
- Minhyuk Kim
- Jungseob Lee
- Heuiseok Lim
affiliations:
- Korea University
arxiv_id: '2608.23149'
url: https://arxiv.org/abs/2608.23149
pdf_url: https://arxiv.org/pdf/2608.23149
published: '2026-08-24'
collected: '2026-08-31'
category: Training
direction: 跨语言LLM · 偏好优化训练
tags:
- Preference Optimization
- Cross-lingual LLM
- DPO
- LambdaLoss
- Learning to Rank
one_liner: 基于层级排序结构迁移英文偏好知识，大幅提升跨语言LLM对齐效果与鲁棒性
practical_value: '- 跨境电商多语言客服、多语言商品文案生成的LLM对齐场景，可复用CRPO的层级偏好设计，用已有的英文高质量偏好对作为锚点，减少小语种偏好数据的标注量，降低对齐成本

  - 现有DPO/ORPO等二元对齐方法出现训练不稳定、效果退化问题时，可借鉴融合LambdaLoss的排序式偏好优化思路，引入多候选的相对排序信号，替代原有二元对比逻辑，提升对齐稳定性和输出质量

  - 低资源语言的LLM应用场景，可复用CRPO的优先级设计逻辑：优先保证输入输出语言一致性，再优化内容质量，从训练层面避免模型输出语言不匹配的问题

  - 多语言偏好优化的工程实现可优先选用nDCG2加权方案，不需要复杂的nDCG2++也能达到不错的效果，兼顾性能和训练效率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM偏好对齐方法严重依赖英文高质量偏好数据，小语种场景下常出现输出语言不匹配、内容质量低的问题，低资源语言场景下甚至会出现对齐崩溃、性能大幅下降的情况；传统二元对比的DPO类方法无法同时建模语言一致性和内容质量两个优化目标，也难以复用已沉淀的英文偏好知识。

### 方法关键点
- 基于LambdaLoss排序框架扩展DPO，构造跨语言四元候选集：目标语言优解$y_t^w$、目标语言劣解$y_t^l$、英文优解$y_e^w$、英文劣解$y_e^l$，设定层级优先级$\psi(y_t^w) > \psi(y_e^w) > \psi(y_t^l) > \psi(y_e^l)$，同时优化语言一致性和内容质量两个维度
- 设计适配的增益函数，控制语言一致性和质量优化的权重比例，避免语言匹配信号压制内容质量优化；最终损失结合NLL损失和排序损失，由超参数$\alpha$平衡两个目标
- 支持LambdaRank、nDCG2、nDCG2++三种加权方案，实验验证nDCG2在多数场景下性价比最优

### 关键实验
在Llama-2-7B、Llama-3-8B、Mistral-7B三个开源模型，中、韩、印尼、斯瓦希里、孟加拉5种高低资源语言上测试，对比SFT+DPO、CLO两个基线：AlpacaEval长度控制胜率最高比基线高15.92%（Llama-3-8B斯瓦希里场景），MMMLU得分最高超基线4.25分，低资源语言场景下的对齐崩溃问题得到显著缓解。

### 核心结论
跨语言对齐不需要从零构建小语种偏好体系，通过层级排序结构迁移已有的英文偏好知识，既能降低标注成本，还能提升小语种对齐的鲁棒性和效果。
