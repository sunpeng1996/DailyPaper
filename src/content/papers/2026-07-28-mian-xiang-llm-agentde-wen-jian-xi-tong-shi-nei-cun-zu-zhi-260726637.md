---
title: 'Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability'
title_zh: 面向LLM Agent的文件系统式内存：组织、演化与可持续性研究
authors:
- Sizhe Zhou
- Sheldon Yu
- Hui Wei
- Junda Wu
- Siru Ouyang
- Yizhu Jiao
- Shijia Pan
- Julian McAuley
- Yu Zhang
- Tong Yu
affiliations:
- University of Illinois Urbana-Champaign
- University of California, San Diego
- University of California, Merced
- Adobe Research
- Texas A&M University
arxiv_id: '2607.26637'
url: https://arxiv.org/abs/2607.26637
pdf_url: https://arxiv.org/pdf/2607.26637
published: '2026-07-28'
collected: '2026-07-31'
category: Agent
direction: Agent 长时内存架构与性能优化
tags:
- LLM Agent
- Long-term Memory
- Filesystem Memory
- Memory Management
- Agent Architecture
one_liner: 首次系统探索LLM Agent文件系统内存的设计空间，量化组织策略、模型能力、工具集的影响
practical_value: '- 电商智能客服/导购Agent的长时用户记忆可复用分层组织方案：用文件夹/Markdown标题嵌套分类用户偏好、历史订单、咨询记录，大内容量场景下检索成本可降低约50%，且结构可解释、易排查

  - 针对不同能力的下游任务执行Agent匹配对应存储策略：弱能力Agent用蒸馏后的结构化技能/规则记忆，强能力Agent直接用原始会话/轨迹日志，平衡任务成功率和部署成本

  - 做Agent内存管理时需添加显式的关键信息保留规则，避免LLM自主整理时丢失用户特殊偏好、强约束等核心信息，防止业务错误

  - 调整内存操作工具集（如操作粒度、是否叠加BM25检索）对内存结构的优化效果不亚于更换大模型，可作为低成本调优杠杆'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前落地的LLM Agent普遍采用文件系统存储长时记忆，但行业默认「Agent可自主维护持续增长的记忆、且结构化组织一定有收益」两个假设从未被系统验证，记忆膨胀、冲突、过期等问题没有可落地的优化框架。

### 方法关键点
- 将文件系统内存拆解为三类角色：管理Agent负责整合输入内容、维护目录结构；搜索Agent负责遍历存储输出带引用的回答；执行Agent负责生成任务轨迹、消费检索到的技能，统一存储同时支撑陈述性记忆和程序性记忆
- 控制变量覆盖4个维度：内存结构（Agent自主组织层级、原始内容dump、分块检索）、输入流规模、操作工具集（沙箱shell、内存专用工具、检索工具）、管理/搜索Agent的模型能力
- 同时在长会话问答、具身任务两个场景开展对比实验

### 关键结果数字
- 结构化组织的内存相比原始verbatim dump，在大内容量场景下检索成本降低约50%，但无任何一种内存结构在所有场景下准确率最优
- 管理Agent的能力仅影响内存组织样式，对最终回答质量影响在7个百分点以内，而搜索Agent能力提升可将回答准确率从62%提升至79%
- 下游消费Agent能力决定最优存储策略：强执行Agent用原始任务日志成功率最高（87.1%），弱执行Agent用蒸馏后的结构化引导成功率最高（76.4%，比原始日志高10个百分点）
- 工具集调整对内存结构的影响幅度与更换模型相当，是可落地的低成本优化杠杆

**最值得记住的一句话**：Agent文件系统内存的组织收益高度条件化，不存在通用最优结构，需根据内容规模、消费模型能力、成本约束选择方案，不要盲目搭建复杂的自主内存整理流程
