---
title: 'Learned, Then Lost: A Measured Single-Example Counterfactual in Pre-training'
title_zh: 学过即遗忘：预训练中单样本反事实影响的量化测量
authors:
- Zachary Speck
- Asa Shepard
affiliations:
- Arizona State University
- Williams College
arxiv_id: '2608.19168'
url: https://arxiv.org/abs/2608.19168
pdf_url: https://arxiv.org/pdf/2608.19168
published: '2026-08-19'
collected: '2026-08-20'
category: LLM
direction: 大语言模型预训练 · 单样本影响量化
tags:
- LLM Pre-training
- Counterfactual Analysis
- Sample Impact
- Model Convergence
- GPT-2
one_liner: 通过32组GPT-2预训练对照实验量化验证预训练中单样本的影响会随训练完全衰减
practical_value: '- 预训练数据清洗无需过度追求100%无异常样本，少量漏网噪声/错误样本不会影响最终收敛的模型效果

  - 预训练中途单次注入的特定知识仅能短期留存，要长期植入知识需重复训练或采用SFT/RAG等后处理方案

  - 小范围预训练对照实验可复用本文的控制变量设计：固定多组种子+仅修改单batch单样本，大幅降低实验成本'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
过往单样本对预训练最终模型的影响只能估算，无法直接测量，全量对照预训练的成本极高。
### 方法关键点
训练32个124M参数的GPT-2模型，分4组对照，在训练第200步（峰值学习率）的256样本batch中替换1个样本，分别注入语料存在的通顺文本、虚构主体通顺文本、随机字符，剩余组为空白对照，全程跟踪模型指标变化。
### 关键结果数字
注入后50步，注入文本组的对应交叉熵比对照组低0.039~0.044 nats，p<1e-4统计显著；训练结束后差异完全消失，无统计显著性。单样本注入带来的权重偏移92%在训练中期就已稳定，仅让模型在同一收敛盆地内移动，不会跳出收敛域。
