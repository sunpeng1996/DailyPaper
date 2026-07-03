---
title: 'AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents'
title_zh: AgenticSTS：面向长程LLM Agent的受限内存测试平台
authors:
- Xiangchen Cheng
- Yunwei Jiang
- Jianwen Sun
- Zizhen Li
- Chuanhao Li
- Xiangcheng Cao
- Yihao Liu
- Fanrui Zhang
- Li Jin
- Kaipeng Zhang
affiliations:
- Alaya Lab
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
- Nankai University
- University of Science and Technology of China
arxiv_id: '2607.02255'
url: https://arxiv.org/abs/2607.02255
pdf_url: https://arxiv.org/pdf/2607.02255
published: '2026-07-01'
collected: '2026-07-03'
category: Agent
direction: 长程LLM Agent · 受限内存契约测试
tags:
- LLM Agent
- Long-Horizon Agent
- Bounded Memory
- Testbed
- Memory Ablation
one_liner: 基于杀戮尖塔2构建了支持分层可消融受限内存契约的长程LLM Agent测试基准
practical_value: '- 长程Agent内存设计可复用分层类型化契约思路：不拼接全量历史上下文，每次决策从固定的协议/规则/经验/技能分层槽位检索组装prompt，解决上下文膨胀问题，可直接迁移到电商导购Agent、多轮推荐会话等长周期交互场景

  - 分层消融实验方法可直接复用：对Agent的规则库、经验记忆、技能库分别做独立消融，快速定位效果瓶颈，适合业务中Agent性能迭代的归因分析，避免盲目调参

  - 触发式技能库设计可迁移到推荐系统：基于场景触发条件匹配对应策略，相比纯相似性RAG检索，能显著提升长周期决策的一致性，适合大促场景下的运营策略匹配、跨session用户长期兴趣匹配'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长程LLM Agent普遍采用拼接全量历史交互记录的内存方案，存在上下文膨胀、性能归因难、组件无法独立消融的问题，现有长程Agent测试集多默认上下文无界增长，缺少对受限内存方案的标准化评估框架；公开的杀戮尖塔2基准中前沿LLM在最低难度下胜率为0，人类胜率仅16%，任务难且未饱和，适合作为内存方案评估载体。

### 方法关键点
- 受限内存契约核心思路：每次决策不拼接跨轮次原始对话，而是从5个类型化分层槽位（固定协议L1、状态schema L2、游戏规则库L3、episodic记忆L4、触发式技能库L5）检索内容组装新prompt，prompt长度不随决策轮次增长，每层可独立开关消融
- 基于杀戮尖塔2搭建测试平台，该游戏单轮需要数百次长短期决策，规则明确可文本化，随机性强，适合评估长程决策能力
- 配套开源298条带条件标签的完整轨迹、冻结的内存/技能快照、prompt记录与分析脚本

### 关键实验
固定最低难度A0下的消融实验显示，无内存无技能的baseline胜率3/10，新增L5技能层后胜率提升至6/10；相比开源的上下文累加式Agent，该方案胜率提升60%，单分数点token消耗降低7~90倍，支持最高难度A6~A8的测试。跨模型迁移显示技能层对基座敏感，在Gemini上效果最优。

### 核心结论
长程Agent的内存不是存储文本的容器，而是约定每一步决策可见内容的契约，类型化分层的受限内存方案能同时解决上下文膨胀和归因难的问题
