---
title: Multiscale Policy Optimization for Long-Horizon LLM Agents
title_zh: 面向长时序LLM Agent的多尺度策略优化算法MPO
authors:
- Tao Ren
- Hui Yang
- Jia Deng
- Tingyang Chen
- Qiyao Wang
- Shuo Tang
- Ziyang Zeng
- Yuhua Jiang
- Guanghao Li
- Huatong Song
affiliations:
- Peking University
- IQuest Research
- Tsinghua University
- Renmin University of China
- The University of Hong Kong
arxiv_id: '2610.35013'
url: https://arxiv.org/abs/2610.35013
pdf_url: https://arxiv.org/pdf/2610.35013
published: '2026-10-25'
collected: '2026-10-28'
category: Agent
direction: 长时序LLM Agent RL策略优化
tags:
- LLM Agent
- Reinforcement Learning
- Policy Optimization
- Credit Assignment
- Long Horizon
one_liner: 提出结合轮次级信用传播与token级精细分配的多尺度策略优化MPO，在多类Agent任务上全面超越现有RL基线
practical_value: '- 电商导购Agent、多轮搜索交互Agent的RL训练，可复用MPO多尺度信用分配逻辑：先按交互轮次分配总信用，再在单轮生成token内做均值保留的精细调权，解决长交互序列信用分配模糊问题

  - 现有GRPO/PPO训练多轮Agent效果不佳的场景，可直接替换为MPO算法，无需额外标注数据，仅需调整轮次GAE系数λ、单轮token级GAE系数λ_intra两个超参即可获得稳定收益

  - 多轮交互Agent的RL更新可复用轮次级重要性采样的stop-gradient trick：前向用完整轮次概率比做clip，反向梯度仅回传给当前token，既保证更新稳定性又保留token级梯度信号'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent RL方法存在明显尺度适配缺陷：序列级方法（如GRPO）为整个生成序列分配单一优势，无法区分不同交互轮次、不同token的贡献差异；纯token级方法（如PPO）忽略「轮次是Agent与环境交互的最小单元」的结构特性，长时序场景下信用分配偏差大、训练不稳定。实际观测发现，critic值约89.5%的方差来自轮次间差异，轮次内值波动极小，存在天然的多尺度结构可利用。

### 方法关键点
- 多尺度优势估计（MAE）：先做轮次级GAE跨轮次传播全局信用，再计算单轮内token级局部优势，通过均值约束的投影将局部优势对齐到轮次总优势，既保证全局信用一致性又区分token级贡献
- 轮次级重要性采样：前向计算完整轮次的概率比用于clip，反向通过stop-gradient操作仅让当前token的梯度回传，避免token级重要性采样带来的额外分布偏移损失
- 超参默认配置：轮次GAE系数λ=0.8，单轮token级GAE系数λ_intra=0.95，局部调整强度β=1.0，适配绝大多数多轮Agent场景

### 关键结果
在搜索、工具使用、自动化三类Agent任务上分别测试4B、30B参数模型，对比GRPO、GSPO、PPO、VAPO、SAO等主流RL基线，所有9项评测指标均为最优：4B模型下BrowseComp-Plus搜索任务pass@1达48.08%，比最强基线高4.33个百分点；30B模型下GAIA任务pass@1达43.42%，比最强基线高3.8个百分点。

最值得记住的一句话：多轮LLM Agent的RL优化要适配「轮次是环境交互最小单元、token是生成最小单元」的双层结构，分开处理两个尺度的信用分配和更新约束，收益远高于单纯的单尺度优化。
