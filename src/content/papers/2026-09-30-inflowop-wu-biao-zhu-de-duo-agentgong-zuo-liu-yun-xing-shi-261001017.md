---
title: 'Pay for the Fault, Not the Flow: Label-Free In-Flow Multi-Agent Workflow Optimization'
title_zh: INFLOWOP：无标注的多Agent工作流运行时动态优化框架
authors:
- Xuehang Guo
- Haoyu Wang
- Shengyu Chen
- Zach Chen
- Wei Cheng
- Qingyun Wang
- Haifeng Chen
affiliations:
- William & Mary
- NEC Corporation of America
arxiv_id: '2610.01017'
url: https://arxiv.org/abs/2610.01017
pdf_url: https://arxiv.org/pdf/2610.01017
published: '2026-09-30'
collected: '2026-10-02'
category: MultiAgent
direction: 多智体工作流 · 无监督运行时优化
tags:
- Multi-Agent
- Workflow Optimization
- Label-Free
- In-Flow Tuning
- Cost Driven
one_liner: 提出无标注成本驱动的多Agent工作流构建与运行时优化框架 较单Agent基线最高提升11.97%
practical_value: '- 可复用成本驱动的动态任务拆分逻辑：电商多Agent导购/合规审核场景下无需预设拆分模板，按Agent能力匹配度+执行latency动态调整任务粒度，平衡准确率与链路耗时

  - 无监督运行时故障修复方案可直接迁移：推荐全链路（召回→排序→创意生成）执行出错时，仅重跑故障关联节点而非全链路，无需标注即可定位故障，大幅降低容错成本

  - 动态Agent池与画像累积机制可借鉴：现有Agent无法覆盖任务时自动创建专项Agent，仅累积成功执行的Agent画像用于后续匹配，适合电商大促等需求快速变化的场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多Agent工作流普遍提前固定任务拆分粒度与Agent分配规则，执行出错后依赖标注数据定位故障、全链路重跑优化，成本极高；同时现有多Agent基准任务大多可被单Agent独立解决，无法验证多Agent协作的真实收益。
### 方法关键点
- 定义统一无标注成本函数，融合Agent能力匹配度、执行latency、新Agent创建成本三个维度，无需标注即可量化任务与Agent的适配性
- 前置COALESCE模块：先将复杂任务拆分为最小执行原子，再自底向上按成本最优规则合并原子，动态确定任务拆分粒度与Agent分配，无适配Agent时自动创建新专项Agent
- 运行时动态优化：每个子任务绑定输入输出契约，执行时通过契约语义匹配无监督定位故障，优先选择成本最低的修复方式（重分配Agent→重拆分子任务），仅重跑故障关联节点，保留已执行进度
- 发布BRAID基准，覆盖8个领域的复杂任务，所有任务均超出单Agent能力边界，可准确衡量多Agent协作效果
### 关键结果
在BRAID基准上，INFLOWOP跨6种不同大小的LLM backbone，较单Agent基线最高提升11.97%，较固定模板的工作流基线最高提升9.64%；小模型叠加INFLOWOP的效果可超过更大参数的单Agent（如Qwen3.5-4B+INFLOWOP准确率超过Qwen3.5-9B、GPT-5-mini单Agent）。
### 核心结论
多Agent工作流的收益核心不在于拆分任务本身，而在于基于成本的动态拆分与局部优化，仅对故障付费而非对整个流程付费。
