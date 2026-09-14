---
title: 'Embodied-BenchForge: A Closed-Loop Agentic Workflow for Embodied Benchmark
  Construction'
title_zh: Embodied-BenchForge：用于具身基准构建的闭环智能体工作流
authors:
- Baoyang Jiang
- Fengchun Zhang
- Leyuan Wang
- Haotian Li
- Yida Wang
- Zhe Ji
- Jinshan Lai
- Xi Ren
- Danyang Li
- Zheng Yang
affiliations:
- QiYuan Lab
- University of Electronic Science and Technology of China
- Beijing University of Posts and Telecommunications
- Tsinghua University
- Beihang University
arxiv_id: '2609.13082'
url: https://arxiv.org/abs/2609.13082
pdf_url: https://arxiv.org/pdf/2609.13082
published: '2026-09-11'
collected: '2026-09-14'
category: Agent
direction: 具身AI · 智能体驱动基准自动化构建
tags:
- Embodied AI
- Agent Workflow
- Benchmark Construction
- Closed-loop Verification
- Skill Reuse
one_liner: 提出闭环智能体框架，自动化生成多场景高质量具身AI评测基准
practical_value: '- 可复用闭环工作流架构：前向技能编排合成+反向分阶段验证修复的模式，可直接迁移到电商场景的用户评测数据集、广告创意合规校验、推荐效果AB测用例自动化生成等场景，降低人工标注/校验成本

  - 分类型契约校验机制：针对不同阶段产出物预设结构化/语义/执行类校验规则的设计，可用于推荐系统特征一致性校验、LLM生成商品文案/推荐理由的自动质检，避免错误向下游传导

  - 可复用技能库设计：将原子操作封装为带输入输出类型约束的可复用技能的思路，可用于搭建Agent业务处理流水线，新增场景仅需开发少量场景适配技能，其余通用模块直接复用'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有具身AI基准构建高度依赖人工，自动化方案仅覆盖孤立环节、仅适配固定场景，且无中间产物校验机制，局部缺陷会传导到最终基准，导致评测结果不可靠，亟需端到端、高复用、高可靠的自动化基准构建框架。

### 方法关键点
- 提出闭环基准合成范式：将前向产物合成与反向验证修复深度结合，从用户评测意图输入到基准输出全链路自动化
- 技能编排式产物合成：将构建操作封装为带类型约束的可复用分层技能，自动组合为执行工作流，用产物依赖图记录中间输出及关联关系，支持跨场景技能复用
- 需求引导的验证修复：为每类产物预设专属校验契约，校验失败时基于溯源信息触发局部重跑或上游回滚，仅重建受影响的下游产物，降低无效计算

### 关键实验
- 构建2类评测基准：离线EQA赛道覆盖家用机器人/自动驾驶/机械臂等6个场景，交互式具身赛道包含220个可执行任务
- 基准质量：6个离线基准LLM评审综合得分88.34~90.75，人工标注一致性达0.87，产物合格率93.7%
- 效率：生成1万条离线基准平均耗时86分钟，吞吐量116.3条/分钟，跨场景技能复用率达91.6%；移除验证修复模块后人工质量评分下降23.25分，合格率降至62.4%

### 核心结论
全链路分阶段校验+局部定向修复的模式，比全流程重跑或仅做终态校验的成本更低、产出质量更稳定
