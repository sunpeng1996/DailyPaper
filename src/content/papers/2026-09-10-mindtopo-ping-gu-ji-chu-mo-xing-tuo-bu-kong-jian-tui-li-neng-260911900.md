---
title: 'MindTopo: Can Foundation Models Reason in Topological Space?'
title_zh: 《MindTopo：评估基础模型拓扑空间推理能力的基准》
authors:
- Yunfei Ge
- Anbang Liu
- Qineng Wang
- Johnalbert Garnica
- Jianwen Lyu
- Zihan Wang
- Reuben Tan
- Jianfeng Gao
- Ruohan Zhang
- Yining Hong
affiliations:
- Northwestern University
- Microsoft Research
- Stanford University
arxiv_id: '2609.11900'
url: https://arxiv.org/abs/2609.11900
pdf_url: https://arxiv.org/pdf/2609.11900
published: '2026-09-10'
collected: '2026-09-11'
category: Eval
direction: 大模型推理 · 拓扑空间能力基准评测
tags:
- Benchmark
- Spatial Reasoning
- MLLM
- Topological Reasoning
- Agent Planning
one_liner: 构建覆盖5类拓扑属性、2个认知层级的拓扑推理基准MindTopo，评测14款MLLM的相关能力
practical_value: '- 做家装布局推荐、线下逛街路径推荐等空间相关Agent时，可复用本基准的拓扑属性评估范式，提前校验模型拓扑推理鲁棒性

  - 开发闭环交互Agent时，可参考「推理-规划」双层评估框架，区分模型静态认知和动态决策的能力差异，针对性迭代优化

  - 针对DIY商品搭配、3D试穿等多模态生成式推荐场景，可引入拓扑关系校验逻辑，避免生成穿戴物穿过身体等拓扑逻辑错误'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有大模型空间推理评估多聚焦距离、角度等度量属性，忽略连续形变下保持不变的拓扑关系，而拓扑关系是人类空间认知的核心基础，相关能力评测存在空白。
### 方法关键点
提出MindTopo基准，覆盖认知科学和形式拓扑定义的连续性、分离性、顺序、包围、结5类核心拓扑属性，设置两层评估维度：推理层要求模型识别拓扑关系或预测变化，规划层要求大模型作为闭环Agent输出环境交互动作；共包含11030个实例，覆盖13类可控难度的程序生成任务。
### 关键结果
14款MLLM在推理任务上的表现均优于规划任务，最优模型性能仍远低于人类水平；对Qwen3-VL-2B-Instruct做SFT和RL优化，推理能力提升幅度显著高于规划能力；生成的观测结果能保留局部线索，但动态过渡无法可靠维持拓扑一致性。
