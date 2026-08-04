---
title: 'GradCuit: Credit-Assigned Gradient Flow Enables Robust and Interpretable Test-Time
  Latent Reasoning'
title_zh: GradCuit：带信用分配的梯度流实现鲁棒可解释的测试时隐式推理
authors:
- Zhaoxin Yu
- Qi Shen
- Hengli Li
- Zhaowei Zhang
- Song-Chun Zhu
- Chi Zhang
- Zilong Zheng
affiliations:
- Beijing Institute for General Artificial Intelligence
- Institute of Automation, Chinese Academy of Sciences
- Beijing University of Posts and Telecommunications
- Peking University
arxiv_id: '2608.02585'
url: https://arxiv.org/abs/2608.02585
pdf_url: https://arxiv.org/pdf/2608.02585
published: '2026-08-02'
collected: '2026-08-04'
category: Reasoning
direction: LLM测试时隐式推理优化
tags:
- Test-Time Optimization
- Latent Reasoning
- Transformer
- Credit Assignment
- Gradient Flow
one_liner: 在Transformer中间层插入可优化隐状态，通过自注意力实现直接梯度回传提升测试时推理性能
practical_value: '- 电商搜索/导购Agent的推理优化场景可复用该测试时隐状态优化思路，不微调基础模型即可提升复杂用户query的推理准确率，避免微调带来的效果波动

  - 可复用中间层隐状态优化的架构选择：优先选择Transformer 25%~50%深度的层作为优化空间，兼顾上下文信息和下游梯度传播效率，鲁棒性远高于输出层隐状态优化

  - 业务侧的自奖励验证机制可参考其设计：用同一基座模型作为轻量自验证器，无需额外训练奖励模型即可实现推理效果的迭代优化，降低落地成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有测试时隐式推理方法依赖解码token作为隐变量与推理路径的接口，梯度仅能通过解码过程回传，存在信用分配间接、隐状态更新对推理的影响不可解释、优化鲁棒性差的问题，不同学习率下效果波动大，难以落地到实际业务场景。

### 方法关键点
- 在Transformer指定中间层的prompt隐表示与生成序列隐表示之间插入可优化隐状态，保持基座模型全参数冻结，仅优化隐状态偏移量
- 利用因果自注意力机制，每个生成token的对数概率均可通过剩余Transformer层获得到所有前置隐状态的可微路径，直接将全序列奖励加权梯度分配给对应隐状态
- 采用轻量自奖励验证机制：用同一基座模型作为验证器，仅校验最终答案正确性给出二元奖励，无需额外训练奖励模型，优化终止条件为验证通过或达到最大10步迭代

### 关键实验
覆盖5个指令微调基座（LLaMA3.2-3B、LLaMA3.1-8B、Qwen2.5-7/14B、Qwen3-4B）、3个推理基准（GPQA-Diamond、GSM8K、MATH-500）、2种答案格式：
- 平均准确率64.5%，较CoT提升6.6pp，较最优竞品LatentSeek提升2.4pp
- 7组学习率下准确率标准差仅0.82，远低于LatentSeek的1.53，鲁棒性显著提升
- 随机梯度更新的变种效果仍与LatentSeek相当，优化空间本身的鲁棒性优势突出

### 核心启示
测试时推理优化无需修改基座模型或依赖复杂奖励模型，通过Transformer自注意力的天然梯度通路直接优化25%~50%深度的中间层隐状态，即可兼顾效果、鲁棒性和可解释性
