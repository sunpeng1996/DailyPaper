---
title: 'VideoMemBench: How Well Do MLLMs Remember in Video Conversations?'
title_zh: VideoMemBench：多模态大语言模型视频对话记忆能力测评基准
authors:
- Zhengdong Hu
- Chao Wang
- Kaituo Feng
- Huanjin Yao
- Mingfei Lu
- Hehe Fan
- Yi Yang
affiliations:
- University of Technology Sydney
- The Chinese University of Hong Kong
- The Hong Kong University of Science and Technology
- Zhejiang University
arxiv_id: '2610.40131'
url: https://arxiv.org/abs/2610.40131
pdf_url: https://arxiv.org/pdf/2610.40131
published: '2026-11-02'
collected: '2026-11-05'
category: Eval
direction: 多模态大模型 · 视频对话记忆测评
tags:
- MLLM
- VideoQA
- Benchmark
- In-context Memory
- Multi-turn Dialogue
one_liner: 构建含跨轮语义依赖的视频多轮对话基准，量化测评MLLM的上下文视频记忆能力
practical_value: '- 开发直播带货导购Agent、短视频内容问答Agent等跨轮多模态交互产品时，可复用基准定义的情景依赖、答案依赖两类场景设计测试用例，验证长会话记忆准确率

  - 构造多轮会话评测数据集时，可复用「planner+generator+judger三角色LLM流水线+人工校验」的方案，保证测试用例满足必要性、无信息泄露要求

  - 优化长会话MLLM性能时，可重点针对跨轮长距离回调、多父依赖的记忆场景做专项调优，当前SOTA模型在此类场景得分不足50%，优化空间大'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
当前MLLM已支持小时级视频处理，视频多轮对话场景要求模型具备复用上下文信息的记忆能力，但现有VideoQA基准问题相互独立，所有问题仅靠视频即可回答，无法测评跨轮信息复用的记忆能力。
### 方法关键点
提出VideoMemBench测评基准，每个样本匹配单条视频+长多轮对话，设置两类跨轮依赖：Episodic Dependency探测视觉内容记忆，Answer Dependency探测模型自身历史回答记忆；采用三角色LLM流水线（planner+generator+judger）+人工审核构造数据集，确保每个依赖满足「无之前轮次信息无法回答」「当前问题不泄露之前轮次信息」两个特性。
### 关键结果数字
基准包含326条视频、2476轮对话，其中1387轮存在跨轮依赖，覆盖多父依赖、长距离回调场景；测评20余款开源/闭源MLLM，最优的Claude Opus 5整体得分仅45.7%。
