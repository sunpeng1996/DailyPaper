---
title: 'τ_0-VLA: a Hierarchical Robot Foundation Model with World-Model-Guided Test-Time
  Computation'
title_zh: τ₀-VLA：带世界模型引导测试时计算的分层机器人基础模型
authors:
- Xiaowei Cai
- Yunuo Cai
- Bingao Chen
- Jingxiao Chen
- Zhi Chen
- Siyuan Feng
- Tengyu Hou
- Jingshun Huang
- Han Jiang
- Runkun Ju
affiliations:
- Shanghai Innovation Institute
- Agibot Finch
- The Chinese University of Hong Kong
arxiv_id: '2608.16885'
url: https://arxiv.org/abs/2608.16885
pdf_url: https://arxiv.org/pdf/2608.16885
published: '2026-08-16'
collected: '2026-08-22'
category: Other
direction: 机器人基础模型 · 世界模型引导推理
tags:
- VLA
- World Model
- Hierarchical Foundation Model
- Test-Time Computation
- Robot Manipulation
one_liner: 提出分层机器人基础模型τ₀-VLA，通过世界模型引导的测试时搜索提升长周期操作任务性能
practical_value: '- 分层决策+测试时动态算力分配的思路，可迁移到电商全链路引导Agent等长路径任务，为高风险决策节点分配额外计算资源提升准确率

  - 「候选提案→世界模型模拟→价值打分→束搜索筛选」的决策框架，可复用在多步跨场景推荐的会话路径规划环节

  - 多来源异质多模态数据联合预训练的范式，可参考用于跨业务域的通用推荐/Agent基座模型训练'
score: 4
source: huggingface-daily
depth: abstract
---

### 动机
长周期机器人操作任务需要同时保障单技能可靠执行、子任务序列连贯，现有分层VLA模型仅通过单次前馈做决策，无法为高难度/高影响决策分配额外计算资源，长路径任务效果受限。
### 方法关键点
1. 分层架构：高层策略负责可扩展计算的子任务推理，低层策略适配多形态机器人执行具体子任务
2. 测试时计算逻辑：高层策略基于执行历史生成候选子任务，结合VLM提案、世界模型模拟结果、价值模型打分做束搜索，筛选最优子任务输出
3. 基于40115小时异质真实世界多模态数据做联合预训练
### 关键结果
域内/分布偏移场景下，增加测试时计算可显著提升子任务预测准确率，长周期闭环操作任务成功率同步提升。
