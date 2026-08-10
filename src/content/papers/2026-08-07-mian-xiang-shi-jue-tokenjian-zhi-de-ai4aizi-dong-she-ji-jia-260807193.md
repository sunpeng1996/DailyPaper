---
title: An AI4AI Framework for Visual Token Pruning
title_zh: 面向视觉Token剪枝的AI4AI自动设计框架AutoPrune
authors:
- Zhen Liu
- Wenli Huang
- Wei Song
- Yuhan Liu
- Zhiqin Yang
- Jingwen Fu
affiliations:
- Xi'an Jiaotong University
- Ningbo University of Technology
- North China University of Technology
- Xiaomi Inc.
- Hong Kong University of Science and Technology
arxiv_id: '2608.07193'
url: https://arxiv.org/abs/2608.07193
pdf_url: https://arxiv.org/pdf/2608.07193
published: '2026-08-07'
collected: '2026-08-10'
category: Multimodal
direction: 多模态大模型 · 视觉Token剪枝推理优化
tags:
- MLLM
- Visual Token Pruning
- Domain Specific Language
- Inference Optimization
- LLM-driven Design
one_liner: 通过LLM驱动的结构化残差搜索自动生成高效可迁移的MLLM视觉Token剪枝策略
practical_value: '- 电商多模态内容理解（商品图问答、短视频打标）场景可直接复用AutoPrune剪枝策略，94.4%视觉Token裁剪下保留99%+性能，大幅降低推理延迟与成本

  - 用LLM自动生成业务策略（如召回规则、特征选择逻辑）时，可借鉴TPDSL设计思路：将策略拆分为可复用原子+基于强基线的残差修改，大幅缩小搜索空间，避免无效输出

  - 多模态推荐的视觉特征压缩环节，可复用其多维度Token评分机制（相关性、显著性、空间中心性等融合），压缩特征的同时保留核心业务信息

  - 推理优化落地可参考其跨场景迁移设计：一次搜索得到的剪枝策略可跨MLLM backbone、跨Token预算直接复用，无需重复调优，降低迭代成本'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
现有多模态大模型（MLLM）的视觉Token剪枝策略均依赖手工设计，需要大量领域专家经验与试错成本，随着MLLM架构、剪枝目标、Token预算的日益多元化，人工遍历庞大的设计空间效率极低，难以适配快速迭代的业务需求。

### 方法关键点
- 提出训练-free的AutoPrune框架，无需微调目标MLLM，通过LLM驱动自动生成剪枝策略，核心是设计了Token剪枝领域特定语言TPDSL，包含131个可复用原子，覆盖预算控制、Token评分、选择约束、Token重组4类核心操作。
- 不要求LLM从零生成完整剪枝代码，而是将候选策略定义为对已有强基线剪枝策略的残差修改，大幅缩小搜索空间，引导LLM聚焦对效果影响最大的策略组件。
- 采用evaluator-in-the-loop迭代流程：LLM基于历史搜索记录提出候选TPDSL配置，经过安全校验（预算合规、索引合法、数值稳定等）后在任务上评估，迭代筛选最优策略，所得策略支持跨Token预算、跨MLLM backbone直接迁移复用，无需重新搜索。

### 关键实验
在14个多模态基准、3个主流MLLM backbone上验证，对比CDPruner、PruMerge+等SOTA手工剪枝方法：
1. 94.4%视觉Token裁剪率下，保留99.7%~99.9%的全量Token性能，比CDPruner高2.4~3.2个点，比PruMerge+高7.9~8.9个点。
2. LLaVA-NeXT-7B 320保留Token设置下，FLOPs降低9.9×，prefill延迟降低6.4×，KV cache从1440MB压缩到160MB，GPU显存占用下降3.4GB。
3. 一次搜索得到的策略直接迁移到Qwen2.5-VL-7B，在80.2%~97.5%的裁剪率下，相对性能比基线高2.9~6.1个百分点。

### 核心结论
LLM驱动的专用领域算法设计，核心不是让LLM自由生成代码，而是通过结构化领域语言将搜索空间约束为对强基线的残差修改，才能兼顾效果、效率与可执行性。
