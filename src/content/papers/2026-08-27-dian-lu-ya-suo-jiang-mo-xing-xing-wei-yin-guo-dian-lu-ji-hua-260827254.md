---
title: 'Circuit Condensation: Post-Training that Concentrates a Behavior''s Causal
  Circuit'
title_zh: 电路压缩：将模型行为因果电路集中化的后训练方法
authors:
- Sai Adith Senthil Kumar
affiliations:
- George Mason University
arxiv_id: '2608.27254'
url: https://arxiv.org/abs/2608.27254
pdf_url: https://arxiv.org/pdf/2608.27254
published: '2026-08-27'
collected: '2026-08-28'
category: LLM
direction: 大模型可解释性·因果电路压缩
tags:
- Mechanistic Interpretability
- LoRA
- Causal Circuit
- Post-Training
- Pruning
one_liner: 提出剪枝加低秩适配后训练方案，将大模型特定行为的因果电路平均缩小8.1倍且保留原有性能
practical_value: '- 可复用「剪枝+LoRA微调」的迭代压缩范式，对LLM4Rec、Agent的核心功能子模块做轻量化，降低推理成本

  - 业务上线大模型功能时，可通过该方法提取对应功能的最小因果电路，排查bad case根因，提升可解释性

  - 针对特定任务（如推荐文案生成、Query改写）训练的大模型，可通过该方案压缩冗余参数，适配端侧或低算力部署场景'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有大模型因果电路挖掘得到的关联边数量过多，无法高效核验、对比，可解释性落地难度大。

### 方法关键点
迭代执行三步操作：1）剪枝低归因权重边；2）训练LoRA适配保留的子图，对齐原模型输出分布；3）仅保留同时满足任务性能、通用能力不下降的剪枝结果。

### 关键结果
在4类行为、8个模型的32组实验中，30组压缩后电路规模小于最强基线，平均缩小8.1倍，最高可达316倍；无权重更新的纯搜索方案仅能在3组实验中得到更小电路；在间接对象识别任务上，压缩后仅保留24个注意力头，其中17个有明确功能定义，远少于基线的61个头。
