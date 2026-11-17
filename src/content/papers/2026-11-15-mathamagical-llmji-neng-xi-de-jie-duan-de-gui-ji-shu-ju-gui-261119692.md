---
title: 'MathaMAGICal: Validating Trajectory Data Attribution During Capability Acquisition'
title_zh: MathaMAGICal：LLM技能习得阶段的轨迹数据归因有效性验证
authors:
- Jason Lee
- Dikshanta Pokhrel
- Phonn Nay Khant
- Victor Lee
- Moritz Weckbecker
- Sebastian Lapuschkin
- Wojciech Samek
- Mark Riedl
- Glenn Matlin
affiliations:
- Algoverse AI Research
- University of California, Los Angeles
- Fraunhofer Heinrich Hertz Institute
- Technische Universität Berlin
- Georgia Institute of Technology
arxiv_id: '2611.19692'
url: https://arxiv.org/abs/2611.19692
pdf_url: https://arxiv.org/pdf/2611.19692
published: '2026-11-15'
collected: '2026-11-17'
category: Training
direction: LLM训练 · 轨迹数据归因有效性验证
tags:
- Data Attribution
- MAGIC
- Training Trajectory
- LLM Capability Acquisition
- Influence Function
one_liner: 验证短窗口MAGIC轨迹归因在LLM技能习得阶段的有效性，明确归因适用边界与可迁移粒度
practical_value: '- 做领域LLM微调/训练数据归因时，避免使用全训练轨迹归因，改用100步以内的短窗口归因，可大幅提升归因结果与实际数据移除效果的相关性，同时避免数值溢出

  - 做训练数据价值评估时，不要依赖单条样本/样本块的归因排名（跨种子/超参数不可迁移），应聚焦数据家族/类别级的归因模式，结论可复现性更强

  - 训练LLM习得特定业务技能（如电商话术生成、推荐理由推理）时，与测试格式对齐的样例类数据、基础事实类数据对技能形成的影响最大，可优先优化这两类数据的质量'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
基于影响函数的轨迹数据归因方法（如MAGIC）可量化训练样本对模型效果的影响，但全训练轨迹归因存在数值溢出问题，且得分与实际数据移除效果的相关性未经过系统验证，尤其缺乏技能习得阶段的适用性边界研究。
### 方法关键点
- 从零训练86M、152M参数量的GPT-2风格模型，训练语料为50%网页文本+50%四类合成算术数据（解题样例、基础事实、自然语言步骤、代码轨迹），测试集为训练未覆盖的运算组合
- 对比全轨迹归因、短窗口（100步以内）归因的效果，以线性数据建模得分（LDS）为核心指标，衡量归因得分与重训损失变化的相关性
- 测试块级归因排名的跨种子/超参数迁移性，对比数据家族级归因模式的可复现性
### 关键结果
- 86M模型全轨迹归因出现数值溢出，元梯度裁剪后LDS仅为0.17~0.22，接近随机水平；100步短窗口归因在152M模型的四个技能习得阶段LDS达0.86~0.99，远优于单checkpoint梯度点积基线（近0相关）
- 单样本块的归因排名跨种子/超参数的Spearman相关≤0.09，不可迁移；家族级模式可跨运行复现，解题样例、基础事实在正负5%得分尾部的占比为语料占比的2.1~2.6倍
### 核心结论
轨迹数据归因仅在经过验证的短窗口内可靠，可迁移的有效分析粒度为数据家族而非单条样本块。
