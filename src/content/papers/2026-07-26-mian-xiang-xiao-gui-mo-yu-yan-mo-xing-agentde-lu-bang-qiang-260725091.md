---
title: Towards Robust Reinforcement Learning for Small-Scale Language Model Agents
title_zh: 面向小规模语言模型Agent的鲁棒强化学习对齐方案
authors:
- Md Rezwanul Haque
- Md. Milon Islam
- Fakhri Karray
affiliations:
- University of Waterloo
- Khulna University of Engineering & Technology
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2607.25091'
url: https://arxiv.org/abs/2607.25091
pdf_url: https://arxiv.org/pdf/2607.25091
published: '2026-07-26'
collected: '2026-07-29'
category: Agent
direction: 端侧SLM Agent 强化学习对齐优化
tags:
- SLM
- PPO
- RLHF
- LoRA
- On-Device Agent
- Alignment
one_liner: 定位70-500M SLM的PPO训练3种失败模式，提三层安全机制实现稳定对齐
practical_value: '- 端侧SLM Agent（如电商端侧导购、推荐文案生成）做PPO训练可直接复用本文稳定性方案：merge SFT LoRA后重初始化新LoRA解决梯度静默，<200M参数模型PPO阶段强制用float32防数值溢出，加奖励白化+权重回滚防策略崩溃

  - 业务场景中判断是否给SLM做PPO对齐可直接用本文决策规则：先测SFT模型PPL，仅当PPL<20时PPO能获得稳定收益，否则优先优化SFT数据质量或调大LoRA
  rank

  - 垂直领域SLM对齐无需海量指令数据，仅用10K样本做SFT+少量PPO迭代，即可超过通用instruction-tuned SLM的领域效果，大幅降低数据成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
70-500M参数的SLM是端侧Agent（如电商端侧导购、个性化内容生成）的核心选型，但传统PPO对齐在该参数区间稳定性极差，现有研究大多直接改用DPO等免RL方法，未系统定位失败根因，也缺乏可复用的工程解决方案。

### 方法关键点
- 定位3种SLM特有的PPO失败模式：PEFT/TRL管线中LoRA参数静默冻结、bfloat16下重要性比值数值溢出、奖励模型误差导致的灾难性策略崩溃
- 对应工程优化：merge-and-reinitialize适配器技术（先把SFT LoRA合并到基模型再挂载新的零初始化LoRA保证梯度流通）、PPO更新阶段全用float32精度、三层安全机制（奖励白化+重要性比值截断+权重回滚）
- 提出容量裕度假设：SLM规模下PPO效果不取决于参数量，而是取决于SFT模型流畅度（PPL<20）+ 有区分度的奖励信号

### 关键结果
在15组（5种SLM模型×3个数据集）配置上验证：满足SFT PPL<20的配置中，PPO对齐后偏好胜率比SFT基线最高提升9.9pct，效果超过SmolLM2-Instruct、Qwen2.5-0.5B-Instruct等通用指令微调基线，训练数据量仅为后者的万分之一级别。

### 最值得记住的一句话
70-500M参数SLM做PPO对齐的前提是SFT模型PPL<20，否则投入资源优化PPO不如先提升SFT质量。
