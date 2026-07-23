---
title: 'Beyond Euclidean Clipping: Overcoming Exploration Collapse in LLM RL via Riemannian
  Isometric Policy Optimization'
title_zh: 黎曼等距策略优化RIPO：破解LLM强化学习的探索崩溃问题
authors:
- Zhicheng Cai
- Xinyuan Guo
- Hanlin Wu
- Mingxuan Wang
- Wei-Ying Ma
- Ya-Qin Zhang
- Hao Zhou
affiliations:
- 清华大学AIR
- ByteDance Seed
- 清华AIR与字节跳动SIA联合实验室
arxiv_id: '2607.10169'
url: https://arxiv.org/abs/2607.10169
pdf_url: https://arxiv.org/pdf/2607.10169
published: '2026-07-10'
collected: '2026-07-23'
category: Training
direction: LLM强化学习 · 策略优化
tags:
- RL
- PPO
- LLM Training
- Policy Optimization
- Riemannian Geometry
- Exploration Collapse
one_liner: 提出基于黎曼几何的动态裁剪RL算法RIPO，解决PPO-Clip探索崩溃问题，多任务性能显著领先基线
practical_value: '- 做LLM-based Agent的强化学习微调时，可替换原有PPO-Clip/GRPO-Clip为RIPO的动态裁剪机制，低概率探索动作会获得更大更新幅度，缓解策略过早收敛到次优解的问题，尤其适合多步决策、搜索规划类Agent任务。

  - 电商/推荐场景中做RL-based排序优化、动态出价、个性化文案生成等任务时，可借鉴RIPO的几何匹配思路，基于策略分布动态调整更新步长，平衡探索（小众需求/商品）和利用（热门需求/商品），避免探索崩溃导致的多样性下降。

  - 工程实现成本极低，仅需在原有PPO/GRPO的裁剪逻辑中，将固定ε替换为ε = sqrt(δ / π_old(a|s))，δ为可调整的全局信任域半径，无需额外模型开销，可快速集成到现有RL训练管线中。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM RL主流框架基于PPO-Clip，存在严重的探索崩溃问题：策略会快速收敛到窄范围的高概率动作，低概率但高价值的动作无法得到有效更新，导致长序列推理、多步决策类任务性能瓶颈；之前的优化方案多为启发式调整裁剪阈值，没有解决本质问题。

### 方法关键点
- 从理论层面指出PPO-Clip的核心缺陷：使用欧氏距离度量策略差异，与KL散度诱导的策略黎曼流形的固有几何结构不匹配，导致低概率区域更新过保守、高概率区域更新过激进，最终引发探索崩溃。
- 提出黎曼等距裁剪（RIC）机制：根据每个动作的历史概率π_old动态调整裁剪阈值，公式为|r(θ)-1| ≤ sqrt(δ/π_old(a|s))，保证每个动作的更新在黎曼流形上消耗相等的信任域预算，低概率动作允许更大更新幅度，高概率动作的更新被适当约束。
- 基于RIC构建RIPO算法，复用GRPO的组相对优势估计、token级损失聚合逻辑，训练稳定性更好，同时实现更优的偏差-方差权衡。

### 关键实验结果
在7个竞赛级数学推理基准、4个不同规模LLM上，RIPO相对GRPO最高获得37.2%的平均性能提升，AIME24数据集上相对GRPO最高提升60%；在编码、多跳搜索任务上相对GRPO分别提升13.2%、15.1%；训练效率是GRPO的5倍，梯度无明显振荡，策略熵稳定在合理区间，无探索崩溃问题。

> 最值得记住的一句话：对策略差异的度量必须匹配其内在几何结构，才能从根本上平衡探索与利用，避免启发式调整的局限性。
