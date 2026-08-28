---
title: 'StreamAV-Bench: A Comprehensive Benchmark for Streaming Audio-Video Generation'
title_zh: StreamAV-Bench：面向流式音视频生成的综合评测基准
authors:
- Kaiqi Liu
- Haoxuan Zeng
- Jingqi Liu
- Jiacong Fang
- Ziqi Cai
- Yunyao Mao
- Henglin Liu
- Yu Sheng
- Shuchen Weng
- Boxin Shi
affiliations:
- BAAI
- PKU
- Kling
- THU
- USTC
arxiv_id: '2608.26336'
url: https://arxiv.org/abs/2608.26336
pdf_url: https://arxiv.org/pdf/2608.26336
published: '2026-08-26'
collected: '2026-08-28'
category: Eval
direction: 多模态生成 · 流式音视频评测
tags:
- Streaming Generation
- Audio-Video Generation
- Evaluation Benchmark
- Multimodal Generation
- Interactive Generation
one_liner: 推出首个面向流式音视频生成的综合评测基准，覆盖双赛道32个细粒度评测维度
practical_value: '- 做电商商品短视频流、实时直播导购类生成业务时，可直接复用该基准的渐进生成稳定性、交互响应速度等指标，无需自研全套评测体系

  - 选型流式音视频生成模型（如数字人导购、实时互动内容生成）时，可将基准指出的时序漂移、响应瓶颈作为核心筛选项，规避性能缺陷模型

  - 开发实时交互Agent的多轮内容生成模块时，可参考基准的状态留存复用评测逻辑，优化多轮交互下的内容一致性'
score: 6
source: arxiv-cs.MM
depth: abstract
---

### 动机
现有音视频生成评测基准仅支持完整序列评估，无法覆盖实时交互场景下流式生成的渐进稳定性、交互响应性等核心特性，存在明显评测体系缺口。

### 方法关键点
- 搭建双赛道统一评测框架：渐进式赛道负责评测指令遵循度、长时生成稳定性；交互式赛道负责评测交互响应能力、状态留存复用能力
- 输出经专家校验的320个评测用例，覆盖32个细粒度维度，适配8类场景×5类音频域、5类主体×4类视觉风格的多元评测需求

### 关键结果
对13款代表性音视频生成系统评测发现，现有模型普遍存在两个核心缺陷：渐进生成阶段时序漂移率高，交互控制阶段响应延迟存在明显瓶颈，为后续原生联合音视频流式模型优化提供明确方向
