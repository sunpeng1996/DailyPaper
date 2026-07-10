---
title: Super Weights in LLMs and the Failure of Selective Training
title_zh: 大语言模型中的超权重现象与选择性训练失效研究
authors:
- Shreyas Subramanian
- Adewale Akinfaderin
- Akarsha Sehwag
affiliations:
- Amazon Web Services
arxiv_id: '2607.08733'
url: https://arxiv.org/abs/2607.08733
pdf_url: https://arxiv.org/pdf/2607.08733
published: '2026-07-09'
collected: '2026-07-10'
category: Training
direction: 大模型PEFT · 微调效率优化
tags:
- Super Weights
- LoRA
- PEFT
- Selective Training
- Fine-tuning
one_liner: 验证大模型超权重为固有结构属性，证明选择性训练超权重失效，全层结构化PEFT效果更优
practical_value: '- 放弃针对单个重要参数的选择性微调方案，这类方案不仅不会提升PEFT效率，反而会导致模型性能暴跌至随机水平，优先选用LoRA这类全层结构化PEFT方法

  - 做LoRA微调时无需对Super Weights做任何特殊处理（如冻结对应位置、限制更新幅值等），这类操作对最终效果无统计意义上的影响，可直接简化工程流程

  - PEFT方案选型时不要盲目追求极致参数稀疏度，稀疏本身不决定效果，更新的层间协调结构才是核心，优先选择能实现全层更新耦合的方法'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
此前研究发现LLM存在Super Weights，删除少量这类参数会让模型困惑度飙升数个量级，业界自然假设针对性训练这些核心参数能以极低参数成本实现高效微调；同时此前Super Weight仅通过单次前向传播识别，无法确认是输入相关的偶然artifact还是模型固有结构属性，该假设的有效性也未经过实证验证。
### 方法关键点
- 先验证Super Weight一致性：在1000条WikiText-2样本上测试，确认9个权重位置在所有输入下均触发激活尖峰，为模型固有结构属性
- 设计多组对照实验：单独训练top-k Super Weights、训练其3×3邻域参数、训练同数量随机down proj层参数、多变体LoRA（冻结与Super Weight坐标匹配的注意力层更新、冻结LoRA自身高幅值更新位置）
- 基于OLMo-1B、OLMo-7B两个规模的模型实验，用ARC-Easy、Winogrande做评测，验证结论跨规模一致性
### 关键结果
- 单独训练100~8192个Super Weights，ARC-Easy准确率直接跌到随机猜测的~25%水平，扩展到36k邻域参数也无改善；而训练同数量随机down proj参数，准确率达64.18%，超过基线60.65%
- vanilla LoRA仅更新0.16%参数就达到66.88%准确率，超过基线6.2个百分点；冻结LoRA中对应Super Weight的位置，效果与原生LoRA无统计差异（p>0.05），80%种子预测结果完全一致

**最值得记住的结论**：参数重要性不等于可单独训练性，高效微调依赖全层的结构化分解，而非单独targeting单个重要权重。
