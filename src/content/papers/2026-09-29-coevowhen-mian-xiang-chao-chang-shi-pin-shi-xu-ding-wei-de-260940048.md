---
title: 'CoEvoWhen: Policy-Tool Coevolution for Ultra-Long Video Temporal Grounding'
title_zh: CoEvoWhen：面向超长视频时序定位的策略-工具协同进化框架
authors:
- Yiduo Jia
- Muzhi Zhu
- Jinchuan Shi
- Hao Zhong
- Yuling Xi
- Ke Liu
- Hao Chen
affiliations:
- Zhejiang University, State Key Lab of CAD & CG
arxiv_id: '2609.40048'
url: https://arxiv.org/abs/2609.40048
pdf_url: https://arxiv.org/pdf/2609.40048
published: '2026-09-29'
collected: '2026-10-01'
category: Agent
direction: Agent自进化 · 策略工具协同优化
tags:
- Agent Self-Evolution
- Video Temporal Grounding
- Tool Use
- Multimodal Agent
- VLM
one_liner: 无需更新VLM参数，通过策略与工具协同进化实现超长视频时序定位的精度提升与推理成本下降
practical_value: '- 可复用「策略+工具联合进化」思路搭建电商/短视频内容检索Agent，无需微调大模型，仅通过历史执行轨迹迭代检索规则和工具，大幅降低迭代成本

  - 长序列检索场景可借鉴「图像全局粗搜+视频局部细查」的观测组合策略，平衡检索精度和token成本，适用于电商直播高光定位、短视频侵权片段检测等场景

  - Agent技能可封装为独立的外部可更新模块（政策文档+可执行工具集），可跨不同VLM底座迁移，降低业务多模型部署的适配成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
超长视频时序定位需要在有限视觉预算下平衡长程证据搜索和细粒度事件理解，现有Agent方法依赖预定义策略和固定工具集，无法自适应优化，要么漏检短时长目标事件，要么细粒度观测带来过高推理成本。

### 方法关键点
- 将高层调用策略和可执行媒体工具联合抽象为外部可复用技能，全程冻结VLM参数，仅通过任务执行轨迹迭代优化技能，无需模型微调
- 外部技能更新器从错误执行轨迹中提炼可迁移经验，一方面优化任务规划、观测编排的高层策略，另一方面自动生成代码升级现有工具或新增工具
- 进化后策略自动协调两类观测工具：图像类工具负责长程全局搜索、候选区快速精炼，视频类工具负责局部动态验证、事件边界精准判定

### 关键实验
在5个基准（3个超长视频时序定位+2个长视频QA）、3款不同参数的Qwen VLM上验证：在平均时长76分钟的ExtremeWhenBench数据集上，Qwen3.5-27B的mIoU提升74.9%，平均视觉token成本降低11.4%；进化后的技能无需额外适配直接迁移到长视频QA任务，LVBench整体精度提升8.65个点。

对基于工具的Agent来说，高层调用策略和底层工具能力是相互依赖的，联合进化能在不更新模型参数的前提下实现性能和成本的双重优化。
