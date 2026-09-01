---
title: 'Hindsight Memory-PRM: Supervising Memory Management with Auditable Hindsight
  Credit'
title_zh: Hindsight Memory-PRM：基于可审计事后信用的Agent内存管理方法
authors:
- Haoxuan Jia
- Yang Liu
- Yingguang Yang
- Yancheng Chen
- Chongyang Zhang
- Hao Zheng
- Qian Li
- Yulin Huang
- Jianshen Zhang
- Yongzhi Qi
affiliations:
- Fullive-AI
- Nanyang Technological University
- JD.com
- Peking University
- University of Chinese Academy of Sciences
arxiv_id: '2608.29605'
url: https://arxiv.org/abs/2608.29605
pdf_url: https://arxiv.org/pdf/2608.29605
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: Agent长时内存管理 · 过程奖励优化
tags:
- Memory Management
- PRM
- LLM Agent
- Long Horizon
- GRPO
- Credit Assignment
one_liner: 通过事后检索/引用记录+可控删除测试训练内存效用PRM，实现长horizon Agent高效内存管理
practical_value: '- 电商客服Agent/用户长时画像构建可复用事后归因逻辑：通过后续检索引用记录+删除测试给记忆写入/合并操作打分，无需人工标注内存操作的好坏，大幅降低标注成本

  - 推荐系统用户行为记忆池迭代可借鉴分层多版本存储设计：保留记忆版本链而非直接覆盖/删除，避免历史行为证据丢失，提升长周期用户兴趣建模准确性

  - 稀疏奖励Agent训练可复用credit分配思路：通过后缀最小化的批评器塑形+权重退火，有效缓解奖励黑客问题，提升训练稳定性，可迁移到导购Agent、搜索Query改写Agent训练'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
长horizon LLM Agent的内存操作（写入/合并/跳过）价值仅在后续检索、回答阶段才能体现，现有方案要么依赖稀疏终局奖励导致信用分配信噪比极低，要么需要重放后续全流程成本极高，无法低成本高效训练内存管理策略。
### 方法关键点
1. 利用内存操作的可审计轨迹：未被任何检索路径命中的记忆直接判定贡献为0，无需额外测试；构造锚定特定记忆的探测问题，通过删除该记忆后回答是否翻转标定其实际效用。
2. 离线训练分操作（写入/合并/NOOP）的内存效用批评器，损失结合效用回归、可检索性分类、跨层级对排序三类任务，提升打分准确性。
3. 在线训练采用GRPO，组合终局任务奖励、干预标定的记忆信用、覆盖率惩罚、退火权重的后缀最小化批评器塑形项作为复合奖励，避免奖励黑客，提升训练稳定性。
4. 采用分层多版本内存存储结构，保留记忆版本链而非执行破坏性删除，避免历史证据丢失。
### 关键结果
- LoCoMo长时对话记忆基准上，8B本地策略准确率达77.5%，比API教师高12.4pp，比Mem0官方k=200配置高2.8pp，仅用其1/8的上下文token。
- LongMemEval基准上准确率达79.0%，比MemBuilder高13pp；样本效率比仅用终局奖励的方案高两个数量级。
### 值得记住的一句话
内存操作的效用完全可以通过下游检索、引用和低成本可控删除测试标定，无需人工标注每一步操作的好坏，也无需重放全流程。
