---
title: 'Rethinking in Spikes: Mitigating Hallucinations in MDLMs with Step-Aware Decoding'
title_zh: 熵尖峰感知解码：缓解多模态扩散大语言模型的生成幻觉
authors:
- Zhongxing Xu
- Zhonghua Wang
- Zhe Qian
- Shiyan Su
- Ming Hu
- Xiaocheng Zou
- Wei Feng
- Mingquan Lin
- Yuyin Zhou
- Yifan Peng
affiliations:
- Monash University
- Cornell University
- UC Santa Cruz
- Northeastern University
- University of Minnesota
arxiv_id: '2611.12901'
url: https://arxiv.org/abs/2611.12901
pdf_url: https://arxiv.org/pdf/2611.12901
published: '2026-10-13'
collected: '2026-11-16'
category: LLM
direction: 多模态扩散LLM · 幻觉缓解 解码优化
tags:
- MDLM
- Hallucination Mitigation
- Decoding Strategy
- Diffusion LLM
- Multimodal LLM
one_liner: 提出无需训练的即插即用StepRefine解码策略，通过检测去噪熵尖峰定向优化降低MDLM生成幻觉
practical_value: '- 生成式推荐/多模态文案生成场景可直接复用熵尖峰检测逻辑，仅在高不确定性步骤做隐空间精炼，无需重新训练模型，即可降低商品描述、营销海报文案的事实性错误，且不增加推理延迟

  - 概率加权embedding+迭代隐空间精炼的trick可迁移到现有生成式推荐的解码模块，替代直接greedy解码，保留候选语义与用户上下文、商品属性的交互，提升推荐理由生成的一致性与相关性

  - 步感知自适应开关的设计思路可复用在电商导购Agent的多步推理模块，仅在置信度波动大的步骤增加知识检索/结果校验，平衡推理效率与准确率，降低导购回答的幻觉

  - StepRefine可与现有KV cache、并行解码等加速方案完全兼容，上线时无需改动底层推理加速逻辑，可直接插接到现有MDLM部署链路中，落地成本极低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多模态扩散大语言模型（MDLM）凭借双向全局建模和迭代去噪特性，在多模态理解、生成任务上表现突出，但现有解码策略多聚焦推理效率优化，未关注去噪过程中的时序不确定性波动，导致生成幻觉问题严重，直接影响电商商品文案生成、多模态搜索结果、导购Agent回答的可信度，亟需无训练、低侵入的幻觉缓解方案。

### 方法关键点
- 熵尖峰检测：计算每个去噪步的掩码平均熵，与前w个步的熵变化均值+标准差比较，识别偏离局部趋势的熵尖峰步骤；统计证明80%的幻觉令牌均来自这些少数尖峰步，且集中在去噪前50%阶段。
- 步感知模式切换：普通步沿用标准离散解码，熵尖峰步切换为隐空间精炼模式，通过概率加权的令牌embedding替换硬掩码，保留多候选语义，迭代与上下文交互，直到连续预测分布的平均KL散度低于稳定性阈值，再切回离散解码。
- 成本控制：精炼阶段的额外前向传播从总去噪步预算中扣除，总推理步数保持不变，不会额外增加延迟。

### 关键实验
在4个主流MDLM backbone（LLaDA-V、Dream-VL等）、12个覆盖通用推理、幻觉评测、数理推理的benchmark上验证，相比基线，通用推理准确率平均提升2.3%~2.8%，幻觉评测集MMHalu得分提升2.3%~4.2%，Bingo得分提升3%~4.4%；可兼容Fast-dLLM、dKV-Cache等所有现有加速方案，速度损失<1%，准确率仍保持2%+的提升。

### 核心结论
扩散类生成模型的幻觉绝大多数来自少数高不确定性的去噪步，仅针对这些步骤做定向优化，即可在不增加推理成本的前提下大幅提升生成质量。
