---
title: 'Learning to Stop without Learning to Stop: Self-Supervised Confidence Training
  Improves Reasoning Efficiency'
title_zh: 无需显式训练停止：自监督置信度训练提升推理效率
authors:
- Parsa Hosseini
- Akasha Tigalappanavara
- Sumit Nawathe
- Chenrui Fan
- Sourya Basu
- Genta Indra Winata
- Anirban Das
- Soheil Feizi
- Nima Chitsazan
affiliations:
- University of Maryland
- Capital One
arxiv_id: '2609.31619'
url: https://arxiv.org/abs/2609.31619
pdf_url: https://arxiv.org/pdf/2609.31619
published: '2026-09-25'
collected: '2026-09-28'
category: Reasoning
direction: 大模型推理效率 · 自监督置信度训练
tags:
- Reasoning Efficiency
- Self-supervised Training
- Confidence Prediction
- LLM Fine-tuning
- Inference Optimization
one_liner: 仅用600题自监督置信度微调，无显式效率目标下推理token最高减25%且精度持平
practical_value: '- 电商导购Agent、智能客服场景可复用ConfSFT范式，通过自监督置信度微调压缩思考链长度，降低推理成本的同时不降低回答准确率

  - 生成式推荐场景中，可在LLM生成推荐理由、多轮推荐决策的中间阶段加入置信度预测目标，减少冗余生成，提升KV cache利用率和响应速度

  - 无需引入显式长度惩罚、推理时早停逻辑，仅通过自监督元认知信号训练即可隐式提升推理效率，避免早停带来的精度损失风险'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前推理型LLM常生成超长思考链，推理算力成本极高；现有效率优化方案要么在推理时加入早停逻辑易造成精度下降，要么在训练时加长度惩罚易破坏原有推理逻辑，亟需无显式效率目标的非侵入式优化方案。
### 方法关键点
- 提出ConfSFT自监督微调范式，仅以推理轨迹中间状态的置信度为唯一训练目标，损失函数无任何推理长度、效率、停止相关的约束项
- 置信度标签无需人工标注，通过中间状态生成试答的token概率几何均值计算得到，仅需少量训练问题即可完成迭代
- 推理阶段完全沿用原生生成逻辑，无需额外置信度提取、早停判断等机制，无推理额外开销
### 关键实验
在Gemma、Qwen、Nemotron、GPT-OSS 4个模型家族的数学、科学、编码三类基准测试上，仅用600道AIME数学题训练，ConfSFT可减少10%~25%生成token，精度与基线模型持平，效率增益与显式优化短推理的方法相当，且训练的效率增益可跨任务迁移到未见过的科学、编码任务。
### 核心结论
高效推理可以作为元认知信号学习的下游效应自然涌现，无需对效率目标做显式优化
