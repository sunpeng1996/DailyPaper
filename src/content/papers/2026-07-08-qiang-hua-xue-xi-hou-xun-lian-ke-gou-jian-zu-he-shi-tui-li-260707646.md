---
title: RL Post-Training Builds Compositional Reasoning Strategies
title_zh: 强化学习后训练可构建组合式推理策略
authors:
- Azwar Abdulsalam
- Nishil Patel
- Andrew Saxe
affiliations:
- Gatsby Computational Neuroscience Unit, UCL
arxiv_id: '2607.07646'
url: https://arxiv.org/abs/2607.07646
pdf_url: https://arxiv.org/pdf/2607.07646
published: '2026-07-08'
collected: '2026-07-09'
category: Training
direction: LLM后训练 · 组合式推理
tags:
- RL Post-Training
- Compositional Reasoning
- GRPO
- Rejection Fine-Tuning
- Reasoning Strategy
one_liner: 在可控重写语法环境下证明RL后训练可将基础技能组合为可复用的高层推理策略
practical_value: '- 做电商导购、query改写等推理类Agent的后训练时，优先选择GRPO这类带同prompt组内负样本对比的RL方法，相比RFT能大幅抑制无效推理路径，提升复杂任务泛化能力

  - 若要让RL后训练组合出新的业务策略（如多步召回规则组合、营销话术组合），预训练阶段需优先喂连续的基础操作链，而非零散的基础操作样本

  - 业务任务难度设计可参考「基础操作序列是否超过生成预算」的分层逻辑，引导RL自动组合出压缩的高阶操作，解决超预算的复杂场景问题'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前业界对RL后训练的作用存在广泛争议：它是仅放大基座模型已有的低概率潜在技能，还是能组合基础技能生成全新的高阶策略？自然语言任务下推理过程不可审计，无法明确机制，因此需要可控环境拆解RL后训练的真实作用。

### 方法关键点
- 设计完全可审计的重写语法环境，基座Transformer预训练仅喂基础符号重写链，不包含任何组合式快捷操作
- 后训练任务要求将长字符串收缩为目标符号，难度按基础收缩步数是否超过256token生成预算划分为1-6级，仅提供最终结果是否正确的二元奖励
- 对比GRPO（RL方法）与RFT（拒绝微调基线）的训练效果，全程审计每一步重写的类型：基础操作、顺序组合、并行组合、无效操作

### 关键结果数字
- RFT早期提升快但快速进入平台期，RL后期反超，难度越高优势越显著；难度4-5的任务基座模型即使pass@1024准确率仍为0，RL后训练后pass@16即可稳定解决
- RL的无效重写占比远低于RFT，且能将发现的组合规则固化为可复用策略库，训练后期80%以上的组合操作是已有规则的复用
- 预训练阶段仅提高基础收缩操作的总数量、不提供连续收缩链时，RL无法有效组合出高阶策略

### 最值得记住的一句话
基座模型提供基础技能的原料，RL后训练不是简单重加权已有能力，而是将零散的基础技能组织为可复用的高阶策略，真正扩展模型的能力边界
