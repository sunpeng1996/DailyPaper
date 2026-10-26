---
title: Every Weight Is a Path of Shared Discrete Decisions
title_zh: TWIG：基于共享离散决策路径的神经网络权重表示方法
authors:
- Ammar Ali
- Stamatis Lefkimmiatis
affiliations:
- LEAD Lab, ITMO University
arxiv_id: '2610.31931'
url: https://arxiv.org/abs/2610.31931
pdf_url: https://arxiv.org/pdf/2610.31931
published: '2026-10-21'
collected: '2026-10-26'
category: LLM
direction: LLM部署 · 权重量化压缩
tags:
- WeightQuantization
- ModelCompression
- EfficientLLM
- HardwareFriendly
- GPTQ
one_liner: 树结构权重表示TWIG，统一压缩、硬件映射、离散优化需求，比GPTQ最高省55%加法
practical_value: '- 端侧LLM部署可直接复用TWIG的移位+加法无乘法电路设计，适合电商端侧推荐Agent、端侧搜索等低延迟场景，大幅降低ASIC芯片面积与推理能耗

  - 现有GPTQ/AWQ量化方案可叠加TWIG的共享决策路径思路，针对推荐大模型门控层等离群值多的权重矩阵，同精度下可省20-55%运算量

  - 多压缩方案统一为TWIG的树编辑操作，无需分别维护剪枝/量化/低秩/码本的不同格式与推理kernel，大幅降低大模型轻量化的工程成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前模型压缩领域各技术路线割裂，剪枝、量化、低秩分解、码本共享各有独立的存储格式、求解器与推理Kernel，组合优化成本极高；固定权重ASIC部署时每个权重需独立常量乘法器，面积与能耗开销大；离散优化器仅能解决rounding等窄范围子问题，缺乏统一的离散权重表示框架。
### 方法关键点
- TWIG树结构权重表示将每个权重对应根到叶的离散决策路径（符号、2的幂次移位、零门控、共享表索引），同组权重共享上层路径决策，仅需存储一次
- 现有所有主流数值格式（FP16/INT8/GPTQ等）都是TWIG的浅树特例，无精度损失
- 当权重量化为2的幂次组合时，推理仅需移位与加法操作，无需乘法器
- 剪枝、量化、低秩分解、码本共享统一为7种树编辑操作，单个优化器即可完成全模型压缩策略的全局选择
### 关键实验
在LLaMA-3-8B的5个线性层权重矩阵上测试，与同层误差的GPTQ对比：3/4比特位宽下普通矩阵可省9~15%加法运算，带强离群值的矩阵可省20~55%加法运算；BF16权值无损压缩可节省24%存储空间。
### 核心结论
所有常见权重压缩方法本质都是对共享离散决策的编辑，统一表示后可在存储、精度、运算成本之间实现全局最优tradeoff。
