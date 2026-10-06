---
title: 'Latent-MOPD: Latent Multi-Teacher On-Policy Distillation'
title_zh: Latent-MOPD：基于隐层表示的多教师同策略蒸馏方法
authors:
- Zhengyu Fang
- Seoyeon Hong
- Jie Yang
- Muyang Li
- Koyoshi Shindo
- Brandon Joseph Lwowski
- Jing Li
affiliations:
- Case Western Reserve University
- Zillow Group, Inc.
- University of Illinois at Chicago
- University of Florida
arxiv_id: '2610.02381'
url: https://arxiv.org/abs/2610.02381
pdf_url: https://arxiv.org/pdf/2610.02381
published: '2026-09-30'
collected: '2026-10-06'
category: Training
direction: 多教师同策略蒸馏 · 隐层表示对齐
tags:
- Knowledge Distillation
- On-Policy Distillation
- Multi-Teacher Distillation
- LLM Training
- Latent Alignment
one_liner: 首个基于隐层表示的LLM多教师同策略蒸馏方法，无需额外训练教师即可集成多领域能力
practical_value: '- 电商/推荐场景做垂直领域大模型蒸馏时，可复用隐层+token双监督架构，相比纯token蒸馏提升5%-15%领域能力，推理无额外开销

  - 多教师蒸馏训练时采用domain-pure批次（单批次仅同领域样本），可避免隐层监督的训练崩溃，无需额外调参

  - 隐层监督可采用per-teacher crossfade调度，前期侧重隐层对齐、后期侧重token拟合，同参数规模下可超过单领域最优教师

  - 跨模型家族蒸馏时用共享线性投影层对齐不同宽度隐层，无需修改学生结构，推理可直接丢弃投影层'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多教师同策略蒸馏（MOPD）仅在输出token层传递教师知识，未利用LLM隐层存储的中间推理信息，单通道监督知识迁移效率低，同参数规模学生很难超过单领域最优教师，跨模型家族蒸馏效果衰减严重。
### 方法关键点
- 双监督通道：同一份学生生成的rollout样本，由路由匹配的领域教师同时提供token预测监督和选中层的隐层表示监督
- 隐层对齐策略：同模型家族教师对齐最后3层隐层，跨家族教师仅对齐最后1层；隐层宽度不一致时用共享线性投影层转换，推理可直接丢弃
- 训练稳定性优化：采用domain-pure批次更新（单批次仅含同领域样本），避免多教师隐层目标冲突导致的训练崩溃
- 动态权重调度：每个教师的监督权重做per-teacher crossfade，训练前期隐层监督权重更高，后期逐步切换为纯token监督
### 关键结果
- 同家族1.5B参数设置下，在数学、代码、逻辑9个benchmark上全面超过token-only、隐层-only、均匀平均baseline，其中5个benchmark超过同参数的单领域最优教师，归一化综合得分1.05，比token-only MOPD的0.90提升16.7%
- 跨家族7B教师蒸馏到1.5B学生设置下，6个benchmark全部超过单通道baseline，归一化得分0.26，比token-only的0.16提升62.5%
- 从参数合并的初始化开始蒸馏，62步即可在5个benchmark上超过初始合并模型，综合得分从0.87提升到1.03

最值得记住的结论：多教师同策略蒸馏结合隐层+token双监督、domain-pure批次、动态权重调度，可让同参数规模的学生集成多个领域专家能力，甚至超过单个最优教师。
