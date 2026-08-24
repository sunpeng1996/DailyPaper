---
title: When does fusing hand-crafted knowledge with learned representations pay? A
  cost-normalized benchmark of stacking, substitution, and interference
title_zh: 手工先验知识与学习表征融合的收益条件及成本归一化基准测试
authors:
- Ahmad AlMughrabi
- Albert Clop
- Benjamin Busam
- Ricardo Marques
- Petia Radeva
affiliations:
- Universitat de Barcelona
- Technical University of Munich
- Universitat Pompeu Fabra
arxiv_id: '2608.21098'
url: https://arxiv.org/abs/2608.21098
pdf_url: https://arxiv.org/pdf/2608.21098
published: '2026-08-21'
collected: '2026-08-24'
category: Training
direction: 模型训练 · 先验知识融合
tags:
- knowledge fusion
- hand-crafted prior
- representation learning
- benchmark
- data-efficient learning
one_liner: 通过大规模基准测试明确手工先验与学习表征融合的三类适用场景及收益条件
practical_value: '- 小样本冷启动场景可优先叠加异构特征/先验（如手工规则+LLM语义特征），同类型特征无需重复叠加避免冗余

  - 针对已完成大规模预训练的模型，新增手工先验时需调低辅助损失权重，避免干扰原有有效表征导致效果下降

  - 先验融合效果可通过小范围冻结特征诊断实验快速预估，无需全量训练验证，大幅降低业务试错成本'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
小样本场景下手工先验与数据驱动学习融合应用广泛，但缺乏明确的收益边界判断标准，无法预判融合会带来增益、冗余甚至负向效果。
### 方法关键点
固定仅训练阶段注入的Gabor先验（训练 overhead ~2%），控制统一实验配置，覆盖13个数据集、9种 backbone、150~1.28M训练数据量级、2.5M~86M参数量，完成3077种分类配置、9471次实验，同时验证分割、检测任务迁移效果。
### 关键结果数字
1. 异构来源先验可堆叠：Gabor先验+DeiT增强在ViT-B/16上最高提升26个准确率点；2. 同来源先验相互替代：与有效自监督预训练融合无额外增益；3. 给已预训练初始化模型强融合先验会产生负向干扰，ImageNet预训练模型上最高降17个点，调低辅助权重可消除；4. 冻结特征增益可将端到端增益预测误差控制在0.17个点内
