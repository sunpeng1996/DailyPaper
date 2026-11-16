---
title: Interpreting Coding Agents Through Their Behavioral Trajectories
title_zh: 基于行为轨迹的代码Agent可解释性分析
authors:
- Ibragim Badertdinov
- Alexander Golubev
affiliations:
- Nebius
arxiv_id: '2611.17440'
url: https://arxiv.org/abs/2611.17440
pdf_url: https://arxiv.org/pdf/2611.17440
published: '2026-11-11'
collected: '2026-11-16'
category: Agent
direction: Agent 行为分析与可解释评估
tags:
- Coding Agent
- Behavioral Analysis
- Execution Trajectory
- Agent Evaluation
- Interpretability
one_liner: 基于14万+代码Agent执行轨迹，量化行为差异并实现跨环境Agent栈识别
practical_value: '- 做Agent系统评估时，可复用「结果匹配配对对比+过程行为指标」的框架，跳出只看最终转化率/成功率的单一评估逻辑，补充工具调用、探索行为等过程维度的诊断能力，定位同性能Agent的成本、鲁棒性差异

  - 异质轨迹归一化的规则parser思路可直接迁移到电商推荐/搜索Agent的日志分析场景，将不同平台、不同框架的异构操作日志映射到统一动作分类体系，实现跨配置、跨场景的策略对比

  - 基于行为特征的Agent栈识别方法可用于推荐系统的异常流量检测、虚假操作识别，也可为不同召回/排序策略构建行为指纹，快速识别上线策略的实际执行是否符合预期'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有代码Agent基准仅评估二元任务成功率，将执行过程视为黑盒，既无法诊断失败根因，也无法区分相同性能的Agent在行为模式上的差异；同时不同Agent框架的执行轨迹格式异构，缺乏统一的语义表示支撑跨系统对比。
### 方法关键点
- 数据集：覆盖125种Agent配置、117个基础模型的143209条完整执行轨迹，包含Python及多语言（Go/Java/Rust/TS）编程任务
- 轨迹归一化：开发规则化parser，将异质原始trace映射到10类高层动作（探索、搜索、读文件、代码修改、测试等），通过6个前沿LLM的5/6共识标签做parser效果审计
- 实验设计：采用结果匹配配对对比（成功率差≤1pp）、跨仓库/跨语言行为特征检索，特征严格排除任务结果、token数、原生工具名
### 关键结果
- Parser对主动作分类的共识准确率达82.4%，读模式准确率达96.6%
- 100%的同性能Agent对在至少2个行为指标上存在显著差异，96.7%在≥3个指标上差异显著，远超同配置分半空测的0.78%假阳率
- 仅用行为特征即可实现跨仓库Agent栈检索Top1准确率85.1%、Top3 96.8%，跨5种语言检索Top1准确率90.3%、Top3 98.8%
> 最值得记住的结论：Agent的最终成功率仅能回答「是否完成任务」，行为轨迹才能回答「如何完成任务」，过程行为是Agent评估不可或缺的补充维度。
