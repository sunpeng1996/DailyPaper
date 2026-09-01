---
title: 'S3Gym: Can LLMs Turn Self-Testing and Self-Judging into Self-Improvement?'
title_zh: S3Gym：大语言模型自测试自判断驱动自改进能力评估基准
authors:
- Jiajun Shi
- Siyuan Tao
- Yuhao Wu
- Zexuan Wang
- Jingyuan Zhang
- Jiaheng Liu
- Xinping Lei
- Xinrong Zhang
- Siyuan Fang
- Zhewen Tan
affiliations:
- ByteDance Seed
- M-A-P
- TokenWave.AI
arxiv_id: '2608.31100'
url: https://arxiv.org/abs/2608.31100
pdf_url: https://arxiv.org/pdf/2608.31100
published: '2026-08-31'
collected: '2026-09-01'
category: Agent
direction: Agent 自进化能力评估基准框架
tags:
- LLM Agent
- Self-Improvement
- Benchmark
- In-Context Learning
- SFT
one_liner: 提出LLM自改进能力统一评估基准S3Gym，对比三类经验复用路径的效果差异
practical_value: '- 做Agent自迭代时根据任务特性选经验复用路径：规则明确的场景用Summary Memory节省上下文，强依赖状态细节的场景直接用History
  ICL

  - 自改进流程中不能完全依赖LLM自判断：自判断和环境真实奖励的一致性最高仅88%，低一致性场景需引入人工或系统校验信号过滤训练/记忆样本

  - 用SFT做Agent自迭代时需做负迁移校验：本次实验中PvZ场景训练后性能下降74%，建议保留历史模型快照回滚机制

  - 推荐系统用户行为反馈归因可参考本结论：仅识别正负反馈不够，需将反馈转化为可执行的召回/排序规则才能实现效果提升'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有Agent基准仅评估固定策略下的任务完成能力，无法衡量LLM能否通过交互经验主动迭代提升，且不同经验复用路径的效果缺乏统一的对比框架，自判断可靠性对自改进的影响也尚未明确。

### 方法关键点
- 设计S3Gym评估框架，拆分宽松配置的探索阶段与严格留资配置的评估阶段，解耦Agent自判断信号与环境真实校验信号
- 覆盖7类文本游戏场景，包含潜规则归纳、空间规划、多智能体策略等不同任务类型，要求Agent提取可迁移知识而非记忆孤立动作
- 对比3种经验复用路径：直接拼接历史轨迹的History ICL、压缩为可复用规则的Summary Memory、参数微调的SFT训练
- 采用平均得分Avg、最高得分Max、超过初始基线的正面积AUC+三类核心评估指标

### 关键结果
- 测评7款主流LLM，结果显示Summary Memory仅在规则可抽象场景生效：Gemini-2.5-Flash的PvZ场景AUC+从24.4提升到238.5，但依赖状态细节的场景效果最高下降98%
- SFT训练稳定性极差：仅在多智能体Trust Evolution场景稳定提升300%，PvZ场景出现严重负迁移，性能从23下降到6
- LLM自判断和真实奖励的二进制一致性最高仅88%，校准误差最高达0.88，且自判断准确性与后续性能提升几乎无相关性（相关系数-0.01）

### 核心结论
仅靠收集交互经验和识别正负反馈无法保证自改进，必须把反馈转化为可执行、可迁移的策略规则才能实现稳定提升。
