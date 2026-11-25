---
title: Understanding Clipping In Zeroth-Order Optimization
title_zh: 零阶优化中梯度裁剪的作用机制与效果研究
authors:
- Saket Gollapudi
- Elisa Bertino
- Sewoong Oh
affiliations:
- University of Washington, Seattle
- Purdue University
arxiv_id: '2611.33062'
url: https://arxiv.org/abs/2611.33062
pdf_url: https://arxiv.org/pdf/2611.33062
published: '2026-11-24'
collected: '2026-11-25'
category: Training
direction: 大模型高效微调 · 零阶优化
tags:
- Zeroth-Order Optimization
- Gradient Clipping
- LLM Fine-tuning
- Training Efficiency
- Robust Optimization
one_liner: 揭示零阶优化逐样本裁剪的调参规则与精度提升机制，验证ηc为常数的最优调参关系
practical_value: '- 用零阶优化做低显存LLM微调（如电商文案生成、推荐prompt微调）时，直接按ηc=常数的规则调参，无需单独扫η和c，可节省70%以上调参成本

  - 业务训练数据存在标注噪声（如用户行为噪声、商品标注错误）时，优先选择逐样本裁剪的零阶优化器，可自动降权错标/歧义样本，无需额外做数据清洗

  - 若业务需要高校准度的模型输出（如搜索query意图识别、广告合规审核），避免使用带裁剪的零阶优化模型，这类模型ECE更高，容易出现过度自信的误判

  - 做模型集成时，可搭配裁剪零阶训练的模型与无裁剪/一阶训练的模型，利用两者解空间的差异提升ensemble效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
零阶优化（ZO）仅需前向传播即可完成LLM微调，显存占用比一阶优化低30%以上，是资源受限场景下大模型微调的核心方案，但此前偶然发现逐样本裁剪能提升ZO优化效果却缺乏系统解释，调参也无明确规则，严重阻碍落地。

### 方法关键点
- 对比逐样本裁剪ZO-SGD、批量裁剪ZO-SGD、Winsorized均值ZO-SGD、一阶SGD四类优化器的收敛行为
- 理论推导了裁剪主导区下梯度期望的加权形式，证明裁剪会对大梯度样本自动降权
- 设计标注噪声注入、数据剪枝对照实验，定位精度提升的核心根源

### 关键结果数字
在SNLI、MNLI、SST-2、Trec四个NLP任务上测试RoBERTa、OPT两类基座：相比无裁剪ZO-SGD，逐样本裁剪版本SNLI任务测试精度从80.7%提升到83.2%（+2.5个百分点）；30%标注噪声场景下精度比无裁剪高5.6个百分点；最优调参严格遵循ηc=5e-4的线性关系，批量裁剪、Winsorized均值等其他鲁棒估计方法无此增益。

最值得记住的结论：零阶优化下逐样本裁剪不是简单的梯度缩放，而是通过隐式降权重错标/歧义样本找到更高精度的独立解空间，调参只需固定ηc乘积即可。
