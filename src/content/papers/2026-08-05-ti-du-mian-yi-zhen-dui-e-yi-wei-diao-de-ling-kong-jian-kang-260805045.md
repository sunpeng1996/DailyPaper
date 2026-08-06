---
title: 'Gradient Immunity: Null-Space Resistance to Malicious Fine-Tuning'
title_zh: 梯度免疫：针对恶意微调的零空间抗性防护方法
authors:
- Yuxuan Huang
- Xingyu Zeng
- Tianhang Zheng
- Chaochao Lu
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Shanghai Jiao Tong University
- Shenzhen University of Advanced Technology
- Zhejiang University
arxiv_id: '2608.05045'
url: https://arxiv.org/abs/2608.05045
pdf_url: https://arxiv.org/pdf/2608.05045
published: '2026-08-05'
collected: '2026-08-06'
category: LLM
direction: 大语言模型 · 恶意微调安全防护
tags:
- LLM Safety
- Fine-tuning Defense
- Null Space
- Open-weight Model
- Adversarial Robustness
one_liner: 提出单向安全门USG，无需下游配合即可防护开源大模型免受恶意微调攻击
practical_value: '- 内部迭代开源LLM支撑电商文案生成、客服Agent等业务时，可插入USG模块，避免业务侧不当微调破坏模型对齐性，减少风险内容输出

  - 训练行业专属LLM时，可基于业务场景自研有害样本集校准USG阈值，既保留下游业务微调能力，又守住安全合规底线

  - 对外提供可微调的电商/广告行业LLM服务时，无需强制下游遵循额外安全流程，仅通过USG即可大幅提高恶意微调的攻击成本'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
已对齐的开源LLM易被下游恶意微调攻破，现有防御方案多针对FTaaS场景，或要求下游遵循额外安全流程，无法适配多数权重可训练、仅核心安全组件固定的PPOW发布场景。

### 方法关键点
1. 在Transformer最后一层后插入单向安全门USG，由零空间三次层+逆适配器组成
2. 下游微调时，三次层会阻断隐藏态落在校准保护区域的有害样本梯度，逆适配器同时还原base模型前向推理效果
3. 基于防御方持有的有害数据校准阈值，保护能力可泛化到分布内相似有害样本

### 关键结果
6组模型-数据集测试中，固定发布阈值下USG使微调后攻击成功率接近模型发布前水平，简单场景下安全通过率保持高位，BeaverTails数据集上安全-效用trade-off更清晰。
