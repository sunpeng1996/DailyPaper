---
title: Elucidating the Design Space of LM Data Attribution
title_zh: 大语言模型数据归因的设计空间梳理与优化方法
authors:
- Steven Yu
- Sheng-Yu Wang
- Kimia Hamidieh
- Antonio Torralba
- David Bau
affiliations:
- Northeastern University
- MIT
arxiv_id: '2610.40655'
url: https://arxiv.org/abs/2610.40655
pdf_url: https://arxiv.org/pdf/2610.40655
published: '2026-10-29'
collected: '2026-10-30'
category: LLM
direction: 大语言模型 · 数据归因评估与优化
tags:
- DataAttribution
- FactTracing
- LLMEvaluation
- GradientBasedMethod
- Benchmark
one_liner: 提出可控归因基准CATT，通过损失与token聚合优化将数据归因性能最高提升4.9倍
practical_value: '- 生成式推荐/商品文案生成的训练数据溯源场景，可将交叉熵梯度替换为负对数-odds梯度，能大幅提升冗余数据、干扰样本下的关键训练样本召回率

  - 做梯度类归因时，无需对全文档token得分平均，仅取top-10左右得分最高的token聚合即可，避免无关内容稀释有效信号，降低计算开销

  - 内部归因工具的效果验收可参考CATT的构造思路，用无预训练先验的虚构事实做可控测试，排除静态基准的混淆变量干扰'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有大语言模型数据归因方法的评估方案通常同时变动多个数据集属性，无法精准定位算法失效根因；且主流梯度类归因方法普遍存在信号稀释问题：交叉熵损失会抑制高置信度关键token的梯度，全文档平均得分的聚合方式进一步掩盖了有效归因信号，导致归因性能随数据冗余、干扰项增加快速下降。
### 方法关键点
- 提出可控归因基准CATT：基于完全虚构的事实微调LM，构造无歧义的归因真值，可单独控制文档冗余度、词汇干扰项、事实数量等变量，精准诊断算法失效原因
- 损失函数优化：将梯度计算所用的交叉熵损失替换为负对数-odds（NLO），解决高置信度关键token的梯度被抑制的问题，有效凸显关键信号
- 归因得分聚合优化：仅保留文档内top-k个token的归因得分做聚合，避免无关token稀释有效信号
### 关键结果
在CATT基准上测试11种主流归因方法，优化后事实追踪Recall相对基线提升35~72个百分点；在外部公开基准FTRACE-TREX上，优化后的TRAK、EK-FAC、Grad-Dot的反事实重训练性能最高提升4.9倍；实验同时验证BM25在有明确词汇匹配线索的场景下性能优于多数梯度类归因方法。
### 核心结论
数据归因的有效信号高度集中在少数关键token上，损失函数选择和token聚合方式对最终效果的影响远大于复杂的Hessian近似算法。
