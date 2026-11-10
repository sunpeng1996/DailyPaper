---
title: 'BRAT: Bounded Residual-Aligned Training for Stable Multi-Pass LLM Post-Training'
title_zh: BRAT：面向稳定多轮LLM后训练的有界残差对齐训练方法
authors:
- Xunlan Zhou
- Yuzhe Zhao
- Xuhong Huang
- Feng Chen
- Xuanlin Chen
- Lang Feng
- Bo An
affiliations:
- Nanjing University
- Shanghai Jiao Tong University
- The University of Hong Kong
- Nanyang Technological University
arxiv_id: '2611.10873'
url: https://arxiv.org/abs/2611.10873
pdf_url: https://arxiv.org/pdf/2611.10873
published: '2026-11-07'
collected: '2026-11-10'
category: Training
direction: LLM后训练 · RLHF 多轮rollout复用优化
tags:
- RLHF
- LLM Post-Training
- Multi-Pass Rollout
- Training Stability
- Policy Optimization
one_liner: 提出带SymMax组归一化与方向饱和token损失的BRAT算法，解决多轮rollout复用的LLM后训练不稳定问题
practical_value: '- 做LLM生成式推荐/Agent的RLHF微调时，可直接复用BRAT的SymMax组归一化，替代GRPO的标准差归一化，避免饱和prompt的奖励放大问题，无需额外超参

  - 多轮rollout复用的训练场景下，用方向饱和（DS）token损失替代PPO硬截断，梯度更平滑，减少训练崩溃，还能提升相同训练步数下的效果稳定性

  - 低资源RLHF场景下，BRAT支持4次rollout复用不崩，能减少生成采样的算力开销，适合业务侧小成本微调垂域LLM'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM后训练的RL类流程为摊薄生成rollout的算力成本，通常将同一批采样的rollout复用多次做梯度更新，但现有方法存在明显缺陷：无截断更新会导致策略漂移崩溃，加负基线的方法会强化所有采样响应，PPO类硬截断会突然切断梯度。核心原因是小批量rollout上拟合的更新方向过拟合，跨到同prompt的未采样rollout时方向对齐度下降近9倍，多轮复用后漂移问题被放大。

### 方法关键点
- SymMax组归一化：每个prompt组的中心化奖励除以`max(ˆp, 1−ˆp)`，组内权重和为0、范围严格限制在[-1,1]，无额外超参，平衡组和近饱和组的奖励权重更合理
- 方向饱和（DS）token损失：每个token的梯度权重随概率比线性衰减，到信任域边界时降为0，梯度全局平滑，避免硬截断的跳变，也不会出现梯度反向
- 两者结合为BRAT算法，约束每步的策略漂移范围，天然适配多轮rollout复用场景

### 关键结果
在Qwen3-8B上用LoRA微调数学推理任务，设置4次rollout复用，对比GRPO、Dr.GRPO、AsymRE基线，6个推理基准上Macro-Avg准确率达40.87%，比次优的AsymRE高1.94个百分点，跨种子标准差比AsymRE低75%，多轮复用下无训练崩溃，Pass@16指标不会随训练迭代下降。

> 最值得记住的一句话：多轮rollout复用的核心瓶颈是更新方向的样本过拟合，用有界平滑的梯度约束比硬截断或无约束更新的鲁棒性和效果都更好
