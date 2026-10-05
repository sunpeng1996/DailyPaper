---
title: Predicting Steering Vectors and Adapter Weights for Few-Shot Author-Style Transfer
title_zh: 面向少样本作者风格迁移的转向向量与适配器权重预测方法
authors:
- Leonard Popp
- Danni Liu
- Supriti Sinhamahapatra
- Jan Niehues
affiliations:
- Karlsruhe Institute of Technology, Germany
arxiv_id: '2610.03163'
url: https://arxiv.org/abs/2610.03163
pdf_url: https://arxiv.org/pdf/2610.03163
published: '2026-10-02'
collected: '2026-10-05'
category: LLM
direction: LLM少样本个性化 · 风格控制
tags:
- LoRA
- Activation Steering
- Hypernetwork
- Few-shot Learning
- Style Transfer
one_liner: 提出三种少样本作者风格迁移方案，实现风格模仿与生成质量的最优平衡
practical_value: '- 电商个性化文案生成冷启动场景可复用超网络预测LoRA的架构，无需为每个用户/商家单独微调，仅需3份样本即可生成专属风格内容，大幅降低部署成本

  - 做Activation Steering时，采用同内容的模型中性生成作为负样本，替代预定义风格库的方案，可有效避免风格与内容纠缠，提升用户/商家风格匹配的准确率

  - LLM干预优先选择中间层注入转向向量或LoRA，避免全层注入导致的生成质量下降，可大幅减少工程调优的试错成本

  - 个性化/风格控制效果验证不要依赖向量相似度指标，多个正交的干预方向可实现相当的业务效果，必须用下游业务指标（点击率、转化率）做最终判断'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
少样本场景下将LLM适配到特定用户/作者的风格难度高，尤其在格式约束强的领域（如科学写作、电商官方文案），表层风格特征少，提取的风格信号极易与内容纠缠；现有方案要么需要预定义风格库，要么需要大量用户历史数据，无法适配仅存少量样本的冷启动个性化需求。

### 方法关键点
- 对比激活转向：将作者真实样本的激活向量与同内容的模型默认风格生成的激活向量做差，得到风格转向向量，无需预定义风格库，固定内容维度消除内容干扰
- 转向向量预测网络：基于少量示例的作者嵌入，通过MLP直接预测各层转向向量，无需额外生成中性样本或进行超参数搜索
- LoRA超网络：基于作者嵌入预测LoRA适配器权重，适配不同层和注意力模块，干预随输入动态调整，灵活性远高于固定偏移的转向向量

### 关键实验
数据集为arXiv 2022年以前cs.AI/cs.LG领域的1232篇论文，覆盖203位作者，每作者仅用3篇摘要作为风格示例；对比零样本提示、少样本提示、全局LoRA三个基线。核心结果：全局LoRA风格准确率最高（49.8%）但生成质量偏好率仅38.1%；超网络方案在见过的作者上风格准确率36.5%、偏好率91.3%，在完全未见过的作者上风格准确率31.4%、偏好率95.5%，是唯一在两个测试集上均处于帕累托最优的方案。

### 核心结论
风格控制的核心不是寻找唯一最优的干预方向，而是在风格匹配度和生成质量的trade-off中选择符合业务需求的平衡点，且多个正交的干预方向可实现相当的控制效果
