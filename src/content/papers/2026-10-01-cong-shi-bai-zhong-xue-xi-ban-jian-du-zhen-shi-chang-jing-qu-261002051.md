---
title: 'Learning from Failure: Leveraging Unreliable Predictions in Semi-Supervised
  Real-World Adverse Weather Removal'
title_zh: 从失败中学习：半监督真实场景去恶劣天气的不可靠预测利用
authors:
- Cap Dang Xuan Kiet
- Tat-Jen Cham
affiliations:
- Nanyang Technological University, Singapore
arxiv_id: '2610.02051'
url: https://arxiv.org/abs/2610.02051
pdf_url: https://arxiv.org/pdf/2610.02051
published: '2026-10-01'
collected: '2026-10-03'
category: Other
direction: 恶劣天气图像修复 · 半监督学习框架
tags:
- Semi-Supervised Learning
- Image Restoration
- Contrastive Learning
- Student-Teacher Framework
- Semantic Constraint
one_liner: 提出师生半监督双样本库框架+相位语义约束，提升真实场景恶劣天气图像修复性能
practical_value: '- 半监督冷启动/少标注场景可复用「错误预测存为负样本+优质预测存为正样本」的对比学习范式，降低标注成本

  - 排序/多任务学习优化可借鉴自适应损失设计，根据样本难度/噪声程度动态调整不同监督信号的权重

  - 多模态内容理解/生成场景可采用轻量频谱类语义约束替代高成本文本监督，降低训练与推理开销'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
现有统一恶劣天气图像修复模型高度依赖合成标注、语义约束不足，在真实场景下泛化性能较差，无法适配复杂多变的真实雨雪雾霾等退化情况。
### 方法关键点
1. 构建师生半监督框架，设计双样本库：可靠库存教师模型高质量预测作为正样本，不可靠库存失败预测作为负样本，联合用于对比学习，同时学习优质修复特征与规避常见错误；
2. 提出相位频谱语义约束，替代计算成本高昂的文本监督，轻量且天然具备语义对齐性；
3. 设计自适应相位一致性损失，根据输入图像的退化程度动态平衡原始输入与教师伪标签的监督权重。
### 关键结果
在真实场景基准测试中，修复质量、感知保真度全面优于现有SOTA方案，真实恶劣天气场景泛化能力显著更强。
