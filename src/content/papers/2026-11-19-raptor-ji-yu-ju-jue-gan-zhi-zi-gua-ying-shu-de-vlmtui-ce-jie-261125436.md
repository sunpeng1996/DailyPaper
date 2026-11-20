---
title: 'Raptor: Rejection-aware Adaptive Tree based on Speculative Decoding'
title_zh: Raptor：基于拒绝感知自适应树的VLM推测解码加速框架
authors:
- Qishu Hu
- Haozhao Wang
- Zicong Hong
- Yufeng Zhan
- Yuanqing Xia
affiliations:
- 北京理工大学
- 华中科技大学
- 洛桑联邦理工学院
arxiv_id: '2611.25436'
url: https://arxiv.org/abs/2611.25436
pdf_url: https://arxiv.org/pdf/2611.25436
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: LLM推理优化 · 树结构推测解码加速
tags:
- Speculative Decoding
- VLM
- Inference Acceleration
- Adaptive Tree
- Training-free
one_liner: 利用解码验证的拒绝反馈动态调整推测树配置，无训练实现VLM最高2.39倍无损加速
practical_value: '- 电商场景下的多模态商品文案生成、智能客服应答等VLM推理服务，可直接将Raptor集成到现有Medusa/EAGLE/ViSpec等树结构推测解码框架中，无需修改模型结构或额外训练，即可获得15%以上的解码提速，降低推理成本

  - 做LLM/VLM推理引擎优化的团队，可复用3种拒绝感知信号的设计，替代原有仅靠接受长度调优的策略，平衡候选覆盖度和冗余计算，提升各类生成场景的推测解码效率

  - 该动态调优思路可迁移到推荐系统的参数自适应场景：用业务反馈（点击、转化等）经EMA平滑+动量更新，动态调整召回深度、多路召回路权值，避免单轮异常反馈导致的参数震荡'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
树结构推测解码是VLM推理加速的主流方案，但长视觉上下文会大幅提升推测计算成本，现有自适应方案仅依赖置信度、接受长度等单一信号，无法区分候选覆盖不足和过度深度扩展两种低效率场景，导致算力浪费，无法平衡加速收益和计算成本。
### 方法关键点
- 提取3种互补的拒绝感知信号：接受长度（本轮解码进度）、前沿缺口（拒绝位置未覆盖的目标模型概率质量）、深度浪费（超过接受长度的冗余节点占比），全面刻画推测解码效率状态
- 设计统一压力映射控制器，将三种异质信号经EMA平滑后映射到[-1,1]的统一压力空间，联合调整推测树的深度、分支宽度、总节点预算三个核心参数
- 加入动量更新和离散投影机制，避免单轮反馈导致的参数震荡，同时区分浅层真实拒绝和路径耗尽场景动态控制扩展范围，无训练、无架构修改即可集成到现有树结构推测解码框架
### 关键实验
在7个多模态基准（MME、MM-Vet、ScienceQA等）上测试LLaVA-1.6、Qwen2.5-VL两个7B模型，对比Medusa、EAGLE、ViSpec三种主流框架的原生版本、SAGE、TALON自适应策略：相比原生框架平均提速14.4%~41.8%，最高实现2.39倍相对自回归解码的平均速度，3.21倍峰值速度，所有场景下加速效果均优于现有自适应策略。
### 核心结论
推测解码的加速效果不与接受长度正相关，额外获得的接受token必须能覆盖构造、验证候选的算力成本才有实际价值。
