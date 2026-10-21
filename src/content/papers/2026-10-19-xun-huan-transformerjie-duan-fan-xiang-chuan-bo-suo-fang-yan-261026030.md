---
title: Truncate or Not? A Scaling Study of Looped Transformers with Truncated Backpropagation
title_zh: 循环Transformer截断反向传播缩放研究：要不要做截断？
authors:
- Xuyuan Xiong
- Siyu Chen
- Zihan Shao
- Yue Su
- Weiyang Jin
- Ping Luo
- Zhuoran Yang
- Xihui Liu
affiliations:
- MMLab, The University of Hong Kong
- Yale University
arxiv_id: '2610.26030'
url: https://arxiv.org/abs/2610.26030
pdf_url: https://arxiv.org/pdf/2610.26030
published: '2026-10-19'
collected: '2026-10-21'
category: Training
direction: 大模型训练 · 循环Transformer缩放律
tags:
- Looped-Transformer
- BPTT
- Scaling-Law
- Truncated-BPTT
- Training-Optimization
one_liner: 通过近600次训练拟合统一缩放律，明确循环Transformer最优反向传播策略与参数高效配置
practical_value: '- 训练用于电商/推荐场景的轻量化LLM（如query理解、个性化文案生成、Agent推理模块）时，可采用2次循环+全BPTT的配置，比同性能非循环Transformer少27%非嵌入参数，推理显存占用更低，适合边缘/端侧部署

  - 训练自定义领域（电商/广告）的循环Transformer时，若可自由调整前向循环数，优先选择全BPTT，同算力下减少前向循环数做全反向传播的效果，优于增加前向循环数再做截断的配置

  - 若业务约束必须固定前向循环数（如需要多步迭代推理），可采用截断BPTT，节省的算力分配给更大模型和更多训练数据，可抵消截断带来的效果损失

  - 若部署时模型大小受显存限制，新增训练算力优先分配给更多训练数据，最优配置下循环数的算力占比仅约24%，盲目增加循环数会浪费算力'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
Looped Transformer通过复用共享层提升参数效率，无需增加参数量即可提升计算深度，但训练时通常采用截断BPTT仅反向传播最后几次循环的梯度，虽能节省训练算力，却会削弱循环结构的收益。此前的缩放研究未联合建模前向、反向循环数的影响，缺乏统一的算力分配与截断策略指导，无法在固定算力下实现效果最优。

### 方法关键点
- 完成近600次训练实验，覆盖58M~919M非嵌入参数、3个数量级的训练token、最多16次前向循环，独立控制前向循环数T与反向循环数B两个变量
- 提出基于有效参数的统一缩放律，引入循环系数g(T,B)量化循环增益与截断折扣，通过9个拟合参数精准刻画损失与参数量、训练token、循环配置的关联关系
- 分别针对固定前向循环数、自由选择循环数两种场景，从理论推导与实验验证两个层面对比截断BPTT与全BPTT的优劣

### 关键结果
实验基于100B token的FineWeb-Edu语料训练，核心数字：
- 同算力下，全BPTT少循环配置（如(4,4)）比截断多循环配置（如(8,2)）的验证损失低0.001~0.003 nats/token
- 2次循环+全BPTT的配置，比同性能非循环Transformer少27%非嵌入参数，仅需多8%的训练算力
- 固定模型大小时，最优循环数随算力呈$C^{0.24}$增长，训练token数随算力呈$C^{0.76}$增长，新增算力优先分配给数据

### 核心结论
除非业务必须固定前向循环数，否则循环Transformer训练优先选择全BPTT，双循环全BPTT是参数效率最高的循环配置
