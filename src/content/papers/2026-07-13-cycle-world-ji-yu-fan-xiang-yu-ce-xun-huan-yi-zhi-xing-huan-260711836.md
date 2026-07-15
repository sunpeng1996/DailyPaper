---
title: 'Cycle-World: Mitigating Error Accumulation in Long-term Video World Models
  via Reverse-Prediction Cycle Consistency'
title_zh: Cycle-World：基于反向预测循环一致性缓解长视频世界模型误差累积
authors:
- Zihan Su
- Teng Hu
- Jiangning Zhang
- Ruiyan Wang
- Ran Yi
- Lizhuang Ma
- Dacheng Tao
affiliations:
- Shanghai Jiao Tong University
- Zhejiang University
- Nanyang Technological University
arxiv_id: '2607.11836'
url: https://arxiv.org/abs/2607.11836
pdf_url: https://arxiv.org/pdf/2607.11836
published: '2026-07-13'
collected: '2026-07-15'
category: Multimodal
direction: 多模态长视频生成·循环一致性优化
tags:
- Video_Generation
- Cycle_Consistency
- Error_Accumulation
- World_Model
- Diffusion_Model
one_liner: 提出训练加反向约束+推理校正的双阶段框架，解决长视频自回归生成的误差累积问题
practical_value: '- 循环一致性约束思路可迁移到长序列生成类业务：比如电商长期用户兴趣序列建模、Agent 长期规划任务，缓解自回归误差累积

  - 「训练加反向模型嵌入约束+推理复用冻结反向模型做校正」的架构，可复用到推荐长序列兴趣预测、广告多轮文案生成等场景

  - 梯度引导迭代修正隐向量的 trick，可用于优化 LLM 多轮对话、RAG 多轮召回的上下文漂移问题'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
自回归扩散模型已实现高质量视频生成，但序列生成特性天然存在误差累积问题，长视频生成时微小预测偏差随时间叠加，会导致无约束生成漂移、结构崩溃、视觉质量严重下降。
### 方法关键点
1. 理论证明循环一致性目标可严格约束正向生成漂移的上界；
2. 训练阶段集成轻量反向预测模型，给正向生成器隐式嵌入因果约束，强制其生成贴合真实视频分布的可逆序列；
3. 推理阶段复用冻结的反向模型作为运行时校正器，通过梯度引导的循环指导迭代修正生成隐向量，在误差存入历史上下文前主动抑制累积。
### 关键结果
在VBench基准上实现SOTA性能，60秒长视频生成的整体质量和长时序一致性均达最优，误差漂移得到显著缓解。
