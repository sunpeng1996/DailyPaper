---
title: 'X-Planner: Event-Structured Task Planning for Embodied Intelligence'
title_zh: X-Planner：面向具身智能的事件结构化任务规划框架
authors:
- Howard Lu
- Shalfun Li
- Porter Pan
- Cris
- Lumen
- Cyril
- Eric Hu
- Lily Li
- Maeve Zhang
- Robert Wang
affiliations:
- X Square Robot Team
arxiv_id: '2609.25187'
url: https://arxiv.org/abs/2609.25187
pdf_url: https://arxiv.org/pdf/2609.25187
published: '2026-09-20'
collected: '2026-09-26'
category: Agent
direction: 具身Agent 事件结构化任务规划
tags:
- Embodied AI
- Task Planning
- Chain-of-Thought
- Staircase Decoding
- VLM
one_liner: 提出事件结构化具身任务规划前端，支持显式可解释事件与隐式并行推理双输出
practical_value: '- 做Agent任务拆解可借鉴事件结构化分层标注方法，将复杂任务拆解为粒度统一的语义事件单元，既方便人工校验也能提升下游执行模块兼容性，可复用在电商导购Agent多步引导、推荐路径规划等场景

  - 双输出架构设计思路可复用，同时对外暴露可读的离散规划结果（用于可解释性要求高的场景，如推荐理由生成、客服应答路径规划）和低延迟隐式连续状态（用于高吞吐量下游推理链路，如推荐排序实时特征注入）

  - Staircase Decoding分层共享计算思路可迁移到长序列CoT推理场景，通过共享底层Transformer编码结果并行生成多步推理状态，降低长路径推理延迟，适合大促等低延迟要求的推荐/广告系统用户意图预判链路

  - 故障感知标注方案可借鉴，训练任务规划模型时补充人工设计的错误案例，降低对单一策略生成故障样本的依赖，提升推荐系统异常路径处理能力，如用户异常交互场景下的意图纠正'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前VLA模型多采用观察直接映射动作的范式，仅适合短周期确定任务，长周期任务的中间规划结构缺失；现有CoT规划器存在三类核心痛点：一是数据标注仅到任务级，缺少事件边界与故障的细粒度监督；二是规划粒度固定，无法兼顾语义可读性与执行效率；三是自回归解码存在长序列延迟与误差累积问题，难以满足Agent实时执行要求。

### 方法关键点
- 数据层：构建多源分层规划数据集，融合Ego、UMI、遥操作三类数据，统一采用L3任务/L2子任务/L1动作/L0片段四层标注体系，补充接管时间标注与人工设计故障案例，覆盖167个数据集、30类任务，分析子集共1500个episode
- 模型层：基于Qwen VLM backbone搭建双接口规划架构，一是离散事件接口输出可解释的结构化事件状态，支持进度追踪、故障识别与人工调整；二是隐式推理接口采用Staircase Decoding，拆分Transformer层为共享底层与并行上层，并行生成连续CoT隐状态，规避自回归序列化延迟
- 训练层：新增冻结隐式到文本的重建损失，保证隐状态保留完整语义信息；新增特征对齐损失，保证规划模块输出适配下游固定世界动作模型的特征空间，无需重新训练下游模块

### 关键实验
离线评估对比Qwen、Doubao、kimi3，X-Planner BERTScore-F1达0.9011，Judge Overall评分达1.411，排名第二仅低于kimi3；实机测试在推理操作集上Task Progress达71.6%，超出基线U-Scratch 12.1个百分点，在泛化集上达53.8%，超出基线DreamZero 25.25个百分点，均为最优。

### 核心结论
事件作为高维意图与低维执行的中间接口，可同时兼顾上层Agent的可解释性要求与下游执行模块的效率要求，是复杂任务规划的核心落地方向
