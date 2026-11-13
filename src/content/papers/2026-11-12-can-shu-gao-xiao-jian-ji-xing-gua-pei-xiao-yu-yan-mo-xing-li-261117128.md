---
title: 'Parameter-Efficient Conciseness Adaptation: Differentiable Length Control
  for Concise Clinical Reasoning in Smaller Language Models'
title_zh: 参数高效简洁性适配：小语言模型临床推理的可微长度控制
authors:
- Tanzeel Abbas
- Ahmad Kamran Malik
- Nafees Qamar
- Sana Liaqat
affiliations:
- COMSATS University Islamabad
- Bryant University
arxiv_id: '2611.17128'
url: https://arxiv.org/abs/2611.17128
pdf_url: https://arxiv.org/pdf/2611.17128
published: '2026-11-12'
collected: '2026-11-13'
category: LLM
direction: 小语言模型 · 参数高效微调 · 生成长度控制
tags:
- SLM
- QLoRA
- Length Control
- Parameter-Efficient Fine-Tuning
- Clinical NLP
one_liner: 提出PECA适配方法，在QLoRA微调中加入可微简洁项，无需额外偏好数据/辅助模型即可控生成长度并提升精度
practical_value: '- 做生成式推荐/Agent回复/商品短文案生成的长度控制时，可复用PECA思路，在SFT阶段直接加EOS概率提升的可微损失项，无需额外训练Reward
  Model，大幅降低工程与标注成本

  - 用QLoRA微调小模型落地业务（如客服Agent、搜索Query改写、商品卖点生成）时，可引入简洁度超参，通过超参扫描得到精度-长度平衡的帕累托边界，匹配不同场景的响应长度要求

  - 对推理耗时、输出长度有严格要求的小模型部署场景，可直接复用PECA的训练pipeline，单消费级GPU即可完成微调，无需偏好标注数据，降低落地门槛'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
小语言模型（SLM）部署成本低，适配垂直领域门槛低，但微调后常存在输出冗余问题，现有长度控制方法依赖偏好优化、Reward Model或专有大模型，反而抬高了SLM落地成本，医疗等对响应效率要求高的场景冗余输出可用性极低。

### 方法关键点
PECA适配方案在QLoRA监督微调目标中加入单可微简洁性项；针对token数离散不可微的问题，在生成超过预设token预算时提升EOS token概率，构造可导训练信号，无需偏好数据、辅助模型，单消费级GPU即可训练；支持通过简洁度强度超参灵活调节输出长度。

### 关键结果
在1.7B参数模型上基于medical-o1-reasoning-SFT语料微调，PECA将平均响应长度降低72.8%，同时多项选择诊断准确率从40.8%提升至44.0%，可通过超参扫描得到可解释的精度-长度权衡曲线。
