---
title: 'DISCO: Distributed Long Context Scaling with Grounding-Reasoning Disaggregation'
title_zh: DISCO：基于接地-推理解耦的分布式长上下文扩展框架
authors:
- Guanzheng Chen
- Viet Dac Lai
- Subhojyoti Mukherjee
- Branislav Kveton
- Seunghyun Yoon
- Franck Dernoncourt
- Qizhe Xie
- Trung Bui
affiliations:
- National University of Singapore
- Adobe Research
arxiv_id: '2609.33485'
url: https://arxiv.org/abs/2609.33485
pdf_url: https://arxiv.org/pdf/2609.33485
published: '2026-09-26'
collected: '2026-09-29'
category: MultiAgent
direction: 多智体协作 · 长上下文推理优化
tags:
- Long-Context LLM
- MultiAgent
- Distributed Inference
- Grounding-Reasoning Disaggregation
- GRPO
- Cost Optimization
one_liner: 解耦上下文接地与推理阶段，分布式多LLM架构消除长上下文context rot，推理成本降超80%
practical_value: '- 长上下文RAG/Agent系统可直接复用Driver-Worker分层架构：用小参数模型做上下文分片并行原子抽取，大参数模型仅负责推理合成，适配电商全量用户行为序列分析、全商品库多跳查询等场景，既避免context
  rot又大幅降低推理成本

  - 可复用GRPO复合奖励训练Agent规划模块：除最终任务准确率外，增加答案与抽取证据一致性奖励、输出格式合规奖励，能显著减少规划重试次数，提升推荐系统用户意图理解、多跳商品归因等长路径任务的执行稳定性

  - 复杂多跳长上下文任务可借鉴DAG动作拆分设计：将需求拆解为仅需本地信息的Narrow抽取动作和需全局聚合的Wide推理动作，避免单步信息丢失，适配长会话用户需求解析、大促全量规则匹配等电商场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有长上下文LLM普遍存在context rot问题：输入长度增长时推理质量暴跌，根源是单块架构中上下文接地（检索相关信息）与逻辑推理两个阶段耦合，注意力带宽被海量检索任务占满，留给复杂推理的容量严重不足。现有方案中，RAG依赖语义匹配召回精度低，串行多Agent工作流延迟随上下文线性增长，均无法兼顾长上下文处理的效果与成本。

### 方法关键点
- 参考Spark分布式计算范式，提出接地-推理解耦架构DISCO：长上下文拆分为独立分片存储在轻量Worker LLM，仅负责并行本地化原子信息抽取；大参数Driver LLM不访问原始上下文，仅负责任务规划、证据聚合与逻辑推理
- Driver用动态DAG调度执行流程：将任务拆分为两类动作，Narrow Action（原子抽取）下发给Worker并行执行，Wide Action（跨分片聚合推理）由Driver本地执行，迭代补全信息直到可输出高置信度答案
- 采用GRPO训练Driver策略，复合奖励覆盖最终答案准确率、答案与抽取证据一致性、DAG格式合法性三类指标，全路径回传奖励优化规划质量

### 关键结果
在LongBench v2、RULER-QA（1M tokens）、∞Bench三个长上下文基准测试，对比全上下文基线、标准RAG、Chain-of-Agents等方案：
- 1M tokens RULER-QA任务上，Qwen3-8B版本DISCO准确率达78.4%，远高于标准RAG的10.9%；LongBench v2长序列子集上Qwen3-14B版本比全上下文基线高9.8个百分点
- 采用Gemini-3-Pro作为Driver时，DISCO性能与全上下文基线持平，推理成本降低80%以上，延迟随上下文长度增长基本保持平稳

### 核心洞见
长上下文扩展的核心不是盲目扩大单模型窗口，而是借鉴分布式大数据系统的设计思路，将信息检索与逻辑计算解耦，用横向扩展的分层架构解决规模问题
