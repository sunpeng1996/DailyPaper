---
title: An Exact Instrument for State Usage in Selective State-Space Models, and the
  Input-Driven Migration It Reveals
title_zh: 选择性SSM状态使用精确度量工具及输入驱动的模式迁移发现
authors:
- Raktim Bhattacharya
affiliations:
- Texas A&M University
arxiv_id: '2607.11796'
url: https://arxiv.org/abs/2607.11796
pdf_url: https://arxiv.org/pdf/2607.11796
published: '2026-07-13'
collected: '2026-07-14'
category: LLM
direction: 大模型序列建模 · SSM/Mamba剪枝优化
tags:
- SSM
- Mamba
- Model Pruning
- State Space Model
- Efficient Inference
one_liner: 提出选择性SSM状态使用精确度量工具，发现输入驱动模式迁移，验证动态剪枝性能增益
practical_value: '- 业务中使用Mamba做长序列建模（如用户长行为序列召回、多轮Agent上下文管理）的团队，可复用本文的精确Gram张量度量方法，离线评估任意剪枝策略的输出误差，无需上线即可预判效果，降低调优成本

  - 之前采用基于timestep活跃度的Mamba剪枝方案的团队可直接替换策略：timestep几乎不贡献模式迁移，基于输入依赖的写映射Bt设计剪枝规则，精度损失更低

  - 对Mamba推理延迟/内存占用有强需求的生成式推荐、长上下文Agent场景，可先落地半窗口剪枝方案：用窗口前半段的模式能量筛选保留状态，能恢复18~25%的两阶段动态剪枝增益，额外开销极低'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
选择性SSM（如Mamba）是长序列建模的主流架构，状态是其计算和内存瓶颈，但现有状态剪枝方法均为静态近似，无法量化不同输入下模型对状态模式的动态使用情况，既无法实现高精度剪枝，也难以解释内部状态分配逻辑，亟需精确的状态使用度量手段。
### 方法关键点
- 利用Mamba状态矩阵对角化的特性，将每个通道的输出精确拆解为各模式的贡献之和，构造（层、通道、窗口）维度的Gram张量，离线即可计算任意模式子集被剪枝后的精确输出误差，相对误差低至2.3×10⁻⁷
- 定义迁移gap指标衡量静态剪枝与输入调度剪枝的误差比，通过冻结信号的反事实实验定位模式迁移的驱动因子
- 设计两阶段输入调度剪枝：第一遍前向计算当前窗口的各模式能量，筛选top-r保留，第二遍仅用保留模式完成推理
### 关键结果
在Mamba-1（130M~2.8B）、7B Falcon-Mamba、Mamba-2上，跨英文散文、代码、技术文本3个域的1024 token窗口测试：
1. 半状态预算下，输入调度剪枝效果优于静态、Hankel-based、LAST等所有基线，甚至超过未剪枝模型：130M参数下perplexity比未剪枝低0.54，7B参数下低0.04
2. 冻结输入依赖的写映射Bt后，迁移gap从0.7升至0.96，说明模式迁移主要由Bt驱动，timestep几乎无贡献
3. 半窗口剪枝（用前512token选模式，后512token推理）可恢复18~25%的两阶段剪枝增益

> 最值得记住的结论：选择性SSM的重要状态模式会随输入上下文动态迁移，基于输入动态选留模式的剪枝效果远优于任何静态剪枝策略
