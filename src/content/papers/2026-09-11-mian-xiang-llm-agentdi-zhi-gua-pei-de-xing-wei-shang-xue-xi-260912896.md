---
title: Behavior Quotient Learning for Low-Rank Adaptation of LLM Agents
title_zh: 面向LLM Agent低秩适配的行为商学习方法
authors:
- Pengyang Zhou
- Xiaobin Tu
- Zhengxi Liu
- Rongkun Xue
- Haochen Li
- Miancan Liu
- Ziyuan Chen
- Yinggui Wang
- Jinkui Ren
- Xiantao Zhang
affiliations:
- Alibaba Cloud
arxiv_id: '2609.12896'
url: https://arxiv.org/abs/2609.12896
pdf_url: https://arxiv.org/pdf/2609.12896
published: '2026-09-11'
collected: '2026-09-14'
category: Agent
direction: Agent高效微调 · LoRA优化
tags:
- LoRA
- LLM Agent
- Parameter Efficient Fine-Tuning
- Trajectory Optimization
- Manifold Learning
one_liner: 提出BQ-LoRA单LoRA适配框架，解决多轨迹冗余和定秩压缩决策失真问题，性能超越多Adapter基线
practical_value: '- 单LoRA适配方案可直接复用在电商导购Agent、商品文案生成Agent的微调场景，避免多LoRA的路由开销和存储成本，适配后推理无额外开销

  - BQB轨迹加权方法可迁移到推荐系统的用户行为轨迹SFT流程，对重复/冗余的点击/交互轨迹降权，提升有限LoRA容量下的行为覆盖度

  - DPC定秩压缩的双目标（权重误差+决策失真）优化思路可复用在GenRec场景的LoRA微调，缓解低秩下生成结果偏离预期的问题'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM Agent适配方案分为两类：多LoRA分能力适配会带来额外存储成本和推理路由开销；单LoRA适配则存在两个核心问题：一是不同交互轨迹的梯度更新可能产生等价决策变化，冗余更新浪费定秩容量；二是聚合更新超出LoRA秩上限时，仅在权重空间压缩会扭曲决策分布，导致Agent行为偏移。

### 方法关键点
- 行为商平衡（BQB）模块：构造局部行为商流形，将轨迹更新映射到决策表示空间，基于切线空间的局部密度对等价行为的轨迹降权，提升差异化行为的贡献占比
- 决策保持压缩（DPC）模块：先将平衡后的梯度投影到当前LoRA的切空间得到仿射目标，再通过联合优化权重近似误差和一阶决策失真，将目标压缩到原定秩范围内，最大化保留决策效果

### 关键实验
在AppWorld（多步交互任务）和BrowseComp-Plus（深度搜索任务）上对比7种基线（含全参数微调、标准LoRA、多LoRA方案MoRAgent、DART等），使用Qwen3.5-4B/9B作为backbone：BQ-LoRA平均性能比最强多LoRA基线MoRAgent高2.12~2.14个百分点，所有场景下交互步数/搜索调用量均为最低；消融实验显示两个模块各自可带来3.5~3.8个百分点的性能提升。

**最值得记住的一句话**：单LoRA适配时，优先保证决策行为的一致性而非单纯权重拟合精度，能在有限参数预算下获得更优的Agent端到端效果。
