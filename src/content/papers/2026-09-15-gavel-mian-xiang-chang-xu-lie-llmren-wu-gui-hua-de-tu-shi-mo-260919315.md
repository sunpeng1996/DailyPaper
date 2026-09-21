---
title: 'GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task
  Planning'
title_zh: GAVEL：面向长序列LLM任务规划的图世界模型校验框架
authors:
- Ruiyang Wang
- Hao-Lun Hsu
- Swarajh Mehta
- Jiwoo Kim
- Zhihao Dou
- Miroslav Pajic
arxiv_id: '2609.19315'
url: https://arxiv.org/abs/2609.19315
pdf_url: https://arxiv.org/pdf/2609.19315
published: '2026-09-15'
collected: '2026-09-21'
category: Agent
direction: 具身Agent长序列规划优化
tags:
- LLM Planning
- Graph World Model
- Embodied Agent
- Long-Horizon Planning
- Partial Observability
one_liner: 结合显式图世界模型校验修复LLM长序列规划，仅语义错误触发LLM重规划，提升成功率与效率
practical_value: '- 规划类Agent可参考分层修复逻辑：规则可推导的错误（如前置条件不满足）直接用符号模型修复，仅语义级错误调用LLM重规划，大幅降低LLM调用成本与延迟，可复用在电商导购Agent、多任务调度Agent场景

  - 多任务排序可借鉴概率分布驱动的动态调度逻辑：基于实体位置/状态的概率分布预估各任务执行成本，每完成一个任务就更新概率重排剩余任务，可迁移到多目标推荐的任务调度、电商履约链路的动态排程场景

  - 小参数LLM落地可参考「小模型生成+符号模型校验修复」架构，用低算力成本达成接近大模型的执行效果，适合端侧Agent、边缘部署的推荐调度系统'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM作为长序列任务规划器时，生成的方案常违反实体约束、出错后难以恢复、部分可观测场景下推理效率低下；纯LLM反馈式重规划调用成本高且易引入新错误，纯符号规划又无法处理复杂语义目标，亟需兼顾语义理解能力与执行可靠性的规划框架。
### 方法关键点
- 构建显式图世界模型，存储实体关系、动作前置条件与效果、未观测实体的位置概率分布，可预演LLM生成的动作序列执行结果，校验约束满足情况
- 分层错误修复机制：规则可推导的错误（如抓取前未导航、容器未打开）直接用动作语义自动修复，仅语义级错误回退LLM重规划，严格控制LLM调用次数
- 多任务动态调度：基于未观测实体的位置概率分布预估各任务预期搜索/导航成本，每完成一个任务就用新观测更新概率，重排剩余任务顺序最小化总执行成本
- 用轻量LoRA微调小参数LLM做任务理解模块，提取任务实体、关系与目标状态，初始化图世界模型
### 关键结果
在BEHAVIOR-1K基准上测试，覆盖100个单长序列任务、500个多任务指令：
1. 单任务场景：Qwen3-8B搭配GAVEL，成功率从纯LLM的41.2%提升至91.8%，平均仅需1.5次LLM调用；Qwen3-4B搭配GAVEL成功率达88.8%，远超纯反馈式重规划的55.4%
2. 多任务场景：Qwen3-8B搭配GAVEL，成功率从纯LLM的19.9%提升至92.6%，概率驱动的动态排序相比静态方案降低约5.4%的移动距离
3. 大模型兼容：GPT-5.6 Sol、Claude Sonnet 5搭配GAVEL后，成功率分别从24.6%、38.6%提升至99.2%、99.4%，增益与小模型一致
### 核心结论
LLM的语义规划能力与显式符号世界模型的校验修复能力是互补而非替代关系，两者结合可用极低额外成本大幅提升长序列规划的可靠性与效率
