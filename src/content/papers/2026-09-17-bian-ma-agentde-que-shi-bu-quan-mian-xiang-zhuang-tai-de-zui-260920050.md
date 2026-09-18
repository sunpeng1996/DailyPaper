---
title: 'The Missing Complement: State-Conditioned Minimal Sufficient Evidence for
  Coding Agents'
title_zh: 编码Agent的缺失补全：面向状态的最小充分证据获取
authors:
- Zhexi Feng
- Ruiyi Zhang
- Yongbo Yang
- Pengtao Xie
arxiv_id: '2609.20050'
url: https://arxiv.org/abs/2609.20050
pdf_url: https://arxiv.org/pdf/2609.20050
published: '2026-09-17'
collected: '2026-09-18'
category: Agent
direction: Agent 检索增强证据补全优化
tags:
- Coding Agent
- Retrieval Augmentation
- Sufficient Evidence
- Set Construction
- Agent Memory
one_liner: 提出面向编码Agent状态的最小充分证据补全方法MSS-Complement，性能优于传统重排检索方案
practical_value: '- 做Agent检索增强时，放弃单段落相似度排序的单一逻辑，新增集合级充分性校验，避免召回重复冗余信息，大幅压缩上下文长度

  - 可复用三步语义调用流程：生成候选充分证据集→校验缺失信息→返回紧凑证据单元，适配电商客服Agent、工单处理等场景的上下文压缩需求

  - 做Agent记忆召回评估时，可借鉴SERBench思路，以决策所需的完整事实覆盖度为核心指标，替代单条召回相关性指标'
score: 8
source: arxiv-cs.IR
depth: abstract
---

### 动机
现有Agent检索依赖单段落相关性排序，易召回大量重复信息，无法覆盖当前决策所需全部缺失事实，导致决策支撑不足。

### 方法关键点
1. 定义状态条件下的最小充分证据恢复任务，目标是从已捕获的Agent状态中提取紧凑证据组合，覆盖下一步决策缺失的所有支撑事实
2. 提出MSS-Complement方法，将证据获取视为集合构造而非排序任务，通过三次语义调用完成：先生成联合充分候选集、再检索缺失信息、最终返回4-8个完整源单元，总token控制在6144以内

### 关键结果
SERBench上，5个召回项时完整事实覆盖率73.0%，8个时达80.6%，比Qwen3嵌入+重排基线分别高11.6/8.2个百分点；AMA-Bench上，回答prompt体积小76.2%，准确率比基准记忆Agent高2.08个点；移除一个必要事实组会导致修复定位精度下降11~12个点
