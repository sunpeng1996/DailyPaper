---
title: SHAPE of Chain-of-Thought in Math Reasoning
title_zh: 面向数学推理思维链的语义空间与启发式分析框架SHAPE
authors:
- Jonghyun Song
- Sangjun Song
- Minjae Oh
- Haesung Pyun
- Sungsik Lee
- Yohan Jo
affiliations:
- Seoul National University
arxiv_id: '2608.28600'
url: https://arxiv.org/abs/2608.28600
pdf_url: https://arxiv.org/pdf/2608.28600
published: '2026-06-27'
collected: '2026-09-01'
category: Reasoning
direction: LLM 数学推理 · CoT 过程分析
tags:
- Chain-of-Thought
- Mathematical Reasoning
- Heuristic Analysis
- Semantic Space
- Reinforcement Learning
one_liner: 提出基于数学教育理论的CoT分析框架SHAPE，可诊断推理模式并指导RL训练提升性能
practical_value: '- 做Agent推理链路优化时，可借鉴SHAPE的「语义空间+启发式动作」双维度建模，拆解用户查询理解、商品推荐决策路径，提取的特征比路径长度、自修正标记等表层特征预测决策有效性的准确率更高

  - RL训练（如电商导购Agent、搜索Query改写的RL优化）时，可参考启发式增强GRPO的思路，在rollout阶段注入领域启发式规则（如电商价格敏感度、库存约束），无需改动奖励函数和模型结构即可获得明显效果提升

  - 做复杂任务的CoT质量评估时，可复用这套自动化标注Pipeline：先拆分内容单元，再打动作标签，最后跟踪语义空间切换，比纯人工标注效率高，可支撑大规模评测'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有CoT分析大多停留在路径长度、自修正词汇、分阶段标签等表层特征，无法捕捉LLM推理背后的语义理解逻辑和策略选择规律，也难以解释RL后训练提升精度的底层机制、以及泛化性下降的原因，亟需具备理论支撑的过程级分析框架。

### 方法关键点
- 框架从数学教育理论引入两个核心分析维度：语义空间（模型对问题的理解视角，如代数求解/枚举试错）、启发式（具体解题动作，如设变量/试特例/反向推导）
- 自动化Pipeline分三步：先将CoT拆分为独立语义内容单元，再用大模型给每个单元打多标签的启发式/非启发式标签，最后跟踪语义空间的切换状态（维持/新建/返回已有空间）
- 设计3个核心度量：有效语义空间数$N_{eff}^{space}$、有效切换次数$N_{eff}^{trans}$、切换密度$\rho$，量化推理过程的专注度与跳转特征

### 关键结果
- 正确性预测任务上，SHAPE的启发式特征AUROC达0.664，显著优于CoT长度（0.504）、自修正特征（0.618）、ThinkARM（0.618）等基线
- 正确推理轨迹的有效语义空间数比错误轨迹平均低10%以上，说明正确推理通常聚焦在少数语义空间，而非频繁跳转
- 启发式增强的GRPO训练在MATH-Perturb难例集上Pass@64比基线Plan-GRPO高0.87个百分点，Avg@64高3.2个百分点

### 核心洞察
RL后训练不会扩展模型的推理策略空间，只会把成功路径收敛到预训练已经覆盖的策略密集区，要提升泛化性需要主动引导启发式多样性
