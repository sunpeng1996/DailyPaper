---
title: Are Frontier VLM Agents Ready to Be Robot Generalists? An Empirical Study with
  the Embodied Agent Arena
title_zh: 前沿VLM智能体能否成为通用机器人？基于具身智能体竞技场的实证研究
authors:
- Haojian Huang
- Pukun Zhao
- Zexi Li
- Yehang Zhang
- Yangkai Wei
- Wenqian Li
- Han Yang
- Kaiwen Zhou
- Ying-Cong Chen
- Yinchuan Li
affiliations:
- HKUST (GZ)
- The Chinese University of Hong Kong
- Knowin AI
arxiv_id: '2610.00854'
url: https://arxiv.org/abs/2610.00854
pdf_url: https://arxiv.org/pdf/2610.00854
published: '2026-10-22'
collected: '2026-11-04'
category: Agent
direction: 具身Agent · VLM通用机器人能力测评
tags:
- VLM
- Embodied Agent
- Robot Generalist
- Benchmark
- Evaluation
one_liner: 构建覆盖5大能力域的具身评估基准Embodied Agent Arena，测评10款VLM的通用机器人适配能力
practical_value: '- 可复用多维度Agent评估思路：将能力拆解为感知、推理、规划、执行四层，同时追踪最终成功率与子目标完成度，适用于电商导购Agent、多轮交互推荐Agent的效果评估，避免仅看最终转化率忽略中间环节瓶颈

  - 可复用bad case归因框架：将错误分为感知偏差、目标绑定错误、执行条件不满足三类，可直接迁移到搜索推荐多轮交互Agent的故障诊断，快速定位是用户意图理解、item召回还是交互逻辑问题

  - 落地选型参考：开源VLM在感知类任务上与闭源差距较小，但多步规划、连续执行能力差距显著，业务落地时简单视觉理解任务可选开源VLM降本，多轮交互复杂任务优先选择闭源大模型

  - 成本优化技巧：Agent失败的token消耗往往集中在少数长尾复杂交互任务，可针对性设置这类任务的交互轮次/token上限，降低大模型推理成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有VLM具身能力评估多聚焦单一任务或单一能力，无法系统性识别从感知到执行的全链路瓶颈，缺少统一框架回答前沿VLM是否满足通用机器人的全流程任务要求。
### 方法关键点
- 搭建Embodied Agent Arena评估框架，覆盖几何估计、空间推理、功能语义接地、任务规划、机械臂操作5大能力域，共1000个测试用例
- 新增GeoProbe专用基准，含168个可控3D场景用例，专门区分尺度偏差、形状畸变、运动感知三类几何误差
- 最小化评估干预，保留所有原生任务的接口与成功判定标准，完整追踪子目标完成度、token消耗、错误类型等细粒度指标
### 关键结果数字
- 测评10款主流VLM，闭源模型在5个能力域全面领先：头部模型规划成功率最高达80.3%，操作成功率最高达47.8%
- 开源VLM空间推理准确率达48%~51.6%，但规划成功率仅19.1%~31.2%，操作成功率仅9.9%~20.9%，规划执行短板显著
- 测试任务中仅8个所有模型均可完成，15个所有模型均失败；62%的代码语法错误修复后仍无法完成任务，多数失败源于目标绑定错误、物理状态未满足
### 核心结论
评估交互型Agent不能仅看最终成功率，拆解感知、绑定、执行三类细粒度错误才能针对性优化系统瓶颈
