---
title: Groupwise Agentic Grading and Advantage Redistribution for Code Agent RL
title_zh: 面向代码智能体强化学习的分组智能评分与优势重分配框架
authors:
- Jinhao Dong
- Liang Zhao
- Zihao Yue
- Wenhan Ma
- Linghao Zhang
- Lei Li
- Shicheng Li
- Yifan Song
- Bowen Ye
- Fuli Luo
affiliations:
- Xiaomi LLM Core
- Renmin University of China
- Peking University
- University of Hong Kong
arxiv_id: '2609.32577'
url: https://arxiv.org/abs/2609.32577
pdf_url: https://arxiv.org/pdf/2609.32577
published: '2026-09-25'
collected: '2026-09-29'
category: Agent
direction: Agent 强化学习信用分配优化
tags:
- RL
- Code Agent
- GRPO
- Reward Shaping
- Credit Assignment
one_liner: 提出Gagar框架，通过分组智能评分重分配RL优势，提升代码Agent性能与训练稳定性
practical_value: '- 做导购Agent、文案生成Agent等业务场景的RL训练时，可放弃单一二元奖励，采用同任务组内多轨迹对比+Agent-as-a-Judge的方式，按业务质量维度（如转化率、合规性、简洁度）给成功轨迹分档加权，避免模型学到低质量可行方案

  - GRPO类分组RL训练中，对成功轨迹做质量降权后必须做总和保留的优势重分配，不能直接降权，否则会导致正负优势失衡、训练不稳定、轨迹长度爆炸，该trick可直接复用在推荐多目标RL、生成式推荐RLHF等场景

  - 多候选质量评估优先用同任务组内对比的方式，比单独打分准确率更高、标注成本更低，可迁移到推荐系统多候选排序、AIGC内容质量校验场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
GRPO等分组RL算法在代码Agent训练中仅给测试通过的轨迹分配相同优势，忽略不同通过方案在实现质量、任务契合度上的差异，会导致模型学到冗余、副作用大的劣等方案，出现后期训练不稳定、轨迹长度爆炸等问题，亟需更细粒度的信用分配机制。

### 方法关键点
1. 提出Gagar框架，仅保留同时包含成功、失败轨迹的分组，让SFT训练的智能评分Agent在同一工作区内对比所有轨迹，可调用工具查询代码、执行校验，从方案适配性、实现精度、改动最小化、无副作用、代码一致性5个维度给通过轨迹分档排序，映射为0.2~1的质量权重
2. 采用总和保留的优势重分配：先按质量权重降权通过轨迹的优势，再统一缩放将所有通过轨迹的优势总和恢复到原值，失败轨迹的优势保持不变，避免正负优势失衡导致的训练不稳定
3. 支持异步评分、边界截断等工程优化，可无缝集成到现有工业级RL流水线

### 关键结果
在310B参数MiMo-V2.6-Flash代码Agent上测试，DeepSWE v1.1 pass rate比二元奖励基线高12.1个百分点，轨迹交互轮数降15.6%、token用量降9.9%，训练稳定性显著提升；1.02T参数Pro版本经过混合任务RL后DeepSWE avg@3达71.9%，超过Kimi K3，接近GPT-5.6 Sol。

**最值得记住的一句话**：分组RL中对成功轨迹的质量加权必须配合优势总和保留机制，否则会打破正负信用平衡，反而导致训练崩溃。
