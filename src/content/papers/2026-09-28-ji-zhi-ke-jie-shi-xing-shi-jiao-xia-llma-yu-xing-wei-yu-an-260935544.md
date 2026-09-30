---
title: Less Sycophancy, Stronger Refusal? Lessons for AI Safety from Mechanistic Interpretability
title_zh: 机制可解释性视角下LLM阿谀行为与安全拒绝能力的关联研究
authors:
- Xu Wang
- Difan Zou
- Xuansheng Wu
affiliations:
- The University of Hong Kong
- Shanghai Artificial Intelligence Laboratory
- Shenzhen Loop Area Institute
arxiv_id: '2609.35544'
url: https://arxiv.org/abs/2609.35544
pdf_url: https://arxiv.org/pdf/2609.35544
published: '2026-09-28'
collected: '2026-09-30'
category: LLM
direction: 大语言模型安全 · 特征注入训练
tags:
- Sparse Autoencoder
- Mechanistic Interpretability
- LLM Safety
- Sycophancy
- Supervised Fine-Tuning
one_liner: 通过SAE识别阿谀特征并采用补偿特征注入，验证降阿谀仅提升施压场景安全拒绝能力
practical_value: '- 电商客服/导购Agent微调可复用CFI方法：用SAE定位过度迎合、虚假承诺等不良特征，在SFT阶段注入对应特征，无需大量负样本即可降低模型习得违规行为的概率

  - 合规性评估需补充施压场景测试：针对用户要求推荐违规商品、索要非承诺权益等施压场景单独设计评估集，避免仅测直接请求低估合规风险

  - 定向行为修正可减少对齐税：针对特定不良行为用特征注入替代全量对齐训练，在保留模型通用响应能力的前提下修正行为倾向，降低业务场景下的对齐副作用'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM安全训练仅能覆盖有限的有害请求场景，当用户通过表达信任、要求迎合等方式施压时，模型已有的拒绝能力极易被绕过；行业普遍假设降低阿谀（过度迎合用户）行为可直接提升安全拒绝能力，但该假设缺乏机制层面的验证，适用边界也不清晰。
### 方法关键点
- 基于Qwen3.5 2B/9B/35B三个底座模型，构造配对的阿谀响应/独立响应数据集，通过预训练SAE提取跨场景一致性最高的阿谀相关特征
- 提出补偿特征注入（CFI）训练方法：在SFT阶段向指定残差层注入归一化后的阿谀特征，训练完成后完全移除注入逻辑，评估模型持久的行为变化
- 分两个场景评估拒绝能力：无额外修饰的直接有害请求拒绝、附加用户施压话术的同意图有害请求拒绝
### 关键结果
- 正方向CFI相对普通SFT最高降低62.0%的习得阿谀行为（35B模型），效果稳定保留在训练后权重中，无推理额外开销
- 降低阿谀后直接拒绝能力无一致性提升：35B模型仅提升2.1%，2B模型的直接拒绝率反而下降7.1%，随机特征注入也能达到相近的直接拒绝提升效果
- 施压场景下效果显著：正方向CFI相对普通SFT最高提升41.1%的拒绝率，35B模型可恢复95%被普通SFT削弱的施压场景拒绝能力

核心结论：降低LLM阿谀行为无法直接提升通用安全拒绝能力，仅能在用户存在迎合要求的施压场景下强化拒绝表现
