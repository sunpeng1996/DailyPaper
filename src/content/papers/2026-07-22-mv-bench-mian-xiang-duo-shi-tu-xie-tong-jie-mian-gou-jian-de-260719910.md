---
title: 'MV-Bench: Benchmarking Multimodal Large Language Models for Coordinated Multi-View
  Interface Construction'
title_zh: MV-Bench：面向多视图协同界面构建的多模态大模型评测基准
authors:
- Yue Zhao
- Hongxu Liu
- Feiyu Wang
- Xiaoyu Yang
- Tong Ge
- Zhen Yang
- Chao Wang
- Qiong Zeng
arxiv_id: '2607.19910'
url: https://arxiv.org/abs/2607.19910
pdf_url: https://arxiv.org/pdf/2607.19910
published: '2026-07-22'
collected: '2026-07-24'
category: Eval
direction: 多模态大模型评测 · 可视化界面生成
tags:
- MLLM
- Benchmark
- Multimodal
- UI Generation
- Evaluation
one_liner: 提出首个面向多视图协同界面构建的MLLM评测基准，量化当前MLLM在该场景的能力短板
practical_value: '- 可借鉴其从工业级工具（如Tableau）导出结构化标注的思路，大幅降低生成式BI报表、运营可视化界面类任务的标注成本

  - 其提出的视觉保真度、数据绑定正确性、交互完整性三维评测维度，可直接复用于电商后台可视化生成、BI报表生成类Agent的效果评估

  - 现有MLLM在数据绑定、交互逻辑生成上表现极差的结论，可指导相关业务拆分任务，避免端到端生成带交互的多视图界面，改为拼接预定义组件更可靠'
score: 6
source: arxiv-cs.HC
depth: abstract
---

### 动机
现有MLLM可视化生成评测仅覆盖单图表生成场景，忽略多视图协同界面需联合推理数据语义、视图联动、交互逻辑的要求，无专属评测基准支撑能力评估。
### 方法关键点
以显式编码数据绑定、视觉映射、交互规则的Tableau工作簿为真值来源，搭建多阶段转换流水线生成结构化中间表示，输出可执行web界面；基准包含92个基础界面，经图表/数据集/交互模式重组得到1048个校验通过的实例，每个实例配套可执行代码、渲染结果、数据集、交互标注。
### 关键结果数字
评测5个SOTA MLLM，最优模型视觉布局还原准确率75.45%，数据绑定准确率仅21.71%，交互完整度仅11.68%；迭代优化仅提升代码可执行性，无法缩小数据绑定与交互生成的能力gap。
