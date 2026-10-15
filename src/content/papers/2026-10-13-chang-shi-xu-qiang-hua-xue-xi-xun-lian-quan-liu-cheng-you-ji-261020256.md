---
title: Long-Horizon RL Needs Muon
title_zh: 长时序强化学习训练全流程优化：基于Muon优化器的适配方案
authors:
- Kai Ruan
- Jinghao Lin
- Tao Chen
- Ziqi Zhou
- Qianshan Wei
- Zihe Huang
affiliations:
- Renmin University of China
- Duke University
- Institute of Automation, CAS
- Institute of Computing Technology, CAS
arxiv_id: '2610.20256'
url: https://arxiv.org/abs/2610.20256
pdf_url: https://arxiv.org/pdf/2610.20256
published: '2026-10-13'
collected: '2026-10-15'
category: Agent
direction: 长时序Agent · 强化学习训练优化
tags:
- Muon
- Long-Horizon Agent
- Reinforcement Learning
- Asynchronous Training
- Policy Optimization
one_liner: 结合Muon优化器、异步更新与辅助奖励的长时序RL训练方案，大幅提升Agent任务成功率
practical_value: '- 训练电商导购、多轮对话推荐这类长时序交互Agent时，可优先用Muon优化器更新隐层参数，嵌入层、输出头仍保留AdamW，能提升训练稳定性与最终效果

  - 长时序Agent训练可直接复用文中辅助奖励设计：增加交互长度惩罚（超2048token最高扣-0.5）、工具调用错误惩罚（单次无效动作扣-0.5），减少冗余交互和错误操作

  - 异步RL训练场景可引入Truncated Importance Sampling（截断阈值设为2）校正策略滞后带来的分布偏差，无需批归一化直接加权token级损失即可生效

  - 多轮交互类Agent训练的损失聚合优先选token-level平均，相比序列平均对长度不均的轨迹适配性更好，避免短轨迹被长轨迹淹没'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长时序Agent需要在多轮交互中协调推理、工具调用和环境反馈，现有基于Adam的异步RL训练存在两个核心痛点：一是稀疏最终奖励下不同长度轨迹的权重分配不合理，二是异步采集的轨迹和当前训练策略存在滞后偏差，容易出现训练崩溃、成功率低的问题，亟需更适配长时序场景的训练优化方案。

### 方法关键点
- 优化器分层设计：隐层权重矩阵采用Muon优化器更新（基于Newton-Schulz迭代近似正交化，控制参数更新的谱范数，避免参数更新幅度过大），嵌入层、输出头、归一化参数等仍用AdamW更新
- 辅助奖励塑形：在二进制最终任务奖励基础上，增加长度惩罚、工具调用错误惩罚，综合辅助项裁剪到[-0.25, 0.25]加入每个token的优势值
- 策略偏差校正：引入Truncated Importance Sampling（TIS），截断阈值设为2，加权token级PPO损失校正异步策略滞后带来的分布差
- 损失聚合：采用token-level平均损失，按轨迹有效token数加权，适配长度差异大的多轮交互轨迹

### 关键实验
数据集采用R2E-Gym的代码仓问题解决任务，对比基线包括SPO+Adam、SPO+Muon、不同组件消融的SPO++变种，测试模型为MiniCPM5-2B和Qwen3.5-4B。核心结果：完整配方在MiniCPM5-2B上训练成功率达84.4%，比SPO+Adam基线（26.8%）提升57.6个百分点，比SPO+Muon基线（45.2%）提升39.2个百分点；在Qwen3.5-4B上完整配方成功率达70.9%，比SPO+Adam基线（25.8%）提升45.1个百分点，移除长度惩罚、工具惩罚或TIS都会带来10%以上的成功率下降，Adam配置下多个方案出现训练崩溃。

### 核心结论
长时序Agent异步RL训练中，Muon优化器搭配合理的奖励塑形、偏差校正和损失聚合，不仅能大幅提升训练成功率，还能有效避免Adam常见的训练崩溃问题。
