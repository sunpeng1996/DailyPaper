---
title: 'AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents'
title_zh: AgentTune：面向工具调用LLM Agent的统一训练生命周期框架
authors:
- R E Zera Marveen Lyngkhoi
- Abhivansh Gupta
- Vidushee Vats
- Ram Mohan Rao Kadiyala
- Vinay Kumar Sankarapu
- Pratinav Seth
affiliations:
- Lexsi Labs
arxiv_id: '2610.13335'
url: https://arxiv.org/abs/2610.13335
pdf_url: https://arxiv.org/pdf/2610.13335
published: '2026-10-09'
collected: '2026-10-12'
category: Agent
direction: LLM Agent工具调用训练全生命周期框架
tags:
- Agent
- ToolCalling
- RLHF
- KnowledgeDistillation
- RAG
one_liner: 开源统一框架打通Agent构建、训练、评估、蒸馏、自愈全流程，复用统一轨迹表示
practical_value: '- 直接复用双层级EventLog轨迹表示方案，统一Agent调用、训练、评估的轨迹格式，避免各模块重复开发格式转换逻辑，降低电商导购、智能客服等业务Agent的迭代成本

  - 可借鉴segment-aware completion-only loss设计，训练工具调用Agent时给tool call段加2倍权重、环境返回段mask损失，显著提升工具调用格式准确率

  - 业务场景可复用其自修复闭环逻辑：自动识别失败请求→分类根因→生成矫正训练样本→触发增量训练→gated部署，大幅降低人工标注和运维成本

  - 对于需要端侧/本地化部署的轻量Agent，可复用其Agent蒸馏方案：用大模型教师生成的工具调用轨迹蒸馏小模型，mask掉工具返回段损失，专注让小模型学习决策逻辑而非复述检索结果'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM Agent的构建、训练、评估、蒸馏、运维各环节工具碎片化，不同阶段的轨迹表示不统一，导致重复开发格式转换、损失计算、审计逻辑，迭代效率低，缺少统一的全生命周期支撑框架。
### 方法关键点
- 核心采用双层级EventLog轨迹表示：light层级存储轨迹内容（工具调用、返回、奖励），可用于评估、审计；full层级额外存储token span、logprob，可直接导出SFT训练样本
- 统一训练栈：封装GRPO、PPO、DPO等5种RL训练算法，共享轨迹输入，支持工具调用场景的rollout、奖励计算，内置26种常用奖励函数
- 支持YAML定义决策工作流，内置自修复闭环：自动检测Agent失败请求→分类根因→生成矫正训练样本→触发增量训练→评估符合阈值再部署
- 内置Agent蒸馏、agentic RAG能力，所有模块复用同一份轨迹数据，无需二次转换
### 关键结果
- 法律合同搜索场景，CUAD多跳问答数据集上，GRPO训练的Qwen3.5-9B Agent相比基线Exact Match从60.0%提升到69.0%，单问题搜索次数从3.00降到2.90
- 训练好的策略零样本迁移到3个未见过的法律数据集，Doc@8最高提升15pct，搜索次数平均降低10%
- 轨迹蒸馏方案：mask掉工具返回段损失训练小模型，Qwen2.5-0.5B在CUAD上Pass@1比未mask方案高4.8个点，比纯问答微调高9.3个点
### 核心结论
Agent全流程迭代的核心瓶颈往往不是算法效果，而是各模块的碎片化适配成本，用统一的轨迹表示打通全链路是提效的核心。
