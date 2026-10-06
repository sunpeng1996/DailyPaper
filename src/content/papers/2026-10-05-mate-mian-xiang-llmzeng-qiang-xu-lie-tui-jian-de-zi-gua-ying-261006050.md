---
title: 'MATE: Adaptive Long- and Short-Term User Memory for LLM-Based Recommendation'
title_zh: MATE：面向LLM增强序列推荐的自适应长短时用户记忆框架
authors:
- Yu Hou
affiliations:
- Yonsei University
arxiv_id: '2610.06050'
url: https://arxiv.org/abs/2610.06050
pdf_url: https://arxiv.org/pdf/2610.06050
published: '2026-10-05'
collected: '2026-10-06'
category: GenRec
direction: 生成式推荐 · 用户长短兴趣建模
tags:
- Sequential Recommendation
- LLM4Rec
- User Modeling
- Long-short Term Interest
- Memory Mechanism
one_liner: 用时序证据驱动双用户记忆自适应更新，提升LLM增强序列推荐性能
practical_value: '- 可复用双记忆更新逻辑：放弃按时间硬切长短兴趣的传统方案，用跨多周期重复的语义相似行为作为长时兴趣证据、近期窗口语义一致性作为短时证据，适配电商用户兴趣漂移场景

  - 轻量化在线部署方案：主模型完全冻结，仅更新用户侧两个小记忆矩阵，单用户仅需1MiB存储、单事件新增处理延迟1.25-1.32ms，符合工业级推荐系统的性能要求

  - 可插拔融合模块：动态上下文门控+时序监督损失的方案可直接迁移到现有LLM4Rec架构，无需修改主干模型即可同时提升长期偏好召回和短期兴趣响应准确率'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前LLM增强推荐系统多依赖物品语义建模，无法有效区分用户历史行为中哪些是长期稳定偏好、哪些是短期临时兴趣，传统时序建模方案要么对新兴趣响应过慢，要么少量短期行为就覆盖长期积累的偏好，导致推荐准确率不足。
### 方法关键点
- 时序证据计算：对每一个新交互，分别计算两类权重：长时证据要求语义相似行为至少出现在2个历史周期且跨期≥30天，权重与出现周期占比正相关；短时证据统计最近7天窗口内语义相似行为占比，设置最低写入权重保证新兴兴趣可被写入。
- 双记忆更新机制：每个用户独立维护长时、短时两个记忆矩阵，长时记忆更新率低、衰减慢，保守保留稳定偏好；短时记忆更新率高、衰减快，快速适配新兴趣，两类证据分别控制对应记忆的写入强度，同一交互可同时更新两个记忆。
- 动态门控融合：基于最近7天的时间衰减语义向量生成门控权重，动态适配当前推荐场景下长短记忆的贡献比例，无需固定融合系数。
### 关键实验
在MovieLens-10M、Amazon Luxury Beauty、KuaiRec三个公开数据集上，对比SASRec、TTT4Rec等SOTA基线，NDCG@10相对提升7.0%~13.2%，同时在短期兴趣延续、长期偏好召回两个任务上均优于基线；单用户仅需1MiB存储，单事件新增处理延迟仅1.25~1.32ms。
### 最值得记住的一句话
用户兴趣建模不要只做静态的历史编码，要将其转化为持续的自适应更新过程，用行为的时序证据决定记忆写入强度，用当前上下文决定记忆读取权重。
