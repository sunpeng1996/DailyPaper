---
title: 'Follow the Gradient: Tracing Safety Degradation Back to Training Data'
title_zh: 基于梯度归因的LLM微调安全退化训练数据溯源方法
authors:
- Saket Reddy
- Amro Abbas
- Anshuman Suri
- Ari Morcos
- David Schwab
- Pratyush Maini
affiliations:
- DatologyAI
- University of Illinois Urbana-Champaign
arxiv_id: '2610.37481'
url: https://arxiv.org/abs/2610.37481
pdf_url: https://arxiv.org/pdf/2610.37481
published: '2026-10-27'
collected: '2026-10-28'
category: Training
direction: LLM微调安全 · 梯度数据归因
tags:
- Gradient Attribution
- LLM Safety
- SFT Data Filtering
- LoRA
- Alignment
one_liner: 提出可扩展SimpleLoRIF梯度嵌入方法，过滤LLM微调数据中的隐性安全风险样本
practical_value: '- 做电商导购Agent、LLM4Rec SFT时，可复用SimpleLoRIF的优化trick：仅反向传播最后4个Transformer块，将梯度压缩为低秩向量，百万级样本的归因计算仅需8卡H100
  1小时，可快速清洗SFT数据中的隐性安全退化样本

  - 不要仅依赖LLM-as-a-judge做内容过滤，梯度归因可识别表面无害但会削弱对齐能力的样本（如工具执行失败样例、简单编码/算术题），可降低业务Agent被jailbreak的风险

  - 安全过滤可参考20%的移除比例，在最高降低22%GCG攻击成功率的同时，几乎不损失模型的通用任务能力，可直接平衡业务安全与效果需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM微调时即使使用表面无害的公开指令数据集，也会悄悄削弱模型的安全对齐能力，常规内容过滤器、LLM-as-a-judge无法识别这类隐性安全退化样本，此前的梯度归因方法计算成本过高，无法支撑百万级微调数据集的规模化过滤。

### 方法关键点
- 提出SimpleLoRIF梯度嵌入方法，在LoRIF基础上去掉曲率校正，仅对最后4个Transformer块做反向传播，保留归因效果的同时计算速度提升91.53%
- 梯度相似性计算采用低秩因子的双线性形式，无需重建完整梯度即可快速计算样本梯度和不安全行为梯度的对齐度
- 构建SafeTulu数据集时，将Tulu 3中与不安全响应梯度对齐度最高的20%样本移除，无需训练额外排序器或辅助模型

### 关键实验
-  emergent misalignment场景下，梯度归因能将不安全代码样本和安全代码样本区分开，AUC最高达0.865
- 基于SafeTulu微调的Qwen、Llama、Olmo模型，GCG攻击成功率最高降低22%，ActorBreaker攻击成功率也显著低于LLM-as-a-judge、传统梯度过滤等基线，同时在通用、编码、数学、医疗等Benchmark上的能力基本持平甚至有所提升

### 核心结论
表面无害的微调样本（如工具执行失败、简单算术题、直接编码任务）也可能导致安全对齐退化，梯度归因是识别这类样本的高效可行方案。
