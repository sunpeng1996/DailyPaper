---
title: 'GOD: Enhancing Generalization via Deep Grafting for Sequential Recommendation'
title_zh: GOD：基于深度嫁接的序列推荐泛化性增强方法
authors:
- WooJoo Kim
- JunYoung Kim
- JaeHyung Lim
- HwanJo Yu
affiliations:
- Pohang University of Science and Technology
arxiv_id: '2608.16073'
url: https://arxiv.org/abs/2608.16073
pdf_url: https://arxiv.org/pdf/2608.16073
published: '2026-08-17'
collected: '2026-08-18'
category: RecSys
direction: 序列推荐 · 知识蒸馏泛化优化
tags:
- Sequential Recommendation
- Knowledge Distillation
- Contrastive Learning
- Model Generalization
- Component Distillation
one_liner: 提出组件级嫁接蒸馏框架，在不增加推理成本的前提下提升序列推荐模型泛化能力
practical_value: '- 业务序列推荐模型蒸馏可直接复用组件嫁接思路：分别替换教师的embedding层、序列编码器为学生对应模块，得到两种混合监督源，避免embedding和编码器误差纠缠，尤其适配冷启动、短交互序列等稀疏场景

  - Transformer类推荐模型蒸馏可复用嫁接编码（GE）设计：训练阶段拼接师生侧embedding做双向互注意力，稳定混合模型表征生成，实测收敛速度比传统双向蒸馏快30%以上，无推理
  overhead

  - 多视图对比蒸馏场景可复用自适应加权策略：基于batch内视图相似度动态调整配对权重，降低高相关视图的冗余监督，比固定权重、可学习权重方案效果更稳定，调参成本更低'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有序列推荐知识蒸馏方法采用师生独立推理后对齐输出/表征的范式，会导致学生的embedding层误差与编码器误差纠缠，难以定位泛化性差的根因，在电商/内容推荐等用户交互稀疏、噪声大的场景下效果受限。
### 方法关键点
- 构建三类混合源模型：原生冻结教师、embedding嫁接教师（替换教师embedding为学生embedding）、编码器嫁接教师（替换教师编码器为学生编码器），输出不同组件组合下的表征，提供组件级反馈
- 针对Transformer类模型设计嫁接编码（GE）：训练阶段拼接师生侧embedding后做双向互注意力，稳定混合模型表征生成，推理阶段不生效，无额外开销
- 采用嫁接感知对比学习（GCL）：动态计算4种视图间6种配对的权重，自适应降低高相似配对的权重，减少冗余监督
- 推理仅保留纯学生模型，无额外计算成本
### 关键结果
在Amazon Beauty、Yelp、MovieLens 1M三个公开数据集上，适配GRU4Rec、FMLPRec、SASRec三类主流序列推荐backbone，相对最优基线最高提升13.92%，在短序列、高噪声场景下增益更显著；自蒸馏场景下相对最优基线最高提升8.12%，训练收敛速度比同类KD方法快30%以上。
### 核心结论
知识蒸馏的收益不仅来自知识信号的内容，更来自知识传递的粒度，组件级耦合的监督比独立路径的输出对齐能带来更强的泛化性
