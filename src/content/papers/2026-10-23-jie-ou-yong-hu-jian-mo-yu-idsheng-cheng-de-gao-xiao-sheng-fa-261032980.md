---
title: Separating Thinking from Spelling for Efficient Generative Recommendation
title_zh: 解耦用户建模与ID生成的高效生成式推荐方法Deco
authors:
- Danil Gusak
- Anna Volodkevich
- Ivan Oseledets
- Evgeny Frolov
arxiv_id: '2610.32980'
url: https://arxiv.org/abs/2610.32980
pdf_url: https://arxiv.org/pdf/2610.32980
published: '2026-10-23'
collected: '2026-10-26'
category: GenRec
direction: 生成式推荐 · Semantic ID 推理加速
tags:
- Generative Recommendation
- Semantic ID
- Efficient Inference
- Knowledge Distillation
- Beam Search
one_liner: 解耦用户建模与Semantic ID生成，用轻量解码器跑beam search，不降精度下提升3-8倍推理吞吐量
practical_value: '- 架构层面：生成式推荐可将用户建模（重backbone）和SID序列生成（轻解码器）解耦，beam search全放在轻量解码器执行，无需反复调用大模型，可复用现有SID和trie约束，改造成本低

  - 训练trick：轻量解码器先用交叉熵训练，再用全量backbone的输出做知识蒸馏，精度可超过teacher模型，且蒸馏仅在训练阶段使用，不增加推理开销

  - 工程优化：可预计算用户的next-item concept向量（仅1KiB大小），在线请求仅跑轻量解码器，50ms p95 latency预算下吞吐量提升3~8倍，还能支持千级别召回候选集

  - 业务适配：针对音乐/内容等重复消费占比高的场景，新增轻量历史copy指针，和生成概率做门控融合，无需修改beam search逻辑，即可大幅提升重复推荐准确率'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前基于Semantic ID（SID）的生成式推荐，beam search阶段需要反复调用大backbone生成多轮SID码，占总推理时长的90%以上，且成本随backbone参数量、SID深度、候选集规模线性增长，严重影响上线可行性，尤其是用LLM做backbone的场景成本极高。

### 方法关键点
- 提出Deco架构，拆分两个独立阶段：重backbone仅做一次用户历史编码，输出固定大小的next-item concept向量；轻量2层Transformer解码器基于concept和已生成的SID前缀，完成全部trie约束的beam search，全程不再调用backbone
- 训练支持两种模式：仅用交互数据的交叉熵训练，或叠加全量backbone teacher的知识蒸馏，后者可进一步提升精度
- 针对重复消费场景，新增轻量历史copy指针，和生成概率做门控融合，无需修改beam search逻辑即可适配

### 关键实验结果
- 覆盖7个数据集：电商（Amazon多品类）、电影（MovieLens）、音乐（Yambda），对比FlatGR、FusedGR等主流SID生成式推荐基线，以及SASRec+等传统召回模型
- 精度持平甚至超过全量backbone基线，50ms p95 latency约束下吞吐量提升3.2~8.6倍；用3B LLM做backbone时，吞吐量比基线高16倍，且用1.5B LLM的Deco和69M小模型基线吞吐量持平，精度更高
- 支持千级别候选集生成，Deco生成1000个候选的速度比基线生成100个还快，召回率提升3倍

### 核心结论
生成式推荐的推理瓶颈不在用户历史编码，而在反复调用大模型生成SID的过程，解耦后轻量解码器完全可以胜任ID生成任务，不损失精度还能大幅降本。
