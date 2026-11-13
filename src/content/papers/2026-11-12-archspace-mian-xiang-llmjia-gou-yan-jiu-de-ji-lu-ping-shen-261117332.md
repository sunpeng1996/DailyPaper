---
title: 'ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research'
title_zh: ArchSpace：面向LLM架构研究的记录、评审与复用公共平台
authors:
- Jie Wang
- Tong Zhu
- JiaHao Kuang
- Zhe Xu
- Yunkai Chai
- Dehong Zheng
- Yu Cheng
- Tao Ji
- ZhouHan Lin
- Qi Zhang
affiliations:
- Shanghai AI Laboratory
- Fudan University
- Shanghai Jiao Tong University
- East China Normal University
arxiv_id: '2611.17332'
url: https://arxiv.org/abs/2611.17332
pdf_url: https://arxiv.org/pdf/2611.17332
published: '2026-11-12'
collected: '2026-11-13'
category: LLM
direction: LLM架构研究 · 缩放定律验证
tags:
- LLM-Architecture
- Scaling-Laws
- Open-Research-Platform
- Model-Training
- Baseline
one_liner: 构建带标准化缩放定律验证框架的LLM架构开源协作平台，提供开箱可用基线与训练范式
practical_value: '- 业务侧垂域LLM（如电商导购Agent、商品理解基座）迭代时，可复用两阶段验证框架：先用小算力跑缩放定律预测大模型效果，避免无效的大规模训练投入，降低架构创新验证成本

  - 其LR/BS超参缩放拟合方法可直接复用，针对业务场景的小基座训练，基于基线缩放律初始化搜索空间，可减少超参搜索成本30%以上

  - 150B token预训练+10B token长上下文续训的范式可直接迁移到电商长文本理解、用户长序列行为建模的LLM微调任务，显著提升长窗口任务效果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前工业界LLM架构迭代的成败经验很少公开，学术界受算力限制、基线不统一，小范围实验结论难以放大到大规模场景，导致架构创新验证成本高、优秀学术方案难以落地，亟需统一的公共平台沉淀、验证、复用架构研究成果。
### 方法关键点
- 两阶段标准化验证框架：Phase I跨1e18~1e20 FLOPs共5个算力梯度，通过拟合缩放定律预测架构在大算力下的loss表现，提供3种不同算力成本的验证设置适配不同创新程度的需求
- Phase II固定1B参数量，采用150B token 8K预训练+10B token 64K长上下文续训的范式，验证架构的下游通用能力与长窗口效果
- 提出耦合形式的缩放律公式，相比传统Chinchilla加法形式，拟合误差降低60%以上
- 提供Qwen3.5、OLMo3两套开箱可用的基线模型、预训练配方、标准化评估套件
### 关键结果
基于Dolma 3数据集训练，基线缩放律的拟合MAPE仅0.25%~0.27%，外推到10倍最大训练算力的loss预测MAPE仅0.32%；Qwen3.5经长上下文续训后64K RULER得分从17.5提升到57.0，Base Main得分从27.9提升到46.3，且该训练配方直接复用给OLMo3也能获得同等幅度的效果提升。
最值得记住的一句话：用小算力的缩放定律预测大模型架构效果，是平衡LLM创新验证成本和结论可靠性的核心路径。
