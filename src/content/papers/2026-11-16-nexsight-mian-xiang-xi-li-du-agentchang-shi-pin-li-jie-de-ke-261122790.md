---
title: 'NexSight: Verifiable Tasks for Fine-Grained Agentic Long-Video Understanding'
title_zh: NexSight：面向细粒度Agent长视频理解的可验证任务框架
authors:
- Tianci Xie
- Li Chen
- Pinxue Guo
- Rui Zheng
affiliations:
- Zhejiang University
- Tongji University
- Shanghai Qiji Zhifeng Co., Ltd.
arxiv_id: '2611.22790'
url: https://arxiv.org/abs/2611.22790
pdf_url: https://arxiv.org/pdf/2611.22790
published: '2026-11-16'
collected: '2026-11-19'
category: Agent
direction: Agent 长视频理解评测与训练
tags:
- Agentic_Video_Understanding
- VideoQA
- Benchmark
- Task_Verification
- Multimodal_Reasoning
one_liner: 提出可验证任务全链路框架 解决Agent长视频细粒度理解的评测与训练痛点
practical_value: '- 可复用「隐去答案的独立验证+反例校验」流程，用于电商短视频/直播内容审核、商品信息抽取Agent的训练数据标注，避免标注偏差，提升数据可靠性

  - 「QA监督+求解器轨迹步级监督」的混合训练范式可直接迁移到搜索推荐多轮交互Agent训练，仅需少量交互数据即可大幅提升工具调用准确率，无需全量行为标注

  - 「全局概览→时序探索→局部校验」的多尺度观测架构可复用在长用户行为序列理解、直播商品卖点抽取场景，降低计算成本的同时提升关键信息召回率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
长视频细粒度理解任务（动作计数、事件排序、状态变更检测等）的答案依赖散布在数小时 footage 中的零散关键帧，固定采样极易漏检。现有Agent方案的评测无法区分错误来自证据缺失、推理失误还是任务本身缺陷，仅答案监督也无法指导Agent学习“在哪看、看什么”的观测决策，导致长视频Agent落地瓶颈突出。
### 方法关键点
- SightForge可验证任务构建：候选任务生成后，由未看过草稿答案的验证器从原始视频重采证据重构答案，经独立审核和反例校验后才入库，构建了含310个带可追溯视觉证据的SightLine基准，覆盖6类核心细粒度能力
- SightLoop多尺度主动观测框架：支持全局概览、时序窗口选择、空间局部检查、证据回溯的全流程交互，全程记录每一步观测数据，可联合评估证据获取和推理能力
- 混合训练范式：结合静态QA监督与求解器在验证任务上的交互轨迹步级监督，无需按最终答案正确性过滤轨迹，保留多样探索行为
### 关键结果
最强通用模型在SightLine上准确率仅54.52%，但拿到标注证据后准确率达79.35%，证据获取是核心瓶颈；同帧预算下，Agent时序选择比固定窗口采样的证据召回率翻倍（19.84%→40.63%）；仅用不到6K样本训练的Sight-35B，交互准确率较base模型提升近1倍（21.29%→42.26%），超过同系列397B模型，在两个外部长视频基准上提升超8个点。
**最值得记住的结论**：可验证的证据链监督比单纯答案监督更能提升Agent主动探索能力，少量高质量步级交互数据的训练效果远超过参数规模堆叠
