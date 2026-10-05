---
title: 'Beyond Single Videos: Benchmarking and Active Evidence Seeking for E-Commerce
  Cross-Video Reasoning'
title_zh: 电商跨视频推理基准构建与主动证据探寻Agent框架
authors:
- Jinghan Zhao
- Yiman Hu
- Liang Wu
- Jian Xu
- Bo Zheng
affiliations:
- Alibaba Group
arxiv_id: '2610.03099'
url: https://arxiv.org/abs/2610.03099
pdf_url: https://arxiv.org/pdf/2610.03099
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: 电商多模态Agent · 跨视频推理优化
tags:
- Multimodal Agent
- Cross-Video Reasoning
- E-commerce Video
- Reinforcement Learning
- SFT
one_liner: 首个电商跨视频推理基准AdsCVR+主动证据探寻Agent框架AdSeek，精度较基线提升27.9%
practical_value: '- 电商多模态内容对比类需求（如广告效果横向评估、同品类商品卖点比对）可复用AdSeek的动态工具调用思路，替代传统固定帧采样+全量内容输入模式，大幅降低冗余计算同时提升推理精度

  - RL训练长序列决策Agent遇到稀疏奖励credit assignment问题时，可复用Rectified Bootstrapping Pipeline：先用RL暴露瓶颈，再用强教师做离线轨迹纠错生成SFT数据校准偏差，最后再做RL精调，解决纯RL训练收敛慢、偏差难修正的问题

  - 电商多模态评测数据集构建可复用AdsCVR的分层过滤流程：先做多维度语义标注，再做可比组划分，最后经过盲测过滤、证据可验证性过滤、难度校准三道关卡，确保数据集无捷径、难度合理'
score: 10
source: arxiv-cs.CV
depth: full_pdf
---

### 动机
电商场景中消费者跨视频比对商品、商家横向评估不同广告素材效果的需求普遍存在，但现有多模态模型仅支持单视频理解，跨视频推理时难以在密集冗余的音视频内容中精准定位细粒度证据，且缺少针对性的电商场景评测基准支撑技术迭代。

### 方法关键点
- 构建首个电商跨视频推理基准AdsCVR：覆盖86个品类2483条视频、6110个QA对，包含类目比对、异常检测、创意策略、视觉构成、时间结构、信息密度6个推理维度，经过多层过滤确保无语言捷径、答案可基于视频证据验证
- 提出AdSeek Agent框架：支持多轮动态调用帧选择、音频选择两类感知工具，主动筛选目标视频、时间片段、模态及视觉区域，过滤无关内容后跨视频对齐证据生成答案
- 提出校正自举训练流水线RBP：第一阶段用RL做策略探索暴露瓶颈，第二阶段用强教师模型离线诊断RL生成的轨迹，补充缺失证据、修正推理错误后生成SFT数据校准偏差，第三阶段再用RL做二次精调，解决稀疏奖励下长序列决策的credit assignment问题

### 关键结果
AdSeek在AdsCVR测试集上准确率达74.30%，较基线Qwen3-VL-8B-Instruct绝对提升27.90%；在通用跨视频基准CrossVid上准确率达31.55%，较基线提升2.08个百分点，具备跨域泛化能力。

> 最值得记住的一句话：多模态长序列推理任务中，动态主动证据获取+RL与离线校正SFT结合的训练范式，效果远优于固定输入+单轮推理的传统模式
