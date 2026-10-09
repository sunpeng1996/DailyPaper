---
title: 'Overcoming Prior Barriers: Supervised Fine-Tuning under Long-Tail Distribution'
title_zh: 长尾分布下基于先验障碍感知的监督微调指令选择方法
authors:
- Haohui Wang
- Jiahao Xu
- Wangzhi Zhan
- Tong Zeng
- Dongqi Fu
- Hong Li
- Swastik Roy
- Naren Ramakrishnan
- Chris North
- Jian Kang
affiliations:
- Virginia Tech
- Amazon
- Meta
- MBZUAI
- Dartmouth College
arxiv_id: '2610.12345'
url: https://arxiv.org/abs/2610.12345
pdf_url: https://arxiv.org/pdf/2610.12345
published: '2026-10-08'
collected: '2026-10-09'
category: Training
direction: 大模型监督微调 · 长尾数据选择
tags:
- SFT
- Instruction Tuning
- Long-tail Distribution
- Data Selection
- LoRA
one_liner: 提出先验障碍概念与PASS自适应指令选择方法，用有限SFT预算提升长尾概念微调效果
practical_value: '- 垂直域LLM（电商客服/推荐文案生成/Agent推理）SFT时，可复用PASS的预算分配逻辑，给长尾概念（小众品类属性、冷门用户意图）分配更多微调数据，避免长尾效果拉胯

  - 可复用「先验barrier」量化方法，评估预训练LLM对业务目标概念的原生支持度，提前识别需要额外优化的长尾能力，减少无效微调投入

  - PASS的指令区分度评估方法可直接复用为SFT数据筛选规则，优先保留能区分目标概念和预训练错误认知的样本，用更少数据达到更好微调效果

  - 微调预算有限时不要均匀分配数据，优先给高先验障碍的长尾概念分配样本，参考论文结论，1.66%的样本量即可超过其他方法2倍预算的效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
SFT是LLM适配下游任务的核心手段，但预训练模型对不同概念的支持度存在长尾差异：头部常见概念预训练支持好、微调门槛低，尾部罕见概念预训练支持弱、存在更高的先验障碍，现有指令选择方法大多不区分概念的先验差异，导致有限微调预算下长尾概念效果差，整体任务表现受限。

### 方法关键点
- 提出「先验barrier」量化指标，衡量预训练模型对目标概念的竞争概念支持度高于目标概念的程度，明确头/尾概念的微调样本量需求差异，推导SFT预测风险上界，证明尾概念需要更多样本克服先验障碍
- 提出PASS框架：1）区分度证据估计：对参考集指令聚类得到目标概念空间，构建每个概念的正/负表示，计算每个候选指令对各概念的区分证据；2）先验障碍感知分配：基于预训练模型估计各概念的先验障碍和原生支持度，自适应分配样本预算，同时加入负样本惩罚和冗余惩罚，贪心选择边际收益最高的样本

### 关键实验
基于30万条公开指令池，覆盖知识、推理、数学、事实性、多语言QA5类下游能力，对比7种SOTA指令选择方法，在Mistral-7B、Qwen2.5-7B两个骨干，5k、10k两个预算下，PASS在所有设置均最优：Mistral-7B上5k样本得分51.5，超过其他方法10k样本的最高得分50.9；比均匀预算分配平均提升0.26~0.56分。

### 最值得记住的一句话
有限SFT预算下的核心优化点不是筛选单个高质量样本，而是根据预训练模型的先验障碍自适应分配预算，覆盖长尾薄弱概念。
