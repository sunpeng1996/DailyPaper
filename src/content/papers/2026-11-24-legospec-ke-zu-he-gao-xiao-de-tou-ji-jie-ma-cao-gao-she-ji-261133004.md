---
title: 'LEGOSpec: A Composable and Efficient Framework for Speculative Draft Design
  and Training'
title_zh: LEGOSpec：可组合高效的投机解码草稿设计与训练框架
authors:
- Hanzhen Wang
- Jiaming Xu
- Guohao Dai
affiliations:
- Shanghai Jiao Tong University
- Infinigence AI
- SII
arxiv_id: '2611.33004'
url: https://arxiv.org/abs/2611.33004
pdf_url: https://arxiv.org/pdf/2611.33004
published: '2026-11-24'
collected: '2026-11-25'
category: LLM
direction: LLM推理加速 · 投机解码框架
tags:
- speculative_decoding
- LLM_inference_acceleration
- training_framework
- long_context
- efficiency
one_liner: 提出可组合投机解码草稿训练框架，组件化调优提升接受长度与训练效率
practical_value: '- 电商场景下的LLM生成类业务（商品文案、Agent话术、搜索query生成等）可直接复用DFlux的投机解码优化，短/长上下文分别选用GQA/SWA骨干，生成速度提升1.57~5.62倍且不损失效果，大幅降低推理成本

  - 训练多组件组合的小模型（如推荐召回/精排蒸馏小模型、垂域小助手）时，可参考LEGOSpec的元数据感知调度+异步执行方案，训练吞吐量最高提升79%，离线数据预处理速度提升3.11倍，降低训练成本

  - 做业务场景小模型蒸馏时，可复用分层监督设计：基础分支负责候选覆盖，上层分支优化最终业务目标，平衡模型精度与推理速度'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有投机解码的草稿模型优化多为完整方案对比，组件效果、交互逻辑与组合增益不清晰，且训练配置（数据规模、优化器等）对效果的影响甚至超过架构改动，缺乏可控的组件对比框架，也没有针对不同场景的最优配置指导。
### 方法关键点
- 将草稿模型拆解为Context、Backbone、Proposal、Objective四大可替换组件，共享统一训练基础设施，可控制变量对比单个组件的效果
- 基于组件实验结论设计通用DFlux草稿：SWA-GQA混合骨干适配长短上下文，Residual Corrector并行生成分词候选平衡接受率与延迟，分层监督同时优化候选覆盖与接受长度
- 训练框架采用元数据感知调度（目标端预取调度、草稿端成本感知调度）+异步执行流水线，降低训练空转与IO开销
### 关键实验结果
在Qwen、Gemma系列模型上验证，对比DFlash、DFlash2、DSpark等SOTA基线，DFlux在常规任务上接受长度最高提升13.7%，长上下文任务最高提升34.7%；训练吞吐量对比SpecForge最高提升79%，离线监督数据预处理速度最高提升3.11倍；SGLang部署后生成吞吐量比基线高4.7%~24.2%，比原生自回归生成提速1.57~5.62倍。
### 核心结论
投机解码的效果优化需要从组件适配场景、训练效率、推理开销三个维度联合优化，而非仅追求单指标提升。
