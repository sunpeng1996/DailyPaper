---
title: 'EliteReplay: Preserving Diverse Solutions in RL Post-Training via Quality-Diversity
  Search'
title_zh: EliteReplay：基于质量多样性搜索的RL后训练多解保留方法
authors:
- Hanane Nour Moussa
- Doeun Lee
- Sachin Kumar
affiliations:
- The Ohio State University
arxiv_id: '2610.22290'
url: https://arxiv.org/abs/2610.22290
pdf_url: https://arxiv.org/pdf/2610.22290
published: '2026-10-15'
collected: '2026-10-17'
category: Training
direction: LLM RL后训练 · 多样性保留
tags:
- GRPO
- Quality Diversity
- Reinforcement Learning
- Post-training
- Solution Diversity
one_liner: 结合GRPO与质量多样性精英存档，RL后训提精度同时保留基模型多样解
practical_value: '- 做Agent多路径推理（如用户模糊query多意图解析、SQL生成工具）时，可复用精英存档+GRPO混合损失架构，避免RL后训导致的解坍塌，提升模糊场景覆盖率

  - 电商搜索/推荐的多结果多样性优化场景，可借鉴基于策略结构的U@k、有效多样性指标，代替单纯的召回率/准确率，更准确衡量策略多样性

  - 做RLHF/RLVR微调大模型时，可复用质量多样性搜索构建精英存档的方法，替代随机采样回放集，保留更多稀有正确策略同时缓解跨域遗忘'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前基于GRPO等RLVR的LLM后训练方法虽能大幅提升单点精度（pass@1），但会触发「行为锐化」效应：模型输出概率集中到少数基模型已有策略上，高pass@k背后实际正确解的策略多样性大幅下降，无法满足模糊query解析、多路径推理等需要多样解的业务场景，现有优化方法仅以pass@k为目标，无法区分解的实际结构差异。

### 方法关键点
- 离线构建精英存档：用冻结基模型跑MAP-Elites质量多样性搜索，先由独立Labeler生成策略标签库，结合SQL AST结构特征划分行为单元格，每个单元格保留1个最优验证解，覆盖尽可能多的正确策略
- 混合损失训练：总损失为(1-μ)GRPO损失 + μ精英回放损失，回放损失为存档解的负对数似然，按解长度归一化避免长解权重过高，μ固定为0.05
- 新增多样性评估指标：提出U@k（k次采样内的唯一正确策略数）、有效多样性、策略保留率三个指标，弥补pass@k无法衡量解结构差异的缺陷

### 关键实验
在文本-to-SQL场景测试，数据集为BIRD（分布内）、Spider（分布外）、AmbiQT（模糊query），对比GRPO、SetPO、DPH-F、MaxRL四个基线：
- Spider数据集pass@128达93.2%，超最强基线6.3pp，独特正确策略数比基线高77%
- BIRD数据集保留62%基模型正确策略，比所有基线至少高23pp
- AmbiQT模糊数据集Both@128达27%，是最强基线的1.9倍，双意图覆盖能力接近翻倍

RL后训不需要为了单点准确率牺牲解多样性，通过质量多样性搜索构建的精英存档做回放，就能同时实现精度提升与多策略保留
