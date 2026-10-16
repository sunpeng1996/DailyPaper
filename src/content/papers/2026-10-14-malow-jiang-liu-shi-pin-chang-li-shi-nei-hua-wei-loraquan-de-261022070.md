---
title: 'Memory as Weights: Internalizing Long-Term History for Streaming Videos'
title_zh: MaLoW：将流视频长历史内化为LoRA权重的记忆框架
authors:
- Zhuoming Liu
- Jinhong Lin
- Lin Zhang
- Yiwu Zhong
- Yin Li
affiliations:
- University of Wisconsin–Madison
- Peking University
arxiv_id: '2610.22070'
url: https://arxiv.org/abs/2610.22070
pdf_url: https://arxiv.org/pdf/2610.22070
published: '2026-10-14'
collected: '2026-10-16'
category: Multimodal
direction: 流式多模态大模型 · 长时记忆优化
tags:
- LoRA
- Streaming VLM
- HyperNetwork
- Long-term Memory
- Vision-Language
one_liner: 将流视频历史内化为动态LoRA权重，避免历史信息挤占当前输入上下文
practical_value: '- 电商直播实时理解、用户长行为序列建模场景可直接借鉴核心思路：将长期历史内化为动态LoRA权重，避免长上下文挤占当前实时输入的token配额，大幅降低推理延迟

  - 可复用双分支隐状态更新设计：用SSM捕获短期时序依赖、门控求和保留长期全局语义，平衡用户短期实时兴趣和长期历史偏好的建模效果

  - 电商交互Agent的长会话记忆模块可复用该方案：将历史交互信息编码为轻量LoRA参数，无需反复拼接长上下文，降低KV cache开销，适配低时延实时交互需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有流式VLM的记忆机制多将压缩或检索后的历史信息放入输入上下文，会和当前观察、用户查询抢占有限的上下文窗口，同时存在历史增量更新成本高、推理延迟大的问题，无法适配长时流处理的低时延、固定内存预算需求。
### 方法关键点
- MaLoW框架将历史上下文编码为动态LoRA权重，基VLM参数全程固定，仅LoRA随新观察增量更新，推理时基模型仅需处理当前输入，彻底避免历史信息挤占上下文
- 采用循环HyperNetwork实现增量更新：先将当前视频片段+文本信息压缩为紧凑表征，再通过双分支更新隐状态：SSM分支捕获局部时序依赖，门控求和分支保留全局语义，最终映射为LoRA权重
- 构建MaLoW-Instruct训练数据集，包含56K条视频、381K条QA对，覆盖实时、回溯、预测三类问题场景，针对性训练模型的记忆编码能力
### 关键结果
在OVO-Bench、StreamingBench、StreamArena三个流视频基准上测试，OVO-Bench回溯任务上比现有记忆方法提升3.9%~11.8%，额外推理延迟仅23ms（占总推理时间<15%）；扩展到VLA机器人场景，动作成功率提升9.3%；跨0.8B~11B不同规模、不同基座模型均获得稳定效果提升。
### 核心结论
记忆不一定非要存在输入上下文或外部向量库中，也可以直接内化为模型的轻量动态参数，在降低资源开销的同时保留强长时记忆能力。
