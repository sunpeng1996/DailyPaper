---
title: 'Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated
  Data'
title_zh: 数据稀缺与模型稀疏：混合专家模型对重复数据过拟合更严重
authors:
- Atindra Jha
- Margaret Li
- Jure Leskovec
- Percy Liang
- Luke Zettlemoyer
affiliations:
- Stanford University
- Paul G. Allen School of Computer Science, University of Washington
arxiv_id: '2609.11917'
url: https://arxiv.org/abs/2609.11917
pdf_url: https://arxiv.org/pdf/2609.11917
published: '2026-09-10'
collected: '2026-09-11'
category: Training
direction: 大模型训练 · MoE过拟合优化
tags:
- MoE
- Data Repetition
- Overfitting
- Regularization
- LLM Training
one_liner: 系统性验证MoE相比稠密模型对训练数据重复更敏感，揭示成因并给出有效正则缓解方案
practical_value: '- 业务中使用MoE做LLM4Rec/生成式推荐时，训练数据重复率需控制在4x以内，超过32x优先选用同计算量稠密模型

  - 缓解MoE数据重复过拟合直接选用dropout、FFN输出掩码、专家dropout等掩码类正则，权重衰减、梯度裁剪、路由抖动几乎无优化效果

  - 若某业务域训练数据不足必须重复，可混入同语义域的不重复数据，能有效降低重复数据带来的过拟合损失

  - 训练数据重复率低于16x时，MoE仍能保持对稠密模型的性能优势，可放心选型'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前大模型训练面临高质量独特数据耗尽的瓶颈，重复训练数据已成为行业常规操作；而MoE作为高计算效率的主流稀疏架构，其在重复数据下的过拟合表现此前缺乏系统性研究，直接影响数据受限场景下的模型选型与训练效果。

### 方法关键点
- 控制计算量匹配，对比80M~1B激活参数的稠密Transformer与不同专家数量、粒度的MoE模型
- 固定总训练token数，调整独特token数量实现1~1024倍的数据重复率变量
- 覆盖单域（网页、代码、学术、百科）、混合域、不同质量过滤数据等多种训练场景
- 测试dropout、权重衰减、梯度裁剪、路由抖动等7种正则方法的缓解效果

### 关键结果数字
- MoE在数据重复率4x时就出现明显性能下降，而稠密模型到8x才会出现明显退化
- 重复率超过32x时，MoE性能反超稠密模型的优势完全消失，表现更差
- 采用p=0.4的dropout或同类掩码正则，MoE在重复率64x时仍能优于同计算量的稠密模型
- MoE路由决策在训练前10%步就稳定（路由稳定性超95%），专家过度特化是过拟合核心成因

### 核心结论
MoE的性能优势仅在独特数据充足时成立，数据稀缺高重复场景下需配合掩码类正则才能保留优势
