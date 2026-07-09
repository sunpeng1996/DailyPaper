---
title: 'DeLS-Spec: Decoupled Long-Short Contexts for Parallel Speculative Drafting'
title_zh: DeLS-Spec：面向并行推测解码的长短上下文解耦方法
authors:
- Hong-Kai Zheng
- Piji Li
affiliations:
- 南京航空航天大学人工智能学院
- 工信部模式分析与机器智能重点实验室
- 教育部脑机智能技术重点实验室
arxiv_id: '2607.07409'
url: https://arxiv.org/abs/2607.07409
pdf_url: https://arxiv.org/pdf/2607.07409
published: '2026-07-08'
collected: '2026-07-09'
category: LLM
direction: LLM推理优化 · 并行推测解码加速
tags:
- Speculative Decoding
- LLM Inference
- DFlash
- Decoupled Training
- Logit Fusion
one_liner: 无需重训DFlash骨干，通过独立训练的轻量局部头补全块内因果性，提升并行推测解码性能
practical_value: '- 现有基于LLM的电商导购/Agent对话场景若已接入DFlash类并行推测解码，可直接复用DeLS-Spec的插件式方案，无需重训原有骨干，仅用少量业务语料独立训练RNN/Markov局部头即可获得2%-5%的解码速度提升，且适配不同规格的DFlash
  checkpoint

  - 多专家logit融合时可借鉴「减去unigram prior修正频率偏置」的trick，避免长/短上下文专家重复计数高频token导致的生成质量下降；固定α=β=0.3即可获得比可学习权重更稳定的效果，省去额外调优成本

  - 低资源场景下做LLM推理加速优先选择解耦式训练的插件式模块，DeLS-Spec的局部头训练仅需1/12的端到端联合微调成本、1/5的显存占用，8B模型也可在单张消费级GPU上完成训练，无需多卡资源'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
块并行推测解码（如DFlash）单次前向生成整段token，推理效率远高于传统自回归草拟，但块内token并行预测缺少显式因果依赖，导致接受长度偏低；现有补全因果性的方案（如Domino、DSpark）需从头训练或联合微调草拟模型，训练成本高、灵活性差，无法直接适配已训练好的DFlash checkpoint。

### 方法关键点
- 架构解耦：固定已有DFlash为长上下文专家，捕捉全局语义与任务约束；新增轻量局部RNN/Markov头作为短上下文专家，建模块内已生成token的因果依赖，两个专家完全独立训练
- 训练逻辑：局部头仅用标准下一词预测目标在纯文本语料上训练，无需目标模型/DFlash的隐状态，也无需联合优化，训练成本极低
- 推理融合：长、短上下文logit加权相加后减去unigram prior修正频率偏置，α、β默认设为0.3即可获得最优效果，无需额外调优

### 关键实验
在Qwen3-4B/8B模型上测试，覆盖数学、代码、对话三类基准，对比EAGLE-3、DART、DFlash等基线：DeLS-Spec在温度0场景下比DFlash平均提速0.19×，平均接受长度提升0.31；温度1场景下平均提速0.11×，接受长度提升0.21；局部头可直接适配不同厂商发布的DFlash checkpoint，无需重新训练，仅损失15%左右的端到端联合训练方案（Domino-FT）的性能，但训练成本降低12倍以上。

最值得记住的一句话：并行推测解码的优化可以走解耦式插件路线，无需重训原有骨干，仅靠独立训练的轻量模块补全缺失的局部依赖就能获得可观的性能收益，工程落地性价比极高
