---
title: 'DCAS: Decoupling CLI Agent Scaffolding to Internalize Planning across Scaffolds'
title_zh: DCAS：解耦CLI Agent脚手架实现跨脚手架规划能力内化
authors:
- Kishanthan Thangarajah
- Boyuan Chen
- Ahmed E. Hassan
affiliations:
- Huawei Canada
- Queen's University
arxiv_id: '2608.06113'
url: https://arxiv.org/abs/2608.06113
pdf_url: https://arxiv.org/pdf/2608.06113
published: '2026-08-05'
collected: '2026-08-10'
category: Agent
direction: Agent 跨框架规划能力优化
tags:
- CLI Agent
- Scaffold Decoupling
- Planning
- Supervised Fine-tuning
- Cross-domain Transfer
one_liner: 提出无侵入的CLI Agent脚手架拦截层DCAS，通过规划感知微调实现跨脚手架性能迁移
practical_value: '- 跨业务框架适配可复用DCAS的拦截层思路：做业务Agent时通过API路由层适配不同业务脚手架的协议，无需修改原有成熟框架即可快速替换后端模型，大幅降低适配成本

  - 规划能力拆分的训练方法可复用：将显式任务拆解和隐式行动规范分开训练，比如电商导购Agent对齐新商家后台规则时，先仅用规划阶段小样本微调，比全量轨迹训练效率高1个数量级

  - 小样本迁移trick可复用：仅需数百条规划感知的高质量轨迹即可实现跨环境增益，无需攒数万条全量轨迹，比如推荐Agent换流量调度框架时，仅需少量对齐规划规范的样本微调即可适配'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前开源CLI Agent几乎都在单一脚手架（如OpenHands）上收集轨迹微调，部署到非训练脚手架时性能暴跌，最高降幅达29个百分点，而未微调的基模型无此差异，说明掉点是微调时学习了训练脚手架的特有规划规范导致，而非模型本身能力不足，现有工具不支持跨脚手架评估和规划感知的轨迹收集，跨环境迁移成本极高。

### 方法关键点
- 设计DCAS后端替换拦截层，无侵入路由任意CLI脚手架与后端模型的API流量，无需修改脚手架即可实现跨脚手架评估、规划感知轨迹收集
- 拆分两类规划能力：显式规划（执行前生成的结构化步骤文档）、隐式规划（Agent循环中的步骤拆分粒度、工具调用序列、故障恢复逻辑等隐式规范）
- 构造两类微调数据集：PlanOnly（仅包含规划阶段的交互样本）、Plan+Exec（包含完整的规划+执行全流程轨迹样本）

### 关键实验结果
基于SWE-bench Verified benchmark测试：
1. 固定模型和脚手架，仅替换更高质量的外部规划即可实现最高15%的Pass@1提升，幅度超过观测到的跨脚手架掉点，确认规划是核心影响因素
2. 仅用576条高质量规划感知轨迹微调，PlanOnly组在无显式规划场景下Pass@1提升11个百分点，Plan+Exec组在自规划场景下提升13个百分点，性能逼近外部前沿规划器注入的效果
3. 微调后的模型在从未见过的脚手架上也有稳定增益：新版本Claude Code提升14.4个百分点，OpenCode提升3.4个百分点，mini-swe-agent提升7个百分点，证明学到的是通用规划能力而非脚手架专属记忆

### 最值得记住的一句话
单一场景下的Agent性能跑分存在系统性高估，将规划能力从固定框架依赖转化为模型内化的通用技能，是大幅降低Agent落地适配成本的核心路径。
