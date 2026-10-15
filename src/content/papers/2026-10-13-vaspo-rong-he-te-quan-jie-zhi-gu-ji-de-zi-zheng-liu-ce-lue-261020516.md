---
title: 'VASPO: Self-Distillation with Privileged Value Estimation'
title_zh: VASPO：融合特权价值估计的自蒸馏策略优化算法
authors:
- Fei Wu
- Zhenrong Zhang
- Jianshu Zhang
- Jun Du
affiliations:
- University of Science and Technology of China
- IFLYTEK Research
arxiv_id: '2610.20516'
url: https://arxiv.org/abs/2610.20516
pdf_url: https://arxiv.org/pdf/2610.20516
published: '2026-10-13'
collected: '2026-10-15'
category: Training
direction: 大模型RL训练 · 自蒸馏优化
tags:
- PPO
- Self-Distillation
- Policy Optimization
- LLM Reasoning
- RLHF
one_liner: 将特权信息同时用于PPO critic价值估计和自教师Token引导，提升大模型推理性能
practical_value: '- 做电商Agent多步决策、搜索Query改写、商品文案生成等需要分步正确性的任务RL训练时，可复用特权信息双路复用思路，无需额外引入大教师模型，即可同时优化价值估计精度与token级引导效果

  - 可直接迁移优势调制trick：仅对正优势token用clip后的自教师-学生概率比做重加权，既能利用特权信号增强优质token梯度，又能避免引入偏置

  - 训练流程优化可复用：每轮采样新轨迹后先更新critic再计算优势，且不做全局优势白化，能稳定提升PPO训练的收敛性与最终效果

  - 电商场景下可将人工标注的优质Query、高转化文案、正确客服回答作为特权信息，用该框架训练生成类模型，在不增加推理成本的前提下提升生成质量'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有On-policy自蒸馏只能提供token级局部偏好，无法对齐学生后续无引导生成的预期收益，易引入风格偏置甚至抑制推理能力；PPO类RL方法仅靠最终奖励做信用分配，在长推理路径上价值估计误差大。两者融合的现有方案仅将特权信息用于教师引导，未挖掘其在价值估计侧的增益空间。

### 方法关键点
- 特权信息双路复用：训练阶段自教师与critic共享参考解答等特权信息，部署阶段学生模型仅输入普通prompt，无额外 overhead
- 特权critic预更新：每轮rollout完成后，先基于最新采样的轨迹更新带特权输入的critic，再计算GAE优势，大幅降低价值估计偏差
- 选择性优势调制：仅对正优势token，用clip后的自教师-学生概率比对优势做重加权，严格保留优势符号，避免特权信号扭曲优化方向
- 验证了无需全局优势白化、优先用完整参考解答而非仅答案作为特权信息等设计的有效性

### 关键实验
在Qwen3-4B、OLMo3-7B两个基座上训练数学推理能力，6个基准平均准确率较PPO分别提升2.59、1.81个百分点；在Knights and Knaves逻辑推理任务上平均准确率达到SOTA，比基线最高提升0.47个百分点。

### 核心结论
特权信息在生成序列的不同位置增益互补：生成早期自教师引导收益更高，生成后期critic价值估计增益更大，双路复用可最大化特权信息的价值
