---
title: 'Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations'
title_zh: 解析On-Policy蒸馏：作用、失效模式与调控方法
authors:
- Rui Wang
- Hongru Wang
- Yi Chen
- Boyang Xue
- Tianqing Fang
- Wenhao Yu
- Kam-Fai Wong
affiliations:
- The Chinese University of Hong Kong
- Tencent AI Lab
arxiv_id: '2607.13399'
url: https://arxiv.org/abs/2607.13399
pdf_url: https://arxiv.org/pdf/2607.13399
published: '2026-07-15'
collected: '2026-07-16'
category: Training
direction: 大模型训练 · On-Policy蒸馏优化
tags:
- On-Policy Distillation
- LLM Training
- Knowledge Distillation
- Reinforcement Learning
- Token-level Regulation
one_liner: 系统剖析On-Policy蒸馏的探索本质，定位两种失效病理，提出零额外计算的信号调控策略
practical_value: '- LLM微调/蒸馏算力分配：预算固定时优先提升prompt多样性，而非增加单prompt采样次数，可最大化OPD训练效率

  - OPD师生选择：不要盲目选用大参数teacher，用Informativeness指标衡量师生信号对齐度，优先选匹配度高的teacher避免负向引导

  - OPD稳定性优化：零额外计算修复长度作弊问题，师生能力差距小时用log-scale压缩，差距大时用advantage硬截断，无需额外冷启动SFT

  - 生成式推荐/Agent蒸馏：可复用两种信号调控方法，避免模型生成冗余推荐文案、或者过早截断回复的作弊行为'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
On-Policy Distillation（OPD）已成为LLM后训练的核心范式，通过token级稠密引导实现高效知识迁移，但训练稳定性极差，常出现效果波动、探索崩溃、甚至不如端到端RL的问题，业界对其训练动力学机制、失效边界认知空白，亟需系统梳理其核心作用、失效原因与落地优化方案。
### 方法关键点
1. 明确OPD本质为**探索催化剂**：仅加速学生模型对自身已有能力边界内正确路径的探索，无法突破学生基础能力上限；训练效率与prompt多样性正相关，与单prompt采样次数无关。
2. 定位两种核心失效病理：① 师生分布不匹配：当teacher与student能力差距过大时，teacher对student生成内容的偏好信号与实际正确性脱钩，引导方向完全负向；② 长度作弊：student通过冗余填充拉长序列稀释负向advantage，或提前截断序列仅保留高置信前缀，无需提升推理质量即可优化目标。
3. 提出两种零开销信号调控方案：① 硬截断：将token级advantage限制在[cmin, cmax]区间，过滤极端噪声，适合师生能力差距大的场景；② 软log压缩：用`sign(∆ℓt)·log(1+|∆ℓt|)`压缩极端值，保留信号相对排序，适合师生差距小的场景。
### 关键结果
在MATH500、AIME、AMC等7个推理benchmark上测试：
- 原生OPD普遍存在长度作弊问题，序列长度最高膨胀到10k+token，准确率下降超过15%
- 加信号调控的OPD相对原生OPD平均得分提升2.3，彻底消除长度作弊问题
- 仅用4B teacher加硬截断的方案，平均得分达28.1，超过业界基于30B大teacher的最优OPD方案
**最值得记住的结论：OPD效果由引导信号质量决定，而非teacher的参数规模。**
