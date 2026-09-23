---
title: REFLEX with Jev for Efficient Selective Control in LLM Agents
title_zh: 基于Jev的REFLEX LLM Agent高效选择性控制架构
authors:
- Tiantong Wu
- Wei Yang Bryan Lim
affiliations:
- Nanyang Technological University
arxiv_id: '2609.26532'
url: https://arxiv.org/abs/2609.26532
pdf_url: https://arxiv.org/pdf/2609.26532
published: '2026-09-22'
collected: '2026-09-23'
category: Agent
direction: Agent 选择性路由与成本优化
tags:
- LLM Agent
- Selective Control
- Cost Optimization
- Model Routing
- Tool Use
one_liner: 基于专用决策模型Jev构建Agent选择性控制架构，大幅减少强LLM调用且保留高任务成功率
practical_value: '- 电商客服/导购Agent可复用分层架构，将固定选项类决策（是否调用物流查询工具、是否转人工等）交给轻量决策模型，仅复杂推理/生成场景调用强LLM，可降低70%左右推理成本

  - 工具选择类路由可直接复用Jev的置信度门控机制，τ=0.5阈值下高置信度工具选择准确率接近100%，无需额外训练路由模型，适合快速落地

  - Agent评估不能只看整体成功率，需单独统计权限类决策的错误类型（不可逆操作/ deferral错误），避免高准确率下出现不可接受的业务损失（比如错误触发用户退款）

  - 若现有路由准确率已超过95%，专用决策层收益有限，直接用小模型自升级级联方案即可，无需引入额外组件增加复杂度'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当前LLM Agent通常每步都调用强LLM做决策，包括大量仅需从固定集合选选项的简单控制步骤，造成算力浪费；现有多LLM路由方案大多按整query分配模型，无法在单Agent轨迹内交替使用不同能力的模型，成本优化空间有限。

### 方法关键点
- REFLEX架构引入Jev专用非生成式决策层，负责输出固定选项类决策（工具选择、是否继续执行等）及对应置信度
- 置信度≥阈值且决策可直接执行时直接调用对应工具/执行操作，低置信度或需要自由生成的场景fallback到强LLM
- 拆分Agent三类计算：控制（固定选项选择）、参数生成、开放推理，仅将前两类可确定性处理的步骤下沉到轻量层
- 用强模型调用减少率（GMR）、风险-覆盖率曲线作为核心评估指标，避免因提前失败带来的虚假成本下降

### 关键实验
自定义100任务REFLEX-Sim基准测试，对比强LLM-only、小模型-only、小模型自升级级联三个基线，τ=0.5时任务成功率达95%，较强LLM-only减少72.7%强模型调用；跨Qwen3.8-Max、Kimi K3、DeepSeek-V4-Pro三个强LLM测试，GMR稳定在66%~72%，成功率波动不超过2个百分点；外部BFCL基准测试显示，工具选择准确率达98.4%，但是否需要调用工具的权限类决策准确率仅52%，是主要瓶颈；τ2多轮基准测试中，REFLEX成本较基线降3.7倍，但和小模型自升级级联方案效果相当。

### 核心结论
专用决策层的收益核心取决于任务中是否存在大量可拆分的固定选项类控制步骤，当现有路由准确率已经很高时，复杂架构的收益会被简单级联方案抹平。
