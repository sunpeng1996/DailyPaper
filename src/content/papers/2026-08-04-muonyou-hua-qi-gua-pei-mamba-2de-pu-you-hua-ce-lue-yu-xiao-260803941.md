---
title: 'Muon Meets Mamba: Spectral Optimization for State Space Models'
title_zh: Muon优化器适配Mamba-2的谱优化策略与效果评估
authors:
- Arslan Battalov
- Karim Kramin
- Alexander Markotenko
- Sofia Sinitsina
affiliations:
- HSE University
arxiv_id: '2608.03941'
url: https://arxiv.org/abs/2608.03941
pdf_url: https://arxiv.org/pdf/2608.03941
published: '2026-08-04'
collected: '2026-08-05'
category: Training
direction: 大模型训练 · 优化器适配
tags:
- Muon
- Mamba-2
- State Space Model
- Optimization
- Spectral Norm
one_liner: 验证Mamba-2中仅对输出投影层应用Muon优化可显著提升训练token效率，优于全矩阵/输入投影配置
practical_value: '- 训练基于Mamba的用户长行为序列召回、长广告文案生成等模型时，可直接复用「仅输出投影层用Muon、其余层用AdamW」的配置，最多可省42%训练token达到相同效果

  - 异构拼接的权重矩阵（如Mamba的多子模块合并输入投影）不要直接应用Muon全局正交更新，会损害效果，需拆分功能子矩阵单独适配

  - 训练资源受限场景（如小参数量垂域大模型、A/B测试快速迭代）优先尝试该配置，token效率提升最显著

  - 不要盲目把Transformer上验证有效的优化器直接迁移到SSM类架构，需针对模块特性做局部适配测试'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
Muon优化器在Transformer架构上已验证可大幅降低训练FLOPs，但缺乏在Mamba等状态空间模型（SSM）上的适配研究，SSM的模块结构、权重矩阵特性与Transformer差异显著，优化器效果无法直接迁移，亟需明确Mamba中适配Muon的最优层配置。
### 方法关键点
- 实验固定为130M参数Mamba-2，仅控制Muon的作用层，设置4组对照：仅输入投影、仅输出投影、输入+输出投影、全参数AdamW，其余超参数完全对齐
- 仅2维投影矩阵可应用Muon，1维参数、深度卷积核、Norm层、Embedding/语言模型头均固定使用AdamW
- 引入有效秩、条件数、谱范数三类谱诊断指标，分析优化配置对权重矩阵谱特性的影响
### 关键结果
- 数据集覆盖OpenWebText、FineWeb-Edu，token预算从10亿到500亿（19倍Chinchilla最优规模）
- 仅输出投影层用Muon的配置效果最优：10亿token下OpenWebText数据集PPL比全AdamW低10.9%，仅需5.8亿token即可达到全AdamW10亿token的验证loss
- 该优势跨数据集、跨token预算稳定存在，即使训练到500亿token时仍优于AdamW，但loss差距随训练步数增加逐渐收窄
- 谱诊断验证：Muon仅降低其作用层的条件数，输出投影层条件数与loss强相关，输入投影层条件数优化与收益完全解耦
### 核心结论
优化器适配不能照搬跨架构经验，针对模块功能和矩阵结构做局部配置的收益远高于全局粗放应用。
