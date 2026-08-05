---
title: 'Balancing Efficiency and Efficacy: Training-Free Attention-Guided Switching
  Between Explicit and Latent Thoughts for MLLMs'
title_zh: 兼顾效率与效果：免训练注意力引导的MLLM显隐思维切换方法
authors:
- Haoqian Kang
- Liupeng Li
- Kuofeng Gao
- Jinpeng Wang
- Zhenyu Lu
- Bin Chen
- Ke Chen
- Yaowei Wang
affiliations:
- 哈尔滨工业大学（深圳）
- 清华大学深圳国际研究生院
- 鹏城实验室
- 中国科学院深圳先进技术研究院
arxiv_id: '2608.03450'
url: https://arxiv.org/abs/2608.03450
pdf_url: https://arxiv.org/pdf/2608.03450
published: '2026-08-04'
collected: '2026-08-05'
category: Reasoning
direction: 多模态大模型 · 推理效率优化
tags:
- MLLM
- Chain-of-Thought
- Latent Reasoning
- Attention Routing
- Training-Free
one_liner: 提出免训练的注意力引导切换策略，动态切换MLLM显/隐式推理，同时提升推理精度与效率
practical_value: '- 电商多模态搜索/商品问答场景的MLLM部署可直接复用该免训练AGS策略，无需微调即可降低推理延迟，同时减少商品属性识别的视觉幻觉，适配高吞吐的线上业务需求

  - 跨模态注意力占比指标可迁移到多模态推荐的用户意图理解场景，用于区分用户当前处于商品视觉感知阶段还是需求逻辑判断阶段，动态调整推荐内容的呈现形式

  - 最小维护窗口+最大切换预算的约束设计可复用在所有大模型推理服务的流式输出控制中，避免模式频繁切换导致的输出不稳定或超时问题'
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

### 动机
当前MLLM推理中，显式CoT推理延迟高、易出现视觉幻觉，现有隐式推理方法需要大量训练成本；直接将纯文本免训练隐式推理方法迁移到多模态场景性能不稳定，核心问题是token级熵无法区分感知歧义（视觉细节不清晰）和逻辑不确定性（推理步骤复杂），导致路由决策错误。

### 方法关键点
- 提出**视觉-文本注意力占比**指标，计算每个解码步骤模型对视觉token和文本token的平均注意力比值，精准区分当前是感知主导还是逻辑主导阶段
- 设计注意力引导切换（AGS）策略，感知主导阶段用概率加权的软token嵌入做隐式推理，避免视觉信息离散化损失，逻辑主导阶段生成显式文本保证推理严谨性
- 引入两个工程约束：显式推理最小维护窗口W（默认512步）避免频繁切换导致逻辑断裂，最大切换预算C（默认4次）避免无限推理循环，保证终止确定性

### 关键实验
在Qwen3-VL、InternVL3.5两个系列2B/4B/8B模型上验证，覆盖MathVista、ScienceQA等6个多模态推理基准；对比显式CoT基线，Qwen3-VL-8B-Thinking模型平均精度从51.7%提升到58.8%，推理步数从2214降至953（延迟降低约57%）；对比熵基路由方法，平均精度提升4个百分点，推理成本进一步降低5.7%。

### 核心结论
多模态推理优化的核心是区分感知与逻辑两个独立过程，基于内部注意力信号的路由比输出熵路由更精准可解释
