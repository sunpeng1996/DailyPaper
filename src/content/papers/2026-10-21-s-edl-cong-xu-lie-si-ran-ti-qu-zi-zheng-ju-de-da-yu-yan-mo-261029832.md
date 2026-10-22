---
title: 'S-EDL: Eliciting Self-Evidence from Sequence Likelihoods for Semantic Calibration
  of LLMs'
title_zh: S-EDL：从序列似然提取自证据的大语言模型语义校准方法
authors:
- Yawei Li
- Jiazheng Li
- David Rügamer
- Bernd Bischl
- Yulan He
- Mina Rezaei
affiliations:
- LMU Munich
- King's College London
- Munich Center for Machine Learning (MCML)
arxiv_id: '2610.29832'
url: https://arxiv.org/abs/2610.29832
pdf_url: https://arxiv.org/pdf/2610.29832
published: '2026-10-21'
collected: '2026-10-22'
category: LLM
direction: LLM训练 · 开放生成语义校准
tags:
- LLM Calibration
- Evidential Deep Learning
- Semantic Calibration
- Open-ended Generation
- LoRA
one_liner: 提出无需固定分类标签的自证据EDL框架，同步提升开放生成准确率与语义校准效果
practical_value: '- 电商客服、商品咨询类Agent可直接复用S-EDL框架做语义校准，无需预设固定答案分类，即可优化生成回复的置信度对齐，降低幻觉导致的客诉

  - 训练实现成本低：仅需在SFT基础上增加EDL损失项，配合LoRA微调即可生效，无需修改模型主干结构，可快速适配现有垂域LLM微调管线

  - 语义聚类的find-first算法可直接复用在推荐场景的生成候选去重、Query改写聚类等任务，将O(N²)的LLM-as-judge调用成本降至接近O(N)

  - 垂域小样本微调优先选S-EDL：跨域测试中其准确率、校准效果均优于SFT、Dr.GRPO等基线，适合电商多品类、多场景的LLM能力迁移'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
开放生成场景下多token序列可表达相同语义，现有校准方法要么适配固定分类任务，要么仅校准单条输出的二元正确性，无法对齐语义级置信度，导致LLM生成内容的可信度难以量化，无法满足Agent、推荐文案生成等场景的可控性要求。
### 方法关键点
- 从LLM自身生成序列的似然构造可微自证据向量，引入温度系数β加权高似然序列的证据权重，适配prompt动态关联的语义类，无需预设固定分类标签
- 基于自证据向量构造Dirichlet先验，联合EDL的MSE损失与SFT损失训练，梯度自动提升正确语义类的似然、抑制最过拟合的错误语义类，不会全局调整token概率分布
- 提出find-first语义聚类算法，将原本O(N²)的语义聚类验证成本降至1.3~3.3倍N次调用，大幅降低训练开销
### 关键实验
在GSM8K、MATH-500等4个开放QA数据集测试，对比SFT、RCFT、Dr.GRPO等6类基线，覆盖3个主流开源7B/8B模型：平均语义校准误差（smECE）比SFT降低最多1/3，Pass@1平均提升9.6个百分点；跨域场景下Pass@1比Dr.GRPO最高高7.3个百分点，smECE低4.7个百分点。
### 核心结论
语义校准需对齐生成分布的语义级置信度，而非仅做token级正则，才能同步提升准确率、校准效果与跨域泛化性。
