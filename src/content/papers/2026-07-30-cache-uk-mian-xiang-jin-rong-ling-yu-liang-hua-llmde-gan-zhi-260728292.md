---
title: 'CACHE-UK: A Stability-Aware Memory Editor for Sequentially Updated Quantized
  LLMs in Finance'
title_zh: CACHE-UK：面向金融领域量化LLM的感知稳定性序列记忆编辑框架
authors:
- Anubhav Lakra
- Yue Feng
affiliations:
- Indian Institute of Technology Madras
- University of Birmingham
arxiv_id: '2607.28292'
url: https://arxiv.org/abs/2607.28292
pdf_url: https://arxiv.org/pdf/2607.28292
published: '2026-07-30'
collected: '2026-07-31'
category: LLM
direction: 大模型量化 · 记忆编辑优化
tags:
- LLM Quantization
- Memory Editing
- LoRA
- Catastrophic Forgetting
- Domain Adaptation
one_liner: 针对4-bit量化LLM序列编辑退化问题，提出三模块稳定编辑框架，知识退化较基线降低11-17%
practical_value: '- 量化LLM做序列知识更新时，可复用rank-1 LoRA扰动方案，仅修改LoRA B矩阵避免全量参数更新的退化问题，适配电商/广告场景的低资源部署需求

  - 可直接复用`degradation debt`闭环控制机制，每次更新后用固定业务校验集监控模型性能，动态衰减后续更新强度，缓解商品/规则等高频更新带来的灾难性遗忘

  - 领域适配场景下可借鉴内容自适应编辑强度策略，对高业务优先级的知识（如电商商品价格/库存、广告投放规则）分配更高更新权重，保证核心信息更新成功率'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
金融领域LLM需高频更新市场、监管、企业事实，4-bit量化是资源受限部署的主流方案，但现有记忆编辑方法在量化模型上做序列更新时会出现严重性能退化，编辑的事实无法泛化到 paraphrased 查询，甚至触发灾难性遗忘，现有方案未覆盖量化场景的编辑稳定性需求。
### 方法关键点
- rank-1 LoRA扰动机制：将事实编辑的秩一更新仅作用于LoRA的B矩阵，而非全量权重，参数规模降低200倍，大幅减少量化空间的碰撞概率
- 领域优先级模块：通过关键词匹配识别编辑内容的领域相关性，对高优先级事实提升编辑强度，保证核心知识更新效果
- 闭环稳定性控制器：引入`degradation debt`指标，每次编辑后在固定留存校验集上评估退化程度，债务超阈值时衰减后续编辑强度，低于阈值时逐步恢复，避免连续编辑的累计干扰
### 关键实验
基于88021条英国金融领域语料微调的4-bit量化OpenLLaMA-3B模型，对比ROME、MEMIT、EasyEdit、KnowledgeEditor四个适配基线：编辑成功率均接近100%的前提下，测试泛化成功率达28%，较最优基线高6个百分点；知识退化率仅55%，较基线降低11-17%；编辑速度达450条/分钟，与基线持平。
### 核心结论
4-bit量化下LLM记忆编辑的泛化能力会出现断崖式下跌，在LoRA子空间做受控编辑是目前兼顾效率与稳定性的可行路径
